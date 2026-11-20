# PokeDaisy Pocket

A single-screen, controller-first derivative of PokeDaisy by Lidor Itzhari.

## Current deliverable

This repository is a real GitHub fork. Branch `pocket` starts at upstream v1.6.1, commit `79bd00e155fcc7d4373f23f5386d6e67c8c423eb`. This first change establishes the four-device scope and preserves the existing implementation unchanged. It is **not a completed port, a new emulator build, or a claim of device compatibility**. Inherited upstream downloads are not Pocket releases.

GitHub Actions are disabled until inherited workflows and the new toolchains have been reviewed. No ROM, save, account credential or private device configuration is part of this fork.

## Requested targets

- **Miyoo Mini Plus:** investigate a 32-bit ARM firmware-compatible core and frontend. Select the SDK, libc ABI and SDL/display path against the installed firmware before building. No device build or runtime test yet.
- **Miyoo Mini v4:** same platform investigation, with separate resolution/scaling acceptance. Onion documents 752x560 with compatible firmware; do not assume that is the active mode on every device. No device build or runtime test yet.
- **Anbernic RG34XXSP:** H700 Cortex-A53, vendor display specification 720x480. Start from the upstream AArch64 Linux/core path, then qualify the actual firmware ABI, controls, audio and lid behavior. No device build or runtime test yet.
- **Anbernic RG35XXH:** H700 Cortex-A53, vendor display specification 640x480. Start from the same native path with a separate device acceptance record. No device build or runtime test yet.

The owner's model spellings in the request were Miyoo Mini Plus, Miyoo Mini v4, RG34XXSP and RG35XXH. RG34XXSP is **not** RG35XXSP. Firmware is not established by the model name. No reflash is required or authorized by this source fork.

## Product direction, not implemented defaults

Initial scope is GB/GBC/GBA. Full-screen gameplay, with a button-operated companion that can use the screen when requested. Favor readable party/move/type/encounter information. No touch-only requirement, compulsory network account, always-on overlay, DS requirement or rewrite of the emulator from scratch.

Performance settings and read-only companion behavior are proposed requirements, not changes already made to upstream. Upstream includes optional game-modifying features; this fork setup has not disabled or audited them. Benchmark before selecting a GBA backend on Miyoo, and do not substitute a faster core without preserving memory-reader compatibility and reviewing its license.

## Source already available

- `linux/main.c`: native SDL2/libretro host, input, audio, game list and core loading.
- `linux/host_io.c`: host persistence helpers. Read actual save semantics before integration.
- `libretro/pd_libretro.c`: emulator/companion integration for the shared GB/GBA core path.
- `libretro/CMakeLists.txt`: mGBA-backed native core build.
- `libretro/armgba/CMakeLists.txt`: armGBA-backed GBA core build.
- `3ds/core/`: portable companion rendering and readers reused by Linux.
- `linux/portmaster/PokeDaisy.sh`: existing PortMaster launch integration, not proof of Onion support.
- `linux/README.md`: upstream build instructions and clearly scoped upstream test reports.

[Understand this app](floorplan/index.html): download this self-contained HTML and open it locally. GitHub's HTML source viewer is not the interactive view. The map covers this fork's selected native architecture and the four port targets, not every file in the inherited Android/3DS/website codebase.

## Acceptance before a target is marked supported

1. Pin the firmware SDK/toolchain and build real executable/core artifacts. Record hashes and ELF architecture/dependencies.
2. Exercise harmless diagnostic ROMs and isolated save backup/write/reopen failure tests.
3. On each physical target, test launch, readable game and companion screens, actual buttons, audio and frame pacing.
4. Verify in-game save, normal exit, relaunch and progress recovery using isolated copies. Never use a save state as the only proof of battery-save preservation.
5. Qualify suspend/resume and firmware power behavior, including the RG34XXSP lid. Do not alter power handling merely to pass a launch test.
6. Package the tested firmware-specific install path with licenses, provenance, removal instructions and no commercial game assets.

## Licensing and maintenance

Retain upstream GPLv3 and all dependency notices in `LICENSE` and `NOTICE`. Public forks cannot be made private on GitHub. This is a public source fork, with no private operational state added. Distribution of modified binaries must meet applicable corresponding-source and attribution obligations. Game ROMs and game artwork are not licensed by this software license.

## References

- Upstream native frontend: https://github.com/lidor30/pokedaisy/blob/v1.6.1/linux/README.md
- Onion installation and Mini v4 resolution: https://onionui.github.io/docs/installation
- Miyoo toolchain candidate, not yet qualified: https://github.com/shauninman/union-miyoomini-toolchain
- RG34XXSP manufacturer specifications: https://anbernic.com/products/rg34xxsp
- RG35XXH manufacturer specifications: https://win.anbernic.com/product/364.html
