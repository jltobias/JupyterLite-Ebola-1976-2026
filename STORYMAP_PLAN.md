# StoryMap plan: 50 years of Ebola history, 1976–2026

The [live StoryMap](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/) lets readers travel through **50 years of Ebola history** while seeing where each selected event occurred and where it belongs in the 1976–2026 timeline. Its first release contains 15 selected stops with a persistent interactive map, year slider, event links, and source links. The timeline sits directly below the header, above the map and story on desktop and mobile. This document records the tour's design and planned expansions. It builds from the [literature review](LITERATURE_REVIEW.md), [rights-checked map catalog](MAP_CATALOG.md), and [references](REFERENCES.md). Updated 25 November 2026.

The opening screen can link to Piot and Muyembe-Tamfum's [2026 *Lancet* lectures, “50 years of Ebola research and response”](https://doi.org/10.1016/S0140-6736(26)01813-1), as companion reading. A short opening panel can introduce their themes of discovery, field investigation, community trust, research during outbreaks, and national scientific capacity. Map events and counts still need the primary investigations and dated WHO/CDC reports cited below. The article's portraits and pages are copyrighted and should not be copied into the StoryMap without permission.

## Core reading experience

Every Map Tour stop shows four persistent cues: **(1)** the active date or range on a 1976–2026 timeline, **(2)** an interactive map centered on its approximate location, **(3)** the event's virus species and name, and **(4)** a stop progress marker. Selecting a timeline event highlights its map pin; selecting a pin moves to its event card. A “View Africa” control restores the continental view. Each stop links to its cited source and a historical visual or related evidence.

Use an introductory map that frames the whole continent, followed by regional and local maps. A “then/now” toggle can show historical country labels alongside current names. A report-date badge separates the date of an outbreak from the date of the source used to describe it. Offer a text-only chronological list with the same citations for accessibility and low-bandwidth reading.

## Proposed chapter sequence

