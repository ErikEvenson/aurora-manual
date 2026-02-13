---
title: "Beam Weapon To-Hit Calculator"
parent: "Tools"
nav_order: 7
---

# Beam Weapon To-Hit Calculator

*Added: v2026.02.13*

Calculate beam weapon hit probability based on range, tracking speed, target speed, and electronic warfare. Compare up to 2 firing scenarios side-by-side.

> **Verification Notice:** The to-hit formula (linear range falloff, tracking ratio, ECM/ECCM modifiers) is community-confirmed through extensive gameplay testing but has no direct database reference. This is the widely accepted model but treat edge-case results with caution.

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
    width: 90px;
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
  .calc-result-row .value.good {
    color: #95d5b2;
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

<div class="calc-wrapper" id="beamCalc">

<div class="calc-disclaimer">
  Community-confirmed formula: The to-hit model is validated through extensive gameplay testing but has no direct game database reference. See <a href="../appendices/A-formulas.html#a42-beam-weapon-accuracy" style="color:#ffe66d">Appendix A.4.2</a>.
</div>

<div class="calc-grid" id="configGrid">
</div>

<div class="calc-formula-note">
<strong>Formulas used (community-confirmed):</strong><br>
<code>Base_Hit = (1 - Range / Max_Range) x 100%</code> — <a href="../appendices/A-formulas.html#a42-beam-weapon-accuracy">ref A.4.2</a><br>
<code>Tracking_Mod = min(1.0, FC_Tracking / Target_Speed)</code><br>
<code>ECM_Mod = max(0, 1 - (Target_ECM - FC_ECCM) x 0.1)</code><br>
<code>Final_Hit% = Base_Hit x Tracking_Mod x ECM_Mod</code>
</div>

</div>

<script>
(function() {
  var CONFIGS = ['A', 'B'];

  function fmtNum(n) {
    if (n >= 1000000) return (n / 1000).toLocaleString('en-US', {maximumFractionDigits: 0}) + 'k';
    if (n >= 1000) return n.toLocaleString('en-US', {maximumFractionDigits: 0});
    if (n >= 1) return n.toLocaleString('en-US', {maximumFractionDigits: 1});
    return n.toLocaleString('en-US', {maximumFractionDigits: 2});
  }

  function row(label, value, cls) {
    return '<div class="calc-result-row"><span class="label">' + label +
      '</span><span class="value' + (cls ? ' ' + cls : '') + '">' + value + '</span></div>';
  }

  function buildConfigCard(id) {
    return '<div class="calc-card active">' +
      '<div class="calc-card-header">Scenario ' + id + '</div>' +
      '<div class="calc-field"><label>Weapon Max Range (km)</label>' +
        '<input type="number" id="bmMax' + id + '" min="10000" max="1000000" value="320000" step="10000" oninput="syncRange(\'' + id + '\');recalcAll()"></div>' +
      '<div class="calc-field"><label>Engagement Range: <span id="bmRangeLabel' + id + '">160,000</span> km</label>' +
        '<div class="range-row">' +
          '<input type="range" id="bmRangeSlider' + id + '" min="0" max="320000" value="160000" step="1000" oninput="syncRangeSlider(\'' + id + '\',this.value)">' +
          '<input type="number" id="bmRangeNum' + id + '" min="0" max="1000000" value="160000" step="1000" oninput="syncRangeNum(\'' + id + '\',this.value)">' +
        '</div></div>' +
      '<div class="calc-field"><label>Fire Control Tracking Speed (km/s)</label>' +
        '<input type="number" id="bmTrack' + id + '" min="0" max="100000" value="5000" step="100" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Target Speed (km/s)</label>' +
        '<input type="number" id="bmSpeed' + id + '" min="0" max="100000" value="4000" step="100" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Target ECM Level (0-10)</label>' +
        '<input type="number" id="bmECM' + id + '" min="0" max="10" value="0" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-field"><label>Fire Control ECCM Level (0-10)</label>' +
        '<input type="number" id="bmECCM' + id + '" min="0" max="10" value="0" step="1" oninput="recalcAll()"></div>' +
      '<div class="calc-results" id="bmResults' + id + '"></div>' +
    '</div>';
  }

  var grid = document.getElementById('configGrid');
  grid.innerHTML = CONFIGS.map(buildConfigCard).join('');

  // Config B defaults: different scenario
  document.getElementById('bmMax' + 'B').value = 192000;
  document.getElementById('bmRangeSlider' + 'B').max = 192000;
  document.getElementById('bmRangeSlider' + 'B').value = 96000;
  document.getElementById('bmRangeNum' + 'B').value = 96000;
  document.getElementById('bmRangeLabel' + 'B').textContent = '96,000';
  document.getElementById('bmTrack' + 'B').value = 3000;
  document.getElementById('bmSpeed' + 'B').value = 6000;
  document.getElementById('bmECM' + 'B').value = 3;
  document.getElementById('bmECCM' + 'B').value = 1;

  // Sync range slider max to weapon max range
  window.syncRange = function(id) {
    var maxRange = parseInt(document.getElementById('bmMax' + id).value) || 10000;
    var slider = document.getElementById('bmRangeSlider' + id);
    var numInput = document.getElementById('bmRangeNum' + id);
    slider.max = maxRange;
    if (parseInt(slider.value) > maxRange) {
      slider.value = maxRange;
      numInput.value = maxRange;
      document.getElementById('bmRangeLabel' + id).textContent = maxRange.toLocaleString('en-US');
    }
  };

  window.syncRangeSlider = function(id, val) {
    document.getElementById('bmRangeNum' + id).value = val;
    document.getElementById('bmRangeLabel' + id).textContent = parseInt(val).toLocaleString('en-US');
    recalcAll();
  };

  window.syncRangeNum = function(id, val) {
    var v = parseInt(val);
    if (isNaN(v) || v < 0) return;
    var maxRange = parseInt(document.getElementById('bmMax' + id).value) || 10000;
    if (v > maxRange) v = maxRange;
    document.getElementById('bmRangeSlider' + id).value = v;
    document.getElementById('bmRangeLabel' + id).textContent = v.toLocaleString('en-US');
    recalcAll();
  };

  window.recalcAll = function() {
    CONFIGS.forEach(function(id) {
      var maxRange = parseFloat(document.getElementById('bmMax' + id).value) || 1;
      var engRange = parseFloat(document.getElementById('bmRangeNum' + id).value) || 0;
      var tracking = parseFloat(document.getElementById('bmTrack' + id).value) || 0;
      var targetSpeed = parseFloat(document.getElementById('bmSpeed' + id).value) || 0;
      var ecm = parseInt(document.getElementById('bmECM' + id).value) || 0;
      var eccm = parseInt(document.getElementById('bmECCM' + id).value) || 0;

      // Base hit chance: linear range falloff
      var baseHit = Math.max(0, (1 - engRange / maxRange)) * 100;

      // Tracking modifier: capped at 1.0
      var trackMod = targetSpeed > 0 ? Math.min(1.0, tracking / targetSpeed) : 1.0;

      // ECM modifier: each net ECM level reduces by 10%
      var netECM = ecm - eccm;
      var ecmMod = Math.max(0, 1 - netECM * 0.1);

      // Final hit probability
      var finalHit = baseHit * trackMod * ecmMod;

      // Color coding for final hit
      var hitClass = finalHit >= 50 ? 'good' : finalHit >= 20 ? '' : 'warning';

      var html = '<div class="calc-results-header">Results</div>' +
        row('Base Hit Chance', fmtNum(baseHit) + '%') +
        row('Tracking Modifier', (trackMod * 100).toFixed(1) + '%' +
          (trackMod < 1 ? ' (' + fmtNum(tracking) + ' / ' + fmtNum(targetSpeed) + ')' : ' (tracking >= speed)'),
          trackMod < 1 ? 'warning' : 'dimmed') +
        row('ECM Modifier', (ecmMod * 100).toFixed(0) + '%' +
          (netECM > 0 ? ' (net ECM ' + netECM + ')' : netECM < 0 ? ' (ECCM advantage)' : ' (no EW)'),
          netECM > 0 ? 'warning' : 'dimmed') +
        row('Final Hit Probability', fmtNum(finalHit) + '%', finalHit > 0 ? 'highlight' : 'warning');

      document.getElementById('bmResults' + id).innerHTML = html;
    });
  };

  recalcAll();
})();
</script>
