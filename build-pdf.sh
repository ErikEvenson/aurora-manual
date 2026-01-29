#!/bin/bash
# Build Aurora 4X Manual PDF
# Uses pandoc + tectonic (LaTeX) for high-quality PDF output
# Version format: YYYY.MM.DD.## (zero-padded sequence per day)
#
# Usage:
#   bash build-pdf.sh              # Auto-increment version
#   bash build-pdf.sh 2026.01.28.07  # Explicit version (for releases)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

OUTPUT_DIR="releases"

# Use explicit version if provided, otherwise auto-increment
if [ $# -ge 1 ]; then
    VERSION="$1"
else
    DATE=$(date +%Y.%m.%d)
    # Determine sequence number for today (zero-padded, e.g., 01, 02)
    SEQ=1
    SEQ_PADDED=$(printf "%02d" $SEQ)
    while [ -f "${OUTPUT_DIR}/aurora-manual-${DATE}.${SEQ_PADDED}.pdf" ]; do
        SEQ=$((SEQ + 1))
        SEQ_PADDED=$(printf "%02d" $SEQ)
    done
    VERSION="${DATE}.${SEQ_PADDED}"
fi
OUTPUT_FILE="${OUTPUT_DIR}/aurora-manual-${VERSION}.pdf"

mkdir -p "$OUTPUT_DIR"


echo "Building Aurora 4X Manual v${VERSION}..."

# Define file order
FILES=(
    # Preface
    preface.md
    # Main chapters
    1-introduction/1.1-what-is-aurora.md
    1-introduction/1.2-installation.md
    1-introduction/1.3-first-launch.md
    2-game-setup/2.1-new-game-options.md
    2-game-setup/2.2-race-creation.md
    2-game-setup/2.3-system-generation.md
    2-game-setup/2.4-racial-traits.md
    2-game-setup/2.5-starting-conditions.md
    3-user-interface/3.1-main-window.md
    3-user-interface/3.2-system-map.md
    3-user-interface/3.3-common-controls.md
    3-user-interface/3.4-event-log.md
    3-user-interface/3.5-galactic-map.md
    4-systems-and-bodies/4.1-star-systems.md
    4-systems-and-bodies/4.2-planets-and-moons.md
    4-systems-and-bodies/4.3-asteroids-and-comets.md
    4-systems-and-bodies/4.4-jump-points.md
    5-colonies/5.1-establishing-colonies.md
    5-colonies/5.2-population.md
    5-colonies/5.3-environment.md
    5-colonies/5.4-infrastructure.md
    5-colonies/5.5-terraforming.md
    6-economy-and-industry/6.1-minerals.md
    6-economy-and-industry/6.2-mining.md
    6-economy-and-industry/6.3-construction.md
    6-economy-and-industry/6.4-wealth-and-trade.md
    6-economy-and-industry/6.5-civilian-economy.md
    7-research/7.1-technology-tree.md
    7-research/7.2-scientists.md
    7-research/7.3-research-facilities.md
    7-research/7.4-tech-categories.md
    8-ship-design/8.1-design-philosophy.md
    8-ship-design/8.2-hull-and-armor.md
    8-ship-design/8.3-engines.md
    8-ship-design/8.4-sensors.md
    8-ship-design/8.5-weapons.md
    8-ship-design/8.6-other-components.md
    8-ship-design/8.7-design-examples.md
    9-fleet-management/9.1-shipyards.md
    9-fleet-management/9.2-construction-and-refit.md
    9-fleet-management/9.3-task-groups.md
    9-fleet-management/9.4-fleet-organization.md
    9-fleet-management/9.5-orders.md
    9-fleet-management/9.6-light-naval-operations.md
    10-navigation/10.1-movement-mechanics.md
    10-navigation/10.2-jump-transit.md
    10-navigation/10.3-survey-operations.md
    10-navigation/10.4-waypoints.md
    11-sensors-and-detection/11.0-sensor-overview.md
    11-sensors-and-detection/11.1-thermal-em-signatures.md
    11-sensors-and-detection/11.2-passive-sensors.md
    11-sensors-and-detection/11.3-active-sensors.md
    11-sensors-and-detection/11.4-stealth.md
    12-combat/12.0-combat-overview.md
    12-combat/12.1-fire-controls.md
    12-combat/12.2-beam-weapons.md
    12-combat/12.3-missiles.md
    12-combat/12.4-point-defense.md
    12-combat/12.5-electronic-warfare.md
    12-combat/12.6-damage-and-armor.md
    12-combat/12.7-planetary-defence-centres.md
    13-ground-forces/13.1-unit-types.md
    13-ground-forces/13.2-training-and-transport.md
    13-ground-forces/13.3-ground-combat.md
    14-logistics/14.1-fuel.md
    14-logistics/14.2-maintenance.md
    14-logistics/14.3-supply-ships.md
    14-logistics/14.4-orbital-habitats.md
    15-diplomacy/15.1-alien-races.md
    15-diplomacy/15.2-communications.md
    15-diplomacy/15.3-treaties.md
    15-diplomacy/15.4-diplomacy.md
    15-diplomacy/15.5-intelligence-gathering.md
    16-commanders/16.1-officer-generation.md
    16-commanders/16.2-skills-and-bonuses.md
    16-commanders/16.3-assignments.md
    17-exploration/17.1-geological-survey.md
    17-exploration/17.2-gravitational-survey.md
    17-exploration/17.3-xenoarchaeology.md
    18-advanced-topics/18.1-game-mechanics.md
    18-advanced-topics/18.2-time-increments.md
    18-advanced-topics/18.3-spoiler-races.md
    18-advanced-topics/18.4-late-game-strategy.md
    18-advanced-topics/18.5-spacemaster-mode.md
    # Appendices
    appendices/A-formulas.md
    appendices/B-glossary.md
    appendices/C-tips-and-mistakes.md
    appendices/D-reference-tables.md
    # Worked Examples
    examples/early-game-economy.md
    examples/exploration-workflow.md
    examples/colony-establishment.md
    examples/mining-network-setup.md
    examples/terraforming-colony.md
    examples/beam-cruiser-design.md
    examples/missile-destroyer-design.md
    examples/missile-salvo-design.md
    examples/fleet-engagement.md
    examples/jump-point-defense.md
    examples/ground-invasion.md
    # UI Window References
    images/ship-design-window.md
    images/missile-design-window.md
    images/fleet-window.md
    images/system-map-window.md
    images/colony-window.md
    images/ground-forces-window.md
    images/diplomacy-window.md
    images/research-window.md
    images/shipyard-window.md
    images/event-log-window.md
)

# Validate all source files exist
for f in "${FILES[@]}"; do
    if [ ! -f "$f" ]; then
        echo "ERROR: Source file not found: $f" >&2
        exit 1
    fi
done

# Build PDF with pandoc + tectonic
pandoc \
    --metadata-file=metadata.yaml \
    --metadata="date:v${VERSION}" \
    --metadata="title:Aurora 4X Manual" \
    --metadata="subtitle:A Comprehensive Reference for Aurora C# (through v2.8.0)" \
    --metadata="author:Aurora Community" \
    --pdf-engine=tectonic \
    --top-level-division=chapter \
    --table-of-contents \
    --toc-depth=3 \
    --resource-path=.:images:images/screenshots:images/.generated \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V urlcolor=blue \
    -o "$OUTPUT_FILE" \
    "${FILES[@]}"

echo "Built: ${OUTPUT_FILE}"
echo "Size: $(du -h "$OUTPUT_FILE" | cut -f1)"
