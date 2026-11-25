# Maps, sources, and uncertainty

This book uses maps to answer **where** and **when** an event was documented. The [live StoryMap](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/) uses OpenStreetMap tiles with visible contributor attribution. Its pins are approximate orientation points chosen from named places or regions in cited reports. The same 15 points are bundled with the notebooks as `data/tour-stops.json`. They are not individual case coordinates or a downloadable epidemiological line list.

## Match the map to the question

| Question | Appropriate evidence | Main limit |
| --- | --- | --- |
| Where was an outbreak investigated? | Original field report or dated WHO/CDC event map | A named place may represent a broad area. |
| How did a situation change? | Two or more dated maps with consistent definitions | Reporting and boundaries can change between snapshots. |
| Where might animal-to-human emergence be possible? | [Pigott and colleagues' ecological suitability model](https://doi.org/10.7554/eLife.04395) | A modeled niche is not a map of observed human cases. |
| How many selected tour stops involve a virus? | The notebook's bundled tour metadata | Stops are editorial selections, not outbreak incidence. |

The [map catalog](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/MAP_CATALOG.md) documents candidate visuals, creators, licenses, source dates, and known third-party restrictions. Wikimedia Commons file pages must be checked individually: a page's text license does not automatically cover every map or photograph on it. The [full reference ledger](https://github.com/jltobias/JupyterLite-Ebola-1976-2026-StoryMaps/blob/main/REFERENCES.md) records underlying data sources for the maps where known.

## Reproducible event fields

A future complete registry should store `event_id`, virus species, start and end dates, geography type, source URL, report date, case definition, coordinate precision, and file revision. The [Mylne et al. dataset](https://doi.org/10.6084/m9.figshare.1168886) is a historical source, not a 1976–2026 registry. The [CDC chronology](https://www.cdc.gov/ebola/outbreaks/) and dated WHO reports cover later events. The [Wikipedia outbreak list, fixed at 13 November 2026](https://en.wikipedia.org/w/index.php?title=List_of_Ebola_outbreaks&oldid=1385469746), can help find missing events, but its community-edited counts are not imported into this book's data.

## Try the notebooks

The next three chapters are executable notebooks. The [JupyterLite Lab](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/lab/lab/index.html) opens the same notebooks with a Python kernel in your browser. Change filters and run cells; the source links remain in the records. These notebooks deliberately use Python's standard library and `IPython.display`, so no epidemiological package or hidden data download is required.
