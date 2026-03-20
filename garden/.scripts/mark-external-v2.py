import os
import re
import sys

garden = sys.argv[1]

# Build set of in-patch stems
in_patch = set()
for root, dirs, files in os.walk(garden):
    for f in files:
        if f.endswith('.md'):
            in_patch.add(f[:-3])
for root, dirs, files in os.walk(os.path.join(garden, 'citations')):
    for d in dirs:
        if d not in ('Archives', 'Renditions'):
            in_patch.add(d)

skip_files = {'README.md', 'EXTERNAL.md', 'AGENTS.md'}

changed = 0
for root, dirs, files in os.walk(garden):
    for f in files:
        if f in skip_files or not f.endswith('.md'):
            continue
        filepath = os.path.join(root, f)
        with open(filepath, 'r') as fh:
            content = fh.read()
        
        original = content
        
        # Find plain [[Target]] (not already linkified or marked)
        # Plain wikilinks look like [[Target]] NOT preceded by backslash-bracket
        # Already-linkified look like [\[\[Target\]\]](url)
        # Already-marked look like [[Target]]↑
        
        def mark_plain(m):
            target = m.group(1)
            if target in in_patch:
                return m.group(0)  # in-patch, leave as plain wikilink
            return '[[' + target + ']]↑'
        
        # Match plain [[Target]] not followed by ↑ or ↗
        # But NOT the linkified ones (which have \[\[ pattern)
        content = re.sub(r'(?<!\\)\[\[([^\]]+)\]\](?![↑↗])', mark_plain, content)
        
        if content != original:
            with open(filepath, 'w') as fh:
                fh.write(content)
            changed += 1
            added = content.count('↑') - original.count('↑')
            if added > 0:
                print(f"  {os.path.relpath(filepath, garden)}: +{added} markers")

print(f"\n{changed} files modified")
