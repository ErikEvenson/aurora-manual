---
title: "Research Time Calculator"
parent: "Tools"
nav_order: 6
---

# Research Time Calculator

*Added: v2026.02.13*

Estimate research project duration accounting for diminishing returns from multiple labs, scientist bonuses, and field specialization. Compare up to 2 configurations side-by-side.

> **Verification Notice:** The diminishing returns formula (each additional lab contributes half the RP of the previous) is sourced from [AuroraWiki](http://aurorawiki.pentarch.org/) (ref A-15), not directly verified against the game database. This is widely accepted by the community but treat results as approximations.

<style>
  .calc-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #e0e0e0;
  }
  .calc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }
  .calc-card {
    background: #1a1a2e;
    border: 1px solid #3d3d5c;
    border-radius: 8px;
    padding: 16px;
  }
  .calc-card.active {
    border-color: #4ecdc4;
  }
  .calc-card-header {
    margin: 0 0 12px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid #3d3d5c;
    font-size: 15px;
    font-weight: 600;
    color: #4ecdc4;
  }
  .calc-field {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
  }
  .calc-field label {
    font-size: 12px;
    color: #aaa;
    margin-bottom: 4px;
  }
  .calc-field select,
  .calc-field input[type="number"] {
    background: #2d2d44;
    border: 1px solid #3d3d5c;
    border-radius: 4px;
    color: #fff;
    padding: 6px 8px;
    font-size: 13px;
  }
  .calc-field select {
    cursor: pointer;
  }
  .calc-field .checkbox-row {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 0;
  }
  .calc-field .checkbox-row input[type="checkbox"] {
    width: 16px;
    height: 16px;
    accent-color: #4ecdc4;
  }
  .calc-field .checkbox-row span {
    font-size: 13px;
    color: #e0e0e0;
  }
  .calc-results {
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid #3d3d5c;
  }
  .calc-results-header {
    margin: 0 0 8px 0;
    font-size: 13px;
    font-weight: 600;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .calc-result-row {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    font-size: 13px;
  }
  .calc-result-row .label {
    color: #aaa;
  }
  .calc-result-row .value {
    font-weight: 600;
    color: #fff;
  }
  .calc-result-row .value.highlight {
    color: #4ecdc4;
    font-size: 15px;
  }
  .calc-result-row .value.warning {
    color: #ff6b6b;
  }
  .calc-result-row .value.dimmed {
    color: #888;
  }
  .calc-disclaimer {
    margin-bottom: 16px;
    padding: 10px 14px;
    background: #2d2d44;
    border: 1px solid #ffe66d;
    border-radius: 6px;
    font-size: 12px;
    color: #ffe66d;
  }
  .calc-formula-note {
    margin-top: 20px;
    padding: 12px 16px;
    background: #1a1a2e;
    border-left: 3px solid #ffe66d;
    border-radius: 0 4px 4px 0;
    font-size: 13px;
    color: #aaa;
  }
  .calc-formula-note code {
    background: #2d2d44;
    padding: 1px 5px;
    border-radius: 3px;
    color: #4ecdc4;
  }
</style>

<div class="calc-wrapper" id="researchCalc">

<div class="calc-disclaimer">
  Wiki-sourced formula: Diminishing returns (0.5^n per lab) from AuroraWiki [ref A-15], not database-verified. Community-accepted but treat as approximate.
</div>

<div class="calc-grid" id="configGrid">
</div>

<div class="calc-formula-note">
<strong>Formulas used (wiki-sourced):</strong><br>
<code>Effective_Labs = sum(0.5^(i-1) for i in 1..n)</code> — 1st lab = 1.0, 2nd = 0.5, 3rd = 0.25... — <a href="../appendices/A-formulas.html#a54-research-speed">ref A-15</a><br>
<code>Scientist_Mult = 1 + (Bonus% x Specialization_Mult) / 100</code><br>
<code>Specialization_Mult = 4 if matching field, 1 otherwise</code><br>
<code>RP_per_Year = Effective_Labs x RP_per_Lab x Scientist_Mult</code><br>
<code>Days = Cost / (RP_per_Year / 365)</code><br>
<br>
<strong>Note:</strong> RP per lab depends on lab type (standard research lab = varies by installation), not on a tech progression. Enter the RP value appropriate for your lab type.
</div>

</div>

<script>
(function() {
  var CONFIGS = ['A', 'B'];

  function fmtNum(n) {
    if (n >= 1000000) return n.toLocaleString('en-US', {maximumFractionDigits: 0});
    if (n >= 100) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    if (n >= 1) return n.toLocaleString('en-US', {maximumFractionDigits: 2});
    return n.toLocaleString('en-US', {maximumFractionDigits: 4});
  }

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  // Diminishing returns: effective lab count [ref A-15]
  function effectiveLabs(n) {
    var total = 0;
    for (var i = 0; i < n; i++) {
      total += Math.pow(0.5, i);
    }
    return total;
  }

  function buildConfigCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Research Project Cost (RP)</label>' +
        '<input type="number" id="rsCost' + id + '" min="1" max="100000000" value="10000" step="100" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Number of Labs</label>' +
        '<input type="number" id="rsLabs' + id + '" min="1" max="50" value="5" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>RP per Lab per Year</label>' +
        '<input type="number" id="rsRPLab' + id + '" min="1" max="10000" value="200" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Scientist Bonus (%)</label>' +
        '<input type="number" id="rsBonus' + id + '" min="0" max="50" value="20" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Field Specialization</label>' +
        '<div class="checkbox-row">' +
          '<input type="checkbox" id="rsSpec' + id + '" onchange="recalcAll()">' +
          '<span>Scientist matches research field (4x bonus)</span>' +
        '</div></div>' +
      '<div class="calc-results" id="rsResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults: more labs, higher cost
  document.getElementById('rsLabs' + 'B').value = 15;
  document.getElementById('rsCost' + 'B').value = 50000;

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var cost = parseFloat(document.getElementById('rsCost' + id).value) || 0;
      var numLabs = parseInt(document.getElementById('rsLabs' + id).value) || 0;
      var rpPerLab = parseFloat(document.getElementById('rsRPLab' + id).value) || 0;
      var bonus = parseFloat(document.getElementById('rsBonus' + id).value) || 0;
      var specialization = document.getElementById('rsSpec' + id).checked;

      var effLabs = effectiveLabs(numLabs);
      var specMult = specialization ? 4 : 1;
      var sciMult = 1 + (bonus * specMult) / 100;
      var rpPerYear = effLabs * rpPerLab * sciMult;
      var days = rpPerYear > 0 ? cost / (rpPerYear / 365) : Infinity;
      var years = days / 365;

      // Marginal RP of next lab
      var nextLabRP = Math.pow(0.5, numLabs) * rpPerLab * sciMult;

      var timeText;
      if (days === Infinity) {
        timeText = 'Never';
      } else if (years >= 2) {
        timeText = fmtNum(years) + ' years';
      } else {
        timeText = fmtNum(Math.ceil(days)) + ' days';
      }

      var html = '<div class="calc-results-header">Results</div>' +
        row('Effective Lab Count', fmtNum(effLabs) + ' / ' + numLabs + ' actual') +
        row('Scientist Multiplier', fmtNum(sciMult) + 'x' + (specialization ? ' (spec.)' : '')) +
        row('Total RP per Year', fmtNum(rpPerYear), 'highlight') +
        row('Estimated Time', timeText, years > 10 ? 'warning' : '') +
        row('Marginal RP of Next Lab', fmtNum(nextLabRP) + ' RP/yr', 'dimmed');

      document.getElementById('rsResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
