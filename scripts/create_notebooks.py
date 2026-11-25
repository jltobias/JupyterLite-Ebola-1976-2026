"""Write the three notebooks shared by Jupyter Book and JupyterLite."""

from pathlib import Path
from textwrap import dedent

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "book" / "notebooks"
OUT.mkdir(parents=True, exist_ok=True)


def md(source: str):
    return nbf.v4.new_markdown_cell(dedent(source).strip())


def code(source: str):
    return nbf.v4.new_code_cell(dedent(source).strip())


def save(name: str, cells: list) -> None:
    notebook = nbf.v4.new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
    )
    nbf.write(notebook, OUT / name)


LOAD = """
import json
from pathlib import Path

stops = json.loads(Path('../data/tour-stops.json').read_text(encoding='utf-8'))
assert len(stops) == 15
print(f'{len(stops)} curated tour stops, {min(s["year"] for s in stops)}–{max(s["year"] for s in stops)}')
"""


save("timeline.ipynb", [
    md("""
    # Timeline explorer: 1976–2026

    These are **15 editorially selected StoryMap stops**, not a count of outbreaks or patients. The 2026 outbreak is ongoing. Data: [project StoryMap](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/) and its cited reports; full [references](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/REFERENCES.md). Change the year and virus filters below, then run the cells again.
    """),
    code(LOAD),
    code("""
    start_year, end_year = 1976, 2026
    virus_filter = 'all'  # 'all', 'Ebola virus', 'Sudan virus', or 'Bundibugyo virus'
    selected = [s for s in stops if start_year <= s['year'] <= end_year
                and (virus_filter == 'all' or s['virus'] == virus_filter)]
    for s in selected:
        print(f"{s['year']} | {s['virus']:<17} | {s['place']} | {s['title']}")
    print(f'\\n{len(selected)} selected stops; this is not an outbreak or case total.')
    """),
    md("""
    ## A visual index of selected stops

Each dot is one tour stop. Horizontal position is the stop's year; color identifies the virus named in that stop. Multiple dots in a year can represent separate events. This chart does not encode outbreak size.
    """),
    code("""
    from html import escape
    from IPython.display import SVG, display

    colors = {'Ebola virus': '#b85639', 'Sudan virus': '#326c9e',
              'Bundibugyo virus': '#80619b'}
    rows = {'Ebola virus': 95, 'Sudan virus': 175, 'Bundibugyo virus': 255}
    x = lambda year: 125 + (year - 1976) * 15.5
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="950" height="335" viewBox="0 0 950 335" role="img" aria-label="Selected Ebola tour stops by year and virus">',
             '<rect width="950" height="335" fill="#f8f6f1"/>']
    for year in [1976, 1986, 1996, 2006, 2016, 2026]:
        xx = x(year)
        parts += [f'<line x1="{xx}" y1="54" x2="{xx}" y2="285" stroke="#d5d9d6"/>',
                  f'<text x="{xx}" y="315" text-anchor="middle" font-size="13" fill="#485b60">{year}</text>']
    for virus, yy in rows.items():
        parts += [f'<text x="12" y="{yy+5}" font-size="13" fill="#263f48">{escape(virus)}</text>',
                  f'<line x1="125" y1="{yy}" x2="900" y2="{yy}" stroke="#ccd4d1"/>']
    for s in selected:
        xx, yy = x(s['year']), rows[s['virus']]
        parts.append(f'<circle cx="{xx}" cy="{yy}" r="9" fill="{colors[s["virus"]]}" stroke="white" stroke-width="2"><title>{escape(str(s["year"]) + " · " + s["place"] + " · " + s["title"])}</title></circle>')
    parts.append('</svg>')
    display(SVG(''.join(parts)))
    """),
    md("""
    **Check the sources:** The [1976 Sudan](https://pmc.ncbi.nlm.nih.gov/articles/PMC2395561/) and [Zaire](https://pmc.ncbi.nlm.nih.gov/articles/PMC2395567/) investigations establish separate first stops. [WHO's 20 November 2026 report](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON630) provides the final stop's dated context. The bundled table is a tour index, not the WHO or CDC surveillance dataset.
    """),
])


