# FSnap — 'Snap Options'

Resource objects are inventoried, not certified features. Captions may be changed at runtime; container objects, labels and controls all count. Complex/multiline property values are not fully decoded.

[Coverage guide](../README.md) · [Source resource](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L1)

| Resource object | Component | Caption / text | Declared event handler(s) |
|---|---|---|---|
| [FSnapOptions](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L1) | TFSnapOptions | 'Snap Options' | OnCreate: [FormCreate](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.pas#L107) |
| [Label8](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L18) | TLabel | 'Snap tolerance (units):' |  |
| [btnSave](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L25) | TButton | 'Save' | OnClick: [btnSaveClick](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.pas#L53) |
| [chkDistancelimit](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L35) | TCheckBox | 'Anchor limit (units):' | OnClick: [chkDistancelimitClick](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.pas#L76) |
| [seDistanceLimit](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L44) | TSpinEdit |  |  |
| [chkSnapDistance](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L55) | TCheckBox | 'Match distance' |  |
| [chkSnapRotate](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L63) | TCheckBox | 'Match rotation' |  |
| [btnReset](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L71) | TButton | 'Defaults' | OnClick: [btnResetClick](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.pas#L41) |
| [seSnapTolerance](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L80) | TSpinEdit |  |  |
| [chkSnap](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L90) | TCheckBox | 'Snap alignment' | OnClick: [chkSnapClick](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.pas#L82) |
| [chkSnapYValue](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FSnap.dfm#L99) | TCheckBox | 'Match Y value' |  |
