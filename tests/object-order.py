"""Browser regression checks: python3 tests/object-order.py (requires Chromium)."""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKS = r"""
<script>
try {
  let checks = 0;
  function equal(actual, expected, label) {
    if (JSON.stringify(actual) !== JSON.stringify(expected))
      throw Error(label + ': ' + JSON.stringify(actual) + ' != ' + JSON.stringify(expected));
    checks++;
  }
  const ids = root => [...root.children].map(g => g.dataset.node || g.dataset.edge || g.dataset.zone);
  const original = {
    nodes: [{id:'n1', type:'router', x:200, y:200, label:'Router'},
            {id:'n2', type:'router', x:200, y:200, label:'Router 2'}],
    edges: [{id:'e1', a:'n1', b:'n2', label:'Link', route:'straight'}],
    zones: [{id:'z1', x:100, y:100, w:300, h:300, label:'Zone', color:'#38bdf8'},
            {id:'z2', kind:'swimlane', orient:'h', lanes:['A','B'],
             x:100, y:100, w:300, h:300, label:'Lanes', color:'#38bdf8'}],
    journey:{steps:[]}
  };
  const base = ['z1','z2','e1','n1','n2'];
  function reset(picked) {
    state = normalizeState(original);
    selection = new Set(picked);
    undoStack = []; redoStack = []; lastSnap = serialize();
    renderAll();
  }
  reset([]);
  equal(ids(objectsLayer), base, 'legacy stacking');
  for (const id of base) {
    for (const mode of ['toBack','back','forward','toFront']) {
      reset([id]);
      const expected = base.filter(x => x !== id);
      const i = base.indexOf(id);
      const dest = mode === 'toBack' ? 0 : mode === 'toFront' ? base.length - 1
        : mode === 'back' ? Math.max(0,i-1) : Math.min(base.length-1,i+1);
      expected.splice(dest, 0, id);
      document.querySelector('[data-order="' + mode + '"]').click();
      equal(ids(objectsLayer), expected, id + ' ' + mode + ' button');
      const depth = undoStack.length;
      if (depth) {
        undo(); equal(ids(objectsLayer), base, 'undo');
        redo(); equal(ids(objectsLayer), expected, 'redo');
      }
    }
  }
  reset(['n1']);
  document.dispatchEvent(new KeyboardEvent('keydown', {key:'[', code:'BracketLeft', ctrlKey:true, shiftKey:true, bubbles:true}));
  const reordered = ['n1','z1','z2','e1','n2'];
  equal(ids(objectsLayer), reordered, 'keyboard send to back');
  const saved = JSON.parse(JSON.stringify(serializeDoc()));
  equal(normalizeFileDoc(saved).pages.find(p => p.id === activePageId).state.drawOrder,
    reordered, 'file save/load');
  state = normalizeState(JSON.parse(serialize())); renderAll();
  equal(ids(objectsLayer), reordered, 'reload state');
  for (const markup of [buildExportSVG().out, buildDiagramSVG(0.5).out,
      buildLiveFrameSVG(800,600,800,600,0.5)]) {
    const exported = new DOMParser().parseFromString(markup, 'image/svg+xml');
    equal(ids(exported.querySelector('#objectsLayer')), reordered, 'export stacking');
    equal(exported.querySelectorAll('#objectsLayer').length, 1, 'no duplicate export layers');
  }
  reset(['e1','n1']);
  reorderSelection('toBack');
  equal(ids(objectsLayer), ['e1','n1','z1','z2','n2'], 'mixed selection relative order');
  reset(['n1']); reorderSelection('toBack');
  state.nodes = state.nodes.filter(n => n.id !== 'n2');
  state.nodes.push({...original.nodes[0], id:'n3'});
  state.edges[0].b = 'n3';
  state.drawOrder.push('n1','deleted'); renderAll();
  equal(ids(objectsLayer), ['n1','z1','z2','e1','n3'], 'new, deleted and duplicate IDs');
  if (typeof FolderModel !== 'undefined') {
    reset([]);
    const before = FolderModel.encode(JSON.parse(JSON.stringify(serializeDoc())));
    selection = new Set(['e1']); reorderSelection('toFront');
    const after = FolderModel.encode(JSON.parse(JSON.stringify(serializeDoc())));
    const merged = FolderModel.apply(before, FolderModel.diff(before, after));
    const decoded = normalizeFileDoc(FolderModel.decode(merged));
    state = decoded.pages.find(p => p.id === activePageId).state; renderAll();
    equal(ids(objectsLayer), ['z1','z2','n1','n2','e1'], 'shared folder order round trip');
  }
  document.body.innerHTML = '<pre id="test-result">PASS ' + checks + ' checks</pre>';
} catch (error) {
  document.body.innerHTML = '<pre id="test-result">FAIL</pre>';
  document.querySelector('#test-result').textContent += '\n' + error.stack;
}
</script>
"""


def main():
    browser = shutil.which("chromium") or shutil.which("google-chrome")
    if not browser:
        raise SystemExit("Chromium is required for these browser checks")
    for name in ("NetDraw.html", "NetDraw-shared-folder.html"):
        with tempfile.TemporaryDirectory(prefix="netdraw-order-") as tmp:
            page = Path(tmp) / name
            page.write_text((ROOT / name).read_text().replace("</body>", CHECKS + "</body>"))
            result = subprocess.run(
                [browser, "--headless", "--no-sandbox", "--disable-gpu",
                 "--no-proxy-server", "--disable-background-networking",
                 f"--user-data-dir={tmp}/profile", "--dump-dom", page.as_uri()],
                capture_output=True, text=True, timeout=45,
            )
            report = re.search(r'<pre id="test-result">(.*?)</pre>', result.stdout, re.S)
            if result.returncode or not report or not report[1].startswith("PASS"):
                raise SystemExit(f"{name}: {report[1] if report else result.stderr[-3000:]}")
            print(f"{name}: {report[1]}")


if __name__ == "__main__":
    main()
