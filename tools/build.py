import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
os.makedirs(OUT, exist_ok=True)

THEMES = {
    "light": dict(bg="#F6F3EF", card="#FFFFFF", border="#E7E0D8", text="#1B1A18", muted="#6B665F",
                  accent="#B05A2C", tile="#F8EAE0", blue="#3A55C8", blue_t="#E6EAF8", green="#2F7D5B",
                  green_t="#E2F1EA", purple="#7A52C7", purple_t="#EEE7F8", ink="#1B1A18", on_ink="#FFFFFF",
                  glow1="#F2DCCB", glow2="#DDE3F5", chip="#F1ECE6"),
    "dark": dict(bg="#171513", card="#211E1B", border="#34302B", text="#F3EEE8", muted="#A39C93",
                 accent="#E08A57", tile="#3A2A20", blue="#8DA2F5", blue_t="#232A47", green="#5CBF92",
                 green_t="#1F3A2F", purple="#B394EE", purple_t="#2E2542", ink="#F3EEE8", on_ink="#171513",
                 glow1="#3A2A20", glow2="#222A44", chip="#2A2622"),
}

SERIF = "Georgia, 'Times New Roman', 'DejaVu Serif', serif"
SANS = "-apple-system, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"

ICONS = {
    "terminal": '<polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "server": '<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/>',
    "network": '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><line x1="12" y1="7" x2="12" y2="12"/><line x1="12" y1="12" x2="5" y2="17"/><line x1="12" y1="12" x2="19" y2="17"/>',
    "activity": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "laptop": '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
    "tv": '<rect x="2" y="7" width="20" height="15" rx="2"/><polyline points="17 2 12 7 7 2"/>',
    "drive": '<line x1="22" y1="12" x2="2" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" y1="16" x2="6.01" y2="16"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>',
    "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    "gamepad": '<path d="M6 12h4M8 10v4M15 13h.01M18 11h.01"/><path d="M17.3 5H6.7a4 4 0 0 0-3.9 3.2l-1.7 8A3 3 0 0 0 4 20c1 0 1.9-.5 2.4-1.3L8 16h8l1.6 2.7c.5.8 1.4 1.3 2.4 1.3a3 3 0 0 0 2.9-3.8l-1.7-8A4 4 0 0 0 17.3 5z"/>',
    "smartphone": '<rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "flask": '<path d="M10 2v7.3L4.7 18a2 2 0 0 0 1.7 3h11.2a2 2 0 0 0 1.7-3L14 9.3V2M8.5 2h7"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.5 13.5 17 22l-5-3-5 3 1.5-8.5"/>',
    "box": '<path d="M21 16V8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4a2 2 0 0 0 1-1.7z"/><path d="M3.3 7 12 12l8.7-5M12 22V12"/>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "search": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "sliders": '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "send": '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
    "message": '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.4 8.4 0 1 1 21 11.5z"/>',
    "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>',
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
    "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
}