| Chapter / tour stops | Map movement | Primary visual and interpretive question |
| --- | --- | --- |
| **1976: two outbreaks** — Nzara, Maridi, Yambuku | Africa → present-day South Sudan → DRC | Locator rebuilt from [original Sudan](https://pmc.ncbi.nlm.nih.gov/articles/PMC2395561/) and [Zaire](https://pmc.ncbi.nlm.nih.gov/articles/PMC2395567/) field reports. How did investigators recognize separate outbreaks and document local spread? |
| **1977–2008: recurring emergence** — DRC, Gabon, Republic of the Congo, Uganda, Côte d’Ivoire | Africa → regional clusters | Small-multiple maps from [Mylne et al.](https://doi.org/10.1038/sdata.2014.42); an optional [1979–2008 archival map](https://commons.wikimedia.org/wiki/File:EbolaSubmit2.png). Why do outbreak locations, species, and map precision vary? |
| **2013–2016: West Africa** — Guinea, Liberia, Sierra Leone and connected locations | Forest region → country and district scales | Dated [CDC 2014 snapshot](https://commons.wikimedia.org/wiki/File:2014_West_Africa_Ebola_virus_outbreak_situation_map.jpg), a timeline of successive reports, and [WHO context](https://www.who.int/emergencies/situations/ebola-outbreak-2014-2016-west-africa). How did scale change the response? |
| **2017–2020: DRC** — Équateur, North Kivu, Ituri, and 2020 Équateur | DRC overview → separate local tours | [June 2018](https://commons.wikimedia.org/wiki/File:20180607_DRC_Congo_Ebola_DailyMap.pdf), [October 2018](https://commons.wikimedia.org/wiki/File:20181031_Map_DRC_NordKivu_Ebola_DailyMap.pdf), [May 2019](https://commons.wikimedia.org/wiki/File:20190522_DailyMap_DRC_NordKivu_Ebola2.pdf), and [August 2020](https://commons.wikimedia.org/wiki/File:ECDM_20200807_DRC_Ebola_update.pdf) maps. Which events were distinct despite overlapping years? |
| **2021–2023: Guinea and Uganda** | Guinea → Uganda | [CDC chronology](https://www.cdc.gov/ebola/outbreaks/) and [Uganda 2022 map](https://commons.wikimedia.org/wiki/File:20221115_Uganda_Ebola_Outbreak.png). What changed by report date, and what did “Sudan virus disease” mean? |
| **2025: separate DRC and Uganda events** | Uganda → DRC | [WHO Uganda 2025 report](https://www.who.int/emergencies/disease-outbreak-news/item/2025-DON566) and [October 2025 DRC map](https://commons.wikimedia.org/wiki/File:ECDM_20251003_DRC_Ebola.pdf). Why must these remain separate timeline records? |
| **2026: a changing outbreak** — DRC and affected cross-border locations | DRC/Ituri → regional locator | Compare a [June 2026 snapshot](https://commons.wikimedia.org/wiki/File:ECDM_20260604_DRC_Ebola_outbreak(1).pdf), a version-pinned [Ituri map](https://commons.wikimedia.org/wiki/File:Map_of_the_Ituri_Province_Ebola_outbreak.svg), and the [WHO report of 20 November 2026](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON630). What was known at each reporting date, and what remains unresolved? |

[Palmer et al.'s September 2026 brief](https://doi.org/10.19088/MHRN.2026.001) can accompany the 2026 stop as a linked explanation of cross-border mobility and preparedness in South Sudan. Keep the brief's August writing date visible; do not imply that corridors of travel or counties at risk are confirmed transmission locations. Its three third-party maps are [not cleared for reuse here](MAP_CATALOG.md#third-party-maps-in-the-cross-border-brief).

The 2026 stop also links the [Africa Center for Strategic Studies explainer](https://africacenter.org/spotlight/ebola-drc/) as secondary context on insecurity, access, and public communication (updated 6 November 2026). Keep its article date in the link label. Its [printable map and AFP photographs are not cleared for reuse](MAP_CATALOG.md#linked-2026-map-without-verified-reuse-rights); the tour's case facts should continue to cite the later WHO report.

## Media and visualization pattern

- One primary map per stop, with a **visible date, scale, source, and license**. Keep a transcript or text description for map-only information.
- One supporting visual when it adds a different explanation: a case time series, a source comparison, a historical photograph, a document excerpt, or a short linked video. Avoid a collection of images that repeats the map.
- Use a chart of reported cases and deaths only when the corresponding WHO/CDC report identifies whether values are suspected, probable, or confirmed. Show changes in reporting definitions as annotations rather than smoothing them away.
- Link the [CDC 1976 lecture](https://www.youtube.com/watch?v=iZ3KWjBVW2k) and [2014–2016 video](https://www.youtube.com/watch?v=XqAtVDP-ELE) as external media. Do not download or edit them without checking the individual reuse rights.
- A candidate 1995 photograph is the [CDC Kikwit hospital image](https://commons.wikimedia.org/wiki/File:H%C3%B4pital_G%C3%A9n%C3%A9ral_de_Kikwit%2C_1995.png), identified as public domain on its file page. The [CDC Museum timeline](https://cdcmuseum.org/exhibits/show/ebola/item/7) supplies narrative context but its images are not cleared for copying here.

## Map design

The live tour uses [OpenStreetMap tiles](https://www.openstreetmap.org/copyright/attribution-guide) for geographic context and displays contributor attribution on the map. Pins are approximate locators, not case coordinates. Future maps can use [Natural Earth public-domain data](https://www.naturalearthdata.com/about/terms-of-use/) for a continent and country locator, plus source-linked outbreak events and health-zone/district boundaries whose licenses have been verified. A 3D option should use terrain only for orientation; offer an equivalent 2D view and do not use perspective height to suggest case counts. If case counts are encoded as columns, label the units and source date explicitly.

Use symbol shape for geographic precision: a point for a documented settlement, a halo for approximate location, a filled polygon for reported district/health-zone extent, and a country outline for country-level evidence. Use distinct, colorblind-readable species colors plus text labels. Do not equate a large administrative polygon with every person inside it being exposed.

## Publication and data checklist

1. Create a versioned event table and source ledger, using [Mylne et al.](https://doi.org/10.6084/m9.figshare.1168886) for eligible historic records and dated WHO/CDC reports for later events. Check the Figshare item licenses before redistribution.

   Use the [fixed 13 November 2026 Wikipedia outbreak list](https://en.wikipedia.org/w/index.php?title=List_of_Ebola_outbreaks&oldid=1385469746) only as a checklist to find potentially omitted events and follow its citations back to original reports; do not ingest its changing counts or map coordinates as the source ledger.
2. For every map and media asset, record creator, source URL, license URL, data-as-of date, file revision, changes, and alt text. [MAP_CATALOG.md](MAP_CATALOG.md) is the starting inventory.
3. The [Jupyter Book](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/book/) and [JupyterLite Lab](https://jltobias.github.io/JupyterLite-Ebola-1976-2026-StoryMaps/lab/lab/index.html) now bundle the same 15-stop tour metadata. Their notebooks link each selected stop to its source and state that stop counts are not case counts.
4. Expand the live tour with more events, accessible media descriptions, and dated map layers. Keep the book and lab synchronized with each new sourced stop; verify every public destination before adding its URL to the README.
