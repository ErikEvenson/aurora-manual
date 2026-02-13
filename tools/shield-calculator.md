---
title: "Shield Strength Calculator"
parent: "Tools"
nav_order: 5
---

# Shield Strength Calculator

*Added: v2026.02.13*

Calculate shield generator strength, regeneration rate, and EM signature. Compare up to 2 configurations side-by-side. All formulas and tech values are verified against the Aurora game database (AuroraDB.db v2.7.1).

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
  .calc-result-row .value.regen {
    color: #95d5b2;
  }
  .calc-result-row .value.em {
    color: #ffe66d;
  }
  .calc-result-row .value.dimmed {
    color: #888;
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

<div class="calc-wrapper" id="shieldCalc">

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Shield Strength Technology (12 tiers) — AuroraDB.db [ref A-5, D-12]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Shield Type</th><th>Strength / HS</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Alpha Shields</td><td>1.0</td><td>1,000</td></tr>
<tr><td>Beta Shields</td><td>1.5</td><td>2,000</td></tr>
<tr><td>Gamma Shields</td><td>2.0</td><td>4,000</td></tr>
<tr><td>Delta Shields</td><td>2.5</td><td>8,000</td></tr>
<tr><td>Epsilon Shields</td><td>3.0</td><td>15,000</td></tr>
<tr><td>Theta Shields</td><td>4.0</td><td>30,000</td></tr>
<tr><td>Xi Shields</td><td>5.0</td><td>60,000</td></tr>
<tr><td>Omicron Shields</td><td>6.0</td><td>120,000</td></tr>
<tr><td>Sigma Shields</td><td>8.0</td><td>250,000</td></tr>
<tr><td>Tau Shields</td><td>10.0</td><td>500,000</td></tr>
<tr><td>Psi Shields</td><td>12.0</td><td>1,000,000</td></tr>
<tr><td>Omega Shields</td><td>15.0</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Shield Regeneration Rate (12 tiers) — AuroraDB.db [ref D-13]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Regen Rate</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>1</td><td>1.0</td><td>1,000</td></tr>
<tr><td>2</td><td>1.5</td><td>2,000</td></tr>
<tr><td>3</td><td>2.0</td><td>4,000</td></tr>
<tr><td>4</td><td>2.5</td><td>8,000</td></tr>
<tr><td>5</td><td>3.0</td><td>15,000</td></tr>
<tr><td>6</td><td>4.0</td><td>30,000</td></tr>
<tr><td>7</td><td>5.0</td><td>60,000</td></tr>
<tr><td>8</td><td>6.0</td><td>125,000</td></tr>
<tr><td>9</td><td>8.0</td><td>250,000</td></tr>
<tr><td>10</td><td>10.0</td><td>500,000</td></tr>
<tr><td>11</td><td>12.0</td><td>1,000,000</td></tr>
<tr><td>12</td><td>15.0</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Strength = Tech x Size_HS x sqrt(Size_HS / 10)</code> (for generators larger than 1 HS) — <a href="../appendices/A-formulas.html#a16-shields">ref A-5</a><br>
<code>Strength = Tech x Size_HS</code> (for 1 HS generators)<br>
<code>Regen_per_5sec = Regen_Tech x Size_HS</code> — <a href="../appendices/A-formulas.html#a16-shields">ref D-13</a><br>
<code>Shield_EM_Signature = Total_Strength x 3</code> — <a href="../appendices/A-formulas.html#a16-shields">ref A-5</a>
</div>

</div>

<script>
(function() {
  // Verified shield strength tiers — AuroraDB.db [ref A-5, D-12]
  var SHIELD_TECHS = [
    { name: 'Alpha (1.0/HS)', strength: 1.0 },
    { name: 'Beta (1.5/HS)', strength: 1.5 },
    { name: 'Gamma (2.0/HS)', strength: 2.0 },
    { name: 'Delta (2.5/HS)', strength: 2.5 },
    { name: 'Epsilon (3.0/HS)', strength: 3.0 },
    { name: 'Theta (4.0/HS)', strength: 4.0 },
    { name: 'Xi (5.0/HS)', strength: 5.0 },
    { name: 'Omicron (6.0/HS)', strength: 6.0 },
    { name: 'Sigma (8.0/HS)', strength: 8.0 },
    { name: 'Tau (10.0/HS)', strength: 10.0 },
    { name: 'Psi (12.0/HS)', strength: 12.0 },
    { name: 'Omega (15.0/HS)', strength: 15.0 }
  ];

  // Verified shield regen tiers — AuroraDB.db [ref D-13]
  var REGEN_TECHS = [
    { name: 'Level 1 (1.0)', rate: 1.0 },
    { name: 'Level 2 (1.5)', rate: 1.5 },
    { name: 'Level 3 (2.0)', rate: 2.0 },
    { name: 'Level 4 (2.5)', rate: 2.5 },
    { name: 'Level 5 (3.0)', rate: 3.0 },
    { name: 'Level 6 (4.0)', rate: 4.0 },
    { name: 'Level 7 (5.0)', rate: 5.0 },
    { name: 'Level 8 (6.0)', rate: 6.0 },
    { name: 'Level 9 (8.0)', rate: 8.0 },
    { name: 'Level 10 (10.0)', rate: 10.0 },
    { name: 'Level 11 (12.0)', rate: 12.0 },
    { name: 'Level 12 (15.0)', rate: 15.0 }
  ];

  var CONFIGS = ['A', 'B'];

  function fmtNum(n) {
    if (n >= 1000) return n.toLocaleString('en-US', {maximumFractionDigits: 0});
    if (n >= 100) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    if (n >= 1) return n.toLocaleString('en-US', {maximumFractionDigits: 2});
    return n.toLocaleString('en-US', {maximumFractionDigits: 3});
  }

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  function buildConfigCard(id) {
    var shieldOpts = SHIELD_TECHS.map(function(t, i) {
      var sel = (i === 0) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + '</option>';
    }).join('');

    var regenOpts = REGEN_TECHS.map(function(t, i) {
      var sel = (i === 0) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + '</option>';
    }).join('');

    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Shield Technology</label>' +
        '<select id="shTech' + id + '" onchange="recalcAll()">' + shieldOpts + '</select></div>' +
      '<div class="calc-field"><label>Generator Size (HS)</label>' +
        '<input type="number" id="shSize' + id + '" min="1" max="100" value="5" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Number of Generators</label>' +
        '<input type="number" id="shCount' + id + '" min="1" max="50" value="1" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Regeneration Technology</label>' +
        '<select id="shRegen' + id + '" onchange="recalcAll()">' + regenOpts + '</select></div>' +
      '<div class="calc-results" id="shResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults: higher tech, larger generator
  document.getElementById('shTech' + 'B').value = 5;
  document.getElementById('shSize' + 'B').value = 10;
  document.getElementById('shRegen' + 'B').value = 5;

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var techIdx = parseInt(document.getElementById('shTech' + id).value);
      var sizeHS = parseFloat(document.getElementById('shSize' + id).value) || 1;
      var count = parseInt(document.getElementById('shCount' + id).value) || 1;
      var regenIdx = parseInt(document.getElementById('shRegen' + id).value);

      var tech = SHIELD_TECHS[techIdx];
      var regen = REGEN_TECHS[regenIdx];

      // Shield strength formula [ref A-5]
      var strengthPerGen;
      if (sizeHS <= 1) {
        strengthPerGen = tech.strength * sizeHS;
      } else {
        strengthPerGen = tech.strength * sizeHS * Math.sqrt(sizeHS / 10);
      }

      var totalStrength = strengthPerGen * count;
      var totalHS = sizeHS * count;
      var efficiencyPerHS = totalHS > 0 ? totalStrength / totalHS : 0;

      // Regeneration [ref D-13]
      var regenPerGen = regen.rate * sizeHS;
      var totalRegen = regenPerGen * count;

      // EM Signature [ref A-5]
      var emSignature = totalStrength * 3;

      // Time to full recharge from zero
      var rechargeTime5s = totalRegen > 0 ? totalStrength / totalRegen : Infinity;
      var rechargeText = rechargeTime5s === Infinity ? 'N/A' :
        rechargeTime5s <= 120 ? fmtNum(rechargeTime5s * 5) + ' sec' :
        fmtNum(rechargeTime5s * 5 / 60) + ' min';

      var html = '<div class="calc-results-header">Results</div>' +
        row('Strength per Generator', fmtNum(strengthPerGen)) +
        row('Total Shield Strength', fmtNum(totalStrength), 'highlight') +
        row('Efficiency', fmtNum(efficiencyPerHS) + ' strength/HS', 'dimmed') +
        row('Total Generator Size', fmtNum(totalHS) + ' HS (' + fmtNum(totalHS * 50) + ' tons)') +
        row('Regen per 5-sec Tick', fmtNum(totalRegen), 'regen') +
        row('Full Recharge Time', rechargeText) +
        row('Shield EM Signature', fmtNum(emSignature), 'em');

      document.getElementById('shResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
