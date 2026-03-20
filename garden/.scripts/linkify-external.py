import os
import re
import sys
import json
from urllib.parse import quote

garden = sys.argv[1]
entries = json.load(open('/tmp/external-entries.json'))

# Build set of found external targets (have entries on EXTERNAL page)
found_external = set(name for name, info in entries.items() if info['found'])

skip_files = {'README.md', 'EXTERNAL.md', 'AGENTS.md'}
changed = 0

for root, dirs, files in os.walk(garden):
    for f in files:
        if f in skip_files or not f.endswith('.md'):
            continue
        filepath = os.path.join(root, f)
        file_dir = os.path.relpath(root, garden)
        
        with open(filepath) as fh:
            content = fh.read()
        
        original = content
        
        # Compute relative path to EXTERNAL.html from this file's directory
        ext_path = os.path.relpath('EXTERNAL.html', file_dir) if file_dir != '.' else 'EXTERNAL.html'
        
        def linkify_external(m):
            target = m.group(1)
            # Create text fragment URL
            # Use the bold name format from EXTERNAL.md: **Target**:
            fragment = quote(target)
            url = f'{ext_path}#:~:text={fragment}'
            return '[\\[\\[' + target + '\\]\\]↑](' + url + ')'
        
        # Match plain [[Target]]↑ (not already linkified)
        content = re.sub(r'(?<!\\)\[\[([^\]]+)\]\]↑', linkify_external, content)
        
        if content != original:
            with open(filepath, 'w') as fh:
                fh.write(content)
            changed += 1
            count = content.count('↑](') - original.count('↑](')
            if count > 0:
                print(f"  {os.path.relpath(filepath, garden)}: {count} external links")

print(f"\n{changed} files modified")
