---
title: "Sensor Detection Range Calculator"
parent: "Tools"
nav_order: 2
---

# Sensor Detection Range Calculator

*Updated: v2026.02.13*

Calculate detection ranges for all three Aurora sensor types: passive thermal, passive EM, and active gravitational. Compare up to 2 configurations side-by-side. All formulas and tech values are verified against the Aurora game database (AuroraDB.db v2.7.1) and referenced in the manual.

<style>
  .calc-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #e0e0e0;
  }
  .calc-mode-bar {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }
  .calc-mode-btn {
    padding: 8px 16px;
    background: #2d2d44;
    border: 1px solid #3d3d5c;
    border-radius: 4px;
    color: #aaa;
    font-size: 14px;
    cursor: pointer;
    font-family: inherit;
  }
  .calc-mode-btn:hover {
    border-color: #4ecdc4;
    color: #fff;
  }
  .calc-mode-btn.active {
    background: #1a1a2e;
    border-color: #4ecdc4;
    color: #4ecdc4;
    font-weight: 600;
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
  .calc-result-row .value.range {
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

<div class="calc-wrapper" id="sensorCalc">

<div class="calc-mode-bar">
  <button class="calc-mode-btn active" data-mode="thermal" onclick="setMode('thermal')">Passive Thermal</button>
  <button class="calc-mode-btn" data-mode="em" onclick="setMode('em')">Passive EM</button>
  <button class="calc-mode-btn" data-mode="active" onclick="setMode('active')">Active Sensor</button>
</div>

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Thermal Sensor Sensitivity (12 tiers) — AuroraDB.db TechTypeID=19 [ref D-14]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Sensitivity</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>1</td><td>5</td><td>1,000</td></tr>
<tr><td>2</td><td>6</td><td>2,000</td></tr>
<tr><td>3</td><td>8</td><td>4,000</td></tr>
<tr><td>4</td><td>11</td><td>8,000</td></tr>
<tr><td>5</td><td>14</td><td>15,000</td></tr>
<tr><td>6</td><td>18</td><td>30,000</td></tr>
<tr><td>7</td><td>24</td><td>60,000</td></tr>
<tr><td>8</td><td>32</td><td>120,000</td></tr>
<tr><td>9</td><td>40</td><td>250,000</td></tr>
<tr><td>10</td><td>50</td><td>500,000</td></tr>
<tr><td>11</td><td>60</td><td>1,000,000</td></tr>
<tr><td>12</td><td>75</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>EM Sensor Sensitivity (12 tiers) — AuroraDB.db TechTypeID=125 [ref D-15]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Sensitivity</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>1</td><td>5</td><td>1,000</td></tr>
<tr><td>2</td><td>6</td><td>2,000</td></tr>
<tr><td>3</td><td>8</td><td>4,000</td></tr>
<tr><td>4</td><td>11</td><td>8,000</td></tr>
<tr><td>5</td><td>14</td><td>15,000</td></tr>
<tr><td>6</td><td>18</td><td>30,000</td></tr>
<tr><td>7</td><td>24</td><td>60,000</td></tr>
<tr><td>8</td><td>32</td><td>120,000</td></tr>
<tr><td>9</td><td>40</td><td>250,000</td></tr>
<tr><td>10</td><td>50</td><td>500,000</td></tr>
<tr><td>11</td><td>60</td><td>1,000,000</td></tr>
<tr><td>12</td><td>75</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Active Grav Sensor Strength (13 tiers) — AuroraDB.db TechTypeID=20 [ref D-16]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Strength</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Conventional</td><td>2</td><td>500</td></tr>
<tr><td>1</td><td>10</td><td>1,000</td></tr>
<tr><td>2</td><td>12</td><td>2,000</td></tr>
<tr><td>3</td><td>16</td><td>4,000</td></tr>
<tr><td>4</td><td>21</td><td>8,000</td></tr>
<tr><td>5</td><td>28</td><td>15,000</td></tr>
<tr><td>6</td><td>36</td><td>30,000</td></tr>
<tr><td>7</td><td>48</td><td>60,000</td></tr>
<tr><td>8</td><td>60</td><td>125,000</td></tr>
<tr><td>9</td><td>80</td><td>250,000</td></tr>
<tr><td>10</td><td>100</td><td>500,000</td></tr>
<tr><td>11</td><td>135</td><td>1,000,000</td></tr>
<tr><td>12</td><td>180</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Thermal Reduction Technology (13 tiers) — AuroraDB.db TechTypeID=127 [ref 11.1-2]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Technology</th><th>Signature Multiplier</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>100% Normal</td><td>1.00x</td><td>Starting</td></tr>
<tr><td>75% Normal</td><td>0.75x</td><td>1,500</td></tr>
<tr><td>50% Normal</td><td>0.50x</td><td>3,000</td></tr>
<tr><td>35% Normal</td><td>0.35x</td><td>6,000</td></tr>
<tr><td>24% Normal</td><td>0.24x</td><td>12,000</td></tr>
<tr><td>16% Normal</td><td>0.16x</td><td>25,000</td></tr>
<tr><td>12% Normal</td><td>0.12x</td><td>50,000</td></tr>
<tr><td>8% Normal</td><td>0.08x</td><td>100,000</td></tr>
<tr><td>6% Normal</td><td>0.06x</td><td>200,000</td></tr>
<tr><td>4% Normal</td><td>0.04x</td><td>400,000</td></tr>
<tr><td>3% Normal</td><td>0.03x</td><td>750,000</td></tr>
<tr><td>2% Normal</td><td>0.02x</td><td>1,500,000</td></tr>
<tr><td>1% Normal</td><td>0.01x</td><td>2,500,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Cloaking Sensor Reduction (10 tiers) — AuroraDB.db TechTypeID=154 [ref 11.4-2]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Technology</th><th>Signature Reduction</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Cloak Sensor Reduction 75%</td><td>75%</td><td>4,000</td></tr>
<tr><td>Cloak Sensor Reduction 80%</td><td>80%</td><td>8,000</td></tr>
<tr><td>Cloak Sensor Reduction 85%</td><td>85%</td><td>15,000</td></tr>
<tr><td>Cloak Sensor Reduction 90%</td><td>90%</td><td>30,000</td></tr>
<tr><td>Cloak Sensor Reduction 93%</td><td>93%</td><td>60,000</td></tr>
<tr><td>Cloak Sensor Reduction 95%</td><td>95%</td><td>125,000</td></tr>
<tr><td>Cloak Sensor Reduction 97%</td><td>97%</td><td>250,000</td></tr>
<tr><td>Cloak Sensor Reduction 98%</td><td>98%</td><td>500,000</td></tr>
<tr><td>Cloak Sensor Reduction 99%</td><td>99%</td><td>1,000,000</td></tr>
<tr><td>Cloak Sensor Reduction 99.5%</td><td>99.5%</td><td>2,000,000</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Passive Range (km) = sqrt(Size_HS * Tech_Value * Signature) * 250,000</code> — <a href="../appendices/A-formulas.html#a33-passive-sensor-detection">ref A-12</a><br>
<code>Active Range (km) = sqrt((Strength * HS * EM_Sens * Res^(2/3)) / PI) * 1,000,000</code> — <a href="../appendices/A-formulas.html#a34-active-sensor-detection">ref A-16</a><br>
<code>Off-Resolution = Base_Range * sqrt(Target_HS / Resolution)</code> — <a href="../appendices/A-formulas.html#a34-active-sensor-detection">ref A-12</a><br>
<code>Thermal Sig = Engine_EP * Thermal_Reduction_Multiplier</code> — <a href="../11-sensors-and-detection/11.1-thermal-em-signatures.html#1111-thermal-signature">ref 11.1-1</a><br>
<code>Cloak Effect = Signature * (1 - Cloak% / 100)</code> — <a href="../11-sensors-and-detection/11.4-stealth.html#1141-cloaking-technology">ref 11.4-1</a><br>
<code>Jammer Effect = Range * max(0, 1 - (SJ - ECCM) * 0.1)</code> — <a href="../appendices/A-formulas.html#a37-electronic-warfare-effects">ref A-17</a> (active sensors only; passive thermal/EM sensors detect emissions and cannot be jammed)
</div>

</div>

<script>
(function() {
  // Verified thermal sensor sensitivity — AuroraDB.db TechTypeID=19 [ref D-14]
  var THERMAL_SENS = [
    {name: '5 (Level 1)', val: 5},
    {name: '6 (Level 2)', val: 6},
    {name: '8 (Level 3)', val: 8},
    {name: '11 (Level 4)', val: 11},
    {name: '14 (Level 5)', val: 14},
    {name: '18 (Level 6)', val: 18},
    {name: '24 (Level 7)', val: 24},
    {name: '32 (Level 8)', val: 32},
    {name: '40 (Level 9)', val: 40},
    {name: '50 (Level 10)', val: 50},
    {name: '60 (Level 11)', val: 60},
    {name: '75 (Level 12)', val: 75}
  ];

  // Verified EM sensor sensitivity — AuroraDB.db TechTypeID=125 [ref D-15]
  // Identical progression to thermal sensors
  var EM_SENS = THERMAL_SENS;

  // Verified active grav sensor strength — AuroraDB.db TechTypeID=20 [ref D-16]
  var ACTIVE_STR = [
    {name: '2 (Conventional)', val: 2},
    {name: '10 (Level 1)', val: 10},
    {name: '12 (Level 2)', val: 12},
    {name: '16 (Level 3)', val: 16},
    {name: '21 (Level 4)', val: 21},
    {name: '28 (Level 5)', val: 28},
    {name: '36 (Level 6)', val: 36},
    {name: '48 (Level 7)', val: 48},
    {name: '60 (Level 8)', val: 60},
    {name: '80 (Level 9)', val: 80},
    {name: '100 (Level 10)', val: 100},
    {name: '135 (Level 11)', val: 135},
    {name: '180 (Level 12)', val: 180}
  ];

  // Verified thermal reduction — AuroraDB.db TechTypeID=127 [ref 11.1-2]
  var THERMAL_RED = [
    {name: '100% Normal', val: 1.00},
    {name: '75% Normal', val: 0.75},
    {name: '50% Normal', val: 0.50},
    {name: '35% Normal', val: 0.35},
    {name: '24% Normal', val: 0.24},
    {name: '16% Normal', val: 0.16},
    {name: '12% Normal', val: 0.12},
    {name: '8% Normal', val: 0.08},
    {name: '6% Normal', val: 0.06},
    {name: '4% Normal', val: 0.04},
    {name: '3% Normal', val: 0.03},
    {name: '2% Normal', val: 0.02},
    {name: '1% Normal', val: 0.01}
  ];

  var CONFIGS = ['A', 'B'];
  var currentMode = 'thermal';

  function fmtRange(km) {
    if (km <= 0) return '0 km';
    if (km >= 1e9) return (km / 1e9).toFixed(2) + ' bn km';
    if (km >= 1e6) return (km / 1e6).toFixed(1) + 'M km';
    return Math.round(km).toLocaleString('en-US') + ' km';
  }

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

  function opts(techs, selected) {
    return techs.map(function(t, i) {
      var sel = (i === selected) ? ' selected' : '';
      return '<option value="' + i + '"' + sel + '>' + t.name + '</option>';
    }).join('');
  }

  // === Card builders ===

  function buildThermalCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Sensor Size (HS)</label>' +
        '<input type="number" id="thSize' + id + '" min="0.1" max="50" value="10" step="0.1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Thermal Sensitivity Tech</label>' +
        '<select id="thTech' + id + '" onchange="recalcAll()">' + opts(THERMAL_SENS, 4) + '</select></div>' +
      '<div class="calc-field"><label>Target Engine Power (EP)</label>' +
        '<input type="number" id="thEP' + id + '" min="0" max="1000000" value="2000" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Target Thermal Reduction</label>' +
        '<select id="thRed' + id + '" onchange="recalcAll()">' + opts(THERMAL_RED, 0) + '</select></div>' +
      '<div class="calc-field"><label>Target Cloak: <span id="thCloakLabel' + id + '">0</span>%</label>' +
        '<div class="range-row">' +
          '<input type="range" id="thCloakRange' + id + '" min="0" max="99.5" value="0" step="0.5" oninput="syncCloak(\'' + id + '\',this.value)">' +
          '<input type="number" id="thCloakNum' + id + '" min="0" max="99.5" value="0" step="0.5" style="width:70px;text-align:right" oninput="syncCloakNum(\'' + id + '\',this.value)">' +
        '</div></div>' +
      '<div class="calc-results" id="thResults' + id + '"></div>' +
    '</div>';
  }

  function buildEMCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Sensor Size (HS)</label>' +
        '<input type="number" id="emSize' + id + '" min="0.1" max="50" value="10" step="0.1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>EM Sensitivity Tech</label>' +
        '<select id="emTech' + id + '" onchange="recalcAll()">' + opts(EM_SENS, 4) + '</select></div>' +
      '<div class="calc-field"><label>Target EM Signature</label>' +
        '<input type="number" id="emSig' + id + '" min="0" max="1000000" value="5000" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="emResults' + id + '"></div>' +
    '</div>';
  }

  function buildActiveCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Sensor Size (HS)</label>' +
        '<input type="number" id="acSize' + id + '" min="0.1" max="50" value="10" step="0.1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Active Grav Strength Tech</label>' +
        '<select id="acStr' + id + '" onchange="recalcAll()">' + opts(ACTIVE_STR, 5) + '</select></div>' +
      '<div class="calc-field"><label>EM Sensitivity Tech</label>' +
        '<select id="acEm' + id + '" onchange="recalcAll()">' + opts(EM_SENS, 4) + '</select></div>' +
      '<div class="calc-field"><label>Sensor Resolution (HS)</label>' +
        '<input type="number" id="acRes' + id + '" min="1" max="500" value="100" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Target Actual Size (HS)</label>' +
        '<input type="number" id="acTarget' + id + '" min="1" max="10000" value="100" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Target Sensor Jammer (0-10)</label>' +
        '<input type="number" id="acSJ' + id + '" min="0" max="10" value="0" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Sensor ECCM (0-10)</label>' +
        '<input type="number" id="acECCM' + id + '" min="0" max="10" value="0" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="acResults' + id + '"></div>' +
    '</div>';
  }

  // === Cloak slider sync ===

  window.syncCloak = function(id, val) {
    document.getElementById('thCloakNum' + id).value = val;
    document.getElementById('thCloakLabel' + id).textContent = val;
    recalcAll();
  };

  window.syncCloakNum = function(id, val) {
    var v = parseFloat(val);
    if (isNaN(v) || v < 0) return;
    if (v > 99.5) v = 99.5;
    document.getElementById('thCloakRange' + id).value = v;
    document.getElementById('thCloakLabel' + id).textContent = v;
    recalcAll();
  };

  // === Jammer calculation ===

  function jammerMult(sj, eccm) {
    var net = Math.max(0, sj - eccm);
    return Math.max(0, 1 - net * 0.1);
  }

  // === Mode-specific calculation ===

  function recalcThermal() {
    CONFIGS.forEach(function(id) {
      var sizeHS = parseFloat(document.getElementById('thSize' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('thTech' + id).value);
      var ep = parseFloat(document.getElementById('thEP' + id).value) || 0;
      var redIdx = parseInt(document.getElementById('thRed' + id).value);
      var cloak = parseFloat(document.getElementById('thCloakNum' + id).value) || 0;

      var techVal = THERMAL_SENS[techIdx].val;
      var redVal = THERMAL_RED[redIdx].val;

      var sensitivity = sizeHS * techVal;
      var thermalSig = ep * redVal;
      var effectiveSig = thermalSig * (1 - cloak / 100);
      var rangeKm = Math.sqrt(sensitivity * effectiveSig) * 250000;

      var html = '<div class="calc-results-header">Results</div>' +
        row('Sensor Sensitivity', fmtNum(sensitivity)) +
        row('Thermal Signature', fmtNum(thermalSig) + ' (EP ' + fmtNum(ep) + ' x ' + redVal + ')') +
        (cloak > 0 ? row('After Cloak (' + cloak + '%)', fmtNum(effectiveSig)) : '') +
        row('Detection Range', fmtRange(rangeKm), 'range');

      document.getElementById('thResults' + id).innerHTML = html;
    });
  }

  function recalcEM() {
    CONFIGS.forEach(function(id) {
      var sizeHS = parseFloat(document.getElementById('emSize' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('emTech' + id).value);
      var emSig = parseFloat(document.getElementById('emSig' + id).value) || 0;

      var techVal = EM_SENS[techIdx].val;

      var sensitivity = sizeHS * techVal;
      var rangeKm = Math.sqrt(sensitivity * emSig) * 250000;

      var html = '<div class="calc-results-header">Results</div>' +
        row('Sensor Sensitivity', fmtNum(sensitivity)) +
        row('Detection Range', fmtRange(rangeKm), 'range');

      document.getElementById('emResults' + id).innerHTML = html;
    });
  }

  function recalcActive() {
    CONFIGS.forEach(function(id) {
      var sizeHS = parseFloat(document.getElementById('acSize' + id).value) || 0;
      var strIdx = parseInt(document.getElementById('acStr' + id).value);
      var emIdx = parseInt(document.getElementById('acEm' + id).value);
      var resolution = parseFloat(document.getElementById('acRes' + id).value) || 1;
      var targetHS = parseFloat(document.getElementById('acTarget' + id).value) || 1;
      var sj = parseInt(document.getElementById('acSJ' + id).value) || 0;
      var eccm = parseInt(document.getElementById('acECCM' + id).value) || 0;

      var strVal = ACTIVE_STR[strIdx].val;
      var emVal = EM_SENS[emIdx].val;

      // Full C# formula [ref A-16]
      var resPow = Math.pow(resolution, 2/3);
      var baseRangeKm = Math.sqrt((strVal * sizeHS * emVal * resPow) / Math.PI) * 1000000;

      // Off-resolution scaling — capped at 1.0 for targets >= resolution
      var scaling = Math.min(1.0, Math.sqrt(targetHS / resolution));
      var effectiveKm = baseRangeKm * scaling;

      var jMult = jammerMult(sj, eccm);
      var jammedKm = effectiveKm * jMult;

      // Sensor GPS (own EM emission) [ref 11.1-9]
      var gps = strVal * sizeHS * resolution;

      var scalingText = scaling >= 1.0 ? '1.00 (target >= resolution)' :
        scaling.toFixed(3) + ' (sqrt(' + targetHS + '/' + resolution + '))';

      var html = '<div class="calc-results-header">Results</div>' +
        row('Base Range (at res ' + resolution + ')', fmtRange(baseRangeKm), 'range') +
        row('Scaling Factor', scalingText) +
        (scaling < 1.0 ? row('Effective Range vs Target', fmtRange(effectiveKm)) : '') +
        (sj > eccm ? row('Jammed Range (SJ' + sj + ' vs ECCM' + eccm + ')', fmtRange(jammedKm), jMult === 0 ? 'warning' : '') : '') +
        row('Sensor GPS (EM output)', fmtNum(gps), 'dimmed');

      document.getElementById('acResults' + id).innerHTML = html;
    });
  }

  // === Mode switching ===

  window.setMode = function(mode) {
    currentMode = mode;
    var btns = document.querySelectorAll('.calc-mode-btn');
    for (var i = 0; i < btns.length; i++) {
      var btn = btns[i];
      if (btn.getAttribute('data-mode') === mode) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }
    var grid = document.getElementById('configGrid');
    if (mode === 'thermal') {
      grid.innerHTML = CONFIGS.map(buildThermalCard).join('');
    } else if (mode === 'em') {
      grid.innerHTML = CONFIGS.map(buildEMCard).join('');
      // Config B defaults: higher tech, larger signature
      document.getElementById('emTech' + 'B').value = 6;
      document.getElementById('emSig' + 'B').value = 24000;
    } else {
      grid.innerHTML = CONFIGS.map(buildActiveCard).join('');
      // Config B defaults: higher tech, lower resolution (missile detection)
      document.getElementById('acStr' + 'B').value = 7;
      document.getElementById('acEm' + 'B').value = 6;
      document.getElementById('acRes' + 'B').value = 10;
    }
    recalcAll();
  };

  window.recalcAll = function() {
    if (currentMode === 'thermal') recalcThermal();
    else if (currentMode === 'em') recalcEM();
    else recalcActive();
  };

  // === Initialize ===

  // Build thermal mode (default)
  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildThermalCard).join('');

  // Config B defaults: better tech, reduced thermal engines
  document.getElementById('thTech' + 'B').value = 6;
  document.getElementById('thEP' + 'B').value = 4000;
  document.getElementById('thRed' + 'B').value = 3;

  recalcAll();
})();
</script>
