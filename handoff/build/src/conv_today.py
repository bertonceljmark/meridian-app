"""Port today-neu's neumorphic layers (shell.html, from the NEUMORPHIC SURFACE layer to the end of the style)
onto the app's Today (pass 6a's z-classes), scoped under .t3. Chrome rules (tab bar, toast, live bar) are left
out here; they are written for the app's own DOM in neu-chrome.css. Prints the CSS."""
import re, sys
S = '/tmp/claude-0/-home-user/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/p7/'
src = open(S + 'shell-neu.css').read()
src = re.sub(r'/\*.*?\*/', '', src, flags=re.S)

MAP = {'row': 'zrow', 'rows': 'zrows', 'open': 'zopen', 'nm': 'znm', 'st': 'zst', 'level': 'zlevel', 'amt': 'zamt', 'key': 'zkey',
  'keyw': 'zkeyw', 'k-round': 'zk-round', 'k-seg': 'zk-seg', 'k-pill': 'zk-pill', 'k-word': 'zk-word', 'fill': 'zfill', 'ck': 'zck',
  'pl': 'zpl', 'livedot': 'zlivedot', 'tm': 'ztm', 'panel': 'zpanel', 'strip': 'zstrip', 'x': 'zx', 'k': 'zk', 'ttl': 'zttl',
  'ln': 'zln', 'big': 'zbig', 'mini': 'zmini', 'nights': 'znights', 'splits': 'zsplits', 'prange': 'zprange', 'r': 'zr', 't': 'zt',
  's': 'zs', 'm': 'zm', 'v': 'zv', 'weekd': 'zweekd', 'c': 'zc', 'just': 'zjust', 'later': 'zlater', 'lg': 'zlg', 'h': 'zh',
  'para': 'zpara', 'tok': 'ztok', 'tn': 'ztn', 'tf': 'ztf', 'tk': 'ztk', 'hp': 'zhp', 'sug': 'zsug', 'sn': 'zsn', 'sr': 'zsr',
  'sb': 'zsb', 'primary': 'zprimary', 'sec2': 'zsec2', 'dots': 'zdots', 'sughold': 'zsughold', 'chips': 'zchips', 'chip': 'zchip',
  'settled': 'zsettled', 'addbtn': 'zaddbtn', 'foot': 'zfoot', 'dateline': 'zdateline', 'head': 'zhead', 'sub': 'zsub',
  'hicons': 'zhicons', 'ib': 'zib', 'ctxchip': 'zctxchip', 'sec': 'zsec', 'sech': 'zsech', 'more': 'zmore', 'first': 'zfirst',
  'welcome': 'zwelcome', 'none': 'znone', 'inl': 'zinl', 'aside': 'zaside', 'tag': 'ztag', 'pv': 'zpv', 'sky': 'zsky', 'task': 'ztask',
  'act': 'zact'}
KEEP = {'on', 'done', 'down', 'anim', 'last', 'pour', 'lead', 'full', 'completing', 'leaving', 'solo', 'gap', 'best', 'some', 'w', 'dim',
  'n', 'b', 'a', 'cur', 'now', 'nt', 'miss', 'focused', 'scrubbing', 'hint', 'ls', 'li', 'hero-dial', 'dl-disc', 'dl-well', 'dl-h',
  'db', 'dbn', 'dbs', 'drec', 'dlv', 'dlvh', 'dlk', 'dlkr', 'dlkp', 'dlhour', 'rel', 'held', 'sm'}
DROP = {'arc', 'hero', 'hero-hours', 'hero-lanes', 'hsw', 'ssw', 'sbar', 'ddata', 'clk', 'topbar', 'lightsurf', 'sw8', 'swatches', 'hdot',
  'sheet', 'grab', 'sh', 'slist', 'scrim', 'btn', 'btns', 'scrub', 'stepper', 'search', 'field', 'bars7', 'splitrows', 'hyp', 'sw', 'f',
  'fk', 'tw', 'nm-r', 'grain', 'app', 'tabbar', 'tab', 'logkey', 'livebar', 'toast', 'tabfade', 'lp', 'undo', 'end', 'close', 'rm', 'dot',
  'dl-side', 'dl-night', 'dl-list', 'dl-r', 'dl-more', 'dl-empty', 'lbl', 'arcnote', 'ghost', 'h1x', 'bar', 'arrive', 'roll'}
DROP |= {c for c in re.findall(r'\.((?:hr|ln)-[\w-]+)', src)}

def conv_sel(sel):
    sel = sel.strip()
    if not sel or sel.startswith(':root') or sel == '*' or sel.startswith('html'):
        return None
    sel = re.sub(r'\.glowsurf\s+', '', sel)
    classes = re.findall(r'\.([a-zA-Z][\w-]*)', sel)
    for c in classes:
        if c in DROP: return None
        if c not in MAP and c not in KEEP:
            sys.stderr.write('unknown class ' + c + ' in ' + sel + '\n'); return None
    out = re.sub(r'\.([a-zA-Z][\w-]*)', lambda m: '.' + MAP.get(m.group(1), m.group(1)), sel)
    return '.t3 ' + out

def conv_decl(d):
    d = re.sub(r'--h(?![\w-])', '--e', d)
    for a, b in [('--surfRGB', '--nSurfRGB'), ('--surf', '--nSurf'), ('--sda', '--nSda'), ('--sla', '--nSla'), ('--sd', '--nSd'), ('--sl', '--nSl'),
                 ('--lift', '--nLift'), ('--deep', '--nDeep'), ('--tx', '--nTx'), ('--elev', '--nElev'), ('--tone', '--nTone'),
                 ('--eR1', '--nR1'), ('--eD1', '--nD1'), ('--eR', '--nR'), ('--eD', '--nD')]:
        d = re.sub(re.escape(a) + r'(?![\w-])', b, d)
    d = d.replace('animation:nrise', 'animation:n7rise')
    return d

out = []
i = 0
# tokenise into rules, handling one level of @media / @keyframes nesting
def rules(s):
    pos = 0
    while True:
        m = re.search(r'([^{}]*)\{', s[pos:])
        if not m: return
        head = m.group(1).strip(); start = pos + m.end()
        depth = 1; j = start
        while depth:
            if s[j] == '{': depth += 1
            elif s[j] == '}': depth -= 1
            j += 1
        yield head, s[start:j - 1]
        pos = j

for head, body in rules(src):
    if head.startswith('@keyframes'):
        name = head.split()[1]
        if name == 'nrise': out.append('@keyframes n7rise{' + conv_decl(body) + '}')
        elif name == 'pourtx': out.append('@keyframes z3pourtx{' + conv_decl(body) + '}')
        continue
    if head.startswith('@media'):
        continue  # reduced motion is handled app-wide
    if head.startswith('@property'): continue
    sels = [conv_sel(x) for x in head.split(',')]
    sels = [x for x in sels if x]
    if not sels: continue
    out.append(',\n'.join(sels) + '{' + conv_decl(body.strip()) + '}')
print('\n'.join(out))
