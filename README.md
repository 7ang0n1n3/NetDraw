# NetDraw

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
- Connect nodes with styled links, labels, arrows, animated traffic, and sneakernet paths.
- Create zones and swimlanes for network segments and process lanes.
- Edit labels, metadata, disposition, effects, colors, lane names, and edge styles from the properties panel.
- Pan by dragging empty canvas, zoom with the mouse wheel or toolbar, and fit the diagram to view.
- Toggle light and dark mode from the top toolbar.
- Collapse and expand palette sections in the left sidebar.
- Save and load diagrams as JSON.
- Export diagrams as PNG, SVG, or animated GIF.
- Record the visible canvas as video with optional microphone or music audio when supported by the browser.

## Local Browser Storage

NetDraw stores the current diagram, view position, theme, and sidebar collapse state in browser `localStorage`.

On startup:

- If a valid local diagram exists, NetDraw restores it.
- If no valid local diagram exists, NetDraw starts with a clear canvas.

Use the `Save` button to export a portable JSON file. Use `Open` to import a saved JSON diagram.

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

## Project Layout

- `NetDraw.html`: Main application.
- `README.md`: Project usage notes.
- `CHANGELOG.md`: Notable changes.
