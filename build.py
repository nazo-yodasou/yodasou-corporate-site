"""project/*.dc.html を GitHub Pages 用の静的HTMLに変換する。"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = {
    "Main.dc.html": "index.html",
    "About.dc.html": "about.html",
    "Faq.dc.html": "faq.html",
    "Contact.dc.html": "contact.html",
}
KV = ["KV-Kudan-A", "KV-Kudan-B", "KV-Clock", "KV-Radio", "KV-RouteEnigma"]
for name in KV:
    PAGES[f"{name}.dc.html"] = f"kv/{name.lower()}.html"


def convert(src: str, out: str) -> str:
    helmet = re.search(r"<helmet>(.*?)</helmet>", src, re.S).group(1).strip()
    body = re.search(r"<x-dc>(.*?)</x-dc>", src, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).strip()
    head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
    head = head.replace('<script src="./support.js"></script>', "")
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">')
    depth = "../" if "/" in out else ""
    for s, d in PAGES.items():
        body = body.replace(f'href="{s}"', f'href="{depth}{d}"')
    lang = re.search(r'<html lang="([^"]+)"', src).group(1)
    return f'<!doctype html>\n<html lang="{lang}">\n<head>{head.rstrip()}\n{helmet}\n</head>\n<body>\n{body}\n</body>\n</html>\n'


for s, d in PAGES.items():
    dest = ROOT / d
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(convert((ROOT / "project" / s).read_text(encoding="utf-8"), d), encoding="utf-8")
    print(s, "->", d)
