---
title: "Ship Speed & Engine Calculator"
parent: "Tools"
nav_order: 1
---

# Ship Speed & Engine Calculator

*Updated: v2026.02.15*

Compare up to 2 engine configurations side-by-side. Formulas and tech values are verified against the Aurora game database (AuroraDB.db v2.7.1) and referenced in the manual, except where marked *(unverified)*.

> **Note:** Fuel consumption and range calculations are intentionally excluded. The manual contains [contradicting formulas for engine-size fuel efficiency](https://github.com/ErikEvenson/aurora-manual/issues/1215) (Appendix A.1.3 vs Section 8.3.5), and runtime fuel consumption claims are [also unverified](https://github.com/ErikEvenson/aurora-manual/issues/1214). Only verified calculations are shown here.

<style>
  .calc-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #e0e0e0;
  }
  .calc-ship-input {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    padding: 16px;
    background: #2d2d44;
    border: 1px solid #4ecdc4;
    border-radius: 8px;
  }
  .calc-ship-input label {
    font-size: 14px;
    font-weight: 600;
    white-space: nowrap;
  }
  .calc-ship-input input {
    width: 120px;
    padding: 8px 12px;
    background: #1a1a2e;
    border: 1px solid #4ecdc4;
    border-radius: 4px;
    color: #fff;
    font-size: 14px;
    text-align: right;
  }
  .calc-ship-input .tonnage-display {
    color: #888;
    font-size: 13px;
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
  .calc-result-row .value.speed {
    color: #4ecdc4;
    font-size: 15px;
  }
  .calc-result-row .value.commercial {
    color: #ffe66d;
  }
  .calc-result-row .value.military {
    color: #ff6b6b;
  }
  .calc-result-row .value.warning {
    color: #ff6b6b;
  }
  .calc-toggle-btn {
    display: inline-block;
    padding: 6px 14px;
    margin-bottom: 12px;
    background: #2d2d44;
    border: 1px solid #3d3d5c;
    border-radius: 4px;
    color: #aaa;
    font-size: 13px;
    cursor: pointer;
  }
  .calc-toggle-btn:hover {
    border-color: #4ecdc4;
    color: #fff;
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

<div class="calc-wrapper" id="engineCalc">

<div class="calc-ship-input">
  <label for="shipHS">Ship Size:</label>
  <input type="number" id="shipHS" min="1" max="100000" value="200" step="1" oninput="recalcAll()">
  <span>HS</span>
  <span class="tonnage-display">(<span id="shipTons">10,000</span> tons)</span>
</div>

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Engine Technology (15 tiers) — AuroraDB.db ref [8.3-1]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Drive Technology</th><th>EP per HS</th><th>Research (RP)</th><th>Era</th></tr></thead>
<tbody>
<tr><td>Conventional Engine</td><td>1.0</td><td>500</td><td>Pre-TN</td></tr>
<tr><td>Nuclear Radioisotope Engine</td><td>5.0</td><td>1,000</td><td>Pre-TN</td></tr>
<tr><td>Nuclear Thermal Engine</td><td>6.4</td><td>2,000</td><td>Starting TN</td></tr>
<tr><td>Nuclear Pulse Engine</td><td>8.0</td><td>4,000</td><td>Early</td></tr>
<tr><td>Nuclear Gas-Core Engine</td><td>10.0</td><td>6,000</td><td>Early</td></tr>
<tr><td>Ion Drive</td><td>12.5</td><td>10,000</td><td>Early-Mid</td></tr>
<tr><td>Magneto-Plasma Drive</td><td>16.0</td><td>20,000</td><td>Mid</td></tr>
<tr><td>Magnetic Confinement Fusion Drive</td><td>20.0</td><td>40,000</td><td>Mid</td></tr>
<tr><td>Inertial Confinement Fusion Drive</td><td>25.0</td><td>80,000</td><td>Mid-Late</td></tr>
<tr><td>Solid Core Anti-matter Drive</td><td>32.0</td><td>150,000</td><td>Late</td></tr>
<tr><td>Gas Core Anti-matter Drive</td><td>40.0</td><td>300,000</td><td>Late</td></tr>
<tr><td>Plasma Core Anti-matter Drive</td><td>50.0</td><td>600,000</td><td>Advanced</td></tr>
<tr><td>Beam Core Anti-matter Drive</td><td>64.0</td><td>1,250,000</td><td>Advanced</td></tr>
<tr><td>Photonic Drive</td><td>80.0</td><td>2,500,000</td><td>Advanced</td></tr>
<tr><td>Quantum Singularity Drive</td><td>100.0</td><td>5,000,000</td><td>Extreme</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Power Modifier Tech — AuroraDB.db ref [8.3-4]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Technology</th><th>Modifier</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Max Engine Power Modifier x1</td><td>1.0x</td><td>(starting)</td></tr>
<tr><td>Max Engine Power Modifier x1.25</td><td>1.25x</td><td>500</td></tr>
<tr><td>Max Engine Power Modifier x1.5</td><td>1.5x</td><td>1,000</td></tr>
<tr><td>Max Engine Power Modifier x1.75</td><td>1.75x</td><td>2,000</td></tr>
<tr><td>Max Engine Power Modifier x2</td><td>2.0x</td><td>4,000</td></tr>
<tr><td>Max Engine Power Modifier x2.5</td><td>2.5x</td><td>8,000</td></tr>
<tr><td>Max Engine Power Modifier x3</td><td>3.0x</td><td>15,000</td></tr>
</tbody>
</table>
<table class="calc-ref-table">
<thead><tr><th>Technology</th><th>Modifier</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Min Engine Power Modifier x0.5</td><td>0.5x</td><td>(starting)</td></tr>
<tr><td>Min Engine Power Modifier x0.4</td><td>0.4x</td><td>1,000</td></tr>
<tr><td>Min Engine Power Modifier x0.3</td><td>0.3x</td><td>2,000</td></tr>
<tr><td>Min Engine Power Modifier x0.25</td><td>0.25x</td><td>4,000</td></tr>
<tr><td>Min Engine Power Modifier x0.2</td><td>0.2x</td><td>8,000</td></tr>
<tr><td>Min Engine Power Modifier x0.15</td><td>0.15x</td><td>15,000</td></tr>
<tr><td>Min Engine Power Modifier x0.1</td><td>0.1x</td><td>30,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Max Engine Size Tech — AuroraDB.db ref [8.3-3]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Max Engine Size (HS)</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>25</td><td>1,000</td></tr>
<tr><td>40</td><td>2,000</td></tr>
<tr><td>60</td><td>4,000</td></tr>
<tr><td>100</td><td>8,000</td></tr>
<tr><td>160</td><td>15,000</td></tr>
<tr><td>250</td><td>30,000</td></tr>
<tr><td>400</td><td>60,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Boost Explosion Chance — AuroraDB.db TechTypeID=42 ref [A-4]</summary>
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

<details class="calc-collapsible">
<summary>Fuel Consumption Tech — AuroraDB.db ref [8.3-7]</summary>
<div class="detail-content">
<p style="color:#aaa;font-size:13px;margin-bottom:8px;">This table shows the base fuel consumption rate technology. Note: the engine-size fuel efficiency modifier is <strong>excluded from the calculator</strong> due to <a href="https://github.com/ErikEvenson/aurora-manual/issues/1215">contradicting formulas (#1215)</a>.</p>
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Litres per EP-Hour</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Base</td><td>1.0</td><td>(starting)</td></tr>
<tr><td>1</td><td>0.9</td><td>1,000</td></tr>
<tr><td>2</td><td>0.8</td><td>2,000</td></tr>
<tr><td>3</td><td>0.7</td><td>4,000</td></tr>
<tr><td>4</td><td>0.6</td><td>8,000</td></tr>
<tr><td>5</td><td>0.5</td><td>15,000</td></tr>
<tr><td>6</td><td>0.4</td><td>30,000</td></tr>
<tr><td>7</td><td>0.3</td><td>60,000</td></tr>
<tr><td>8</td><td>0.25</td><td>120,000</td></tr>
<tr><td>9</td><td>0.2</td><td>250,000</td></tr>
<tr><td>10</td><td>0.16</td><td>500,000</td></tr>
<tr><td>11</td><td>0.125</td><td>1,000,000</td></tr>
<tr><td>12</td><td>0.1</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Fuel Storage Modules — AuroraDB.db TechTypeID=94, ComponentTypeID=3 ref [14.1-4]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Module</th><th>Size (HS)</th><th>Capacity (litres)</th><th>HTK</th><th>Cost (BP)</th></tr></thead>
<tbody>
<tr><td>Fuel Storage - Minimal</td><td>0.002</td><td>100</td><td>0</td><td>0.01</td></tr>
<tr><td>Fuel Storage - Fighter</td><td>0.02</td><td>1,000</td><td>0</td><td>0.08</td></tr>
<tr><td>Fuel Storage - Tiny</td><td>0.1</td><td>5,000</td><td>0</td><td>0.3</td></tr>
<tr><td>Fuel Storage - Small</td><td>0.2</td><td>10,000</td><td>0</td><td>0.5</td></tr>
<tr><td>Fuel Storage - Standard</td><td>1.0</td><td>50,000</td><td>1</td><td>2.0</td></tr>
<tr><td>Fuel Storage - Large</td><td>5.0</td><td>250,000</td><td>1</td><td>5.0</td></tr>
<tr><td>Fuel Storage - Very Large</td><td>20.0</td><td>1,000,000</td><td>1</td><td>10.0</td></tr>
<tr><td>Fuel Storage - Ultra Large</td><td>100.0</td><td>5,000,000</td><td>1</td><td>25.0</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Speed (km/s) = Total_EP * 1000 / Ship_Size_HS</code> — <a href="../appendices/A-formulas.html#a11-ship-speed">ref A-1, A-2</a><br>
<code>Engine_Power = Size_HS * EP_per_HS * Power_Modifier</code> — <a href="../appendices/A-formulas.html#a12-engine-power">ref A-3</a><br>
<code>Commercial = Power_Modifier <= 0.5 AND Size >= 25 HS</code> — <a href="../8-ship-design/8.3-engines.html#831-engine-technology">ref 8.3-6</a><br>
<code>Boost_Penalty = (4 ^ Modifier) / 4</code> — <a href="../appendices/A-formulas.html#a14-fuel-consumption-rate">ref A-11</a><br>
<br>
<strong>Excluded:</strong> Fuel consumption rate, range, and engine-size fuel efficiency — see <a href="https://github.com/ErikEvenson/aurora-manual/issues/1215">#1215</a> and <a href="https://github.com/ErikEvenson/aurora-manual/issues/1214">#1214</a> for details.
</div>

</div>

<script>
(function() {
  // Verified engine tech tiers — AuroraDB.db TechTypeID=40 [ref 8.3-1]
  var ENGINE_TECHS = [
    { name: 'Conventional Engine', epPerHS: 1.0 },
    { name: 'Nuclear Radioisotope', epPerHS: 5.0 },
    { name: 'Nuclear Thermal', epPerHS: 6.4 },
    { name: 'Nuclear Pulse', epPerHS: 8.0 },
    { name: 'Nuclear Gas-Core', epPerHS: 10.0 },
    { name: 'Ion Drive', epPerHS: 12.5 },
    { name: 'Magneto-Plasma', epPerHS: 16.0 },
    { name: 'Mag. Confinement Fusion', epPerHS: 20.0 },
    { name: 'Inertial Confinement Fusion', epPerHS: 25.0 },
    { name: 'Solid Core Anti-matter', epPerHS: 32.0 },
    { name: 'Gas Core Anti-matter', epPerHS: 40.0 },
    { name: 'Plasma Core Anti-matter', epPerHS: 50.0 },
    { name: 'Beam Core Anti-matter', epPerHS: 64.0 },
    { name: 'Photonic Drive', epPerHS: 80.0 },
    { name: 'Quantum Singularity', epPerHS: 100.0 }
  ];

  // Verified boost explosion chances — AuroraDB.db TechTypeID=42 [ref A-4]
  // "No Power Plant Boost" (TechSystemID=24625) confirms 5% base rate at x1.0.
  var BOOST_EXPLOSION = {
    1.0: 5, /* verified: TechSystemID=24625, AdditionalInfo2=5.0 */ 1.1: 7, 1.2: 10, 1.3: 15,
    1.4: 20, 1.6: 30, 1.8: 40, 2.0: 50
  };

  var CONFIGS = ['A', 'B'];

  function fmt(n) {
    if (n >= 1000000) return n.toLocaleString('en-US', {maximumFractionDigits: 0});
    if (n >= 100) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    if (n >= 10) return n.toLocaleString('en-US', {maximumFractionDigits: 2});
    return n.toLocaleString('en-US', {maximumFractionDigits: 3});
  }

  function buildConfigCard(id) {
    var techOptions = ENGINE_TECHS.map(function(t, i) {
      var sel = (i === 2) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + ' (' + t.epPerHS + ' EP/HS)</option>';
    }).join('');

    return '<div class="calc-card active" id="card' + id + '">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field">' +
        '<label>Engine Technology</label>' +
        '<select id="tech' + id + '" onchange="recalcAll()">' + techOptions + '</select>' +
      '</div>' +
      '<div class="calc-field">' +
        '<label>Engine Size (HS): <span id="sizeLabel' + id + '">10</span></label>' +
        '<div class="range-row">' +
          '<input type="range" id="sizeRange' + id + '" min="1" max="400" value="10" step="1" oninput="syncSize(\'' + id + '\',this.value)">' +
          '<input type="number" id="sizeNum' + id + '" min="0.1" max="400" value="10" step="0.1" oninput="syncSizeNum(\'' + id + '\',this.value)">' +
        '</div>' +
      '</div>' +
      '<div class="calc-field">' +
        '<label>Power Modifier: <span id="powerLabel' + id + '">1.0</span>x</label>' +
        '<div class="range-row">' +
          '<input type="range" id="powerRange' + id + '" min="1" max="30" value="10" step="1" oninput="syncPower(\'' + id + '\',this.value)">' +
          '<input type="number" id="powerNum' + id + '" min="0.1" max="3.0" value="1.0" step="0.1" oninput="syncPowerNum(\'' + id + '\',this.value)">' +
        '</div>' +
      '</div>' +
      '<div class="calc-field">' +
        '<label>Number of Engines</label>' +
        '<input type="number" id="count' + id + '" min="0" max="100" value="2" step="1" oninput="recalcAll()">' +
      '</div>' +
      '<div class="calc-results" id="results' + id + '"></div>' +
    '</div>';
  }

  // Initialize config grid
  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Sync helpers
  window.syncSize = function(id, val) {
    document.getElementById('sizeNum' + id).value = val;
    document.getElementById('sizeLabel' + id).textContent = val;
    recalcAll();
  };
  window.syncSizeNum = function(id, val) {
    var v = parseFloat(val);
    if (isNaN(v) || v < 0.1) return;
    document.getElementById('sizeRange' + id).value = Math.round(v);
    document.getElementById('sizeLabel' + id).textContent = v;
    recalcAll();
  };
  window.syncPower = function(id, val) {
    var p = (parseInt(val) / 10).toFixed(1);
    document.getElementById('powerNum' + id).value = p;
    document.getElementById('powerLabel' + id).textContent = p;
    recalcAll();
  };
  window.syncPowerNum = function(id, val) {
    var v = parseFloat(val);
    if (isNaN(v) || v < 0.1) return;
    document.getElementById('powerRange' + id).value = Math.round(v * 10);
    document.getElementById('powerLabel' + id).textContent = v.toFixed(1);
    recalcAll();
  };

  window.recalcAll = function() {
    var shipHS = parseFloat(document.getElementById('shipHS').value) || 1;
    var shipTons = shipHS * 50;
    document.getElementById('shipTons').textContent = shipTons.toLocaleString('en-US');

    CONFIGS.forEach(function(id) {
      var techIdx = parseInt(document.getElementById('tech' + id).value);
      var sizeHS = parseFloat(document.getElementById('sizeNum' + id).value) || 0;
      var powerMod = parseFloat(document.getElementById('powerNum' + id).value) || 0;
      var numEngines = parseInt(document.getElementById('count' + id).value) || 0;

      var tech = ENGINE_TECHS[techIdx];
      var epPerEngine = sizeHS * tech.epPerHS * powerMod;
      var totalEP = epPerEngine * numEngines;
      var engineTonsEach = sizeHS * 50;
      var totalEngineTons = engineTonsEach * numEngines;
      var totalEngineHS = sizeHS * numEngines;
      var speed = shipHS > 0 ? (totalEP * 1000 / shipHS) : 0;
      var remainingTons = shipTons - totalEngineTons;

      // Commercial classification: power <= 0.5x AND size >= 25 HS [ref 8.3-6]
      var isCommercial = (powerMod <= 0.5 && sizeHS >= 25);

      // Explosion chance lookup — only for power > 1.0x
      var explosionText = 'N/A';
      if (powerMod > 1.0) {
        // Find closest boost level at or below the modifier
        var boostKeys = [1.0, 1.1, 1.2, 1.3, 1.4, 1.6, 1.8, 2.0];
        var closest = 1.0;
        for (var i = 0; i < boostKeys.length; i++) {
          if (boostKeys[i] <= powerMod) closest = boostKeys[i];
        }
        if (BOOST_EXPLOSION[closest] !== undefined && closest > 1.0) {
          explosionText = BOOST_EXPLOSION[closest] + '%';
          if (powerMod > 2.0) explosionText = '>50% (beyond max tech)';
        } else {
          explosionText = '5% (base)';
        }
      } else {
        explosionText = '5% (base)';
      }

      // Engine HTK = SQRT(size)
      var htk = Math.floor(Math.sqrt(sizeHS));

      var html = '<div class="calc-results-header">Results</div>' +
        row('Speed', fmt(speed) + ' km/s', 'speed') +
        row('EP / Engine', fmt(epPerEngine)) +
        row('Total EP', fmt(totalEP)) +
        row('Engine Tons (each)', fmt(engineTonsEach) + ' t') +
        row('Total Engine Tons', fmt(totalEngineTons) + ' t (' + fmt(totalEngineHS) + ' HS)') +
        row('Remaining', remainingTons >= 0 ? fmt(remainingTons) + ' t' : fmt(remainingTons) + ' t (OVER)', remainingTons < 0 ? 'warning' : '') +
        row('Classification', isCommercial ? 'Commercial' : 'Military', isCommercial ? 'commercial' : 'military') +
        row('Engine HTK', htk + ' (per engine)') +
        row('Explosion Risk', explosionText);

      document.getElementById('results' + id).innerHTML = html;
    });
  };

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  // Set different defaults for configs B and C
  document.getElementById('tech' + 'B').value = 4; // Nuclear Gas-Core
  document.getElementById('sizeNum' + 'B').value = 15;
  document.getElementById('sizeRange' + 'B').value = 15;
  document.getElementById('sizeLabel' + 'B').textContent = '15';

  // Initial calculation
  recalcAll();
})();
</script>
