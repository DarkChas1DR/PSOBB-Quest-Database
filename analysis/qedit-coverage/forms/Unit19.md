# Unit19 — 'Items list manager'

Resource objects are inventoried, not certified features. Captions may be changed at runtime; container objects, labels and controls all count. Complex/multiline property values are not fully decoded.

[Coverage guide](../README.md) · [Source resource](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.dfm#L1)

| Resource object | Component | Caption / text | Declared event handler(s) |
|---|---|---|---|
| [Form19](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.dfm#L1) | TForm19 | 'Items list manager' |  |
| [StringGrid1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.dfm#L18) | TStringGrid |  | OnDrawCell: [StringGrid1DrawCell](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.pas#L46); OnSetEditText: [StringGrid1SetEditText](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.pas#L38) |
| [Button1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.dfm#L47) | TButton | 'Close' | OnClick: [Button1Click](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit19.pas#L33) |
