# Classes, races and appearance IDs

Player class IDs are not NPC DAT skin IDs: RAmar is class 3, while the Qedit default Bernie/RAmar DAT type is 36 (0x24). Race is derived from class flags, not an interchangeable DAT race ID.

Appearance counts below come from newserv V3/V4 lobby normalization. For a positive count N the indices are 0 to N−1; zero means normalization forces zero. These are not face thumbnails or proof that every extra NPC model supports each combination.

| Class ID | Class | Race | Gender | Costume count | Skin count | Face count | Head count | Hair count |
|---|---|---|---|---:|---:|---:|---:|---:|
| 0 | HUmar | HUMAN | male | 18 | 4 | 5 | 0 | 10 |
| 1 | HUnewearl | NEWMAN | female | 18 | 4 | 5 | 0 | 10 |
| 2 | HUcast | ANDROID | male | 0 | 25 | 0 | 5 | 0 |
| 3 | RAmar | HUMAN | male | 18 | 4 | 5 | 0 | 10 |
| 4 | RAcast | ANDROID | male | 0 | 25 | 0 | 5 | 0 |
| 5 | RAcaseal | ANDROID | female | 0 | 25 | 0 | 5 | 0 |
| 6 | FOmarl | HUMAN | female | 18 | 4 | 5 | 0 | 10 |
| 7 | FOnewm | NEWMAN | male | 18 | 4 | 5 | 0 | 10 |
| 8 | FOnewearl | NEWMAN | female | 18 | 4 | 5 | 0 | 10 |
| 9 | HUcaseal | ANDROID | female | 0 | 25 | 0 | 5 | 0 |
| 10 | FOmar | HUMAN | male | 18 | 4 | 5 | 0 | 10 |
| 11 | RAmarl | HUMAN | female | 18 | 4 | 5 | 0 | 10 |

[Visual structure, limits and NPC safety substitutions](reference/PlayerSubordinates.hh) · [Machine-readable classes](classes.json) · [Decoded quest visual blocks](npc-visual-blocks.json)

See README for remaining appearance and NPC linkage gaps.
