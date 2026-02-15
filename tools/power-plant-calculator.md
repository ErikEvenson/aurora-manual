---
title: "Power Plant Calculator"
parent: "Tools"
nav_order: 8
---

# Power Plant Calculator

*Updated: v2026.02.15*

Calculate power plant output with boost multipliers and explosion risk trade-offs. Compare up to 2 configurations side-by-side. Formulas and tech values are verified against the Aurora game database (AuroraDB.db v2.7.1).

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
  .calc-field input[type="number"],
  .calc-field input[type="range"] {
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
  .calc-field .range-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .calc-field .range-row input[type="range"] {
    flex: 1;
    padding: 0;
    height: 6px;
    -webkit-appearance: none;
    appearance: none;
    background: #3d3d5c;
    border: none;
    border-radius: 3px;
    outline: none;
  }
  .calc-field .range-row input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #4ecdc4;
    cursor: pointer;
  }
  .calc-field .range-row input[type="number"] {
    width: 70px;
    text-align: right;
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

<div class="calc-wrapper" id="ppCalc">

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Power Plant Technology (15 tiers) — AuroraDB.db [ref D-19]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Power Plant Type</th><th>Power / HS</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Conventional Reactor</td><td>0.5</td><td>150</td></tr>
<tr><td>Radioisotope Thermal Generator</td><td>2.0</td><td>600</td></tr>
<tr><td>Pressurised Water Reactor</td><td>2.5</td><td>1,200</td></tr>
<tr><td>Pebble Bed Reactor</td><td>3.2</td><td>2,400</td></tr>
<tr><td>Gaseous Fission Reactor</td><td>4.0</td><td>3,600</td></tr>
<tr><td>Magnetic Mirror Fusion</td><td>5.0</td><td>6,000</td></tr>
<tr><td>Stellarator Fusion</td><td>6.4</td><td>12,000</td></tr>
<tr><td>Tokamak Fusion</td><td>8.0</td><td>24,000</td></tr>
<tr><td>Inertial Confinement Fusion</td><td>10.0</td><td>45,000</td></tr>
<tr><td>Solid-core Anti-matter</td><td>12.8</td><td>90,000</td></tr>
<tr><td>Gas-core Anti-matter</td><td>16.0</td><td>180,000</td></tr>
<tr><td>Plasma-core Anti-matter</td><td>20.0</td><td>375,000</td></tr>
<tr><td>Beam Core Anti-matter</td><td>24.0</td><td>750,000</td></tr>
<tr><td>Vacuum Energy</td><td>32.0</td><td>1,500,000</td></tr>
<tr><td>Quantum Singularity</td><td>40.0</td><td>3,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Power Plant Boost Levels (8 tiers) — AuroraDB.db [ref D-20]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Boost Level</th><th>Multiplier</th><th>Explosion Chance</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>None</td><td>x1.0</td><td>5%</td><td>250</td></tr>
<tr><td>+10%</td><td>x1.1</td><td>7%</td><td>500</td></tr>
<tr><td>+20%</td><td>x1.2</td><td>10%</td><td>1,000</td></tr>
<tr><td>+30%</td><td>x1.3</td><td>15%</td><td>2,000</td></tr>
<tr><td>+40%</td><td>x1.4</td><td>20%</td><td>4,000</td></tr>
<tr><td>+60%</td><td>x1.6</td><td>30%</td><td>8,000</td></tr>
<tr><td>+80%</td><td>x1.8</td><td>40%</td><td>15,000</td></tr>
<tr><td>+100%</td><td>x2.0</td><td>50%</td><td>30,000</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Power_Output = Tech x Size_HS x sqrt(Size_HS)</code> — <a href="../appendices/A-formulas.html#a17-power-plants">ref A-4</a><br>
<code>Boosted_Output = Power_Output x Boost_Multiplier</code> — <a href="../appendices/A-formulas.html#a17-power-plants">ref D-20</a><br>
<code>HTK = floor(sqrt(Size_HS))</code><br>
<em>Note: Power plants use <code>sqrt(Size)</code>, not the <code>sqrt(Size/10)</code> scaling used by shields.</em>
</div>

</div>

<script>
(function() {
  // Verified power plant tech tiers — AuroraDB.db [ref D-19]
  var PP_TECHS = [
    { name: 'Conventional (0.5/HS)', power: 0.5 },
    { name: 'Radioisotope (2.0/HS)', power: 2.0 },
    { name: 'Pressurised Water (2.5/HS)', power: 2.5 },
    { name: 'Pebble Bed (3.2/HS)', power: 3.2 },
    { name: 'Gaseous Fission (4.0/HS)', power: 4.0 },
    { name: 'Mag. Mirror Fusion (5.0/HS)', power: 5.0 },
    { name: 'Stellarator Fusion (6.4/HS)', power: 6.4 },
    { name: 'Tokamak Fusion (8.0/HS)', power: 8.0 },
    { name: 'Inertial Conf. Fusion (10.0/HS)', power: 10.0 },
    { name: 'Solid-core AM (12.8/HS)', power: 12.8 },
    { name: 'Gas-core AM (16.0/HS)', power: 16.0 },
    { name: 'Plasma-core AM (20.0/HS)', power: 20.0 },
    { name: 'Beam Core AM (24.0/HS)', power: 24.0 },
    { name: 'Vacuum Energy (32.0/HS)', power: 32.0 },
    { name: 'Quantum Singularity (40.0/HS)', power: 40.0 }
  ];

  // Verified boost levels — AuroraDB.db [ref D-20]
  // Base 5% explosion rate confirmed: TechTypeID=42, AdditionalInfo2=5.0
  var BOOST_LEVELS = [
    { name: 'None (x1.0)', mult: 1.0, explosion: 5 }, /* AuroraDB TechTypeID=42 AdditionalInfo2=5.0 */
    { name: '+10% (x1.1)', mult: 1.1, explosion: 7 },
    { name: '+20% (x1.2)', mult: 1.2, explosion: 10 },
    { name: '+30% (x1.3)', mult: 1.3, explosion: 15 },
    { name: '+40% (x1.4)', mult: 1.4, explosion: 20 },
    { name: '+60% (x1.6)', mult: 1.6, explosion: 30 },
    { name: '+80% (x1.8)', mult: 1.8, explosion: 40 },
    { name: '+100% (x2.0)', mult: 2.0, explosion: 50 }
  ];

  var CONFIGS = ['A', 'B'];

  function fmtNum(n) {
    if (n >= 1000000) return n.toLocaleString('en-US', {maximumFractionDigits: 0});
    if (n >= 100) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    if (n >= 1) return n.toLocaleString('en-US', {maximumFractionDigits: 2});
    return n.toLocaleString('en-US', {maximumFractionDigits: 3});
  }

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  function buildConfigCard(id) {
    var techOpts = PP_TECHS.map(function(t, i) {
      var sel = (i === 2) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + '</option>';
    }).join('');

    var boostOpts = BOOST_LEVELS.map(function(b, i) {
      var sel = (i === 0) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + b.name + '</option>';
    }).join('');

    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Power Plant Technology</label>' +
        '<select id="ppTech' + id + '" onchange="recalcAll()">' + techOpts + '</select></div>' +
      '<div class="calc-field"><label>Generator Size: <span id="ppSizeLabel' + id + '">5</span> HS</label>' +
        '<div class="range-row">' +
          '<input type="range" id="ppSizeRange' + id + '" min="1" max="50" value="5" step="1" oninput="syncPPSize(\'' + id + '\',this.value)">' +
          '<input type="number" id="ppSizeNum' + id + '" min="0.1" max="50" value="5" step="0.1" oninput="syncPPSizeNum(\'' + id + '\',this.value)">' +
        '</div></div>' +
      '<div class="calc-field"><label>Number of Generators</label>' +
        '<input type="number" id="ppCount' + id + '" min="1" max="50" value="1" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Boost Level</label>' +
        '<select id="ppBoost' + id + '" onchange="recalcAll()">' + boostOpts + '</select></div>' +
      '<div class="calc-results" id="ppResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults: higher tech, boosted
  document.getElementById('ppTech' + 'B').value = 7;
  document.getElementById('ppSizeNum' + 'B').value = 10;
  document.getElementById('ppSizeRange' + 'B').value = 10;
  document.getElementById('ppSizeLabel' + 'B').textContent = '10';
  document.getElementById('ppBoost' + 'B').value = 3;

  window.syncPPSize = function(id, val) {
    document.getElementById('ppSizeNum' + id).value = val;
    document.getElementById('ppSizeLabel' + id).textContent = val;
    recalcAll();
  };

  window.syncPPSizeNum = function(id, val) {
    var v = parseFloat(val);
    if (isNaN(v) || v < 0.1) return;
    document.getElementById('ppSizeRange' + id).value = Math.round(v);
    document.getElementById('ppSizeLabel' + id).textContent = v;
    recalcAll();
  };

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var techIdx = parseInt(document.getElementById('ppTech' + id).value);
      var sizeHS = parseFloat(document.getElementById('ppSizeNum' + id).value) || 1;
      var count = parseInt(document.getElementById('ppCount' + id).value) || 1;
      var boostIdx = parseInt(document.getElementById('ppBoost' + id).value);

      var tech = PP_TECHS[techIdx];
      var boost = BOOST_LEVELS[boostIdx];

      // Power output formula [ref A-4] — Tech x Size x sqrt(Size)
      // Verified against FCT_ShipDesignComponents for 14 power plant components
      var basePerGen = tech.power * sizeHS * Math.sqrt(sizeHS);

      var boostedPerGen = basePerGen * boost.mult;
      var totalBase = basePerGen * count;
      var totalBoosted = boostedPerGen * count;
      var totalHS = sizeHS * count;
      var totalTons = totalHS * 50;
      var efficiencyPerHS = totalHS > 0 ? totalBoosted / totalHS : 0;
      var htk = Math.floor(Math.sqrt(sizeHS));

      var html = '<div class="calc-results-header">Results</div>' +
        row('Base Output per Generator', fmtNum(basePerGen)) +
        (boost.mult > 1 ? row('Boosted Output per Generator', fmtNum(boostedPerGen)) : '') +
        row('Total Power Output', fmtNum(totalBoosted), 'highlight') +
        row('Efficiency', fmtNum(efficiencyPerHS) + ' power/HS', 'dimmed') +
        row('Total Size', fmtNum(totalHS) + ' HS (' + fmtNum(totalTons) + ' tons)') +
        row('HTK per Generator', fmtNum(htk)) +
        row('Explosion Risk', boost.explosion + '%', boost.explosion >= 20 ? 'warning' : '');

      document.getElementById('ppResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
