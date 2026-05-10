"""
Run this script to generate placeholder SVG icons.
Replace with real PNG icons by placing files with the same names in content/images/.
"""

icons = {
    "seeds_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#8B5E3C" opacity="0.15" stroke="#8B5E3C" stroke-width="2"/>
  <ellipse cx="40" cy="45" rx="14" ry="18" fill="#6B8C42" opacity="0.9"/>
  <ellipse cx="40" cy="35" rx="8" ry="10" fill="#4a6b2a"/>
  <line x1="40" y1="20" x2="40" y2="12" stroke="#6B8C42" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="40" y1="16" x2="35" y2="11" stroke="#6B8C42" stroke-width="2" stroke-linecap="round"/>
  <line x1="40" y1="16" x2="45" y2="11" stroke="#6B8C42" stroke-width="2" stroke-linecap="round"/>
</svg>""",

    "plant_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#6B8C42" opacity="0.15" stroke="#6B8C42" stroke-width="2"/>
  <line x1="40" y1="65" x2="40" y2="25" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="28" cy="38" rx="12" ry="7" fill="#6B8C42" transform="rotate(-30 28 38)"/>
  <ellipse cx="52" cy="32" rx="12" ry="7" fill="#4a6b2a" transform="rotate(30 52 32)"/>
  <ellipse cx="40" cy="22" rx="10" ry="14" fill="#6B8C42" opacity="0.85"/>
</svg>""",

    "harvest_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#C17F3E" opacity="0.15" stroke="#C17F3E" stroke-width="2"/>
  <path d="M20 55 Q40 20 60 55" fill="none" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/>
  <line x1="40" y1="55" x2="40" y2="68" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/>
  <circle cx="40" cy="37" r="5" fill="#C17F3E"/>
  <circle cx="28" cy="44" r="4" fill="#C17F3E"/>
  <circle cx="52" cy="44" r="4" fill="#C17F3E"/>
</svg>""",

    "create_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#7B6B9D" opacity="0.15" stroke="#7B6B9D" stroke-width="2"/>
  <rect x="28" y="50" width="24" height="4" rx="2" fill="#8B5E3C"/>
  <path d="M32 50 L32 28 Q40 18 48 28 L48 50" fill="none" stroke="#7B6B9D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="35" cy="36" r="2" fill="#7B6B9D"/>
  <circle cx="40" cy="34" r="2" fill="#7B6B9D"/>
  <circle cx="45" cy="36" r="2" fill="#7B6B9D"/>
</svg>""",

    "culture_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#C1703E" opacity="0.15" stroke="#C1703E" stroke-width="2"/>
  <circle cx="40" cy="35" r="10" fill="none" stroke="#C1703E" stroke-width="2.5"/>
  <path d="M25 58 Q25 45 40 45 Q55 45 55 58" fill="none" stroke="#C1703E" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="27" cy="30" r="6" fill="none" stroke="#8B5E3C" stroke-width="2" opacity="0.7"/>
  <circle cx="53" cy="30" r="6" fill="none" stroke="#8B5E3C" stroke-width="2" opacity="0.7"/>
</svg>""",

    "connection_icon": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="38" fill="#4E8B7A" opacity="0.15" stroke="#4E8B7A" stroke-width="2"/>
  <circle cx="40" cy="40" r="14" fill="none" stroke="#4E8B7A" stroke-width="2"/>
  <circle cx="40" cy="40" r="22" fill="none" stroke="#4E8B7A" stroke-width="1.5" opacity="0.5"/>
  <line x1="40" y1="18" x2="40" y2="26" stroke="#4E8B7A" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="40" y1="54" x2="40" y2="62" stroke="#4E8B7A" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="18" y1="40" x2="26" y2="40" stroke="#4E8B7A" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="54" y1="40" x2="62" y2="40" stroke="#4E8B7A" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""
}

import os
out_dir = os.path.join(os.path.dirname(__file__))
for name, svg in icons.items():
    path = os.path.join(out_dir, f"{name}.svg")
    with open(path, "w") as f:
        f.write(svg)
    print(f"Created {path}")

print("Done! Replace these SVGs with real PNGs if desired.")
