#!/usr/bin/env python3
"""Generates the pixel-style SVG assets for the GitHub profile README.
Run:  python3 tools/build.py   (writes into ./assets)"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(OUT, exist_ok=True)

THEMES = {
    "light": dict(bg="#f8f4ec", bg2="#f2ede3", cell="#fbf8f2", line="#e2dbcd", line2="#d6cebd",
                  text="#1d1a17", muted="#4d4843", dim="#8a8378", accent="#5b43d6", accdk="#3f2da6",
                  soft="#ece6fb", icon="#efe9dd", term="#16141f", termtx="#c9c3dc", ok="#2f9e6b"),
    "dark": dict(bg="#15131c", bg2="#1a1823", cell="#1c1a26", line="#2d2a3a", line2="#3a3649",
                 text="#f1ede4", muted="#bdb6c9", dim="#857e94", accent="#8b74ff", accdk="#5b43d6",
                 soft="#2a2445", icon="#25222f", term="#0e0d14", termtx="#c9c3dc", ok="#5fd4a0"),
}
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

# ---------------------------------------------------------------- pixel font (5x7)
G = {
 "A":".###.|#...#|#...#|#####|#...#|#...#|#...#", "B":"####.|#...#|#...#|####.|#...#|#...#|####.",
 "C":".####|#....|#....|#....|#....|#....|.####", "D":"####.|#...#|#...#|#...#|#...#|#...#|####.",
 "E":"#####|#....|#....|####.|#....|#....|#####", "F":"#####|#....|#....|####.|#....|#....|#....",
 "G":".####|#....|#....|#.###|#...#|#...#|.####", "H":"#...#|#...#|#...#|#####|#...#|#...#|#...#",
 "I":"#####|..#..|..#..|..#..|..#..|..#..|#####", "J":"..###|....#|....#|....#|#...#|#...#|.###.",
 "K":"#...#|#..#.|#.#..|##...|#.#..|#..#.|#...#", "L":"#....|#....|#....|#....|#....|#....|#####",
 "M":"#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#", "N":"#...#|##..#|#.#.#|#..##|#...#|#...#|#...#",
 "O":".###.|#...#|#...#|#...#|#...#|#...#|.###.", "P":"####.|#...#|#...#|####.|#....|#....|#....",
 "Q":".###.|#...#|#...#|#...#|#.#.#|#..#.|.##.#", "R":"####.|#...#|#...#|####.|#.#..|#..#.|#...#",
 "S":".####|#....|#....|.###.|....#|....#|####.", "T":"#####|..#..|..#..|..#..|..#..|..#..|..#..",
 "U":"#...#|#...#|#...#|#...#|#...#|#...#|.###.", "V":"#...#|#...#|#...#|#...#|#...#|.#.#.|..#..",
 "W":"#...#|#...#|#...#|#.#.#|#.#.#|##.##|#...#", "X":"#...#|#...#|.#.#.|..#..|.#.#.|#...#|#...#",
 "Y":"#...#|#...#|.#.#.|..#..|..#..|..#..|..#..", "Z":"#####|....#|...#.|..#..|.#...|#....|#####",
 "0":".###.|#...#|#..##|#.#.#|##..#|#...#|.###.", "1":"..#..|.##..|..#..|..#..|..#..|..#..|.###.",
 "2":".###.|#...#|....#|...#.|..#..|.#...|#####", "3":"####.|....#|....#|.###.|....#|....#|####.",
 "4":"#...#|#...#|#...#|#####|....#|....#|....#", "5":"#####|#....|#....|####.|....#|....#|####.",
 "6":".###.|#....|#....|####.|#...#|#...#|.###.", "7":"#####|....#|...#.|..#..|..#..|..#..|..#..",
 "8":".###.|#...#|#...#|.###.|#...#|#...#|.###.", "9":".###.|#...#|#...#|.####|....#|....#|.###.",
 "$":"..#..|.####|#.#..|.###.|..#.#|####.|..#..", "/":"....#|...#.|...#.|..#..|.#...|.#...|#....",
 "+":".....|..#..|..#..|#####|..#..|..#..|.....", "-":"...|...|...|###|...|...|...",
 "·":".|.|.|#|.|.|.", ".":".|.|.|.|.|.|#", ":":".|#|.|.|.|#|.", "!":"#|#|#|#|#|.|#",
 "'":"#|#|.|.|.|.|.", ",":".|.|.|.|.|#|#", "↗":".....|.####|...##|..#.#|.#..#|#....|.....",
 "→":".....|..#..|...#.|#####|...#.|..#..|.....", " ":"...|...|...|...|...|...|...",
 "?":".###.|#...#|....#|...#.|..#..|.....|..#..", "#":".#.#.|#####|.#.#.|.#.#.|.#.#.|#####|.#.#.",
}
G = {k: v.split("|") for k, v in G.items()}

def px_width(txt, s, track):
    w = 0
    for ch in txt:
        w += len(G.get(ch, G[" "])[0]) * s + s + track
    return w - s - track if txt else 0

def px_text(txt, x, y, s, fill, track=0, anchor="start"):
    """Render text as crisp pixel blocks. y = top edge."""
    total = px_width(txt, s, track)
    if anchor == "middle": x -= total / 2
    elif anchor == "end": x -= total
    d = []
    cx = x
    for ch in txt:
        rows = G.get(ch, G[" "])
        for r, row in enumerate(rows):
            c = 0
            while c < len(row):
                if row[c] == "#":
                    run = 1
                    while c + run < len(row) and row[c + run] == "#": run += 1
                    d.append(f"M{cx+c*s:.2f} {y+r*s:.2f}h{run*s:.2f}v{s:.2f}h{-run*s:.2f}z")
                    c += run
                else:
                    c += 1
        cx += len(rows[0]) * s + s + track
    return f'<path fill="{fill}" d="{"".join(d)}"/>' if d else ""

def t(x, y, s, fill, size, fam=SANS, weight=400, anchor="start", ls=0, op=None):
    a = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{html.escape(s)}</text>')

def wrap(s, n):
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + (1 if line else 0) > n:
            out.append(line); line = w
        else:
            line = (line + " " + w).strip()
    if line: out.append(line)
    return out

def svg(w, h, body, extra_defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img"><defs>{extra_defs}</defs>{body}</svg>')

def save(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w") as f:
        f.write(content)

# ---------------------------------------------------------------- icons (24x24 stroke)
IC = {
 "net": '<rect x="9" y="2" width="6" height="5"/><rect x="2" y="17" width="6" height="5"/><rect x="16" y="17" width="6" height="5"/><path d="M12 7v5M5 17v-3h14v3M12 12v2"/>',
 "cloud": '<path d="M7 18a5 5 0 0 1-.6-9.96A6 6 0 0 1 18 8a4.5 4.5 0 0 1-.5 10Z"/>',
 "shield": '<path d="M12 2 4 5v6c0 5 3.4 9.3 8 11 4.6-1.7 8-6 8-11V5Z"/><path d="m9 12 2 2 4-4"/>',
 "disk": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 "server": '<rect x="3" y="3" width="18" height="7" rx="1"/><rect x="3" y="14" width="18" height="7" rx="1"/><path d="M7 6.5h.01M7 17.5h.01"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/>',
 "camera": '<path d="M3 7h4l2-3h6l2 3h4v13H3Z"/><circle cx="12" cy="13" r="4"/>',
 "device": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 12 10 5 10-5M2 17l10 5 10-5"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-5 3 3 5-7"/>',
 "tv": '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 22h8M10 11.5l4-2.5v5Z"/>',
 "cpu": '<rect x="6" y="6" width="12" height="12" rx="1"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9Z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 "drive": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M12 11v5M9.5 13.5 12 11l2.5 2.5"/>',
 "panel": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
 "term": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m6 9 3 3-3 3M12 15h6"/>',
 "code": '<path d="m8 6-6 6 6 6M16 6l6 6-6 6"/>',
 "game": '<rect x="2" y="7" width="20" height="11" rx="5"/><path d="M7 11v3M5.5 12.5h3M15 11h.01M18 13h.01"/>',
 "grid": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>',
 "badge": '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 8 5-3 5 3-1.5-8"/>',
 "flask": '<path d="M9 2h6M10 2v7L4 20a1 1 0 0 0 .9 1.5h14.2A1 1 0 0 0 20 20L14 9V2"/><path d="M7 15h10"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12Z"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 3.8 5.8 3.8 9s-1.3 6.2-3.8 9c-2.5-2.8-3.8-5.8-3.8-9S9.5 5.8 12 3Z"/>',
 "tool": '<path d="M14.7 6.3a4 4 0 0 0 5 5L21 13l-8 8-3-3 8-8-1.3-1.3a4 4 0 0 1-5-5L13 2Z"/>',
}

def icon_box(x, y, size, name, c):
    s = size / 54
    inner = size * 0.44
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{c["icon"]}" stroke="{c["line2"]}"/>'
            f'<path d="M{x+size-2*s} {y+2*s}V{y+size-2*s}H{x+2*s}" fill="none" stroke="{c["line"]}" stroke-width="{3*s}"/>'
            f'<g transform="translate({x+(size-inner)/2} {y+(size-inner)/2}) scale({inner/24})" fill="none" '
            f'stroke="{c["accent"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{IC[name]}</g>')

# ---------------------------------------------------------------- hero
KINDS = [("CISCO","#1f5f8b","ASR 1001"),("MIKROTIK","#50596a","CCR2004"),("FORTINET","#9b2a22","FG-100F"),
         ("JUNIPER","#4c6b2a","MX204"),("ARISTA","#324f9c","7050X"),("PALO ALTO","#a3481f","PA-440"),
         ("HUAWEI","#8e1d2a","NE40E"),("ARUBA","#b0620f","CX 6300"),("VEEAM","#1d8a4f","VBR 12"),
         ("NOKIA","#1d4fb0","7750 SR"),("PROXMOX","#9a5212","PVE-NODE"),("SYNOLOGY","#4a4a4a","RS3621")]
LEDS = ["#5fd4a0","#5fd4a0","#f2c46b","#5fd4a0","#ee6a5a"]

def hero(c):
    W, H = 1000, 440
    cols, dw, dh, gap = 7, 128, 104, 12
    ox = (W - (cols * dw + (cols - 1) * gap)) / 2
    body = [f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>', '<g opacity=".42" mask="url(#fade)">']
    i = 0
    for r in range(4):
        for col in range(cols):
            k = KINDS[(i * 5 + i // 7) % len(KINDS)]
            x, y = ox + col * (dw + gap), 14 + r * (dh + gap)
            body.append(f'<rect x="{x}" y="{y}" width="{dw}" height="{dh}" rx="3" fill="{k[1]}"/>')
            body.append(f'<rect x="{x}" y="{y}" width="18" height="{dh}" fill="#000" opacity=".25"/>')
            for j in range(4):
                body.append(f'<circle cx="{x+30+j*9}" cy="{y+14}" r="3" fill="{LEDS[(i+j*3)%5]}"/>')
            body.append(px_text(k[2], x + 26, y + 26, 1.6, "#ffffff80", 1))
            for p in range(16):
                px_, py_ = x + 26 + (p % 8) * 12, y + dh - 30 + (p // 8) * 12
                body.append(f'<rect x="{px_}" y="{py_}" width="9" height="9" fill="#000" opacity=".45"/>')
            i += 1
    body.append('</g>')
    body.append(f'<rect width="{W}" height="{H}" fill="url(#veil)"/>')
    body.append(px_text("ADIN DARVISH", W / 2, 120, 7.2, c["text"], 7, "middle"))
    body.append(px_text("NETWORK · CLOUD ARCHITECT", W / 2, 202, 4, c["accent"], 4, "middle"))
    lines = ["Enterprise networks, hybrid cloud, multi-vendor security and backup & DR.",
             "CCIE · Apple Certified Specialist · infrastructure that stays boring in production."]
    for n, ln in enumerate(lines):
        body.append(t(W / 2, 282 + n * 30, ln, c["text"], 18, SANS, 400, "middle"))
    body.append(t(W / 2, 372, "BGP · OSPF · MPLS · ZERO TRUST · PROXMOX", c["muted"], 13, MONO, 400, "middle", 4))
    defs = (f'<linearGradient id="veil" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{c["bg"]}" stop-opacity=".5"/><stop offset=".45" stop-color="{c["bg"]}" stop-opacity=".55"/>'
            f'<stop offset=".95" stop-color="{c["bg"]}"/></linearGradient>'
            f'<radialGradient id="rg" cx=".5" cy=".42" r=".62"><stop offset=".35" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
            f'<mask id="fade"><rect width="{W}" height="{H}" fill="url(#rg)"/></mask>')
    return svg(W, H, "".join(body), defs)

# ---------------------------------------------------------------- buttons
def button(label, c, primary):
    s = 1.8
    tw = px_width(label, s, 4)
    W, H = int(tw + 48), 52
    if primary:
        face, edge, fg = c["accent"], c["accdk"], "#ffffff"
        body = (f'<rect x="1" y="1" width="{W-2}" height="{H-8}" fill="{face}" stroke="{edge}" stroke-width="2"/>'
                f'<rect x="1" y="{H-8}" width="{W-2}" height="6" fill="{edge}"/>'
                f'<path d="M{W-5} 4V{H-11}H4" fill="none" stroke="{edge}" stroke-width="4"/>'
                f'<path d="M4 {H-12}V4H{W-6}" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="3"/>')
    else:
        fg = c["text"]
        stripes = "".join(f'<rect x="2" y="{y}" width="{W-4}" height="1" fill="{c["bg2"]}"/>' for y in range(5, H - 8, 4))
        body = (f'<rect x="1" y="1" width="{W-2}" height="{H-8}" fill="{c["cell"]}" stroke="{c["line2"]}" stroke-width="2"/>{stripes}'
                f'<rect x="1" y="{H-8}" width="{W-2}" height="6" fill="{c["line2"]}"/>'
                f'<path d="M{W-4} 4V{H-10}H4" fill="none" stroke="{c["line"]}" stroke-width="3"/>')
    body += px_text(label, W / 2, (H - 8) / 2 - 3.5 * s, s, fg, 4, "middle")
    return svg(W, H, body)

# ---------------------------------------------------------------- vendor marquee
DEV = {
 "router": lambda c: f'<rect x="3" y="14" width="56" height="20" rx="4" fill="{c}"/><rect x="9" y="22" width="5" height="5" fill="#fff" opacity=".8"/><rect x="17" y="22" width="5" height="5" fill="#fff" opacity=".8"/><rect x="25" y="22" width="5" height="5" fill="#fff" opacity=".8"/><circle cx="50" cy="24" r="2.5" fill="#5fd4a0"/><path d="M14 14 10 3M48 14l4-11" stroke="#666" stroke-width="3" stroke-linecap="round"/>',
 "switch": lambda c: f'<rect x="1" y="13" width="60" height="18" rx="2" fill="{c}"/>' + "".join(f'<rect x="{6+i*6}" y="19" width="4" height="4" fill="#fff" opacity=".85"/>' for i in range(8)) + '<circle cx="56" cy="21" r="2" fill="#5fd4a0"/>',
 "fw": lambda c: f'<rect x="6" y="6" width="50" height="32" rx="3" fill="{c}"/><path d="M6 17h50M6 28h50M22 6v11M40 6v11M14 17v11M31 17v11M48 17v11M22 28v10M40 28v10" stroke="#fff" stroke-opacity=".45" stroke-width="2"/>',
 "ap": lambda c: f'<ellipse cx="31" cy="30" rx="20" ry="9" fill="{c}"/><circle cx="31" cy="29" r="3" fill="#5fd4a0"/><path d="M21 14a14 14 0 0 1 20 0M25 19a8 8 0 0 1 12 0" stroke="{c}" stroke-width="3" fill="none" stroke-linecap="round"/>',
 "server": lambda c: f'<rect x="10" y="4" width="42" height="11" rx="2" fill="{c}"/><rect x="10" y="17" width="42" height="11" rx="2" fill="{c}"/><rect x="10" y="30" width="42" height="11" rx="2" fill="{c}"/><circle cx="45" cy="9.5" r="2" fill="#5fd4a0"/><circle cx="45" cy="22.5" r="2" fill="#5fd4a0"/><circle cx="45" cy="35.5" r="2" fill="#f2c46b"/>',
}
VENDORS = [("Cisco","router","#1f5f8b"),("MikroTik","router","#50596a"),("Juniper","router","#4c6b2a"),("Arista","switch","#324f9c"),
           ("Huawei","switch","#b0233a"),("HPE Aruba","ap","#e07b12"),("UniFi","ap","#1c8fc0"),("Fortinet","fw","#d8322a"),
           ("Palo Alto","fw","#e0561f"),("Check Point","fw","#b0206f"),("Sophos","fw","#2f6fe4"),("Meraki","ap","#5a9c3a"),
           ("Veeam","server","#1d8a4f"),("Proxmox","server","#d06a10"),("Synology","server","#4a4a4a"),("Nokia","router","#1d4fb0")]

def marquee(c):
    W, H, cw = 1000, 176, 150
    top = 30
    cells = []
    n = len(VENDORS)
    for rep in range(2):
        for i, (name, k, col) in enumerate(VENDORS):
            x = (rep * n + i) * cw
            cells.append(f'<g transform="translate({x} {top})"><path d="M0 0V{H-top}" stroke="{c["line"]}"/>'
                         f'<g transform="translate({(cw-62)/2} 28)">{DEV[k](col)}</g>'
                         f'{t(cw/2, 112, name.upper(), c["muted"], 11, MONO, 400, "middle", 2.4)}</g>')
    total = n * cw
    body = (f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>'
            f'{t(0, 16, "16 vendor platforms", c["muted"], 12, MONO, 400, "start", 3.5)}'
            f'{t(W, 16, "Routing · Switching · Firewalls · Backup", c["muted"], 12, MONO, 400, "end", 3.5)}'
            f'<g mask="url(#m)"><path d="M0 {top+.5}H{W}M0 {H-.5}H{W}" stroke="{c["line"]}"/>'
            f'<g>{"".join(cells)}<animateTransform attributeName="transform" type="translate" from="0 0" to="-{total} 0" dur="48s" repeatCount="indefinite"/></g></g>')
    defs = (f'<linearGradient id="mg"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".06" stop-color="#fff"/>'
            f'<stop offset=".94" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<mask id="m"><rect width="{W}" height="{H}" fill="url(#mg)"/></mask>')
    return svg(W, H, body, defs)

# ---------------------------------------------------------------- section title
def title(txt, ic, c, sub=None):
    s = 3
    tw = px_width(txt, s, 5)
    W = int(max(64 + 20 + tw, 0) + 8)
    H = 64
    body = icon_box(2, 5, 54, ic, c) + px_text(txt, 76, (H - 7 * s) / 2, s, c["text"], 5)
    return svg(W, H, body)

# ---------------------------------------------------------------- bento (what I do)
DOMAINS = [
 ("net","ENTERPRISE NETWORKING","BGP, OSPF, MPLS and EVPN-VXLAN design, datacenter fabrics, and multi-vendor switching and routing that behaves the same on Monday as it did in the change window."),
 ("cloud","CLOUD","Azure and AWS hybrid links over VPN, ExpressRoute and Direct Connect, landing zones and IaC."),
 ("shield","SECURITY","NGFW policy, zero-trust segmentation, NAC, IDS/IPS and threat-detection pipelines."),
 ("disk","BACKUP · DR","3-2-1-1-0 design, RTO/RPO planning, immutable backups and DR runbooks."),
 ("server","SERVERS","Windows and Linux builds, clustering, patching and capacity planning."),
 ("layers","VIRTUALIZATION","vSphere with NSX-T, Proxmox VE and PBS clusters, NAS and storage design."),
 ("phone","VOIP · UC","SIP trunking, PBX deployment and call routing engineering."),
 ("camera","CCTV","NVR and VMS design, camera fleet rollout, ONVIF integration."),
 ("device","APPLE","Jamf and MDM fleets, macOS and iOS deployment, Apple Business Manager."),
 ("chart","MONITORING","Metrics, log aggregation, alerting, uptime and SLA tracking."),
 ("tv","MEDIA · IPTV","Plex, Jellyfin, Emby and FFmpeg ABR streaming pipelines."),
 ("cpu","AI HOSTING","Local LLM stacks, GPU compute and vector databases."),
 ("bolt","AUTOMATION","Ansible, Terraform, Bash, Python and CI/CD for infra configs."),
]

def card(x, y, w, h, ic, name, desc, c, big=False):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c["cell"]}" stroke="{c["line"]}"/>']
    out.append(f'<g opacity=".05" transform="translate({x+w-130} {y+h-110}) scale(7)" fill="none" stroke="{c["text"]}" stroke-width=".35">{IC[ic]}</g>')
    pad = 28 if not big else 36
    out.append(icon_box(x + pad, y + pad, 48 if not big else 54, ic, c))
    out.append(t(x + w - pad + 6, y + pad + 12, "↗", c["muted"], 13, SANS, 400, "end"))
    if big:
        a, b = name.split(" ", 1)
        out.append(px_text(a, x + pad + 76, y + pad + 2, 3, c["text"], 4))
        out.append(px_text(b, x + pad + 76, y + pad + 31, 3, c["text"], 4))
        ly = y + pad + 104
        for ln in wrap(desc, 50):
            out.append(t(x + pad, ly, ln, c["muted"], 16)); ly += 25
    else:
        out.append(px_text(name, x + pad, y + pad + 70, 1.9, c["text"], 3))
        ly = y + pad + 116
        for ln in wrap(desc, 27):
            out.append(t(x + pad, ly, ln, c["muted"], 13.5)); ly += 21
    return "".join(out)

def topo(x, y, c):
    sp = [(x + 96, y + 20), (x + 292, y + 20)]
    lf = [(x + 20 + i * 116, y + 118) for i in range(4)]
    out = []
    for a in sp:
        for b in lf:
            out.append(f'<path d="M{a[0]+40} {a[1]+40}L{b[0]+36} {b[1]}" stroke="{c["text"]}" stroke-opacity=".22" stroke-width="1.5"/>')
    for (a, b, dur) in [(sp[0], lf[2], "1.6s"), (sp[1], lf[0], "2s")]:
        out.append(f'<path d="M{a[0]+40} {a[1]+40}L{b[0]+36} {b[1]}" stroke="#5b43d6" stroke-width="2.5" stroke-dasharray="5 7">'
                   f'<animate attributeName="stroke-dashoffset" from="0" to="-48" dur="{dur}" repeatCount="indefinite"/></path>')
    for n, (sx, sy) in enumerate(sp):
        out.append(f'<rect x="{sx}" y="{sy}" width="80" height="40" fill="#5b43d6"/>')
        out.append(px_text(f"SPINE-{n+1}", sx + 40, sy + 14.75, 1.5, "#fff", 1, "middle"))
    for n, (lx, ly) in enumerate(lf):
        out.append(f'<rect x="{lx}" y="{ly}" width="72" height="34" fill="#3a3530"/>')
        out.append(px_text(f"LEAF-{n+1}", lx + 36, ly + 11.75, 1.5, "#f1ede4", 1, "middle"))
    return "".join(out)

def bento(c):
    W, cw, ch = 1000, 250, 250
    H = ch * 4
    out = [f'<rect width="{W}" height="{H}" fill="{c["cell"]}"/>']
    ic, name, desc = DOMAINS[0]
    out.append(card(0, 0, cw * 2, ch * 2, ic, name, desc, c, big=True))
    out.append(topo(36, 300, c))
    pos = [(2, 0), (3, 0), (2, 1), (3, 1)] + [(i % 4, 2 + i // 4) for i in range(8)]
    for (col, row), d in zip(pos, DOMAINS[1:]):
        out.append(card(col * cw, row * ch, cw, ch, *d, c))
    out.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="{c["line"]}"/>')
    return svg(W, H, "".join(out))

# ---------------------------------------------------------------- certifications
def certs(c):
    W, H = 1000, 120
    items = [("ASSOCIATE", "CCNA", False), ("PROFESSIONAL", "CCNP", False), ("EXPERT", "CCIE", True), ("CERTIFIED", "APPLE", False)]
    out = [f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>']
    bw, gap, x = 205, 58, 0
    for n, (sm, big, top) in enumerate(items):
        fill = c["soft"] if top else c["cell"]
        stroke = c["accent"] if top else c["line2"]
        out.append(f'<rect x="{x+1}" y="20" width="{bw}" height="84" fill="{fill}" stroke="{stroke}" stroke-width="{2 if top else 1}"/>')
        out.append(t(x + 22, 50, sm, c["dim"], 11, MONO, 400, "start", 3))
        out.append(px_text(big, x + 22, 64, 3, c["accent"] if top else c["text"], 4))
        if n < 3:
            sym = "→" if n < 2 else "+"
            out.append(px_text(sym, x + bw + gap / 2 + 1, 52, 2.6, c["dim"], 0, "middle"))
        x += bw + gap
    return svg(W, H, "".join(out))

# ---------------------------------------------------------------- service cards
SERVICES = [("search", "SEARCH", "Private search platform.", "search.cloudtrix.ir", "OPEN ↗"),
            ("tv", "TV", "Movies and shows on demand.", "tv.cloudtrix.ir", "WATCH ↗"),
            ("drive", "DRIVE", "File storage and sharing.", "drive.cloudtrix.ir", "OPEN ↗"),
            ("panel", "PANEL", "VPS hosting customer panel.", "panel.cloudtrix.ir", "SIGN IN ↗")]

def service(i, c):
    ic, name, desc, dom, cta = SERVICES[i]
    W, H = 240, 300
    out = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="{c["cell"]}" stroke="{c["line"]}"/>']
    out.append(icon_box(26, 28, 52, ic, c))
    out.append(px_text(name, 26, 104, 2.6, c["text"], 4))
    out.append(t(26, 152, desc, c["muted"], 14.5))
    dw = len(dom) * 7.6 + 18
    out.append(f'<rect x="26.5" y="170.5" width="{dw}" height="26" fill="{c["bg"]}" stroke="{c["line2"]}"/>')
    out.append(t(35, 188, dom, c["text"], 12.5, MONO))
    s = 1.7
    bw = px_width(cta, s, 4) + 36
    bx, by, bh = 26, 222, 44
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{c["accent"]}" stroke="{c["accdk"]}" stroke-width="2"/>'
               f'<rect x="{bx}" y="{by+bh}" width="{bw}" height="5" fill="{c["accdk"]}"/>'
               f'<path d="M{bx+bw-3} {by+3}V{by+bh-3}H{bx+3}" fill="none" stroke="{c["accdk"]}" stroke-width="3"/>')
    out.append(px_text(cta, bx + bw / 2, by + bh / 2 - 3.5 * s, s, "#fff", 4, "middle"))
    return svg(W, H, "".join(out))

# ---------------------------------------------------------------- lab terminal
LAB = [("vsphere-nsx", "vSphere + NSX-T overlay, micro-seg", "running"),
       ("multi-as", "MikroTik + Cisco, BGP/OSPF", "running"),
       ("pve-cluster", "Proxmox VE HA + PBS offsite sync", "running"),
       ("veeam-lab", "Veeam B&R, SureBackup-style tests", "running"),
       ("fw-bench", "Fortinet, pfSense, OPNsense + AI VLAN", "running"),
       ("observability", "Zabbix + Grafana, full-stack alerts", "running"),
       ("media-pipeline", "Plex / Jellyfin + FFmpeg restream", "running"),
       ("apple-fleet", "Jamf MDM across macOS / iOS gens", "testing"),
       ("android-roms", "AOSP builds, Magisk, TWRP", "building")]

def lab(c):
    W, H = 1000, 505
    out = [f'<rect width="{W}" height="{H}" fill="{c["cell"]}" stroke="{c["line"]}"/>',
           f'<rect width="{W}" height="{H}" fill="url(#dots)"/>']
    wx, wy, ww, wh = 36, 34, W - 72, H - 68
    out.append(f'<rect x="{wx+.5}" y="{wy+.5}" width="{ww}" height="{wh}" fill="{c["cell"]}" stroke="{c["line2"]}"/>')
    out.append(f'<rect x="{wx+1}" y="{wy+1}" width="{ww-1}" height="40" fill="{c["bg2"]}"/><path d="M{wx} {wy+41}H{wx+ww}" stroke="{c["line"]}"/>')
    for n, col in enumerate([c["accent"], c["accent"], c["line2"]]):
        out.append(f'<rect x="{wx+18+n*17}" y="{wy+15}" width="11" height="11" fill="{col}"/>')
    out.append(t(wx + ww - 18, wy + 26, "~/LAB", c["muted"], 12, MONO, 400, "end", 2.5))
    tx, ty = wx + 16, wy + 56
    out.append(f'<rect x="{tx}" y="{ty}" width="{ww-32}" height="{wh-72}" fill="{c["term"]}"/>')
    y = ty + 34
    out.append(f'<text x="{tx+22}" y="{y}" font-family="{MONO}" font-size="14"><tspan fill="#a893ff">adin@lab:~$</tspan><tspan fill="#f1ede4"> lab status</tspan></text>')
    y += 32
    out.append(t(tx + 22, y, "TOPOLOGY          STACK                                   STATE", "#857e94", 13.5, MONO, 400, "start", 0) .replace('<text', '<text xml:space="preserve"'))
    y += 8
    for name, stack, state in LAB:
        y += 26
        col = "#5fd4a0" if state == "running" else "#f2c46b"
        line = f"{name:<18}{stack:<40}"
        out.append(f'<text xml:space="preserve" x="{tx+22}" y="{y}" font-family="{MONO}" font-size="13.5"><tspan fill="{c["termtx"]}">{html.escape(line)}</tspan><tspan fill="{col}">● {state}</tspan></text>')
    y += 40
    out.append(f'<text x="{tx+22}" y="{y}" font-family="{MONO}" font-size="14"><tspan fill="#a893ff">adin@lab:~$</tspan><tspan fill="#f1ede4"> </tspan></text>')
    out.append(f'<rect x="{tx+128}" y="{y-13}" width="9" height="16" fill="#a893ff"><animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/></rect>')
    defs = f'<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="11" cy="11" r="1.1" fill="{c["line2"]}"/></pattern>'
    return svg(W, H, "".join(out), defs)

# ---------------------------------------------------------------- stats
def stats(c):
    W, H = 1000, 150
    items = [("CCIE", "Expert level"), ("13", "Practice areas"), ("9", "Lab topologies"), ("2AM", "BGP debugging")]
    out = [f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>']
    for n, (big, lab_) in enumerate(items):
        cx = 125 + n * 250
        out.append(px_text(big, cx, 30, 6, c["text"], 3, "middle"))
        out.append(t(cx, 116, lab_, c["muted"], 14, MONO, 400, "middle", 3))
    return svg(W, H, "".join(out))

# ---------------------------------------------------------------- contact
def contact(c):
    W, H = 1000, 380
    out = [f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>', f'<ellipse cx="{W/2}" cy="{H/2}" rx="460" ry="170" fill="url(#glow)"/>']
    gl = "✕○□△"
    for i in range(44):
        x = ((i * 37.3) % 96 + 2) / 100 * W
        y = ((i * 53.7) % 92 + 4) / 100 * H
        if 150 < x < 850 and 85 < y < 300: continue
        out.append(t(round(x, 1), round(y, 1), gl[i % 4], c["dim"], 14, MONO, 400, "middle", 0, .45))
    out.append(t(W / 2, 110, "Consulting · Reviews · Training", c["accent"], 15, MONO, 400, "middle", 4.5))
    out.append(px_text("LET'S BUILD SOMETHING", W / 2, 150, 4.6, c["text"], 5, "middle"))
    out.append(t(W / 2, 250, "Architecture reviews, migrations and strange routing problems.", c["muted"], 18, SANS, 400, "middle"))
    out.append(t(W / 2, 280, "Something that scales, and comes back online when things go wrong.", c["muted"], 18, SANS, 400, "middle"))
    defs = f'<radialGradient id="glow"><stop offset="0" stop-color="{c["accent"]}" stop-opacity=".13"/><stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/></radialGradient>'
    return svg(W, H, "".join(out), defs)

# ---------------------------------------------------------------- build
TITLES = {
 "t-whoami": ("$ WHOAMI", "user"), "t-do": ("WHAT I ACTUALLY DO", "grid"), "t-certs": ("CERTIFICATIONS", "badge"),
 "t-services": ("CLOUDTRIX SERVICES", "globe"), "t-backup": ("BACKUP · DR · CONTINUITY", "disk"),
 "t-cloud": ("CLOUD · VIRTUALIZATION", "cloud"), "t-proxmox": ("PROXMOX VE ECOSYSTEM", "layers"),
 "t-network": ("NETWORKING · SECURITY", "shield"), "t-monitor": ("MONITORING · IT OPS", "chart"),
 "t-voip": ("VOIP · UNIFIED COMMS", "phone"), "t-cctv": ("PHOTOGRAPHY · CCTV", "camera"),
 "t-apple": ("APPLE ECOSYSTEM", "device"), "t-iptv": ("IPTV · STREAMING · TV", "tv"),
 "t-nas": ("NAS · STORAGE", "server"), "t-panels": ("CONTROL PANELS · CMS", "tool"),
 "t-ai": ("AI SELF-HOSTING · GPU", "cpu"), "t-gaming": ("GAMING · GAME SERVERS", "game"),
 "t-android": ("ANDROID · ROMS", "device"), "t-linux": ("LINUX DISTRIBUTIONS", "term"),
 "t-lang": ("LANGUAGES · DATABASES", "code"), "t-lab": ("CURRENT LAB SETUP", "flask"),
}
BUTTONS = {"b-website": ("WEBSITE ↗", True), "b-telegram": ("TELEGRAM", False), "b-linkedin": ("LINKEDIN", False),
           "b-discord": ("DISCORD", False), "b-instagram": ("INSTAGRAM", False)}

for th, c in THEMES.items():
    save("hero", th, hero(c))
    save("vendors", th, marquee(c))
    save("domains", th, bento(c))
    save("certs", th, certs(c))
    save("lab", th, lab(c))
    save("stats", th, stats(c))
    save("contact", th, contact(c))
    for k, (txt, ic) in TITLES.items():
        save(k, th, title(txt, ic, c))
    for k, (lbl, prim) in BUTTONS.items():
        save(k, th, button(lbl, c, prim))
    for i, s in enumerate(SERVICES):
        save(f"svc-{s[1].lower()}", th, service(i, c))
print("assets:", len(os.listdir(OUT)))
