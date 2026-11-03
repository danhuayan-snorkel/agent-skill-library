#!/usr/bin/env python3
"""Check multi-host plugin manifests, skill metadata, and local references."""
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
    codex = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    claude = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    require(codex['name'] == claude['name'], 'Marketplace identity mismatch')
    codex_names = [e['name'] for e in codex['plugins']]
    claude_entries = {e['name']: e for e in claude['plugins']}
    require(len(set(codex_names)) == len(codex_names), 'Duplicate plugin names')
    require(set(codex_names) == set(claude_entries), 'Marketplace plugin mismatch')
    require(set(codex_names) == {p.name for p in (ROOT / 'plugins').iterdir() if p.is_dir()},
            'Unlisted plugin directory')
    skill_names = set()
    skill_containers = set()
    for entry in codex['plugins']:
        require(entry['source']['source'] == 'local', 'Expected relative plugin source')
        require(entry['policy']['installation'] == 'AVAILABLE', 'Plugin not available')
        require(entry['policy']['authentication'] in {'ON_INSTALL', 'ON_USE'}, 'Invalid auth policy')
        plugin = local_path(ROOT, entry['source']['path'])
        centry = claude_entries[entry['name']]
        require(local_path(ROOT, centry['source']) == plugin, 'Host source mismatch')
        portable = json.loads((plugin / 'plugin.json').read_text())
        compatibility = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
        cmanifest = json.loads((plugin / '.claude-plugin/plugin.json').read_text())
        for key in ('name', 'version', 'description'):
            require(portable[key] == compatibility[key] == cmanifest[key], f'Manifest mismatch: {key}')
        require(portable['name'] == entry['name'], 'Marketplace name mismatch')
        require(portable['version'] == centry['version'], 'Marketplace version mismatch')
        require(re.fullmatch(r'\d+\.\d+\.\d+', portable['version']), 'Invalid semantic version')
        require(portable['extensions']['com.openai']['interface'] == compatibility['interface'],
                'Interface metadata mismatch')
        skills = local_path(plugin, compatibility['skills'])
        skill_containers.add(skills)
        entries = list(skills.glob('*/SKILL.md'))
        require(bool(entries), f'Plugin has no skills: {plugin}')
        require({local_path(plugin, p) for p in centry['skills']} == {s.parent for s in entries},
                'Cross-agent declared skills mismatch')
        for skill in entries:
            body = skill.read_text()
            match = re.match(r'^---\n(.*?)\n---', body, re.S)
            require(match is not None, f'Missing frontmatter: {skill}')
            front = match[1]
            name = re.search(r'^name: (.+)$', front, re.M)
            require(name is not None and name[1] == skill.parent.name, 'Skill name mismatch')
            require(name[1] not in skill_names, 'Duplicate skill names')
            skill_names.add(name[1])
            require(re.search(r'^description: .+', front, re.M), 'Missing description')
            require('TODO' not in body, 'Unfinished skill scaffold')
            require((skill.parent / 'agents/openai.yaml').is_file(), 'Missing UI metadata')
    discovery = json.loads((ROOT / 'skills.sh.json').read_text())
    require({local_path(ROOT, p) for p in discovery['paths']} == skill_containers,
            'Portable discovery paths mismatch')
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
    print(f'PASS: {len(codex_names)} plugins, {len(skill_names)} skills, 3 manifest formats, '
          f'2 marketplaces, portable discovery, and {checked} local links')


if __name__ == '__main__':
    main()
