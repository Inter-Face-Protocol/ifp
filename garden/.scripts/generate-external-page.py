import json
import sys
from urllib.parse import quote

entries = json.load(open('/tmp/external-entries.json'))

# Group by domain, then by form type
groups = {}
for name, info in sorted(entries.items()):
    if not info['found']:
        continue
    domain = info['domain'] or 'Uncategorized'
    if domain not in groups:
        groups[domain] = {}
    ft = info['form_type'] or 'Untyped'
    if ft not in groups[domain]:
        groups[domain][ft] = []
    groups[domain][ft].append((name, info))

# Build the page
lines = []
lines.append('# External References')
lines.append('')
lines.append('Nodes referenced by this garden patch that exist in the source garden but are not included here. Each entry shows the node name, form type, and brief summary from the source garden.')
lines.append('')
lines.append('When you see `[[Node Name]]↑` in a garden node, it links here. The ↑ marker means the node exists in the source garden but is not published or included in this patch.')
lines.append('')
lines.append(f'**{sum(1 for v in entries.values() if v["found"])} nodes documented** from the source garden. {sum(1 for v in entries.values() if not v["found"])} references could not be located (may be ghost links or informal references).')
lines.append('')

# Domain order
domain_order = ['Deep Context Architecture', 'Self-Sovereign Identity', 'Synpraxis']
other_domains = sorted(d for d in groups if d not in domain_order)

for domain in domain_order + other_domains:
    if domain not in groups:
        continue
    lines.append(f'## {domain}')
    lines.append('')
    
    # Form type order within domain
    ft_order = ['Decision', 'Model Form', 'Pattern Form', 'Principle Form', 
                'Conviction Form', 'Inquiry Form', 'Gloss Form', 'Boundary Form',
                'Domain Form', 'Citation Form', 'Value Form', 'Protocol Form',
                'Case Form', 'Reference Form', 'Research Form', 'Scenario Form',
                'Skill Form', 'Opus Form', 'Form Type']
    
    seen = set()
    for ft in ft_order:
        if ft in groups[domain]:
            seen.add(ft)
            items = groups[domain][ft]
            lines.append(f'### {ft}')
            lines.append('')
            for name, info in items:
                brief = info['brief'] or info['tagline'] or '*(no summary available)*'
                lines.append(f'**{name}**: {brief}')
                lines.append('')
            
    # Any remaining form types
    for ft in sorted(groups[domain]):
        if ft not in seen:
            items = groups[domain][ft]
            lines.append(f'### {ft}')
            lines.append('')
            for name, info in items:
                brief = info['brief'] or info['tagline'] or '*(no summary available)*'
                lines.append(f'**{name}**: {brief}')
                lines.append('')

# Add not-found section
not_found = [(name, info) for name, info in sorted(entries.items()) if not info['found']]
if not_found:
    lines.append('## Not Located')
    lines.append('')
    lines.append('These references appear in the patch but could not be found in the source garden. They may be ghost links, informal references, or person/concept names.')
    lines.append('')
    for name, info in not_found:
        lines.append(f'- {name}')
    lines.append('')

print('\n'.join(lines))