save("geography.ipynb", [
    md("""
    # Geographic locator lab

This plot shows **approximate StoryMap orientation points** on longitude and latitude axes. It has no country outlines or case coordinates. Open the [interactive 2D StoryMap](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/) for geographic context and source links at each stop. All locations and event descriptions are recorded in the project [references](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/REFERENCES.md).
    """),
    code(LOAD),
    code("""
    start_year, end_year = 1976, 2026
    virus_filter = 'all'
    selected = [s for s in stops if start_year <= s['year'] <= end_year
                and (virus_filter == 'all' or s['virus'] == virus_filter)]
    print(f'{len(selected)} approximate locators selected.')
    """),
    code("""
    from html import escape
    from IPython.display import SVG, display

    colors = {'Ebola virus': '#b85639', 'Sudan virus': '#326c9e',
              'Bundibugyo virus': '#80619b'}
    # Equirectangular coordinate view; this is not a basemap or risk surface.
    x = lambda lon: 90 + (lon + 20) / 65 * 760
    y = lambda lat: 510 - (lat + 35) / 60 * 440
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="930" height="570" viewBox="0 0 930 570" role="img" aria-label="Approximate tour stop coordinates in Africa">',
             '<rect width="930" height="570" fill="#f8f6f1"/>',
             '<rect x="90" y="70" width="760" height="440" fill="#e6f0ec" stroke="#829b9b"/>']
    for lon in [-20, 0, 20, 40]:
        xx = x(lon)
        parts += [f'<line x1="{xx}" y1="70" x2="{xx}" y2="510" stroke="#c9d9d7"/>',
                  f'<text x="{xx}" y="534" text-anchor="middle" font-size="12">{lon}°</text>']
    for lat in [-30, -10, 10]:
        yy = y(lat)
        parts += [f'<line x1="90" y1="{yy}" x2="850" y2="{yy}" stroke="#c9d9d7"/>',
                  f'<text x="48" y="{yy+4}" font-size="12">{lat}°</text>']
    for s in selected:
        xx, yy = x(s['lon']), y(s['lat'])
        tooltip = escape(f"{s['year']} · {s['place']} · {s['virus']}")
        parts.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="8" fill="{colors[s["virus"]]}" stroke="white" stroke-width="2"><title>{tooltip}</title></circle>')
    parts += ['<text x="470" y="558" text-anchor="middle" font-size="14" fill="#263f48">Longitude · approximate locators, not case locations</text>', '</svg>']
    display(SVG(''.join(parts)))
    """),
    code("""
    for s in selected:
        print(f"{s['year']} | ({s['lat']:.2f}, {s['lon']:.2f}) | {s['place']} | {s['sourceUrl']}")
    """),
    md("""
    The coordinates simplify places named in source reports. A health zone, district, or region should be mapped with its own documented boundary when doing epidemiology. The [map catalog](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/MAP_CATALOG.md) identifies maps with known creators, dates, data provenance, and reuse conditions. An ecological suitability map such as [Pigott et al.](https://doi.org/10.7554/eLife.04395) answers a different question from a map of observed human cases.
    """),
])


save("sources.ipynb", [
    md("""
    # Source audit: follow a stop to its evidence

The tour metadata records a source and visual link for each stop. This notebook checks that links are present and displays a small source ledger; it does **not** fetch live pages or certify that source contents are unchanged. For publication details and media rights, use [REFERENCES.md](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/REFERENCES.md) and the [map catalog](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/MAP_CATALOG.md).
    """),
    code(LOAD),
    code("""
    required = ['id', 'year', 'virus', 'lat', 'lon', 'source', 'sourceUrl', 'visual', 'visualUrl']
    missing = [(s.get('id', '?'), key) for s in stops for key in required if key not in s]
    non_https = [(s['id'], key) for s in stops for key in ('sourceUrl', 'visualUrl')
                 if not s[key].startswith('https://')]
    assert not missing, missing
    assert not non_https, non_https
    assert len({s['id'] for s in stops}) == len(stops)
    print('All 15 stops have unique IDs and required, HTTPS source and visual links.')
    """),
    code("""
    from html import escape
    from urllib.parse import urlparse
    from IPython.display import HTML, display

    start_year, end_year = 1976, 2026
    selected = [s for s in stops if start_year <= s['year'] <= end_year]
    rows = []
    for s in selected:
        domain = urlparse(s['sourceUrl']).netloc
        rows.append('<tr>' + ''.join(f'<td>{escape(str(value))}</td>' for value in
                    (s['year'], s['title'], s['virus'], domain)) + '</tr>')
    table = ('<table><caption>Selected tour stops and source domains; not case counts</caption>'
             '<thead><tr><th>Year</th><th>Stop</th><th>Virus</th><th>Source domain</th></tr></thead>'
             '<tbody>' + ''.join(rows) + '</tbody></table>')
    display(HTML(table))
    """),
    code("""
    for s in selected:
        print(f"{s['year']} · {s['title']}\\n  Evidence: {s['source']}\\n  {s['sourceUrl']}\\n  Visual: {s['visual']}\\n  {s['visualUrl']}\\n")
    """),
    md("""
    **Reading the ledger:** A link to a figure does not confer image reuse rights. The 2026 stop cites [WHO's 20 November report](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON630) for provisional outbreak facts, while an [ERCC map dated 4 June](https://commons.wikimedia.org/wiki/File:ECDM_20260604_DRC_Ebola_outbreak(1).pdf) is explicitly an early visual snapshot. The [Wikipedia outbreak list](https://en.wikipedia.org/w/index.php?title=List_of_Ebola_outbreaks&oldid=1385469746) can help find omissions but is not imported as a surveillance table.
    """),
])

print("Wrote three book and lab notebooks to", OUT)
