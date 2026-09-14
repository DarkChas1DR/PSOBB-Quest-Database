# Supported appearance selector gallery

443 offline render sheets: **424 individual selector values**, 12 class baselines, and 7 special models. Each sheet shows front, head detail and back, rendered from the supplied Qedit NJ meshes and AFS textures using the source texture assignments.

This covers every value in the audited class selector table, one field at a time. It does **not** establish full appearance compatibility: combinations, RGB hair colours, proportion sliders, Section ID variations, animations and client/Qedit equivalence remain unverified. These are offline reference renders, not game screenshots.

All unchanged selectors use zero; hair tint is white and Section ID is zero. The named selector and value override that baseline. IDs are decimal. Visual class IDs and extra_model selectors are **not DAT NPC type IDs**.

[Selector records](selectors.json) · [Source asset SHA-256 hashes](asset-hashes.json) · [Unbound material slots](unbound-materials.json) · [Existing NPC previews](../README.md) · [Special-character ID evidence](../special-characters.md)

## Classes

| Visual class ID | Class | Sheets |
|---|---|---|
| 0 | [HUmar](class-00.md) | 39 |
| 1 | [HUnewearl](class-01.md) | 39 |
| 2 | [HUcast](class-02.md) | 31 |
| 3 | [RAmar](class-03.md) | 39 |
| 4 | [RAcast](class-04.md) | 31 |
| 5 | [RAcaseal](class-05.md) | 31 |
| 6 | [FOmarl](class-06.md) | 39 |
| 7 | [FOnewm](class-07.md) | 39 |
| 8 | [FOnewearl](class-08.md) | 39 |
| 9 | [HUcaseal](class-09.md) | 31 |
| 10 | [FOmar](class-10.md) | 39 |
| 11 | [RAmarl](class-11.md) | 39 |

## Special models

[GM, Rico, Sonic, Knuckles, Tails, Flowen and Elly](special-models.md). NiGHTS poses and an Eggman identity are not supplied by these seven extra_model entries; consult the separate special-character evidence. No missing model ID is invented.

## Reproduction and fidelity

Source: [Qedit NPCBuild.pas at pinned commit 2af5d144](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas), with mesh/texture decoding based on D3DEngin.pas in the same revision. Source/executable equivalence has not been tested.

Install Python, Pillow and NumPy. From the repository root run:

```text
python analysis/tools/build_supported_gallery.py --assets "PATH/TO/Qedit/charmodel" --source "PATH/TO/qedit-source/NPCBuild.pas"
```

The renderer uses a depth buffer and static base transforms. Lighting, animation, blending, slider proportions and the original Direct3D material pipeline are not reproduced. Alpha uses a cutoff. Unbound material slots on RAcast head IDs 1/3 and FOnewm body are shown neutral white and recorded separately; their exact native appearance needs checking. Successful decoding is not visual/runtime validation. Images were inspected as a class/special-model contact sheet; exhaustive individual comparison against Qedit is pending.
