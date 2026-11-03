#!/usr/bin/env python3
"""Build one shareable ZIP per plugin from tracked package files."""
import argparse
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    destination = args.output_dir.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    checksums = []
    for plugin in sorted((ROOT / 'plugins').iterdir()):
        if not plugin.is_dir():
            continue
        manifest = json.loads((plugin / 'plugin.json').read_text())
        name, version = manifest['name'], manifest['version']
        if not re.fullmatch(r'[a-z0-9-]+', name) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
            raise ValueError(f'Unsafe package identity: {name} {version}')
        tracked = subprocess.check_output(
            ['git', 'ls-files', '-z', '--', str(plugin.relative_to(ROOT))], cwd=ROOT
        ).decode().split('\0')
        files = sorted(ROOT / item for item in tracked if item)
        names = {p.relative_to(plugin).as_posix() for p in files}
        if 'plugin.json' not in names or not any(n.startswith('skills/') and n.endswith('/SKILL.md') for n in names):
            raise ValueError(f'Manifest and skills must be tracked: {plugin}')
        archive = destination / f'{name}-{version}.zip'
        with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as package:
            for path in files:
                if path.is_symlink() or not path.is_file():
                    raise ValueError(f'Expected regular tracked file: {path}')
                info = zipfile.ZipInfo(path.relative_to(plugin).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                package.writestr(info, path.read_bytes())
        with zipfile.ZipFile(archive) as package:
            if package.testzip() is not None or set(package.namelist()) != names:
                raise ValueError(f'Archive verification failed: {archive}')
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        checksums.append(f'{digest}  {archive.name}')
        print(f'{archive.name}: {len(files)} files, {archive.stat().st_size:,} bytes; verified')
    (destination / 'SHA256SUMS.txt').write_text('\n'.join(checksums) + '\n')


if __name__ == '__main__':
    main()
