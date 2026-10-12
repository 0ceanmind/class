import html, pathlib

cards = []
for f in sorted(pathlib.Path("contributors").glob("*.md")):
    if f.name.startswith("_"):
        continue
    user = f.stem
    lines = [l.strip() for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    line = lines[0] if lines else "(empty card)"
    cards.append((user, line[:140]))

items = "\n".join(
    f'''<a class="card" href="https://github.com/{html.escape(u)}">
  <img src="https://github.com/{html.escape(u)}.png?size=120" alt="" onerror="this.style.visibility='hidden'">
  <h3>@{html.escape(u)}</h3><p>{html.escape(l)}</p></a>'''
    for u, l in cards
)

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Class Wall</title>
<style>
body{{margin:0;background:#00111c;color:#e6fbff;font-family:system-ui,sans-serif;padding:40px}}
h1{{font-size:44px;margin:0}} .sub{{color:#6fb6c2;margin:8px 0 32px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}}
.card{{display:block;text-decoration:none;color:inherit;background:#04202c;border:1px solid #17d6e0;border-radius:14px;padding:18px;transition:transform .15s}}
.card:hover{{transform:translateY(-4px) rotate(-1deg)}}
.card img{{width:64px;height:64px;border-radius:50%;border:2px solid #17d6e0}}
.card h3{{margin:10px 0 6px;color:#17e5ee}} .card p{{margin:0}}
</style></head><body>
<h1>🧱 Class Wall</h1>
<div class="sub">{len(cards)} students have joined. Fork, add your card, open a pull request!</div>
<div class="grid">{items}</div></body></html>'''

out = pathlib.Path("site"); out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print(f"Built wall with {len(cards)} cards")
