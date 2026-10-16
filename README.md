# NetDraw

Current version: `v1.1.12`

NetDraw is a self-contained browser-based network diagram editor. The original app lives in `NetDraw.html` and runs locally without a build step or server. `NetDraw-shared-folder.html` is a standalone alternative that lets multiple clients exchange diagram updates through a shared folder.

This project is based on `mr-r3b00t.github.io/net_draw/` with enhancements.

## Open

Open `NetDraw.html` directly in a modern browser.

```bash
xdg-open NetDraw.html
```

If `xdg-open` is not available, open the file from your browser with `File -> Open`.

## Features

- Drag network, server, endpoint, people, Docker, HULFT, A-AUTO, place, process, and threat objects onto the canvas.
- Add AWS, Google Cloud Platform, Azure, HULFT, and A-AUTO service objects from palette sections below Docker, with cloud service names sourced from the official provider icon packages.
- Draw curved, straight, or angled connections between nodes, zones, and free canvas points, with labels, arrows, animated traffic, and sneakernet paths.
- Create zones and swimlanes for network segments and process lanes.
- Create multiple pages from bottom tabs; each page keeps its own canvas and view.
- Build page-level journey walkthroughs with ordered reveal/highlight steps and captions.
- Resize objects and zones from selection handles.
- Copy and paste selected objects or groups with their internal connections using NetDraw's in-page clipboard.
- Edit labels, metadata, disposition, effects, colors, lane names, and edge styles from the properties panel.
- Pan by dragging empty canvas, zoom with the mouse wheel or toolbar, and fit the diagram to view.
- Toggle light and dark mode from the top toolbar.
- Collapse and expand individual palette sections, or use the top palette control to collapse or expand all sections at once.
- Search palette items by item or section name using the search field above Sections.
- Save and load diagrams as one JSON file, including all pages.
- Reset the full document from the upper-right trash button after a warning confirmation.
- Export diagrams as PNG, SVG, or animated GIF. PNG and GIF exports include NetDraw and the current version in image software metadata.
- Record the visible canvas as video with optional microphone or music audio; supported browsers offer available WebM/MP4 recording formats.

## Shared Folder Collaboration

Open `NetDraw-shared-folder.html` directly in a current desktop Chrome or Edge browser with folder access enabled. All code is embedded in this HTML copy; no collaboration server or additional scripts are required. Browser policies may restrict folder access. API reference: https://developer.chrome.com/docs/capabilities/web-apis/file-system-access

### Open the same diagram on two computers

1. Make the same shared folder available on both computers, using an operating-system-mounted network share (SMB/NAS) or a locally synced folder. Both users need read/write access. A web folder URL cannot be selected directly; mount or sync it first.
2. User A opens the shared-folder HTML copy, clicks **Shared folder**, chooses **Choose shared folder**, and grants the browser read/write access.
3. Enter a diagram name and click **Create from this canvas** to create a shared document containing every page in the current canvas.
4. User B opens their HTML copy, chooses the same shared folder, and opens the named diagram from the list. Use **Refresh list** if the files are still arriving.
5. Edit normally. Changes write automatically, and clients check for new files every two seconds when active. **Save to folder** or `Ctrl+S` requests an immediate check. Export/import is not required for routine sharing.

Each user can keep their HTML copy locally. Reopening a shared diagram after restarting the browser requires choosing the shared folder and diagram again.

### Files and concurrent changes

NetDraw creates a dedicated structure inside the selected folder:

```text
NetDrawShared/
  <document UUID>/
    document.json           Initial document, written once
    changes/
      <change UUID>.json    An immutable update
      <change UUID>.json    Another client's update
```

Clients write separate change files instead of overwriting a common diagram file. Both clients merge the same history in deterministic order. Preserve the initial document and the complete `changes` directory when backing up or syncing; do not edit, rename, delete, or selectively exclude files inside a shared document directory.

- Changes to different objects or different properties merge.
- Causally later changes take precedence. Concurrent changes to the same property resolve by logical sequence number and then change ID, so clients converge regardless of arrival order or clock differences. The last physical mouse movement is not guaranteed to win.
- Deletion wins over stale edits to a deleted object or page. Concurrent page deletions that leave no pages produce a blank **Recovered page**.
- Journey step lists and drawing-order lists are whole values; competing edits within the same list resolve as one value. Concurrent object additions remain present.
- Active page, pan, zoom, and selection stay personal. Remote updates wait during an active interaction or presentation. Applying a remote update clears snapshot undo history to avoid restoring old shared content.

### Recovery and limitations

Committed changes are backed up in browser storage before being queued for writing. If the folder becomes unavailable, keep editing in the open tab; **Updates paused** indicates a problem. Reconnect the folder and use **Shared folder → Check / retry**, or wait for an automatic check. After a reload, choose the same folder and diagram to recover pending changes from that browser. Clearing browser storage or changing profiles removes access to that recovery queue. If browser storage fills up, keep the tab open and download a backup.

**Up to date with folder** means local changes were written and the currently visible folder was scanned. A cloud provider may still be uploading/downloading files, and background tabs may poll less often. Delivery speed depends on the share or sync provider.

Use **Download backup** in the Shared folder dialog for a conventional JSON snapshot. **Disconnect** waits for pending writes before returning the canvas to local-draft mode. JSON import is disabled while a shared document is open. This copy uses separate local-draft browser storage from the original application.

This is a prototype without collaborator cursors, user accounts, object locks, conflict-choice dialogs, or a history browser. Folder permissions control access. The complete change history is retained and replayed without compaction; individual files are limited to 8 MB, and browser recovery storage has its own quota.

