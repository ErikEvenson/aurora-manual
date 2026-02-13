---
title: "Terraforming Time Calculator"
parent: "Tools"
nav_order: 3
---

# Terraforming Time Calculator

*Added: v2026.02.13*

Estimate terraforming duration based on installation count, technology level, and target atmospheric change. Compare up to 2 configurations side-by-side. All tech values are verified against the Aurora game database (AuroraDB.db v2.7.1).

> **Note:** Gas-specific modifiers vary by gas type but exact per-gas values are not fully database-verified. The default modifier of 1.0 is used; adjust manually if you know the modifier for your target gas. Effective rate also scales with planet radius — this calculator assumes Earth-sized bodies unless adjusted.

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
  .calc-collapsible {
    margin-bottom: 8px;
  }
  .calc-collapsible summary {
    cursor: pointer;
    padding: 8px 12px;
    background: #2d2d44;
    border: 1px solid #3d3d5c;
    border-radius: 4px;
    font-size: 14px;
    color: #e0e0e0;
    list-style: none;
  }
  .calc-collapsible summary::-webkit-details-marker {
    display: none;
  }
  .calc-collapsible summary::before {
    content: '\25b6  ';
    font-size: 10px;
    color: #4ecdc4;
  }
  .calc-collapsible[open] summary::before {
    content: '\25bc  ';
  }
  .calc-collapsible[open] summary {
    border-radius: 4px 4px 0 0;
    border-bottom: 1px solid #4ecdc4;
  }
  .calc-collapsible .detail-content {
    padding: 12px;
    border: 1px solid #3d3d5c;
    border-top: none;
    border-radius: 0 0 4px 4px;
    background: #1a1a2e;
  }
  .calc-ref-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 8px 0 16px 0;
  }
  .calc-ref-table th {
    background: #2d2d44;
    color: #4ecdc4;
    padding: 6px 10px;
    text-align: left;
    border-bottom: 1px solid #4ecdc4;
    font-weight: 600;
  }
  .calc-ref-table td {
    padding: 5px 10px;
    border-bottom: 1px solid #2d2d44;
    color: #ccc;
  }
  .calc-ref-table tr:hover td {
    background: #2d2d44;
  }
  .calc-formula-note {
    margin-top: 20px;
    padding: 12px 16px;
    background: #1a1a2e;
    border-left: 3px solid #4ecdc4;
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

<div class="calc-wrapper" id="terraCalc">

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Terraforming Rate Technology (13 tiers) — AuroraDB.db [ref A-9]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Technology</th><th>Rate (atm/yr)</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Racial Starting Rate</td><td>0.00025</td><td>--</td></tr>
<tr><td>Terraforming Rate 1</td><td>0.00032</td><td>3,000</td></tr>
<tr><td>Terraforming Rate 2</td><td>0.0004</td><td>5,000</td></tr>
<tr><td>Terraforming Rate 3</td><td>0.00048</td><td>10,000</td></tr>
<tr><td>Terraforming Rate 4</td><td>0.0006</td><td>20,000</td></tr>
<tr><td>Terraforming Rate 5</td><td>0.00075</td><td>40,000</td></tr>
<tr><td>Terraforming Rate 6</td><td>0.00096</td><td>80,000</td></tr>
<tr><td>Terraforming Rate 7</td><td>0.0012</td><td>150,000</td></tr>
<tr><td>Terraforming Rate 8</td><td>0.0015</td><td>300,000</td></tr>
<tr><td>Terraforming Rate 9</td><td>0.0019</td><td>600,000</td></tr>
<tr><td>Terraforming Rate 10</td><td>0.0024</td><td>1,200,000</td></tr>
<tr><td>Terraforming Rate 11</td><td>0.003</td><td>2,500,000</td></tr>
<tr><td>Terraforming Rate 12</td><td>0.00375</td><td>5,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Rate = Installations x Tech_Rate x Gas_Modifier x (Earth_Radius / Planet_Radius)^2</code> — <a href="../appendices/A-formulas.html#a55-terraforming">ref A-9</a><br>
<code>Years = Target_Atm_Change / Rate</code><br>
<br>
<strong>Omitted:</strong> Exact per-gas modifier values are not fully database-verified. Use 1.0 as default and adjust if known.
</div>

</div>

<script>
(function() {
  // Verified terraforming rate tiers — AuroraDB.db [ref A-9]
  var TERRA_TECHS = [
    { name: 'Starting (0.00025)', rate: 0.00025 },
    { name: 'Rate 1 (0.00032)', rate: 0.00032 },
    { name: 'Rate 2 (0.0004)', rate: 0.0004 },
    { name: 'Rate 3 (0.00048)', rate: 0.00048 },
    { name: 'Rate 4 (0.0006)', rate: 0.0006 },
    { name: 'Rate 5 (0.00075)', rate: 0.00075 },
    { name: 'Rate 6 (0.00096)', rate: 0.00096 },
    { name: 'Rate 7 (0.0012)', rate: 0.0012 },
    { name: 'Rate 8 (0.0015)', rate: 0.0015 },
    { name: 'Rate 9 (0.0019)', rate: 0.0019 },
    { name: 'Rate 10 (0.0024)', rate: 0.0024 },
    { name: 'Rate 11 (0.003)', rate: 0.003 },
    { name: 'Rate 12 (0.00375)', rate: 0.00375 }
  ];

  var CONFIGS = ['A', 'B'];

  function fmtNum(n) {
    if (n >= 1000) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    if (n >= 1) return n.toLocaleString('en-US', {maximumFractionDigits: 2});
    return n.toLocaleString('en-US', {maximumFractionDigits: 6});
  }

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  function buildConfigCard(id) {
    var techOptions = TERRA_TECHS.map(function(t, i) {
      var sel = (i === 0) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + '</option>';
    }).join('');

    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field">' +
        '<label>Number of Installations</label>' +
        '<input type="number" id="tfInst' + id + '" min="1" max="10000" value="10" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field">' +
        '<label>Terraforming Tech Level</label>' +
        '<select id="tfTech' + id + '" onchange="recalcAll()">' + techOptions + '</select></div>' +
      '<div class="calc-field">' +
        '<label>Target Atmospheric Change (atm)</label>' +
        '<input type="number" id="tfTarget' + id + '" min="0.001" max="100" value="0.30" step="0.01" oninput="recalcAll()"></div>' +
      '<div class="calc-field">' +
        '<label>Gas Modifier (default 1.0)</label>' +
        '<input type="number" id="tfGas' + id + '" min="0.01" max="10" value="1.0" step="0.01" oninput="recalcAll()"></div>' +
      '<div class="calc-field">' +
        '<label>Planet Radius (Earth = 1.0)</label>' +
        '<input type="number" id="tfRadius' + id + '" min="0.01" max="100" value="1.0" step="0.01" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="tfResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults
  document.getElementById('tfInst' + 'B').value = 50;
  document.getElementById('tfTech' + 'B').value = 6;

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var installations = parseInt(document.getElementById('tfInst' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('tfTech' + id).value);
      var targetAtm = parseFloat(document.getElementById('tfTarget' + id).value) || 0;
      var gasMod = parseFloat(document.getElementById('tfGas' + id).value) || 1.0;
      var radius = parseFloat(document.getElementById('tfRadius' + id).value) || 1.0;

      var tech = TERRA_TECHS[techIdx];
      var radiusFactor = 1 / (radius * radius);
      var ratePerInst = tech.rate * gasMod * radiusFactor;
      var totalRate = installations * ratePerInst;
      var years = totalRate > 0 ? targetAtm / totalRate : Infinity;
      var days = years * 365;

      var yearsText = years === Infinity ? 'Never' :
        years >= 1 ? fmtNum(years) + ' years' :
        fmtNum(days) + ' days';

      var html = '<div class="calc-results-header">Results</div>' +
        row('Rate per Installation', fmtNum(ratePerInst) + ' atm/yr') +
        row('Total Rate', fmtNum(totalRate) + ' atm/yr') +
        (radius !== 1.0 ? row('Planet Radius Factor', fmtNum(radiusFactor) + 'x') : '') +
        row('Estimated Time', yearsText, years > 100 ? 'warning' : 'highlight');

      document.getElementById('tfResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
