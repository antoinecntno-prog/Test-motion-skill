/* Kit du conte d'ombres : marionnettes, décors, toile, grain et lumière, en SVG.
 * Chaque fonction rend une chaîne SVG. Repère : 1920 x 1080, y vers le bas.
 * Marionnettes : pieds à (0, 0) dans leur repère local, profil tourné vers la droite (flip: -1 pour la gauche).
 * Angles des membres en degrés : 0 = membre pendant vers le bas, négatif = vers l'avant (la droite du profil).
 * Toutes les pièces sont déterministes (graine), sans Math.random. */
(function () {
  const C = {
    ombre: '#1B120B', ombre2: '#2A1C11', brume: '#8A6440', brume2: '#5E4128',
    toile: '#EFDDB8', creme: '#FFF4DC', or: '#C98A2E', orClair: '#E0A84A', bordeaux: '#7A1E2E',
  };
  const R = (seed) => { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
  const f = (n) => Math.round(n * 10) / 10;
  const rad = (d) => d * Math.PI / 180;

  /* Segment de membre effilé, pivot en (px, py), longueur len, largeurs w0 -> w1, angle a. Rend [svg, xFin, yFin]. */
  function seg(px, py, len, w0, w1, a) {
    const d = `M${f(-w0 / 2)},0 L${f(-w1 / 2)},${f(len)} A${f(w1 / 2)},${f(w1 / 2)} 0 0 0 ${f(w1 / 2)},${f(len)} ` +
      `L${f(w0 / 2)},0 A${f(w0 / 2)},${f(w0 / 2)} 0 0 0 ${f(-w0 / 2)},0 Z`;
    const ex = px - len * Math.sin(rad(a)), ey = py + len * Math.cos(rad(a));
    return [`<path d="${d}" transform="translate(${f(px)},${f(py)}) rotate(${f(a)})"/>`, ex, ey];
  }
  /* Petit rivet (pivot de marionnette) : un point de lumière à l'articulation. */
  const rivet = (x, y, r = 2.6) => `<circle class="rivet" cx="${f(x)}" cy="${f(y)}" r="${r}"/>`;

  /* ---------------------------------------------------------------- le père */
  function pere(o = {}) {
    const p = Object.assign({ x: 0, y: 0, s: 1, flip: 1, armF: [-20, -40], armB: [12, -10], legF: [-8, 6], legB: [10, 4],
      head: 0, hand: null, extra: '', fill: C.ombre, rivets: true }, o);
    let g = '';
    // jambe arrière, bras arrière (derrière le manteau)
    const leg = (hx, hy, [hip, knee]) => {
      const [t, kx, ky] = seg(hx, hy, 112, 17, 12, hip);
      const [s2, ax, ay] = seg(kx, ky, 112, 12, 9, hip + knee);
      const shoe = `<path d="M${f(ax - 7)},${f(ay - 6)} L${f(ax + 28)},${f(ay + 1)} C${f(ax + 36)},${f(ay + 3)} ${f(ax + 36)},${f(ay + 10)} ${f(ax + 28)},${f(ay + 10)} L${f(ax - 9)},${f(ay + 10)} Z"/>`;
      return t + s2 + shoe + (p.rivets ? rivet(kx, ky) : '');
    };
    const arm = (sx, sy, [sh, el], hand) => {
      const [u, ex, ey] = seg(sx, sy, 116, 13, 10, sh);
      const [fa, wx, wy] = seg(ex, ey, 104, 10, 8, sh + el);
      const ha = sh + el;
      const mitt = `<g transform="translate(${f(wx)},${f(wy)}) rotate(${f(ha)})"><path d="M-6,-2 C-8,10 -6,22 0,26 C6,24 8,12 6,-2 Z"/>` +
        `<path d="M4,2 C10,4 13,10 11,14 C8,12 6,9 3,8 Z"/></g>`;
      return u + fa + (hand === 'none' ? '' : mitt) + (p.rivets ? rivet(ex, ey) : '');
    };
    g += leg(-8, -222, p.legB);
    g += arm(-2, -478, p.armB);
    g += leg(8, -222, p.legF);
    // manteau raide, col
    g += `<path d="M-24,-496 L18,-496 C30,-492 34,-480 34,-466 L38,-340 L52,-210 L-46,-210 L-32,-340 L-30,-466 C-30,-484 -28,-492 -24,-496 Z"/>`;
    g += `<path d="M8,-497 L24,-480 L14,-468 Z"/>`;
    // tête de profil (aucune expression), légère inclinaison
    g += `<g transform="rotate(${p.head},4,-500)"><path d="M-8,-506 C-26,-520 -30,-552 -20,-574 C-10,-594 18,-600 30,-588 C38,-580 41,-570 39,-561 L53,-545 L40,-541 C42,-535 40,-529 36,-526 L40,-517 C32,-511 20,-509 12,-507 L10,-494 L-6,-494 Z"/>` +
      `<path d="M-24,-560 C-30,-580 -14,-602 8,-603 C24,-604 34,-596 38,-586 C26,-592 10,-594 -2,-588 C-14,-582 -20,-572 -24,-560 Z"/></g>`;
    g += arm(6, -478, p.armF, p.hand);
    if (p.rivets) g += rivet(6, -478, 3) + rivet(8, -222, 3);
    g += p.extra;
    return `<g transform="translate(${f(p.x)},${f(p.y)}) scale(${f(p.s * p.flip * 1000) / 1000},${p.s})" fill="${p.fill}">${g}</g>`;
  }
  /* Point de la main avant du père dans le repère de la scène (pour une tige ou un objet tenu). */
  function mainPere(o, bras = 'F') {
    const p = Object.assign({ x: 0, y: 0, s: 1, flip: 1, armF: [-20, -40], armB: [12, -10] }, o);
    const [sx, sy] = bras === 'B' ? [-2, -478] : [6, -478];
    const [sh, el] = bras === 'B' ? p.armB : p.armF;
    const ex = sx - 116 * Math.sin(rad(sh)), ey = sy + 116 * Math.cos(rad(sh));
    const wx = ex - 104 * Math.sin(rad(sh + el)), wy = ey + 104 * Math.cos(rad(sh + el));
    return [p.x + wx * p.s * p.flip, p.y + wy * p.s];
  }
  /* Centre de la lentille du balancier de l'horloge, dans le repère de la scène. */
  function lentille(o) {
    const p = Object.assign({ x: 0, y: 0, s: 1, balancier: 8 }, o);
    const lx = -132 * Math.sin(rad(p.balancier)), ly = -262 + 132 * Math.cos(rad(p.balancier));
    return [p.x + lx * p.s, p.y + ly * p.s];
  }

  /* ---------------------------------------------------------------- la fillette (cinq ans, deux couettes) */
  function fille(o = {}) {
    const p = Object.assign({ x: 0, y: 0, s: 1, flip: 1, armF: [-30, -30], armB: [14, -10], legF: [-6, 4], legB: [8, 2],
      head: 0, seated: false, fill: C.ombre, rivets: true }, o);
    let g = '';
    const leg = (hx, hy, [hip, knee]) => {
      const [t, kx, ky] = seg(hx, hy, 62, 11, 9, hip);
      const [s2, ax, ay] = seg(kx, ky, 58, 9, 7, hip + knee);
      return t + s2 + `<path d="M${f(ax - 6)},${f(ay - 4)} L${f(ax + 14)},${f(ay - 3)} C${f(ax + 23)},${f(ay - 2)} ${f(ax + 24)},${f(ay + 8)} ${f(ax + 15)},${f(ay + 8)} L${f(ax - 8)},${f(ay + 8)} Z"/>` + (p.rivets ? rivet(kx, ky, 2) : '');
    };
    const arm = (sx, sy, [sh, el]) => {
      const [u, ex, ey] = seg(sx, sy, 56, 9, 8, sh);
      const [fa, wx, wy] = seg(ex, ey, 50, 8, 7, sh + el);
      return u + fa + `<circle cx="${f(wx)}" cy="${f(wy)}" r="7"/>` + (p.rivets ? rivet(ex, ey, 2) : '');
    };
    if (!p.seated) { g += leg(-8, -124, p.legB); }
    g += arm(-2, -226, p.armB);
    if (!p.seated) { g += leg(6, -124, p.legF); }
    // robe trapèze
    g += `<path d="M-15,-238 L11,-238 C21,-234 24,-226 24,-214 L50,-118 C28,-110 -28,-110 -48,-118 L-24,-214 C-24,-228 -22,-235 -15,-238 Z"/>`;
    // tête ronde de profil, couettes
    g += `<g transform="rotate(${p.head},0,-240)">` +
      `<path d="M-26,-262 C-41,-280 -37,-312 -14,-322 C4,-330 30,-324 40,-304 C44,-296 45,-290 44,-284 L51,-277 L43,-272 C42,-264 38,-256 30,-252 C20,-246 6,-246 -4,-248 L-2,-236 L-14,-236 L-16,-250 C-22,-254 -24,-258 -26,-262 Z"/>` +
      // frange
      `<path d="M-30,-300 C-26,-326 8,-336 30,-318 C40,-310 44,-300 44,-292 C36,-304 22,-312 6,-312 C-8,-312 -22,-306 -30,-300 Z"/>` +
      // couette côté proche, en arrière
      `<path d="M-30,-298 C-48,-306 -66,-296 -72,-276 C-70,-264 -64,-256 -58,-252 C-60,-264 -58,-276 -50,-282 C-46,-284 -40,-286 -34,-288 Z"/>` +
      `<circle cx="-34" cy="-294" r="7"/>` +
      // couette côté lointain, qui dépasse au-dessus
      `<path d="M-14,-322 C-20,-342 -36,-354 -54,-350 C-46,-344 -40,-336 -38,-328 C-30,-326 -22,-324 -14,-322 Z"/>` +
      `<circle cx="-16" cy="-324" r="6"/></g>`;
    if (p.menton) {
      // coudes posés sur les genoux, avant-bras qui remontent en V devant la robe, mains sous le menton
      g += `<path d="M2,-232 L12,-222 L70,-122 L60,-118 Z"/>`;
      g += `<path d="M58,-124 L68,-128 L52,-248 L44,-246 Z"/><path d="M66,-120 L76,-122 L58,-244 L50,-244 Z"/>`;
      g += `<circle cx="48" cy="-250" r="7.5"/><circle cx="55" cy="-247" r="7"/>` + (p.rivets ? rivet(64, -122, 2.2) : '');
    } else {
      g += arm(6, -226, p.armF);
    }
    if (p.seated) {
      g += leg(-4, -118, [-88, 86]) + leg(8, -118, [-84, 80]);
    }
    return `<g transform="translate(${f(p.x)},${f(p.y)}) scale(${f(p.s * p.flip * 1000) / 1000},${p.s})" fill="${p.fill}">${g}</g>`;
  }

  /* ---------------------------------------------------------------- engrenage */
  function engrenage(cx, cy, r, dents = 10, rot = 0, trou = 0.32) {
    let d = '';
    const n = dents * 2;
    for (let i = 0; i < n; i++) {
      const a0 = rad(rot + (i / n) * 360), a1 = rad(rot + ((i + 1) / n) * 360);
      const rr = i % 2 === 0 ? r : r * 0.8;
      d += (i === 0 ? 'M' : 'L') + f(cx + rr * Math.cos(a0)) + ',' + f(cy + rr * Math.sin(a0)) + ' L' + f(cx + rr * Math.cos(a1)) + ',' + f(cy + rr * Math.sin(a1)) + ' ';
    }
    d += 'Z ';
    const h = r * trou;
    d += `M${f(cx + h)},${f(cy)} A${f(h)},${f(h)} 0 1 0 ${f(cx - h)},${f(cy)} A${f(h)},${f(h)} 0 1 0 ${f(cx + h)},${f(cy)} Z`;
    return `<path fill-rule="evenodd" d="${d}"/>`;
  }
  const disque = (cx, cy, r) => `M${f(cx + r)},${f(cy)} A${f(r)},${f(r)} 0 1 0 ${f(cx - r)},${f(cy)} A${f(r)},${f(r)} 0 1 0 ${f(cx + r)},${f(cy)} Z`;

  /* ---------------------------------------------------------------- le Temps perdu : horloge comtoise trapue */
  function horloge(o = {}) {
    const p = Object.assign({ x: 0, y: 0, s: 1, heure: -60, minute: 140, balancier: 8, armL: [24, -30], armR: [-24, 30],
      fill: C.ombre, or: false, rivets: true }, o);
    let g = '';
    // roulettes de bois (moyeu ajouré)
    for (const rx of [-48, 48]) g += `<path fill-rule="evenodd" d="${disque(rx, -21, 21)} ${disque(rx, -21, 7)}"/>`;
    g += `<path d="M-80,-36 L80,-36 L72,-66 L-72,-66 Z"/>`;
    // ventre bombé avec sa fenêtre en lentille (ajourée)
    g += `<path fill-rule="evenodd" d="M-70,-64 C-106,-112 -106,-204 -66,-252 C-60,-264 -60,-280 -54,-292 L54,-292 C60,-280 60,-264 66,-252 C106,-204 106,-112 70,-64 Z ` +
      `M0,-272 C42,-238 42,-118 0,-88 C-42,-118 -42,-238 0,-272 Z"/>`;
    // balancier : tige, lentille, engrenage
    const ba = p.balancier, lx = 0 - 132 * Math.sin(rad(ba)), ly = -262 + 132 * Math.cos(rad(ba));
    g += `<path d="M-2,-262 L2,-262 L${f(lx + 2)},${f(ly)} L${f(lx - 2)},${f(ly)} Z"/>`;
    g += `<path fill-rule="evenodd" d="${disque(lx, ly, 22)} ${disque(lx, ly, 9)}"/>`;
    g += engrenage(-14, -232, 17, 9, 12) + engrenage(14, -214, 12, 7, 30);
    // taille et chapeau
    g += `<path d="M-56,-290 L56,-290 L60,-312 L-60,-312 Z"/>`;
    // cadran : disque plein, grande fenêtre ronde, graduations et aiguilles en plein dans la fenêtre
    g += `<path fill-rule="evenodd" d="${disque(0, -386, 80)} ${disque(0, -386, 58)}"/>`;
    for (let i = 0; i < 12; i++) {
      const a = rad(i * 30), r0 = 48, r1 = i % 3 === 0 ? 58 : 54;
      g += `<path d="M${f(Math.sin(a) * r0 - 2)},${f(-386 - Math.cos(a) * r0)} L${f(Math.sin(a) * r1 - 2)},${f(-386 - Math.cos(a) * r1)} L${f(Math.sin(a) * r1 + 2)},${f(-386 - Math.cos(a) * r1)} L${f(Math.sin(a) * r0 + 2)},${f(-386 - Math.cos(a) * r0)} Z" transform="rotate(0)"/>`;
    }
    const aig = (ang, len, w) => `<path d="M${-w / 2},4 L${-w / 3},${-len} L0,${-len - 8} L${w / 3},${-len} L${w / 2},4 Z" transform="translate(0,-386) rotate(${ang})"/>`;
    g += aig(p.heure, 30, 8) + aig(p.minute, 46, 5) + `<circle cx="0" cy="-386" r="7"/>`;
    // couronne et pommeaux
    g += `<path d="M-74,-430 C-52,-486 52,-486 74,-430 C60,-446 30,-458 0,-458 C-30,-458 -60,-446 -74,-430 Z"/>`;
    g += `<circle cx="-70" cy="-440" r="9"/><circle cx="70" cy="-440" r="9"/><circle cx="0" cy="-482" r="11"/>`;
    // bras courts sur tiges
    const arm = (sx, sy, [sh, el]) => {
      const [u, ex, ey] = seg(sx, sy, 52, 9, 8, sh);
      const [fa, wx, wy] = seg(ex, ey, 46, 8, 7, sh + el);
      return u + fa + `<g transform="translate(${f(wx)},${f(wy)}) rotate(${f(sh + el)})"><path d="M-7,0 L-7,13 A7,7 0 0 0 7,13 L7,0 Z"/></g>` + (p.rivets ? rivet(ex, ey, 2.4) : '');
    };
    g += arm(-88, -190, p.armL) + arm(88, -190, p.armR);
    if (p.rivets) g += rivet(-88, -190, 3) + rivet(88, -190, 3);
    const fill = p.or ? 'url(#orGrad)' : p.fill;
    return `<g transform="translate(${f(p.x)},${f(p.y)}) scale(${p.s})" fill="${fill}"${p.or ? ' filter="url(#glow)"' : ''}>${g}</g>`;
  }

  /* ---------------------------------------------------------------- chaîne de papier (maillons ajourés) */
  function chaine(pts, o = {}) {
    const p = Object.assign({ pas: 30, rx: 15, ry: 23, fill: C.ombre }, o);
    let g = '', k = 0;
    for (let i = 0; i < pts.length - 1; i++) {
      const [x0, y0] = pts[i], [x1, y1] = pts[i + 1];
      const L = Math.hypot(x1 - x0, y1 - y0), n = Math.max(1, Math.floor(L / p.pas));
      const ang = Math.atan2(y1 - y0, x1 - x0) * 180 / Math.PI;
      for (let j = 0; j < n; j++, k++) {
        const t = j / n, x = x0 + (x1 - x0) * t, y = y0 + (y1 - y0) * t;
        const plat = k % 2 === 1;
        const rx = plat ? p.rx * 0.35 : p.rx, ry = p.ry;
        g += `<path fill-rule="evenodd" transform="translate(${f(x)},${f(y)}) rotate(${f(ang - 90)})" d="M0,${-ry} C${rx * 1.3},${-ry} ${rx * 1.3},${ry} 0,${ry} C${-rx * 1.3},${ry} ${-rx * 1.3},${-ry} 0,${-ry} Z ` +
          (plat ? '' : `M0,${-ry + 7} C${(rx - 7) * 1.3},${-ry + 7} ${(rx - 7) * 1.3},${ry - 7} 0,${ry - 7} C${-(rx - 7) * 1.3},${ry - 7} ${-(rx - 7) * 1.3},${-ry + 7} 0,${-ry + 7} Z`) + `"/>`;
      }
    }
    return `<g fill="${p.fill}">${g}</g>`;
  }

  /* ---------------------------------------------------------------- pile de devis (tranches de papier, jours de lumière) */
  function pile(x, y, n, o = {}) {
    const p = Object.assign({ w: 150, h: 9, gap: 2.2, seed: 3, fill: C.ombre }, o);
    const r = R(p.seed); let g = '', yy = y;
    for (let i = 0; i < n; i++) {
      const dx = (r() - 0.5) * 16, w = p.w * (0.92 + r() * 0.12), rot = (r() - 0.5) * 2.4;
      g += `<rect x="${f(x - w / 2 + dx)}" y="${f(yy - p.h)}" width="${f(w)}" height="${p.h}" transform="rotate(${f(rot)},${f(x)},${f(yy)})"/>`;
      yy -= p.h + p.gap;
    }
    return `<g fill="${p.fill}">${g}</g>`;
  }
  /* Feuille de devis vue de face, colonnes de chiffres ajourées. */
  function devis(x, y, w = 120, h = 160, rot = 0, fill = C.ombre) {
    let d = `M0,0 L${w},0 L${w},${h} L0,${h} Z `;
    for (let r = 0; r < 7; r++) {
      const yy = 22 + r * 18;
      d += `M12,${yy} L${w * 0.5},${yy} L${w * 0.5},${yy + 6} L12,${yy + 6} Z M${w * 0.68},${yy} L${w - 12},${yy} L${w - 12},${yy + 6} L${w * 0.68},${yy + 6} Z `;
    }
    return `<path fill="${fill}" fill-rule="evenodd" transform="translate(${f(x)},${f(y)}) rotate(${rot})" d="${d}"/>`;
  }

  /* ---------------------------------------------------------------- le petit dinosaure sous son champignon (papier découpé) */
  function dino(x, y, s = 1, fill = C.ombre, o = {}) {
    let g = '';
    if (o.champignon !== false) {
      g += `<path d="M-92,-176 C-96,-120 -100,-56 -108,0 L-52,0 C-58,-56 -62,-120 -62,-176 Z"/>`;
      g += `<path fill-rule="evenodd" d="M-196,-170 C-188,-268 54,-268 62,-170 C10,-160 -144,-160 -196,-170 Z ${disque(-140, -196, 12)} ${disque(-86, -228, 15)} ${disque(-26, -206, 11)} ${disque(24, -184, 8)} ${disque(-176, -178, 7)}"/>`;
    }
    g += `<path fill-rule="evenodd" d="M-104,-12 C-84,-16 -66,-22 -56,-30 C-60,-60 -30,-80 6,-78 C28,-77 40,-74 48,-86 C56,-104 60,-124 74,-138 C84,-146 100,-144 104,-132 C106,-124 100,-118 90,-118 C80,-118 74,-112 72,-100 C70,-80 64,-56 56,-40 C52,-22 40,-12 24,-10 L-40,-10 C-60,-10 -84,-8 -104,-12 Z ${disque(92, -133, 3.6)}"/>`;
    g += `<path d="M-44,-66 L-38,-82 L-30,-70 L-22,-86 L-14,-74 L-6,-88 L2,-77 Z"/>`;
    g += `<rect x="-38" y="-16" width="15" height="16" rx="5"/><rect x="-16" y="-16" width="15" height="16" rx="5"/><rect x="14" y="-16" width="15" height="16" rx="5"/><rect x="32" y="-16" width="15" height="16" rx="5"/>`;
    return `<g transform="translate(${f(x)},${f(y)}) scale(${s})" fill="${fill}">${g}</g>`;
  }

  /* ---------------------------------------------------------------- arbre nu (branches récursives) */
  function arbre(x, y, h, seed = 1, o = {}) {
    const p = Object.assign({ fill: C.ombre, lean: 0, depth: 6, w: h * 0.07 }, o);
    const r = R(seed); let d = '';
    const branch = (bx, by, len, ang, w, dep) => {
      const ex = bx + len * Math.sin(rad(ang)), ey = by - len * Math.cos(rad(ang));
      const nx = Math.cos(rad(ang)), ny = Math.sin(rad(ang));
      const w1 = w * 0.62;
      d += `M${f(bx - nx * w / 2)},${f(by - ny * w / 2)} L${f(ex - nx * w1 / 2)},${f(ey - ny * w1 / 2)} L${f(ex + nx * w1 / 2)},${f(ey + ny * w1 / 2)} L${f(bx + nx * w / 2)},${f(by + ny * w / 2)} Z `;
      if (dep <= 0 || len < 8) return;
      const k = 2 + (r() < 0.45 ? 1 : 0);
      for (let i = 0; i < k; i++) {
        const na = ang + (r() - 0.5) * 70 + (i - (k - 1) / 2) * 22;
        branch(ex, ey, len * (0.62 + r() * 0.18), na, w1, dep - 1);
      }
    };
    branch(x, y, h * 0.36, p.lean, p.w, p.depth);
    return `<path fill="${p.fill}" d="${d}"/>`;
  }
  function herbes(x0, x1, y, h, seed = 2, fill = C.ombre, dens = 1.4) {
    const r = R(seed); let d = '';
    for (let x = x0; x < x1; x += 3 / dens + r() * 5) {
      const hh = h * (0.4 + r() * 0.8), lean = (r() - 0.5) * hh * 0.6, w = 2 + r() * 3;
      d += `M${f(x)},${f(y)} Q${f(x + lean * 0.3)},${f(y - hh * 0.6)} ${f(x + lean)},${f(y - hh)} Q${f(x + lean * 0.3 + w)},${f(y - hh * 0.55)} ${f(x + w)},${f(y)} Z `;
    }
    return `<path fill="${fill}" d="${d}"/>`;
  }
  function corbeau(x, y, s = 1, ailes = 0, fill = C.ombre) {
    const a = ailes;
    return `<g transform="translate(${f(x)},${f(y)}) scale(${s})" fill="${fill}"><path d="M-30,4 C-20,-6 0,-8 18,-4 L30,-10 L26,0 C30,4 20,8 10,8 L-8,10 L-30,14 Z"/>` +
      `<path d="M-6,-2 C-14,${-24 - a} -34,${-36 - a} -44,${-30 - a} C-30,${-20 - a / 2} -20,-8 -10,0 Z"/></g>`;
  }
  function cloture(x0, x1, y, h, seed = 4, fill = C.ombre) {
    const r = R(seed); let g = '';
    for (let x = x0; x < x1; x += 70 + r() * 40) {
      const hh = h * (0.8 + r() * 0.4), tilt = (r() - 0.5) * 8;
      g += `<rect x="${f(x)}" y="${f(y - hh)}" width="10" height="${f(hh)}" transform="rotate(${f(tilt)},${f(x)},${f(y)})"/>`;
    }
    g += `<path d="M${x0},${y - h * 0.62} Q${(x0 + x1) / 2},${y - h * 0.5} ${x1},${y - h * 0.64}" stroke="${fill}" stroke-width="2.5" fill="none"/>`;
    g += `<path d="M${x0},${y - h * 0.32} Q${(x0 + x1) / 2},${y - h * 0.22} ${x1},${y - h * 0.34}" stroke="${fill}" stroke-width="2.5" fill="none"/>`;
    return `<g fill="${fill}">${g}</g>`;
  }
  /* Tige de marionnette : trait fin depuis un point vers le bord du cadre. */
  const tige = (x0, y0, x1, y1, w = 2.2, fill = C.ombre) => `<path d="M${f(x0)},${f(y0)} L${f(x1)},${f(y1)}" stroke="${fill}" stroke-width="${w}" stroke-linecap="round" fill="none"/>`;

  /* ---------------------------------------------------------------- maison : pièces de décor */
  function lampe(x, y, s = 1, allumee = true, fill = C.ombre) {
    let g = `<g transform="translate(${f(x)},${f(y)}) scale(${s})" fill="${fill}">` +
      `<path d="M-30,0 L30,0 L22,-12 L12,-14 C20,-24 22,-38 14,-48 L-14,-48 C-22,-38 -20,-24 -12,-14 L-22,-12 Z"/>` +
      `<path fill-rule="evenodd" d="M-12,-50 C-22,-70 -22,-96 -10,-112 L10,-112 C22,-96 22,-70 12,-50 Z M-6,-58 C-12,-72 -12,-92 -4,-104 L4,-104 C12,-92 12,-72 6,-58 Z"/></g>`;
    if (allumee) g = `<circle cx="${f(x)}" cy="${f(y - 80 * s)}" r="${f(120 * s)}" fill="url(#flamme)"/>` + g;
    return g;
  }
  function table(x, y, w = 360, h = 150, fill = C.ombre) {
    return `<g fill="${fill}"><rect x="${f(x - w / 2)}" y="${f(y - h)}" width="${w}" height="14"/>` +
      `<rect x="${f(x - w / 2 + 16)}" y="${f(y - h)}" width="12" height="${h}"/><rect x="${f(x + w / 2 - 28)}" y="${f(y - h)}" width="12" height="${h}"/></g>`;
  }
  function chaise(x, y, s = 1, flip = 1, fill = C.ombre) {
    return `<g transform="translate(${f(x)},${f(y)}) scale(${s * flip},${s})" fill="${fill}"><rect x="-40" y="-120" width="84" height="12"/>` +
      `<rect x="-40" y="-120" width="10" height="120"/><rect x="34" y="-120" width="10" height="120"/><rect x="-40" y="-260" width="10" height="140"/>` +
      `<rect x="-40" y="-250" width="30" height="8"/><rect x="-40" y="-200" width="30" height="8"/></g>`;
  }
  function balancoire(x, yTop, yAssise, angle = 0, fill = C.ombre) {
    const L = yAssise - yTop;
    return `<g transform="translate(${f(x)},${f(yTop)}) rotate(${angle})" fill="${fill}"><path d="M-46,0 L-44,${L} M46,0 L44,${L}" stroke="${fill}" stroke-width="3"/>` +
      `<rect x="-56" y="${L - 4}" width="112" height="12" rx="2"/></g>`;
  }
  /* Grandes lettres de papier suspendues (mobile) : texte Fraunces, fils. */
  function lettres(txt, x, y, size, o = {}) {
    const p = Object.assign({ fill: C.ombre, fils: true, rot: 0, gold: false, anchor: 'middle', weight: 700 }, o);
    const fill = p.gold ? 'url(#orGrad)' : p.fill;
    return `<g transform="translate(${f(x)},${f(y)}) rotate(${p.rot})">` +
      (p.fils ? `<path d="M0,${-size * 0.8} L0,-1200" stroke="${p.gold ? C.orClair : C.ombre}" stroke-width="1.6"/>` : '') +
      `<text x="0" y="0" text-anchor="${p.anchor}" font-family="Fraunces" font-weight="${p.weight}" font-size="${size}" fill="${fill}"${p.gold ? ' filter="url(#glow)"' : ''}>${txt}</text></g>`;
  }
  /* Poussière d'étincelles dorées. */
  function etincelles(x0, y0, x1, y1, n, seed = 7) {
    const r = R(seed); let g = '';
    for (let i = 0; i < n; i++) {
      const x = x0 + r() * (x1 - x0), y = y0 + r() * (y1 - y0), rr = 0.8 + Math.pow(r(), 3) * 4;
      g += `<circle cx="${f(x)}" cy="${f(y)}" r="${f(rr)}" fill="${r() < 0.5 ? C.orClair : '#FFE7B0'}" opacity="${f(0.35 + r() * 0.65)}"/>`;
    }
    return `<g filter="url(#glowS)">${g}</g>`;
  }

  /* ---------------------------------------------------------------- toile, brume, grain, vignette */
  function defs(o = {}) {
    const L = Object.assign({ x: 960, y: 420, r: 1100, nuit: false }, o);
    const T = L.nuit ? ['#7A5426', '#5E3E1C', '#3E2812', '#24160A', '#0E0804'] : ['#FFF3D6', '#F3DFB6', '#D9B784', '#A27646', '#5B3A20'];
    return `<defs>
<radialGradient id="toileGrad" cx="${L.x}" cy="${L.y}" r="${L.r}" gradientUnits="userSpaceOnUse">
  <stop offset="0" stop-color="${T[0]}"/><stop offset=".18" stop-color="${T[1]}"/><stop offset=".45" stop-color="${T[2]}"/>
  <stop offset=".75" stop-color="${T[3]}"/><stop offset="1" stop-color="${T[4]}"/></radialGradient>
<radialGradient id="vignette" cx="960" cy="540" r="1150" gradientUnits="userSpaceOnUse">
  <stop offset=".45" stop-color="#140B05" stop-opacity="0"/><stop offset=".8" stop-color="#140B05" stop-opacity=".45"/><stop offset="1" stop-color="#0C0603" stop-opacity=".92"/></radialGradient>
<radialGradient id="flamme"><stop offset="0" stop-color="#FFF6DD" stop-opacity=".95"/><stop offset=".35" stop-color="#F6D9A0" stop-opacity=".55"/><stop offset="1" stop-color="#E9C68A" stop-opacity="0"/></radialGradient>
<radialGradient id="halo"><stop offset="0" stop-color="#FFE9B8" stop-opacity=".9"/><stop offset=".4" stop-color="#E0A84A" stop-opacity=".35"/><stop offset="1" stop-color="#C98A2E" stop-opacity="0"/></radialGradient>
<linearGradient id="orGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7B0"/><stop offset=".45" stop-color="#E0A84A"/><stop offset="1" stop-color="#C98A2E"/></linearGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="${L.seed || 3}"/>
  <feColorMatrix values="0 0 0 0 .16  0 0 0 0 .10  0 0 0 0 .05  0 0 0 -1.25 .98"/></filter>
<filter id="fibres" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".0015 .035" numOctaves="2" seed="11"/>
  <feColorMatrix values="0 0 0 0 .25  0 0 0 0 .16  0 0 0 0 .08  0 0 0 -1.6 1.05"/></filter>
<filter id="taches" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".006" numOctaves="4" seed="5"/>
  <feColorMatrix values="0 0 0 0 .32  0 0 0 0 .20  0 0 0 0 .10  0 0 0 -2.2 1.2"/></filter>
${[1.2, 2.5, 4, 6, 9, 14, 22, 34].map((b) => `<filter id="b${String(b).replace('.', '_')}" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="${b}"/></filter>`).join('\n')}
<filter id="glow" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur in="SourceAlpha" stdDeviation="9" result="b"/>
  <feFlood flood-color="#F2C46A" flood-opacity=".75"/><feComposite in2="b" operator="in" result="h"/><feMerge><feMergeNode in="h"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowS" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<style>.rivet{fill:#5A4028}</style>
</defs>`;
  }
  const toile = () => `<rect width="1920" height="1080" fill="url(#toileGrad)"/>` +
    `<rect width="1920" height="1080" filter="url(#taches)" opacity=".55" style="mix-blend-mode:multiply"/>`;
  const brume = (cx, cy, rx, ry, op = 0.45, fill = C.brume, blur = 34) =>
    `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${fill}" opacity="${op}" filter="url(#b${blur})"/>`;
  const voile = () => `<rect width="1920" height="1080" filter="url(#fibres)" opacity=".16" style="mix-blend-mode:multiply"/>` +
    `<rect width="1920" height="1080" filter="url(#grain)" opacity=".38" style="mix-blend-mode:multiply"/>` +
    `<rect width="1920" height="1080" fill="url(#vignette)"/>`;

  window.OMBRES = { C, R, seg, pere, mainPere, lentille, fille, horloge, engrenage, chaine, pile, devis, dino, arbre, herbes, corbeau, cloture,
    tige, lampe, table, chaise, balancoire, lettres, etincelles, defs, toile, brume, voile, disque };
})();
