"""pass 7d (from the 7a chain): p6i -> p7d. The approved neumorphic Ink look app-wide: palette onto Ink, the neu stylesheets, the v3 screens'
neu template, the dial hero and the clay rise, and the few JSX hooks they need. Function is untouched."""
import re, sys, os
S = '/tmp/claude-0/-home-user/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/p7d/'
B = '/mnt/project-files/meridian/evolve/base7/'
src = open(B + 'meridian-src-p6i.html').read()
sys.path.insert(0, S); import r24; src = r24.apply(src); import r25; src = r25.apply(src)  # review r24 first, then the look

def rep(s, a, b, n=1):
    c = s.count(a)
    if c != n: sys.exit(f'patch count {c} != {n}: {a[:90]!r}')
    return s.replace(a, b)

# ---- 1. palette: warm black and cream become Ink and its cool cream (every theme block, every shadow sheet, inline styles) ----
PAL = [('243,237,228', '232,239,248'), ('243, 237, 228', '232, 239, 248'), ('242,239,233', '232,239,248'), ('14,13,12', '29,38,51'), ('14, 13, 12', '29, 38, 51'),
       ('142,147,232', '152,162,252'), ('143,136,126', '154,163,178')]
HEX = [('#F3EDE4', '#E8EFF8'), ('#F2EFE9', '#E8EFF8'), ('#0E0D0C', '#1D2633'), ('#161513', '#202936'), ('#1F1D1A', '#222B39'), ('#292622', '#27303E'),
       ('#26231F', '#27303E'), ('#22201D', '#242D3A'), ('#24211E', '#242D3A'), ('#191816', '#252E3C'), ('#070706', '#131923'), ('#121110', '#171E29'),
       ('#1A1917', '#1F2836'), ('#8F887E', '#9AA3B2'), ('#8E93E8', '#98A2FC'), ('#0B1019', '#1D2633'), ('#1C1916', '#1D2633')]
for a, b in PAL: src = src.replace(a, b)
for a, b in HEX: src = re.sub(re.escape(a), b, src, flags=re.I)

# ---- 2. JSX hooks ----
# the dial reads each light's routine and amount
src = rep(src, "const L = { id: e.id || it.id + ':' + e.t, m, at: end,", "const L = { id: e.id || it.id + ':' + e.t, item: it.id, v: e.v, m, at: end,")
# rows carry their routine's hue (as light: the groove, the done key, the glyph) and a progress groove
src = rep(src, "return <div className={cx('zrow', lead && 'lead', q && 'full', comp && 'completing', holding && holding.cls === 'lingering' && 'lingering')} data-tile={it.id} data-row={it.id}>",
  "const n7pr = ev.state === 'met' ? 100 : ev.tg && ev.tg.v && ev.tg.cmp !== 'none' ? Math.min(100, 100 * (ev.v || 0) / ev.tg.v) : 0; /* 7a: the row's groove fills with its period */\n"
  "  return <div className={cx('zrow', hueCls(it), lead && 'lead', q && 'full', comp && 'completing', holding && holding.cls === 'lingering' && 'lingering')} style={hueStyle(it)} data-tile={it.id} data-row={it.id}>\n"
  "    <span className=\"zinl\" aria-hidden=\"true\"><i style={{ height: n7pr + '%' }} /></span>")
