import os
os.makedirs('images', exist_ok=True)

# Profile placeholder (circular initials)
with open('images/profile.svg', 'w') as f:
    f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#a3e635"/><stop offset="1" stop-color="#3b82f6"/>
</linearGradient></defs>
<circle cx="200" cy="200" r="200" fill="url(#g)"/>
<text x="50%" y="50%" text-anchor="middle" dy="0.35em" font-family="Inter,sans-serif" font-size="160" font-weight="700" fill="#0a0a0a">PM</text>
</svg>''')

projects = [
    ("podcastiq", "PodcastIQ", "#a3e635", "wave"),
    ("whoozcooking", "WhoozCooking API", "#f97316", "grid"),
    ("f1", "F1 Tire Strategy", "#ef4444", "line"),
    ("employee", "Employee Analysis", "#8b5cf6", "bar"),
    ("ecommerce", "E-Commerce DB", "#06b6d4", "grid"),
    ("pulse", "Pulse Diagnosis", "#ec4899", "wave"),
    ("sleep", "Sleep Sentiment", "#14b8a6", "pie"),
    ("leetcode", "LeetCode", "#eab308", "code"),
]

def make_svg(slug, title, color, kind):
    vis = ""
    if kind == "bar":
        bars = [60, 120, 90, 160, 110, 140, 80, 130]
        vis = "".join(f'<rect x="{50+i*38}" y="{220-h}" width="28" height="{h}" fill="{color}" opacity="{0.4+i*0.07}"/>' for i,h in enumerate(bars))
    elif kind == "line":
        pts = "40,200 90,150 140,170 190,100 240,130 290,70 340,110 390,60"
        vis = f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>'
        vis += "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>' for x,y in [(40,200),(90,150),(140,170),(190,100),(240,130),(290,70),(340,110),(390,60)])
    elif kind == "wave":
        vis = f'<path d="M 20 150 Q 80 60 140 150 T 260 150 T 380 150" stroke="{color}" stroke-width="3" fill="none"/>'
        vis += f'<path d="M 20 180 Q 80 90 140 180 T 260 180 T 380 180" stroke="{color}" stroke-width="2" fill="none" opacity="0.5"/>'
    elif kind == "grid":
        for i in range(5):
            for j in range(8):
                op = 0.15 + ((i*j) % 5)*0.15
                vis += f'<rect x="{30+j*45}" y="{70+i*30}" width="38" height="24" fill="{color}" opacity="{op}"/>'
    elif kind == "pie":
        vis = f'<circle cx="200" cy="150" r="80" fill="none" stroke="{color}" stroke-width="30" stroke-dasharray="180 502" transform="rotate(-90 200 150)"/>'
        vis += f'<circle cx="200" cy="150" r="80" fill="none" stroke="{color}" stroke-width="30" stroke-dasharray="120 502" stroke-dashoffset="-180" opacity="0.6" transform="rotate(-90 200 150)"/>'
        vis += f'<circle cx="200" cy="150" r="80" fill="none" stroke="{color}" stroke-width="30" stroke-dasharray="100 502" stroke-dashoffset="-300" opacity="0.3" transform="rotate(-90 200 150)"/>'
    elif kind == "code":
        lines = [("{", 0), ("  function solve(nums) {", 20), ("    let map = new Map();", 40), ("    for (let i = 0; i < n; i++)", 40), ("      return result;", 60), ("  }", 20), ("}", 0)]
        for i, (t, indent) in enumerate(lines):
            vis += f'<text x="{40+indent}" y="{80+i*22}" font-family="monospace" font-size="14" fill="{color}" opacity="0.7">{t}</text>'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">
<rect width="400" height="260" fill="#111111"/>
<rect width="400" height="30" fill="#1a1a1a"/>
<circle cx="15" cy="15" r="5" fill="#ff5f56"/>
<circle cx="32" cy="15" r="5" fill="#ffbd2e"/>
<circle cx="49" cy="15" r="5" fill="#27c93f"/>
<text x="200" y="19" text-anchor="middle" font-family="monospace" font-size="11" fill="#666">{title}</text>
{vis}
<text x="20" y="245" font-family="monospace" font-size="10" fill="#666">$ analyze --dataset {slug}</text>
</svg>'''
    with open(f'images/{slug}.svg', 'w') as f:
        f.write(svg)

for p in projects:
    make_svg(*p)
print("done")
