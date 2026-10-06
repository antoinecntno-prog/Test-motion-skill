/* Aquarelle : les primitives des images de style (et, plus tard, du kit des séquences).
   Tout est du SVG : des taches aux bords qui ondulent et foncent en séchant (filtre #aq), des traits d'encre à main
   levée (#ink), des silhouettes peintes en taches, des gouttes. Déterministe : un seed par forme, jamais Math.random. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const rnd = (seed) => { let s = seed * 9301 + 49297; return () => { s = (s * 9301 + 49297) % 233280; return s / 233280; }; };

  function el(name, attrs, parent) {
    const e = document.createElementNS(NS, name);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  /* filtres partagés : #aq (bord d'aquarelle, granulation), #aq-soft (lavis large, bord plus doux), #ink (trait vivant) */
  function aqDefs(svg) {
    if (svg.querySelector("#aq")) return;
    const defs = el("defs", {}, svg);
    defs.innerHTML = `
      <filter id="aq" x="-25%" y="-25%" width="150%" height="150%">
        <feTurbulence type="fractalNoise" baseFrequency=".018" numOctaves="3" seed="11" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="46" xChannelSelector="R" yChannelSelector="G" result="d"/>
        <feGaussianBlur in="d" stdDeviation="2.2" result="b"/>
        <feMorphology in="d" operator="erode" radius="10" result="e"/>
        <feGaussianBlur in="e" stdDeviation="8" result="eb"/>
        <feComposite in="b" in2="eb" operator="arithmetic" k1="0" k2="1" k3="-0.35" k4="0" result="ring"/>
        <feTurbulence type="fractalNoise" baseFrequency=".6" numOctaves="2" seed="4" result="g"/>
        <feColorMatrix in="g" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .25 .85" result="gm"/>
        <feComposite in="ring" in2="gm" operator="in"/>
      </filter>
      <filter id="aq-soft" x="-25%" y="-25%" width="150%" height="150%">
        <feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="3" seed="21" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="70" xChannelSelector="R" yChannelSelector="G" result="d"/>
        <feGaussianBlur in="d" stdDeviation="6"/>
      </filter>
      <filter id="ink" x="-10%" y="-10%" width="120%" height="120%">
        <feTurbulence type="fractalNoise" baseFrequency=".04" numOctaves="2" seed="5" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="5"/>
      </filter>
      <filter id="aq-blur" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>`;
  }

  /* une tache organique : rayon r, ondulation w (0 à 1), n sommets ; chemin fermé en courbes */
  function aqBlob(cx, cy, r, seed, w = 0.22, n = 9, ry = 1) {
    const R = rnd(seed), pts = [];
    for (let i = 0; i < n; i++) {
      const a = (i / n) * Math.PI * 2 + (R() - 0.5) * 0.4, k = 1 + (R() - 0.5) * 2 * w;
      pts.push([cx + Math.cos(a) * r * k, cy + Math.sin(a) * r * k * ry]);
    }
    let d = "";
    for (let i = 0; i < n; i++) {
      const p0 = pts[(i - 1 + n) % n], p1 = pts[i], p2 = pts[(i + 1) % n], p3 = pts[(i + 2) % n];
      const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6], c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
      d += (i ? "" : `M${p1[0].toFixed(1)} ${p1[1].toFixed(1)}`) + ` C${c1[0].toFixed(1)} ${c1[1].toFixed(1)} ${c2[0].toFixed(1)} ${c2[1].toFixed(1)} ${p2[0].toFixed(1)} ${p2[1].toFixed(1)}`;
    }
    return d + " Z";
  }

  /* un lavis : d (chemin) ou {cx, cy, r, ry, seed}, couleur, opacité, filtre aq ou aq-soft ; en multiply */
  function aqWash(svg, shape, color, opacity = 0.8, soft = false, parent) {
    const g = el("g", { filter: `url(#${soft ? "aq-soft" : "aq"})`, opacity, style: "mix-blend-mode:multiply" }, parent || svg);
    const d = typeof shape === "string" ? shape : aqBlob(shape.cx, shape.cy, shape.r, shape.seed || 1, shape.w, shape.n, shape.ry);
    el("path", { d, fill: color }, g);
    return g;
  }

  /* un trait d'encre à main levée */
  function aqInk(svg, d, width = 5, color = "#3A2A24", parent, extra = {}) {
    const g = parent || el("g", { filter: "url(#ink)" }, svg);
    if (!parent) g.setAttribute("filter", "url(#ink)");
    return el("path", Object.assign({ d, fill: "none", stroke: color, "stroke-width": width, "stroke-linecap": "round", "stroke-linejoin": "round" }, extra), g);
  }

  /* une goutte avec sa traînée */
  function aqDrop(svg, x, y, r, color, seed = 3, parent) {
    const g = aqWash(svg, { cx: x, cy: y, r, seed, w: 0.18, n: 7 }, color, 0.85, false, parent);
    return g;
  }

  /* une silhouette peinte en taches, vue de dos ou de trois quarts : un buste en dôme et une tête ronde.
     h = hauteur totale ; pose "dos" (buste large), "penche" (buste incliné), "bras-leve" (un bras tendu) */
  function aqFigure(svg, x, y, h, color, seed = 5, pose = "dos", parent) {
    const g = el("g", {}, parent || svg);
    const head = h * 0.16, sh = y + head * 2.4, bw = h * 0.3, bot = y + h;
    const tilt = pose === "penche" ? h * 0.08 : 0;
    const body = `M${x - bw} ${bot} L${x - bw} ${sh + h * 0.12} C ${x - bw} ${sh - h * 0.1} ${x - bw * 0.5 + tilt} ${sh - h * 0.14} ${x + tilt} ${sh - h * 0.12} C ${x + bw * 0.5 + tilt} ${sh - h * 0.14} ${x + bw} ${sh - h * 0.1} ${x + bw} ${sh + h * 0.12} L${x + bw} ${bot} Z`;
    aqWash(svg, body, color, 0.82, false, g);
    if (pose === "bras-leve") aqWash(svg, `M${x + bw * 0.7} ${sh + h * 0.06} C ${x + bw * 1.1} ${sh - h * 0.1} ${x + bw * 1.25} ${y - h * 0.02} ${x + bw * 1.3} ${y - h * 0.16} L ${x + bw * 1.42} ${y - h * 0.12} C ${x + bw * 1.36} ${y + h * 0.02} ${x + bw * 1.2} ${sh - h * 0.02} ${x + bw * 0.86} ${sh + h * 0.12} Z`, color, 0.82, false, g);
    aqWash(svg, { cx: x + tilt * 1.4, cy: y + head, r: head, seed: seed + 1, w: 0.1, n: 8 }, color, 0.9, false, g);
    return g;
  }

  /* une fenêtre d'interface dessinée à l'encre (chat, mail, document) : cadre, barre, et le contenu que l'appelant ajoute */
  function aqWindow(svg, x, y, w, h, opts = {}) {
    const g = el("g", { transform: `translate(${x} ${y})` }, opts.parent || svg);
    el("rect", { x: 0, y: 0, width: w, height: h, rx: 14, fill: opts.fill || "rgba(251,246,236,.92)" }, g);
    const ink = el("g", { filter: "url(#ink)" }, g);
    aqInk(svg, `M14 0 L${w - 14} 0 Q${w} 0 ${w} 14 L${w} ${h - 14} Q${w} ${h} ${w - 14} ${h} L14 ${h} Q0 ${h} 0 ${h - 14} L0 14 Q0 0 14 0 Z`, opts.stroke || 4.5, opts.color || "#3A2A24", ink);
    if (opts.bar !== false) aqInk(svg, `M0 ${opts.barH || 56} L${w} ${opts.barH || 56}`, 3, opts.color || "#3A2A24", ink);
    return g;
  }

  window.AQ = { el, rnd, aqDefs, aqBlob, aqWash, aqInk, aqDrop, aqFigure, aqWindow };
})();
