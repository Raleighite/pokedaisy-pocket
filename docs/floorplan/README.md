# Curated native map

Open `index.html` locally after downloading the raw file. The expandable cards and guided journey require no server, scripts or external assets.

## Coverage

This manually authored map explains the selected native launch, core, companion, save and firmware-packaging paths. It does not claim per-file descriptions or coverage of inherited Android, website, DS or all 3DS implementation. No full third-party Floorplan export was generated. The native path is pinned to upstream v1.6.1, commit `79bd00e155fcc7d4373f23f5386d6e67c8c423eb`.

## Freshness

Run `python3 -B docs/floorplan/check.py` from a complete Git checkout. The manifest watches the Git-tracked file set and file contents under `linux/`, `libretro/` and `3ds/core/`, plus `docs/POCKET.md`, `LICENSE`, `NOTICE`, and the HTML artifact digest. A new, removed or changed tracked file in that admitted source set fails closed. Untracked changes and code outside the admitted set are not covered. This is not an automatic map generator or a test of application behavior.

Regeneration is manual: inspect each source change and its architecture impact, update the plain-English cards and journeys, review for public-source-only content, test the interactive HTML, then recompute the admitted manifest from the reviewed Git index. Never refresh hashes merely to hide a stale description. For architectural scope changes, update this coverage statement and checker selection too. Keep applicable upstream GPLv3 and dependency notices.
