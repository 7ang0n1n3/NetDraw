# Changelog

## v1.1.7 - 2026-08-06

- Updated the displayed NetDraw version to `v1.1.7`.
- Added object resize handles for selected nodes, with saved custom dimensions and backward-compatible automatic sizing for existing diagrams.
- Added connections between zones and objects, including zone-to-zone and zone-to-node links using the existing side-point routing model.
- Added `Down`, `Missing`, and `Unavailable` effects/status entries for nodes.
- Fixed zone connection hit testing so the temporary connection preview does not block zone targets.

## v1.1.6 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.6`.
- Added a top palette control to collapse or expand all object sections at once.

## v1.1.5 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.5`.
- Added an A-AUTO palette section under HULFT with product-fit icons for cross-platform job scheduling, batch jobs, progress monitoring, A-AUTO/LINK, ERP jobs, carryover jobs, and 24/365 operation.

## v1.1.4 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.4`.
- Added a HULFT palette section under Azure with product-fit icons for HULFT10 file transfer, management information, jobs, triggers, code conversion, ciphering, cloud storage, logs, and clustering.

## v1.1.3 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.3`.
- Added an Azure palette section under Google Cloud Platform with 624 entries from the official Microsoft Azure Architecture Icons SVG package.

## v1.1.2 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.2`.
- Added a Google Cloud Platform palette section under AWS with 250 entries from the official Google Cloud icon packages.

## v1.1.1 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.1`.
- Added an AWS palette section under Docker with 305 AWS service entries from the official AWS Architecture Icons package.

## v1.1.0 - 2026-08-05

- Updated the displayed NetDraw version to `v1.1.0`.
- Added page-level Journey workflows with step authoring, object picking, captions, camera focus, and playback controls.

## v1.0.0 - 2026-08-05

- Started versioning at `v1.0.0` and displayed the version next to the NetDraw name in the top-left header.
- Added connection endpoint points so lines can attach to the top, right, bottom, or left side of each object.
- Added connection arrow options for start, end, and two-way directions.
- Changed animated traffic flow so start and end arrow connections flow toward the arrow.
- Added connection route choices: curved, straight, and elbow.
- Added draggable bend handles for selected elbow connections.
- Added object ordering controls for selected nodes, zones, swimlanes, and connections.
- Fixed the connection properties panel delete button.

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
