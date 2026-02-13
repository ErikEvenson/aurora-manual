---
title: "Mining & Construction Calculator"
parent: "Tools"
nav_order: 4
---

# Mining & Construction Calculator

*Added: v2026.02.13*

Calculate annual output for construction factories, mines, and fuel refineries. Switch between production types using the mode buttons. All tech values are verified against the Aurora game database (AuroraDB.db v2.7.1).

> **Note:** Governor manufacturing/mining bonuses (formula: `1 + Governor_Skill x 0.05`) are intentionally excluded. While the bonus structure is documented in the manual, the 0.05 coefficient has no database citation. Only verified calculations are shown.

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

<div class="calc-wrapper" id="prodCalc">

<div class="calc-mode-bar">
  <button class="calc-mode-btn active" data-mode="construction" onclick="setProdMode('construction')">Construction</button>
  <button class="calc-mode-btn" data-mode="mining" onclick="setProdMode('mining')">Mining</button>
  <button class="calc-mode-btn" data-mode="fuel" onclick="setProdMode('fuel')">Fuel Production</button>
</div>

<div class="calc-grid" id="configGrid">
</div>

<h2>Reference Tables</h2>

<details class="calc-collapsible">
<summary>Construction Rate Technology (12 tiers) — AuroraDB.db [ref A-6, D-31]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>BP / Factory / Year</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Base</td><td>10</td><td>--</td></tr>
<tr><td>1</td><td>12</td><td>3,000</td></tr>
<tr><td>2</td><td>14</td><td>5,000</td></tr>
<tr><td>3</td><td>16</td><td>10,000</td></tr>
<tr><td>4</td><td>20</td><td>20,000</td></tr>
<tr><td>5</td><td>25</td><td>40,000</td></tr>
<tr><td>6</td><td>30</td><td>80,000</td></tr>
<tr><td>7</td><td>36</td><td>150,000</td></tr>
<tr><td>8</td><td>42</td><td>300,000</td></tr>
<tr><td>9</td><td>50</td><td>600,000</td></tr>
<tr><td>10</td><td>60</td><td>1,250,000</td></tr>
<tr><td>11</td><td>70</td><td>2,500,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Mining Production Technology (12 tiers) — AuroraDB.db [ref A-7, D-32]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Tons / Mine / Year</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Base</td><td>10</td><td>--</td></tr>
<tr><td>1</td><td>12</td><td>3,000</td></tr>
<tr><td>2</td><td>14</td><td>5,000</td></tr>
<tr><td>3</td><td>16</td><td>10,000</td></tr>
<tr><td>4</td><td>20</td><td>20,000</td></tr>
<tr><td>5</td><td>25</td><td>40,000</td></tr>
<tr><td>6</td><td>30</td><td>80,000</td></tr>
<tr><td>7</td><td>36</td><td>150,000</td></tr>
<tr><td>8</td><td>42</td><td>300,000</td></tr>
<tr><td>9</td><td>50</td><td>600,000</td></tr>
<tr><td>10</td><td>60</td><td>1,250,000</td></tr>
<tr><td>11</td><td>70</td><td>2,500,000</td></tr>
</tbody>
</table>
</div>
</details>

<details class="calc-collapsible">
<summary>Fuel Refinery Output Technology (12 tiers) — AuroraDB.db [ref A-8, D-33]</summary>
<div class="detail-content">
<table class="calc-ref-table">
<thead><tr><th>Tech Level</th><th>Litres / Refinery / Year</th><th>Research (RP)</th></tr></thead>
<tbody>
<tr><td>Base</td><td>40,000</td><td>--</td></tr>
<tr><td>1</td><td>48,000</td><td>3,000</td></tr>
<tr><td>2</td><td>56,000</td><td>5,000</td></tr>
<tr><td>3</td><td>64,000</td><td>10,000</td></tr>
<tr><td>4</td><td>80,000</td><td>20,000</td></tr>
<tr><td>5</td><td>100,000</td><td>40,000</td></tr>
<tr><td>6</td><td>120,000</td><td>80,000</td></tr>
<tr><td>7</td><td>144,000</td><td>150,000</td></tr>
<tr><td>8</td><td>168,000</td><td>300,000</td></tr>
<tr><td>9</td><td>200,000</td><td>600,000</td></tr>
<tr><td>10</td><td>240,000</td><td>1,250,000</td></tr>
<tr><td>11</td><td>280,000</td><td>2,500,000</td></tr>
</tbody>
</table>
</div>
</details>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Construction: Annual_BP = Factories x BP_per_Factory</code> — <a href="../appendices/A-formulas.html#a51-construction-output">ref A-6</a><br>
<code>Mining: Annual_Tons = Mines x Tons_per_Mine x Accessibility</code> — <a href="../appendices/A-formulas.html#a52-mining-output">ref A-7</a><br>
<code>Fuel: Annual_Litres = Refineries x Litres_per_Refinery</code> — <a href="../appendices/A-formulas.html#a53-fuel-production">ref A-8</a><br>
<br>
<strong>Omitted:</strong> Governor bonus (<code>1 + Governor x 0.05</code>) — the 0.05 coefficient lacks a database citation.
</div>