# the stored hue shows as the nearest of the six Ink hues (display only; the record is never rewritten)
src = rep(src, "    .map(it => ({ ...it, targets: it.targets.filter(t => t.from <= today || t.future),", "    .map(it => ({ ...it, hue: typeof neuHue === 'function' ? neuHue(it) : it.hue, targets: it.targets.filter(t => t.from <= today || t.future),")
src = rep(src, "const items0 = t3SampleItems(s); const byId = {};", "const items0 = t3SampleItems(s).map(it => typeof neuHue === 'function' && it.hue != null ? { ...it, hue: neuHue(it) } : it); const byId = {};")
src = rep(src, "const HUES = [195, 232, 268, 310, 350, 30, 70, 140];", "const HUES = [82, 232, 138, 178, 300, 8]; /* 7a: the six Ink hues; night and ember are reserved */")
src = rep(src, "const [hue, setHue] = useState(195);", "const [hue, setHue] = useState(232);")
src = rep(src, "background: `oklch(.7 .12 ${hue})`", "background: `oklch(.76 .14 ${hue})`")
# Today's hero: the dial
src = rep(src, "<T3Arc db={db} onOpen={() => S.sheet.open({ k: 'day3' })} dayOne={db.today === firstUse(db)} />", "<NeuDial db={db} onOpen={() => S.sheet.open({ k: 'day3' })} dayOne={db.today === firstUse(db)} />")
# Ink is the design in every appearance (the v3 screens were dark-only already)
src = rep(src, "if (theme === 'auto') r.removeAttribute('data-theme'); else r.setAttribute('data-theme', theme);", "r.setAttribute('data-theme', 'dark'); /* 7a: Ink in every appearance */")
src = rep(src, "        <div className=\"eyebrow\" style={{ margin: '16px 0 8px' }}>Appearance</div>\n        <Seg options={[{ v: 'auto', l: 'System' }, { v: 'light', l: 'Light' }, { v: 'dark', l: 'Dark' }]} value={S.theme} onChange={S.setTheme} />\n", "")
a = src.index("    { l: 'Appearance', kw: 'dark mode, light, theme, colours, colors'"); b = src.index('\n', a)
src = src[:a] + src[b + 1:]
# the v3 screens' stylesheet gains the neu layer
src = rep(src, "return rd('common') + '\\n' + (scr && scr !== 'common' ? rd(scr) : ''); };", "return rd('common') + '\\n' + (scr && scr !== 'common' ? rd(scr) : '') + '\\n' + rd('neu'); };")

# ---- 3. stylesheets ----
C = S + 'css/'
light = '\n'.join(open(C + f).read() for f in ['tokens.css', 'statics.css', 'recipe-light.css', 'chrome.css', 'generic.css', 'clay.css'])
tn = open(S + 'today-neu.css').read()
# the app marks a held key with .down (pointer events); :active (keyboard, forced states) looks the same
def addact(m):
    sels = [x.strip() for x in m.group(1).split(',')]
    more = [x.replace('.down', ':active') for x in sels if '.down' in x and not x.startswith('@')]
    return ',\n'.join(sels + more) + '{'
tn = re.sub(r'(?<=[}\n])([^{}@]+)\{', addact, '\n' + tn)
light += '\n/* ---------- Today (today-neu v7 on the z-classes) ---------- */\n' + tn + '\n' + open(C + 'today-extra.css').read() + '\n' + open(C + 'plate.css').read()
# the app's older layers fight with long :is() chains and !important; an id inside :is() lifts every neu rule above them
# (it never has to match: :is() takes its most specific argument)
light = re.sub(r'(?<![\w-])\.screen(?![\w-])', ':is(.screen,#n7a)', light)
light = re.sub(r'(?<![\w-])\.t3(?=[\s])', ':is(.t3,#n7a)', light)
light = light.replace('.n7cl { isolation', ':is(.n7cl,#n7a#n7b) { isolation')
light += '\n@media (prefers-reduced-motion: reduce) { .screen *, .screen *::before, .screen *::after { transition-duration: 0s !important; } }\n'
shadow = open(C + 'recipe-shadow.css').read() + '\n' + open(C + 'shadow.css').read() + '\n' + open(C + 'clay.css').read() + '\n' + open(C + 'plate-shadow.css').read()
v3app_end = src.index('</style>', src.index('<style id="v3-app">')) + len('</style>')
src = src[:v3app_end] + '\n<style id="neu7">\n' + light + '\n</style>' + src[v3app_end:]
tpl_at = src.index('<template id="v3-css-common">')
src = src[:tpl_at] + '<template id="v3-css-neu">' + shadow + '</template>\n' + src[tpl_at:]

# ---- 4. the neu block, before block 4 ----
marker = '<script type="text/babel" data-presets="react">\n/* pass 6g: the feel picker'
i = src.index(marker)
neu = open(S + 'neu.jsx').read()
src = src[:i] + '<script type="text/babel" data-presets="react">\n' + neu + '\n</script>\n' + src[i:]
src = r25.late(src)
import r26; src = r26.late(src)  # r26: honesty (versioned period type) and the copy
import r27; src = r27.late(src)  # r27: every reading of the past by its own rule and type; units
import r28; src = r28.late(src)  # r28: Mark's calls on the 7c preview (status bar, page changes, the plate, the Time chart)
open(os.environ.get('OUT', B) + 'meridian-src-p7d.html', 'w').write(src)
print('ok', len(src))
