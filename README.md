# NetDraw

Current version: `v1.1.2`

NetDraw is a self-contained browser-based network diagram editor. The app lives in `NetDraw.html` and runs locally without a build step or server.

This project is based on `mr-r3b00t.github.io/net_draw/` with enhancements.

## Open

Open `NetDraw.html` directly in a modern browser.

```bash
xdg-open NetDraw.html
```

If `xdg-open` is not available, open the file from your browser with `File -> Open`.

## Features

- Drag network, server, endpoint, people, Docker, place, process, and threat objects onto the canvas.
- Add AWS and Google Cloud Platform service objects from palette sections below Docker, with service names sourced from the official provider icon packages.
- Connect nodes with styled links, labels, structured routes, arrows, animated traffic, and sneakernet paths.
- Create zones and swimlanes for network segments and process lanes.
- Create multiple pages from bottom tabs; each page keeps its own canvas and view.
- Build page-level journey walkthroughs with ordered reveal/highlight steps and captions.
- Edit labels, metadata, disposition, effects, colors, lane names, and edge styles from the properties panel.
- Pan by dragging empty canvas, zoom with the mouse wheel or toolbar, and fit the diagram to view.
- Toggle light and dark mode from the top toolbar.
- Collapse and expand palette sections in the left sidebar.
- Save and load diagrams as one JSON file, including all pages.
- Export diagrams as PNG, SVG, or animated GIF.
- Record the visible canvas as video with optional microphone or music audio when supported by the browser.

## Local Browser Storage

NetDraw stores the current document, page view positions, theme, and sidebar collapse state in browser `localStorage`.

On startup:

- If a valid local diagram exists, NetDraw restores it.
- If no valid local diagram exists, NetDraw starts with a clear canvas.

Use the `Save` button to export a portable JSON file containing every page in the document. Use `Open` to import a saved JSON diagram. Older single-page NetDraw JSON files are imported as a one-page document.

## Pages

Use the tabs along the bottom edge of the canvas to switch pages. Click `+` to add a page, double-click a page tab to rename it, and use the trash button to delete the current page. A document must always have at least one page.

## Connections

Select a connection to edit its label, line style, route, source point, destination point, arrow direction, and animated traffic flow from the properties panel.

Connection routes can be `Curved`, `Straight`, or `Elbow`. Existing diagrams default to `Curved`. For `Elbow` routes, select the connection and drag the bend handles on the line to move the structured path.

Connections can attach to the `Top`, `Right`, `Bottom`, or `Left` point on each object. Drag from a visible side point to another object to create a pinned connection, or change `From point` and `To point` on an existing connection.

Arrow options are `None`, `Start with`, `End with`, and `Two-way`. Animated traffic flow follows the selected start or end arrow direction; two-way arrows keep the current single-line animation behavior.

## Objects

Select a node, zone, swimlane, or connection to move it backward, forward, to the back, or to the front from the properties panel. Ordering is applied inside the selected item's drawing layer.

## AWS

The AWS palette section contains 305 service entries from the official AWS Architecture Icons package published on April 30, 2026. Each AWS object uses the official AWS service SVG graphic and preserves the official service name in the palette and object label.

## Google Cloud Platform

The Google Cloud Platform palette section sits directly under AWS and contains 250 de-duplicated entries from the official Google Cloud product icon packages: product category icons, core product icons, and legacy console icons. Each Google Cloud object uses the official Google Cloud SVG graphic and preserves the product or category name in the palette and object label.

## Journey

Use `Journey` to create a guided walkthrough for the current page. Add steps, pick the objects each step reveals, write captions, and play the journey with the presentation controls. Journey steps are saved in the exported JSON document with their page.

## Keyboard Shortcuts

- `V`: Select
- `C`: Connect
- `Z`: Draw zone
- `L`: Draw swimlane
- `H`: Pan tool
- `F`: Fit diagram
- `Delete` / `Backspace`: Delete selection
- `Ctrl+Z`: Undo
- `Ctrl+Y` or `Ctrl+Shift+Z`: Redo
- `Ctrl+D`: Duplicate selection
- `Ctrl+A`: Select all
- `Ctrl+S`: Save JSON
- `Ctrl+[`: Move selection backward
- `Ctrl+]`: Move selection forward
- `Ctrl+Shift+[`: Send selection to back
- `Ctrl+Shift+]`: Bring selection to front

## Project Layout

- `NetDraw.html`: Main application.
- `README.md`: Project usage notes.
- `CHANGELOG.md`: Notable changes.