</div>

<script>
(function() {
  // Verified construction rates — AuroraDB.db [ref A-6, D-31]
  var CONSTRUCTION_TECHS = [
    { name: 'Base (10 BP)', output: 10 },
    { name: 'Level 1 (12 BP)', output: 12 },
    { name: 'Level 2 (14 BP)', output: 14 },
    { name: 'Level 3 (16 BP)', output: 16 },
    { name: 'Level 4 (20 BP)', output: 20 },
    { name: 'Level 5 (25 BP)', output: 25 },
    { name: 'Level 6 (30 BP)', output: 30 },
    { name: 'Level 7 (36 BP)', output: 36 },
    { name: 'Level 8 (42 BP)', output: 42 },
    { name: 'Level 9 (50 BP)', output: 50 },
    { name: 'Level 10 (60 BP)', output: 60 },
    { name: 'Level 11 (70 BP)', output: 70 }
  ];

  // Verified mining rates — AuroraDB.db [ref A-7, D-32]
  var MINING_TECHS = [
    { name: 'Base (10 t)', output: 10 },
    { name: 'Level 1 (12 t)', output: 12 },
    { name: 'Level 2 (14 t)', output: 14 },
    { name: 'Level 3 (16 t)', output: 16 },
    { name: 'Level 4 (20 t)', output: 20 },
    { name: 'Level 5 (25 t)', output: 25 },
    { name: 'Level 6 (30 t)', output: 30 },
    { name: 'Level 7 (36 t)', output: 36 },
    { name: 'Level 8 (42 t)', output: 42 },
    { name: 'Level 9 (50 t)', output: 50 },
    { name: 'Level 10 (60 t)', output: 60 },
    { name: 'Level 11 (70 t)', output: 70 }
  ];

  // Verified fuel refinery output — AuroraDB.db [ref A-8, D-33]
  var FUEL_TECHS = [
    { name: 'Base (40k)', output: 40000 },
    { name: 'Level 1 (48k)', output: 48000 },
    { name: 'Level 2 (56k)', output: 56000 },
    { name: 'Level 3 (64k)', output: 64000 },
    { name: 'Level 4 (80k)', output: 80000 },
    { name: 'Level 5 (100k)', output: 100000 },
    { name: 'Level 6 (120k)', output: 120000 },
    { name: 'Level 7 (144k)', output: 144000 },
    { name: 'Level 8 (168k)', output: 168000 },
    { name: 'Level 9 (200k)', output: 200000 },
    { name: 'Level 10 (240k)', output: 240000 },
    { name: 'Level 11 (280k)', output: 280000 }
  ];

  var CONFIGS = ['A', 'B'];
  var currentMode = 'construction';

  function fmtNum(n) {
    return n.toLocaleString('en-US', {maximumFractionDigits: 1});
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

  function buildConstructionCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Number of Factories</label>' +
        '<input type="number" id="cNum' + id + '" min="0" max="100000" value="200" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Construction Tech Level</label>' +
        '<select id="cTech' + id + '" onchange="recalcAll()">' + opts(CONSTRUCTION_TECHS, 0) + '</select></div>' +
      '<div class="calc-results" id="cResults' + id + '"></div>' +
    '</div>';
  }

  function buildMiningCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Number of Mines</label>' +
        '<input type="number" id="mNum' + id + '" min="0" max="100000" value="100" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Mining Tech Level</label>' +
        '<select id="mTech' + id + '" onchange="recalcAll()">' + opts(MINING_TECHS, 0) + '</select></div>' +
      '<div class="calc-field"><label>Mineral Accessibility (0.1 - 1.0)</label>' +
        '<input type="number" id="mAcc' + id + '" min="0.1" max="1.0" value="0.8" step="0.1" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="mResults' + id + '"></div>' +
    '</div>';
  }

  function buildFuelCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Number of Refineries</label>' +
        '<input type="number" id="fNum' + id + '" min="0" max="100000" value="50" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Fuel Production Tech Level</label>' +
        '<select id="fTech' + id + '" onchange="recalcAll()">' + opts(FUEL_TECHS, 0) + '</select></div>' +
      '<div class="calc-results" id="fResults' + id + '"></div>' +
    '</div>';
  }

  // === Mode-specific calculations ===

  function recalcConstruction() {
    CONFIGS.forEach(function(id) {
      var num = parseInt(document.getElementById('cNum' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('cTech' + id).value);
      var tech = CONSTRUCTION_TECHS[techIdx];
      var perFactory = tech.output;
      var total = num * perFactory;

      var html = '<div class="calc-results-header">Results</div>' +
        row('Output per Factory', fmtNum(perFactory) + ' BP/yr') +
        row('Total Annual Output', fmtNum(total) + ' BP/yr', 'highlight');

      document.getElementById('cResults' + id).innerHTML = html;
    });
  }

  function recalcMining() {
    CONFIGS.forEach(function(id) {
      var num = parseInt(document.getElementById('mNum' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('mTech' + id).value);
      var acc = parseFloat(document.getElementById('mAcc' + id).value) || 0;
      var tech = MINING_TECHS[techIdx];
      var perMine = tech.output;
      var effectivePerMine = perMine * acc;
      var total = num * effectivePerMine;

      var html = '<div class="calc-results-header">Results</div>' +
        row('Base Output per Mine', fmtNum(perMine) + ' tons/yr') +
        row('Effective per Mine (x' + acc + ')', fmtNum(effectivePerMine) + ' tons/yr') +
        row('Total Annual Output', fmtNum(total) + ' tons/yr', 'highlight');

      document.getElementById('mResults' + id).innerHTML = html;
    });
  }

  function recalcFuel() {
    CONFIGS.forEach(function(id) {
      var num = parseInt(document.getElementById('fNum' + id).value) || 0;
      var techIdx = parseInt(document.getElementById('fTech' + id).value);
      var tech = FUEL_TECHS[techIdx];
      var perRefinery = tech.output;
      var total = num * perRefinery;

      var html = '<div class="calc-results-header">Results</div>' +
        row('Output per Refinery', fmtNum(perRefinery) + ' litres/yr') +
        row('Total Annual Output', fmtNum(total) + ' litres/yr', 'highlight');

      document.getElementById('fResults' + id).innerHTML = html;
    });
  }

  // === Mode switching ===

  window.setProdMode = function(mode) {
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
    if (mode === 'construction') {
      grid.innerHTML = CONFIGS.map(buildConstructionCard).join('');
      document.getElementById('cTech' + 'B').value = 5;
      document.getElementById('cNum' + 'B').value = 500;
    } else if (mode === 'mining') {
      grid.innerHTML = CONFIGS.map(buildMiningCard).join('');
      document.getElementById('mTech' + 'B').value = 5;
      document.getElementById('mNum' + 'B').value = 200;
      document.getElementById('mAcc' + 'B').value = 0.5;
    } else {
      grid.innerHTML = CONFIGS.map(buildFuelCard).join('');
      document.getElementById('fTech' + 'B').value = 5;
      document.getElementById('fNum' + 'B').value = 100;
    }
    recalcAll();
  };

  window.recalcAll = function() {
    if (currentMode === 'construction') recalcConstruction();
    else if (currentMode === 'mining') recalcMining();
    else recalcFuel();
  };

  // === Initialize ===
  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConstructionCard).join('');
  document.getElementById('cTech' + 'B').value = 5;
  document.getElementById('cNum' + 'B').value = 500;
  recalcAll();
})();
</script>