def icon(name, x, y, size, color, sw=1.8):
    s = size / 24.0
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def svg(w, h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="{SANS}"><defs>{defs}</defs>{body}</svg>')


def write(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
        f.write(content)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def logo(x, y, s, c):
    k = s / 64.0
    return (f'<g transform="translate({x},{y}) scale({k})">'
            f'<rect width="64" height="64" rx="16" fill="{c["ink"]}"/>'
            f'<text x="32" y="43" text-anchor="middle" font-family="{SERIF}" font-size="30" font-weight="700" fill="{c["on_ink"]}">A<tspan fill="{c["accent"]}">D</tspan></text>'
            f'</g>')


def hero(t, c):
    W, H = 900, 440
    defs = (f'<radialGradient id="g1" cx="0" cy="0" r="1"><stop offset="0" stop-color="{c["glow1"]}"/><stop offset="1" stop-color="{c["bg"]}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="g2" cx="1" cy="0.2" r="1"><stop offset="0" stop-color="{c["glow2"]}"/><stop offset="1" stop-color="{c["bg"]}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="cp"><rect width="{W}" height="{H}" rx="28"/></clipPath>')
    b = f'<g clip-path="url(#cp)"><rect width="{W}" height="{H}" fill="{c["bg"]}"/>'
    b += f'<ellipse cx="60" cy="40" rx="420" ry="260" fill="url(#g1)"/><ellipse cx="860" cy="120" rx="380" ry="260" fill="url(#g2)"/></g>'
    b += f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="28" fill="none" stroke="{c["border"]}"/>'
    b += logo(32, 26, 40, c)
    b += f'<text x="84" y="53" font-size="20" font-weight="700" fill="{c["text"]}">Adin <tspan fill="{c["accent"]}">Darvish</tspan></text>'
    nav = [("download", "Backup"), ("cloud", "Cloud"), ("network", "Network"), ("phone", "VoIP"), ("cpu", "AI")]
    x = 290
    for ic, lab in nav:
        b += icon(ic, x, 37, 16, c["muted"], 1.7)
        b += f'<text x="{x+23}" y="50" font-size="14.5" font-weight="500" fill="{c["muted"]}">{lab}</text>'
        x += 23 + len(lab) * 8 + 26
    b += f'<line x1="0" y1="86" x2="{W}" y2="86" stroke="{c["border"]}"/>'
    b += f'<text x="{W/2}" y="190" text-anchor="middle" font-family="{SERIF}" font-size="68" font-weight="700" fill="{c["text"]}">Network &amp; Cloud</text>'
    b += f'<text x="{W/2}" y="266" text-anchor="middle" font-family="{SERIF}" font-size="68" font-weight="700" fill="{c["accent"]}">Architect.</text>'
    b += f'<text x="{W/2}" y="316" text-anchor="middle" font-size="17" fill="{c["muted"]}">Enterprise networking, hybrid cloud, multi-vendor security and</text>'
    b += f'<text x="{W/2}" y="342" text-anchor="middle" font-size="17" fill="{c["muted"]}">disaster recovery design, resilient by architecture, not by accident.</text>'
    pw = 520
    px = (W - pw) / 2
    b += f'<rect x="{px}" y="368" width="{pw}" height="46" rx="23" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += icon("award", px + 20, 380, 22, c["accent"], 1.8)
    b += f'<text x="{px+54}" y="397" font-size="15.5" fill="{c["text"]}" font-weight="500">CCNA → CCNP → CCIE · Apple Certified Specialist</text>'
    return svg(W, H, b, defs)


def badge(t, c, key, label, w):
    H = 40
    b = f'<rect x="0.5" y="0.5" width="{w-1}" height="{H-1}" rx="20" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += f'<rect x="6" y="6" width="28" height="28" rx="14" fill="{c["tile"]}"/>'
    b += icon(key, 12, 12, 16, c["accent"], 2)
    b += f'<text x="44" y="25" font-size="14" font-weight="600" fill="{c["text"]}">{label}</text>'
    return svg(w, H, b)


def title(t, c, key, text):
    W, H = 900, 76
    b = f'<rect x="0" y="14" width="48" height="48" rx="14" fill="{c["tile"]}" stroke="{c["border"]}"/>'
    b += icon(key, 12, 26, 24, c["accent"], 1.8)
    b += f'<text x="66" y="48" font-family="{SERIF}" font-size="30" font-weight="700" fill="{c["text"]}">{esc(text)}</text>'
    b += f'<line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="{c["border"]}"/>'
    return svg(W, H, b)


VENDORS = ["Cisco", "MikroTik", "Juniper", "Fortinet", "Palo Alto", "Check Point", "Sophos", "Huawei",
           "Aruba", "Ubiquiti", "Proxmox", "VMware", "Veeam", "Dell EMC", "HPE", "Synology"]


def vendors(t, c):
    W = 900
    pad = 28
    b = ""
    y = 62
    x = pad
    rows = []
    cur = []
    cw = pad
    for v in VENDORS:
        w = len(v) * 8.2 + 28
        if cw + w > W - pad:
            rows.append(cur)
            cur = []
            cw = pad
        cur.append((v, w))
        cw += w + 10
    rows.append(cur)
    H = 62 + len(rows) * 48 + 14
    b += f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="24" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += icon("layers", pad, 22, 20, c["accent"], 1.8)
    b += f'<text x="{pad+30}" y="38" font-family="{SERIF}" font-size="20" font-weight="700" fill="{c["text"]}">16 vendor platforms</text>'
    for r in rows:
        x = pad
        for v, w in r:
            b += f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="18" fill="{c["chip"]}" stroke="{c["border"]}"/>'
            b += f'<text x="{x+w/2}" y="{y+23}" text-anchor="middle" font-size="14" font-weight="600" fill="{c["text"]}">{v}</text>'
            x += w + 10
        y += 48
    return svg(W, H, b)


DOMAINS = [("network", "Networking"), ("cloud", "Cloud"), ("shield", "Security"), ("drive", "Backup & DR"),
           ("server", "Servers"), ("box", "Virtualization"), ("phone", "VoIP"), ("camera", "CCTV"),
           ("laptop", "Apple"), ("activity", "Monitoring"), ("tv", "Media / IPTV"), ("cpu", "AI hosting"),
           ("code", "Automation")]


def domains(t, c):
    W = 900
    cols = 5
    gap = 15
    tw = (W - gap * (cols - 1)) / cols
    th = 66
    rows = (len(DOMAINS) + cols - 1) // cols
    H = rows * th + (rows - 1) * gap
    b = ""
    for i, (ic, lab) in enumerate(DOMAINS):
        r, k = divmod(i, cols)
        x = k * (tw + gap)
        y = r * (th + gap)
        b += f'<rect x="{x+0.5}" y="{y+0.5}" width="{tw-1}" height="{th-1}" rx="18" fill="{c["card"]}" stroke="{c["border"]}"/>'
        b += f'<rect x="{x+14}" y="{y+15}" width="36" height="36" rx="11" fill="{c["tile"]}"/>'
        b += icon(ic, x + 23, y + 24, 18, c["accent"], 1.9)
        b += f'<text x="{x+60}" y="{y+39}" font-size="14.5" font-weight="600" fill="{c["text"]}">{esc(lab)}</text>'
    return svg(W, H, b)


def certs(t, c):
    W, H = 900, 150
    cw, gap = 192, 44
    items = [("Associate", "CCNA", "Cisco", False), ("Professional", "CCNP", "Cisco", False),
             ("Expert", "CCIE", "Cisco", True), ("Specialist", "Apple", "Certified Specialist", False)]
    b = ""
    x = 0
    for i, (lab, big, sub, hi) in enumerate(items):
        fill = c["ink"] if hi else c["card"]
        tcol = c["on_ink"] if hi else c["text"]
        mcol = c["on_ink"] if hi else c["muted"]
        b += f'<rect x="{x+0.5}" y="0.5" width="{cw-1}" height="{H-1}" rx="24" fill="{fill}" stroke="{c["border"]}"/>'
        b += f'<text x="{x+24}" y="38" font-size="12.5" font-weight="700" letter-spacing="1.4" fill="{c["accent"]}">{lab.upper()}</text>'
        b += f'<text x="{x+24}" y="88" font-family="{SERIF}" font-size="38" font-weight="700" fill="{tcol}">{big}</text>'
        b += f'<text x="{x+24}" y="118" font-size="15" fill="{mcol}">{sub}</text>'
        if i < 3:
            gx = x + cw + gap / 2
            sym = "plus" if i == 2 else "arrow"
            if sym == "arrow":
                b += icon("arrow", gx - 10, H / 2 - 10, 20, c["accent"], 2.2)
            else:
                b += f'<text x="{gx}" y="{H/2+10}" text-anchor="middle" font-family="{SERIF}" font-size="32" font-weight="700" fill="{c["accent"]}">+</text>'
        x += cw + gap
    return svg(W, H, b)


SERVICES = {
    "search": ("search", "Search", "search.cloudtrix.ir", "blue", "blue_t"),
    "tv": ("tv", "TV", "tv.cloudtrix.ir", "accent", "tile"),
    "drive": ("drive", "Drive", "drive.cloudtrix.ir", "green", "green_t"),
    "panel": ("sliders", "Panel", "panel.cloudtrix.ir", "purple", "purple_t"),
}


def service(t, c, key):
    ic, name, dom, col, tint = SERVICES[key]
    W, H = 260, 170
    b = f'<clipPath id="cc"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="24"/></clipPath>'
    b = f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="24" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += f'<g clip-path="url(#cc)"><circle cx="{W-24}" cy="{H-6}" r="62" fill="{c[tint]}"/></g>'
    b += f'<rect x="22" y="22" width="46" height="46" rx="14" fill="{c[col]}"/>'
    b += icon(ic, 33, 33, 24, "#FFFFFF" if t == "light" else c["bg"], 2)
    b += f'<text x="22" y="108" font-family="{SERIF}" font-size="28" font-weight="700" fill="{c["text"]}">{name}</text>'
    b += f'<text x="22" y="130" font-size="13" fill="{c["muted"]}">{dom}</text>'
    b += f'<text x="22" y="153" font-size="13.5" font-weight="600" fill="{c[col]}">Open</text>'
    b += icon("arrow", 58, 142, 14, c[col], 2.2)
    return svg(W, H, b, f'<clipPath id="cc"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="24"/></clipPath>')


def lab(t, c):
    W, H = 900, 150
    b = f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="24" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += f'<text x="32" y="78" font-family="{SERIF}" font-size="64" font-weight="700" fill="{c["accent"]}">9</text>'
    b += f'<text x="32" y="108" font-size="15" fill="{c["muted"]}">lab topologies</text>'
    cw, gap = 58, 12
    x0 = 200
    for i in range(9):
        r, k = divmod(i, 5)
        x = x0 + k * (cw + gap) + (0 if r == 0 else 0)
        y = 30 + r * 52
        if r == 1 and i >= 5:
            pass
        b += f'<rect x="{x}" y="{y}" width="{cw}" height="40" rx="12" fill="{c["chip"]}" stroke="{c["border"]}"/>'
        b += f'<text x="{x+cw/2}" y="{y+26}" text-anchor="middle" font-size="14" font-weight="700" fill="{c["text"]}">T{i+1:02d}</text>'
    b += icon("flask", 800, 30, 40, c["accent"], 1.5)
    return svg(W, H, b)


def stats(t, c):
    W, H = 900, 110
    gap = 16
    cw = (W - gap * 3) / 4
    items = [("award", "CCIE", "Certified"), ("layers", "13", "Practice areas"), ("flask", "9", "Lab topologies"),
             ("server", "16", "Vendors")]
    b = ""
    for i, (ic, big, lab_) in enumerate(items):
        x = i * (cw + gap)
        b += f'<rect x="{x+0.5}" y="0.5" width="{cw-1}" height="{H-1}" rx="24" fill="{c["card"]}" stroke="{c["border"]}"/>'
        b += f'<rect x="{x+20}" y="27" width="56" height="56" rx="16" fill="{c["tile"]}"/>'
        b += icon(ic, x + 34, 41, 28, c["accent"], 1.8)
        b += f'<text x="{x+92}" y="60" font-family="{SERIF}" font-size="34" font-weight="700" fill="{c["text"]}">{big}</text>'
        b += f'<text x="{x+92}" y="84" font-size="14" fill="{c["muted"]}">{lab_}</text>'
    return svg(W, H, b)


def contact(t, c):
    W, H = 900, 240
    defs = f'<clipPath id="cl"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="30"/></clipPath>'
    b = f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="30" fill="{c["card"]}" stroke="{c["border"]}"/>'
    b += f'<g clip-path="url(#cl)"><circle cx="{W-60}" cy="{H+30}" r="150" fill="{c["tile"]}"/><circle cx="{W-250}" cy="{H+90}" r="110" fill="{c["blue_t"]}"/></g>'
    b += logo(48, 34, 56, c)
    b += f'<text x="48" y="150" font-family="{SERIF}" font-size="54" font-weight="700" fill="{c["text"]}">Let\'s build <tspan fill="{c["accent"]}">something.</tspan></text>'
    b += f'<text x="48" y="190" font-size="16.5" fill="{c["muted"]}">Networks, backup, cloud and self-hosted infrastructure, boring in production.</text>'
    return svg(W, H, b, defs)


TITLES = [
    ("whoami", "user", "About me"), ("do", "layers", "What I actually do"), ("certs", "award", "Certifications"),
    ("backup", "shield", "Backup, Disaster Recovery & Business Continuity"),
    ("cloud", "cloud", "Cloud, Virtualization & Hardware"), ("proxmox", "box", "Proxmox VE Ecosystem"),
    ("network", "network", "Networking & Security"), ("monitor", "activity", "Monitoring, Observability & IT Ops"),
    ("voip", "phone", "VoIP & Unified Communications"), ("cctv", "camera", "Photography & CCTV Surveillance"),
    ("apple", "laptop", "Apple Ecosystem: Devices & OS (1976–Present)"),
    ("iptv", "tv", "IPTV, Streaming & TV Brands"), ("nas", "drive", "NAS & Storage"),
    ("panels", "grid", "Control Panels & CMS"), ("ai", "cpu", "AI Self-Hosting, GPU & Models"),
    ("gaming", "gamepad", "Gaming & Game Servers"),
    ("linux", "terminal", "Linux Distributions"), ("lang", "code", "Languages, Databases & Automation"),
    ("lab", "flask", "Current lab setup"),
]

BADGES = [("website", "globe", "Website", 124), ("telegram", "send", "Telegram", 128),
          ("linkedin", "linkedin", "LinkedIn", 124), ("discord", "message", "Discord", 122),
          ("instagram", "instagram", "Instagram", 132)]

for t, c in THEMES.items():
    write("hero", t, hero(t, c))
    write("vendors", t, vendors(t, c))
    write("domains", t, domains(t, c))
    write("certs", t, certs(t, c))
    write("lab", t, lab(t, c))
    write("stats", t, stats(t, c))
    write("contact", t, contact(t, c))
    for k, ic, lab_, w in BADGES:
        write(f"b-{k}", t, badge(t, c, ic, lab_, w))
    for k, ic, tx in TITLES:
        write(f"t-{k}", t, title(t, c, ic, tx))
