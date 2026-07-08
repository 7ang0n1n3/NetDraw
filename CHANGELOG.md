# Changelog

## 2026-07-08

- Added bottom page tabs for multi-page diagrams, including add, rename, switch, and delete page actions.
- Changed JSON save/load to use one portable document file containing all pages, while keeping old single-page JSON imports compatible.
- Added Docker palette section with Docker, Container, Image, Volume, Network, and Port items.
- Added light/dark mode toggle in the top toolbar.
- Made SVG-rendered nodes, labels, edge chips, zones, handles, and hint/editor overlays theme-aware.
- Added browser-local diagram restore on startup, with clear-canvas fallback when no valid save exists.
- Changed empty-canvas dragging to pan by default; `Shift`+drag keeps marquee selection.
- Made left sidebar palette sections collapsible and persisted their collapsed state locally.
- Moved Load Balancer into the Network palette section.
- Added server palette items: Mainframe, Solaris, Server Appliance, and ESX.
- Added People & Misc palette items: SMS and Call; moved Fax into People & Misc.
- Hardened JSON import and local restore with document normalization and validation.
- Fixed duplicated swimlanes sharing lane arrays with the original.
- Fixed GIF export selection restoration after export failures.
- Added README and changelog documentation.
