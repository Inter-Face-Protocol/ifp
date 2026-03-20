import os
import re
import sys
import subprocess
import json

garden = sys.argv[1]
vault = sys.argv[2]

# 1. Collect all external targets (have ↑ marker)
external_targets = set()
for root, dirs, files in os.walk(garden):
    for f in files:
        if not f.endswith('.md'):
            continue
        with open(os.path.join(root, f)) as fh:
            content = fh.read()
        for m in re.finditer(r'\[\[([^\]]+)\]\]↑', content):
            external_targets.add(m.group(1))
        # Also check linkified ↑ markers
        for m in re.finditer(r'\\\[\\\[([^\]]+)\\\]\\\].*?↑', content):
            external_targets.add(m.group(1))

print(f"Found {len(external_targets)} unique external targets", file=sys.stderr)

# 2. Find each target in the vault and read its frontmatter
entries = {}
for target in sorted(external_targets):
    # Search for the file
    found = None
    for root, dirs, files in os.walk(vault):
        # Skip .claude, .git, .obsidian, ai-chats-archive-vault
        rel = os.path.relpath(root, vault)
        if any(rel.startswith(skip) for skip in ['.claude', '.git', '.obsidian', 'ai-chats-archive-vault', 'WORKTREES']):
            continue
        for f in files:
            stem = f[:-3] if f.endswith('.md') else f
            if stem == target:
                found = os.path.join(root, f)
                break
        if found:
            break
    
    if not found:
        # Check if it's a folder (compound node)
        for root, dirs, files in os.walk(vault):
            rel = os.path.relpath(root, vault)
            if any(rel.startswith(skip) for skip in ['.claude', '.git', '.obsidian', 'ai-chats-archive-vault', 'WORKTREES']):
                continue
            for d in dirs:
                if d == target:
                    lead = os.path.join(root, d, d + '.md')
                    if os.path.exists(lead):
                        found = lead
                        break
            if found:
                break
    
    if found:
        # Read frontmatter
        with open(found) as fh:
            content = fh.read()
        
        brief = ''
        tagline = ''
        
        # Extract from YAML frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            bm = re.search(r'brief_summary:\s*"([^"]*)"', fm)
            if bm:
                brief = bm.group(1)
            tm = re.search(r'tagline:\s*"([^"]*)"', fm)
            if tm:
                tagline = tm.group(1)
        
        # Determine form type from body predicates
        form_type = ''
        ft_match = re.search(r'is_a::\[\[([^\]]+)\]\]', content)
        if ft_match:
            form_type = ft_match.group(1)
        
        # Determine domain
        domain = ''
        dm_match = re.search(r'in_domain::\[\[([^\]]+)\]\]', content)
        if dm_match:
            domain = dm_match.group(1)
        
        # Get relative path in vault
        rel_path = os.path.relpath(found, vault)
        
        entries[target] = {
            'brief': brief,
            'tagline': tagline,
            'form_type': form_type,
            'domain': domain,
            'path': rel_path,
            'found': True
        }
    else:
        entries[target] = {
            'brief': '',
            'tagline': '',
            'form_type': '',
            'domain': '',
            'path': '',
            'found': False
        }

# 3. Output JSON for the next step
print(json.dumps(entries, indent=2))
