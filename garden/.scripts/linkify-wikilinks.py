import os
import re
import sys

garden = sys.argv[1]

# Build map of in-patch stems to their relative paths (from garden root)
stem_to_path = {}
for root, dirs, files in os.walk(garden):
    for f in files:
        if f.endswith('.md'):
            stem = f[:-3]
            rel = os.path.relpath(os.path.join(root, f), garden)
            # Convert .md to .html for GitHub Pages
            html_rel = rel[:-3] + '.html'
            stem_to_path[stem] = html_rel

# Also map compound folder names
for root, dirs, files in os.walk(os.path.join(garden, 'citations')):
    for d in dirs:
        if d not in ('Archives', 'Renditions'):
            # Compound citation: folder name = stem, lead file inside
            lead = os.path.join(root, d, d + '.md')
            if os.path.exists(lead):
                rel = os.path.relpath(lead, garden)
                html_rel = rel[:-3] + '.html'
                stem_to_path[d] = html_rel

skip_files = {'README.md', 'EXTERNAL.md', 'AGENTS.md'}

changed = 0
for root, dirs, files in os.walk(garden):
    for f in files:
        if f in skip_files or not f.endswith('.md'):
            continue
        filepath = os.path.join(root, f)
        file_dir = os.path.relpath(root, garden)
        
        with open(filepath, 'r') as fh:
            content = fh.read()
        
        original = content
        
        def linkify(m):
            full = m.group(0)
            target = m.group(1)
            after = m.group(2) if m.group(2) else ''
            
            if target not in stem_to_path:
                return full  # external or ghost — leave as-is
            
            # Compute relative path from this file's directory
            target_path = stem_to_path[target]
            if file_dir != '.':
                rel_path = os.path.relpath(target_path, file_dir)
            else:
                rel_path = target_path
            
            # URL-encode spaces
            rel_path = rel_path.replace(' ', '%20')
            # Encode parentheses for markdown link compatibility
            rel_path = rel_path.replace('(', '%28').replace(')', '%29')
            
            # Return clickable link with brackets shown
            return '[\\[\\[' + target + '\\]\\]](' + rel_path + ')' + after
        
        # Match [[Target]] optionally followed by ↑ (but only for non-↑ ones since those are external)
        # Only convert wikilinks that are NOT followed by ↑
        content = re.sub(r'\[\[([^\]]+)\]\]([↑↗]?)', 
                        lambda m: m.group(0) if m.group(2) else linkify(m), 
                        content)
        
        if content != original:
            with open(filepath, 'w') as fh:
                fh.write(content)
            changed += 1
            count = content.count('\\[\\[') - original.count('\\[\\[')
            print(f"  {os.path.relpath(filepath, garden)}: {count} links")

print(f"\n{changed} files modified")
