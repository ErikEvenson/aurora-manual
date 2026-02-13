---
title: "Magazine Capacity Calculator"
parent: "Tools"
nav_order: 9
---

# Magazine Capacity Calculator

*Added: v2026.02.13*

Calculate magazine capacity, missile storage, and salvo endurance for ship design. Compare up to 2 configurations side-by-side. All formulas are verified against the Aurora game database (AuroraDB.db v2.7.1).

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
  .calc-field input[type="number"] {
    background: #2d2d44;
    border: 1px solid #3d3d5c;
    border-radius: 4px;
    color: #fff;
    padding: 6px 8px;
    font-size: 13px;
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
  .calc-result-row .value.good {
    color: #95d5b2;
  }
  .calc-result-row .value.dimmed {
    color: #888;
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

<div class="calc-wrapper" id="magCalc">

<div class="calc-grid" id="configGrid">
</div>

<div class="calc-formula-note">
<strong>Formulas used:</strong><br>
<code>Magazine_Capacity (MSP) = Magazine_HS x 20</code> — <a href="../appendices/D-reference-tables.html#d52-magazine-capacity">ref D-34</a><br>
<code>Missiles_Stored = floor(Total_MSP / Missile_Size_MSP)</code><br>
<code>Salvos = floor(Missiles_Stored / Missiles_per_Salvo)</code><br>
<code>1 MSP = 0.25 HS = 12.5 tons</code> — <a href="../appendices/D-reference-tables.html#d52-magazine-capacity">ref D-35</a>
</div>

</div>

<script>
(function() {
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
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Configuration ' + id + '</div>' +
      '<div class="calc-field"><label>Magazine Size (HS)</label>' +
        '<input type="number" id="magHS' + id + '" min="0.1" max="500" value="10" step="0.1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Number of Magazines</label>' +
        '<input type="number" id="magCount' + id + '" min="1" max="50" value="1" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Missile Size (MSP)</label>' +
        '<input type="number" id="magMSP' + id + '" min="1" max="100" value="4" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Launchers</label>' +
        '<input type="number" id="magLaunchers' + id + '" min="1" max="100" value="8" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="magResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults: larger magazine, bigger missiles
  document.getElementById('magHS' + 'B').value = 20;
  document.getElementById('magMSP' + 'B').value = 6;
  document.getElementById('magLaunchers' + 'B').value = 12;

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var magHS = parseFloat(document.getElementById('magHS' + id).value) || 0;
      var magCount = parseInt(document.getElementById('magCount' + id).value) || 1;
      var missileMSP = parseFloat(document.getElementById('magMSP' + id).value) || 1;
      var launchers = parseInt(document.getElementById('magLaunchers' + id).value) || 1;

      // Magazine capacity: 20 MSP per HS [ref D-34]
      var mspPerMag = magHS * 20;
      var totalMSP = mspPerMag * magCount;
      var totalMagHS = magHS * magCount;
      var totalMagTons = totalMagHS * 50;

      // Missile storage
      var missilesStored = Math.floor(totalMSP / missileMSP);

      // Salvo calculations
      var missilesPerSalvo = launchers;
      var salvos = Math.floor(missilesStored / missilesPerSalvo);
      var leftover = missilesStored - (salvos * missilesPerSalvo);

      // Missile weight contribution
      var missileTons = missileMSP * 12.5;

      // Salvo endurance class
      var salvoClass = salvos >= 10 ? 'good' : salvos >= 3 ? '' : 'warning';

      var html = '<div class="calc-results-header">Results</div>' +
        row('Capacity per Magazine', fmtNum(mspPerMag) + ' MSP') +
        row('Total Magazine Capacity', fmtNum(totalMSP) + ' MSP', 'highlight') +
        row('Magazine Size', fmtNum(totalMagHS) + ' HS (' + fmtNum(totalMagTons) + ' tons)') +
        row('Missiles Stored', fmtNum(missilesStored) + ' missiles') +
        row('Missile Weight (each)', fmtNum(missileTons) + ' tons (' + fmtNum(missileMSP) + ' MSP)') +
        row('Full Salvos', fmtNum(salvos) + (leftover > 0 ? ' + ' + leftover + ' extra' : ''), salvoClass) +
        row('Missiles per Salvo', fmtNum(missilesPerSalvo) + ' (' + launchers + ' launchers)', 'dimmed');

      document.getElementById('magResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
