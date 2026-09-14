# TCom — 'Add command'

Resource objects are inventoried, not certified features. Captions may be changed at runtime; container objects, labels and controls all count. Complex/multiline property values are not fully decoded.

[Coverage guide](../README.md) · [Source resource](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1)

| Resource object | Component | Caption / text | Declared event handler(s) |
|---|---|---|---|
| [Form5](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1) | TForm5 | 'Add command' |  |
| [Label1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L16) | TLabel | 'Opcode : ' |  |
| [Label6](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L23) | TLabel | 'Label' |  |
| [Image1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L30) | TImage |  |  |
| [Button1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L36) | TButton | 'Insert' | OnClick: [Button1Click](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L231) |
| [Button2](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L45) | TButton | 'Cancel' | OnClick: [Button2Click](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L135) |
| [Edit5](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L55) | TEdit |  |  |
| [ComboBox1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L62) | TComboBox |  | OnChange: [ComboBox1Change](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L103); OnDrawItem: [ComboBox1DrawItem](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L720); OnKeyUp: [ComboBox1KeyUp](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L1053) |
| [UnicodeStringGrid1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L72) | TStringGrid |  | OnDrawCell: [UnicodeStringGrid1DrawCell](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L778); OnEnter: [UnicodeStringGrid1Enter](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L799); OnExit: [UnicodeStringGrid1Exit](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L805); OnKeyUp: [ComboBox1KeyUp](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L1053); OnMouseMove: [UnicodeStringGrid1MouseMove](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L974); OnMouseUp: [UnicodeStringGrid1MouseUp](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L815); OnSelectCell: [UnicodeStringGrid1SelectCell](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L986); OnSetEditText: [UnicodeStringGrid1SetEditText](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L997) |
| [TabControl1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L100) | TTabControl |  | OnChange: [TabControl1Change](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L745) |
| [ImageList1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L114) | TImageList |  |  |
| [ImageList2](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1173) | TImageList |  |  |
| [ActionList1](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1302) | TActionList |  |  |
| [AddNewLabel](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1305) | TAction | 'New label' | OnExecute: [AddNewLabelExecute](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L157) |
| [AddNewRegister](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.dfm#L1310) | TAction | 'New register' | OnExecute: [AddNewRegisterExecute](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/TCom.pas#L186) |
