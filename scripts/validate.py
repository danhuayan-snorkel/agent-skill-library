#!/usr/bin/env python3
"""Validate local package wiring and reference reachability; standard library only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(base, value):
    require(value.startswith('./'), f'Expected ./ relative path: {value}')
    result = (base / value).resolve()
    require(result.is_relative_to(base.resolve()), f'Path escapes package: {value}')
    require(result.exists(), f'Missing path: {result}')
    return result


def main():
    marketplace = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    require(len(marketplace['plugins']) == 1, 'Expected the Chinese Writing plugin')
    entry = marketplace['plugins'][0]
    require(entry['source']['source'] == 'local', 'Expected local marketplace source')
    require(entry['policy']['installation'] == 'AVAILABLE', 'Plugin must be available')
    require(entry['policy']['authentication'] in {'ON_INSTALL', 'ON_USE'}, 'Invalid auth policy')
    require(entry['category'] == 'Productivity', 'Missing category')
    plugin = local_path(ROOT, entry['source']['path'])
    portable = json.loads((plugin / 'plugin.json').read_text())
    compatibility = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
    for key in ('name', 'version', 'description'):
        require(portable[key] == compatibility[key], f'Manifest mismatch: {key}')
    require(portable['name'] == entry['name'], 'Marketplace name mismatch')
    require(re.fullmatch(r'\d+\.\d+\.\d+', portable['version']), 'Expected semantic version')
    require(portable['extensions']['com.openai']['interface'] == compatibility['interface'],
            'Interface metadata mismatch')
    skills = local_path(plugin, compatibility['skills'])
    entries = list(skills.glob('*/SKILL.md'))
    require(len(entries) == 1, 'Expected one packaged skill')
    for skill in entries:
        body = skill.read_text()
        require(body.startswith('---\n'), f'Missing frontmatter: {skill}')
        front = body.split('---', 2)[1]
        name = re.search(r'^name: (.+)$', front, re.M)
        require(name is not None and name[1] == skill.parent.name, 'Skill name mismatch')
        require(re.search(r'^description: .+', front, re.M), 'Missing skill description')
        require('TODO' not in body, 'Unfinished skill scaffold')
        require((skill.parent / 'agents/openai.yaml').is_file(), 'Missing UI metadata')
    checked = 0
    for md in ROOT.rglob('*.md'):
        if '.git' in md.parts:
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', md.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            path = target.split('#', 1)[0]
            require((md.parent / path).exists(), f'Broken link in {md}: {target}')
            checked += 1
    print(f'PASS: manifests, marketplace, skill metadata, and {checked} local links')


if __name__ == '__main__':
    main()