Validation covered two browser clients using real shared browser directory handles, synchronization with HTTP networking disabled, unavailable-folder recovery after reload, concurrent merges, and real disk-file exchange. An actual NAS/SMB server or cloud sync provider still needs validation on the target machines.

## Local Browser Storage

NetDraw stores the current document, page view positions, theme, and sidebar collapse state in browser `localStorage`.

On startup:

- If a valid local diagram exists, NetDraw restores it.
- If no valid local diagram exists, NetDraw starts with a clear canvas.

Use the `Save` button to export a portable JSON file containing every page in the document. Use `Open` to import a saved JSON diagram. Older single-page NetDraw JSON files are imported as a one-page document.

The upper-right trash button performs a full reset: after confirmation, NetDraw deletes every page in the current document and starts a new blank `Page 1`.

## Pages

Use the tabs along the bottom edge of the canvas to switch pages. Click `+` to add a page, double-click a page tab to rename it, and use the trash button to delete the current page. A document must always have at least one page.

## Connections

Select a connection to edit its label, line style, route, source point, destination point, arrow direction, and animated traffic flow from the properties panel.

Choose `Curved`, `Straight`, or `Angled (elbow)` from the route selector beside the Connect tool in the top toolbar. Choosing a route activates Connect mode: click two objects to connect them, or drag between their side points. The preview and new connections use the selected route until you choose another.

To change an existing connection, select it and use `Line route` in the properties panel. Existing diagrams default to `Curved`. For `Angled (elbow)` routes, select the connection and drag the bend handles on the line to adjust its right-angle path.

Connections can be left unfinished: release a dragged connection on empty canvas, or click an object and then an empty spot in Connect mode. You can also draw a line between two empty canvas points. Select an unfinished line to reveal its free endpoint handles; drag a handle to move the endpoint or attach it to an object or zone later. Free endpoints are included in saved JSON and image exports. Press `Escape` to cancel a connection before placing its endpoint.

Connections can attach to the `Top`, `Right`, `Bottom`, or `Left` point on each object or zone. Drag from a visible object side point or use Connect mode on a zone to create a pinned connection, or change `From point` and `To point` on an existing connection.

Arrow options are `None`, `Start with`, `End with`, and `Two-way`. Animated traffic flow follows the selected start or end arrow direction; two-way arrows keep the current single-line animation behavior.

## Objects

Use the search field above `Sections` in the left palette to filter items as you type. Search ignores case and matches item and section names; use multiple words to narrow results, such as `azure storage`. Matching items appear even in collapsed sections. Clear the field or press `Escape` to restore all items and the saved section collapse state. Click a matching item or drag it onto the canvas to add it.

Select a node to show corner resize handles, then drag a handle to resize the object. Existing diagrams keep their automatic object sizes until an object is resized.

The Effects / status list includes operational states such as `Down`, `Missing`, and `Unavailable`, along with security-focused states.

Select a node, zone, swimlane, or connection to move it backward, forward, to the back, or to the front from the properties panel. Ordering is applied inside the selected item's drawing layer.

## AWS

The AWS palette section contains 305 service entries from the official AWS Architecture Icons package published on April 30, 2026. Each AWS object uses the official AWS service SVG graphic and preserves the official service name in the palette and object label.

## Google Cloud Platform

The Google Cloud Platform palette section sits directly under AWS and contains 250 de-duplicated entries from the official Google Cloud product icon packages: product category icons, core product icons, and legacy console icons. Each Google Cloud object uses the official Google Cloud SVG graphic and preserves the product or category name in the palette and object label.

## Azure

The Azure palette section sits directly under Google Cloud Platform and contains 624 de-duplicated service entries from the official Microsoft Azure Architecture Icons SVG package, version 23. Each Azure object uses the official Azure SVG graphic and preserves the service name in the palette and object label.

## HULFT

The HULFT palette section sits directly under Azure and contains product-fit icons for HULFT10 file transfer diagrams: HULFT Server, HULFT Manager, HULFT API Gateway, Send File, Receive File, File ID, Send Management Info, Receive Management Info, Transfer Group, Host Information, Job Information, File Trigger, Format Information, Code Conversion, Cipher Option, Cloud Storage Option, Operation Log, and HULFT Cluster.

## A-AUTO

The A-AUTO palette section sits directly under HULFT and contains product-fit icons for A-AUTO job scheduling diagrams: A-AUTO Scheduler, Job Network, Batch Job, Schedule Date, Progress Monitor, A-AUTO Agent, A-AUTO/LINK, A-SUPERVISION Client, ERP Job, Heterogeneous Platforms, Carryover Job, and 24/365 Operation.

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
- `Ctrl+C`: Copy selected objects
- `Ctrl+V`: Paste copied objects
- `Ctrl+D`: Duplicate selection
- `Ctrl+A`: Select all
- `Ctrl+S`: Save JSON
- `Ctrl+[`: Move selection backward
- `Ctrl+]`: Move selection forward
- `Ctrl+Shift+[`: Send selection to back
- `Ctrl+Shift+]`: Bring selection to front
- `+` / `=`: Zoom in
- `-`: Zoom out
- `Space` (hold) + drag: Pan

## Project Layout

- `NetDraw.html`: Original local application.
- `NetDraw-shared-folder.html`: Standalone shared-folder collaboration copy.
- `README.md`: Project usage notes.
- `CHANGELOG.md`: Notable changes.
- `LICENSE`: Project license.
