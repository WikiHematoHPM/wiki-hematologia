/*
 * Calculadoras de la wiki (scores aditivos y R-ISS).
 * Uso docente: no reemplaza el juicio clínico ni las fuentes originales.
 *
 * Marcado esperado en la página:
 *   <div class="calc" data-bands='[[max, "etiqueta"], ...]'>
 *     <input type="checkbox" data-pts="1">        suma data-pts si está marcado
 *     <input type="radio" name="x" data-pts="2">  suma data-pts del radio marcado
 *     <select> <option data-pts="0">…</option>     suma data-pts de la opción elegida
 *     <div class="calc-out"></div>
 *   </div>
 * Las bandas se recorren en orden y se usa la primera con total <= max.
 * data-bands2 (opcional) agrega una segunda clasificación (p. ej., Wells dicotómico).
 * data-calc="riss" activa el cálculo especial ISS / R-ISS.
 */
(function () {
  "use strict";

  function fmt(n) {
    return Number.isInteger(n) ? String(n) : n.toFixed(1).replace(".", ",");
  }

  function pick(bands, total) {
    for (var i = 0; i < bands.length; i++) {
      if (total <= bands[i][0]) return bands[i][1];
    }
    return "";
  }

  function sumCalc(calc) {
    var total = 0;
    calc.querySelectorAll("input[data-pts]").forEach(function (el) {
      if (el.checked) total += parseFloat(el.getAttribute("data-pts")) || 0;
    });
    calc.querySelectorAll("select").forEach(function (sel) {
      var opt = sel.options[sel.selectedIndex];
      if (opt && opt.hasAttribute("data-pts")) total += parseFloat(opt.getAttribute("data-pts")) || 0;
    });
    return Math.round(total * 10) / 10;
  }

  function issStage(b2m, alb) {
    if (isNaN(b2m) || isNaN(alb)) return null;
    if (b2m >= 5.5) return 3;
    if (b2m < 3.5 && alb >= 3.5) return 1;
    return 2;
  }

  function rissStage(iss, highRiskCA, highLDH) {
    if (iss === null) return null;
    if (iss === 1 && !highRiskCA && !highLDH) return 1;
    if (iss === 3 && (highRiskCA || highLDH)) return 3;
    return 2;
  }

  function updateRiss(calc) {
    var out = calc.querySelector(".calc-out");
    var b2m = parseFloat((calc.querySelector("[data-field=b2m]").value || "").replace(",", "."));
    var alb = parseFloat((calc.querySelector("[data-field=alb]").value || "").replace(",", "."));
    var ca = calc.querySelector("[data-field=ca]").checked;
    var ldh = calc.querySelector("[data-field=ldh]").checked;
    var iss = issStage(b2m, alb);
    if (iss === null) {
      out.textContent = "Ingresa β2-microglobulina (mg/L) y albúmina (g/dL).";
      return;
    }
    var r = rissStage(iss, ca, ldh);
    var issTxt = ["", "ISS I (SG mediana 62 meses)", "ISS II (44 meses)", "ISS III (29 meses)"][iss];
    var rTxt = ["", "R-ISS I (SG a 5 años 82 %)", "R-ISS II (62 %)", "R-ISS III (40 %)"][r];
    out.innerHTML = "<strong>" + issTxt + "</strong> · <strong>" + rTxt + "</strong>";
  }

  function update(calc) {
    if (calc.getAttribute("data-calc") === "riss") {
      updateRiss(calc);
      return;
    }
    var out = calc.querySelector(".calc-out");
    if (!out) return;
    var total = sumCalc(calc);
    var txt = "Puntaje: <strong>" + fmt(total) + "</strong>";
    try {
      var b1 = JSON.parse(calc.getAttribute("data-bands") || "[]");
      var l1 = pick(b1, total);
      if (l1) txt += " → " + l1;
      var b2 = JSON.parse(calc.getAttribute("data-bands2") || "[]");
      var l2 = pick(b2, total);
      if (l2) txt += " · " + l2;
    } catch (e) {
      /* bandas mal formadas: se muestra solo el puntaje */
    }
    out.innerHTML = txt;
  }

  function initAll() {
    document.querySelectorAll(".calc").forEach(update);
  }

  document.addEventListener("input", function (ev) {
    var calc = ev.target.closest && ev.target.closest(".calc");
    if (calc) update(calc);
  });
  document.addEventListener("change", function (ev) {
    var calc = ev.target.closest && ev.target.closest(".calc");
    if (calc) update(calc);
  });
  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest && ev.target.closest(".calc-reset");
    if (!btn) return;
    var calc = btn.closest(".calc");
    calc.querySelectorAll("input").forEach(function (el) {
      if (el.type === "checkbox" || el.type === "radio") el.checked = el.defaultChecked;
      else el.value = "";
    });
    calc.querySelectorAll("select").forEach(function (sel) { sel.selectedIndex = 0; });
    update(calc);
  });

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initAll);
  else initAll();
  /* Compatibilidad con carga instantánea de Material/Zensical, si se activa */
  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    window.document$.subscribe(initAll);
  }

  /* Exportado solo para pruebas automáticas */
  if (typeof module !== "undefined") module.exports = { pick: pick, issStage: issStage, rissStage: rissStage };
})();
