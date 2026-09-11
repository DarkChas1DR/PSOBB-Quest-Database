import pathlib,sys,json
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent/'pythonlibs'))
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_32
root=pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB'); out=pathlib.Path(__file__).resolve().parents[1]/'extracted'
specs=[('Qedit1',root/'Qedit/Qedit1.exe',[(0x9d71ca,0x9d7330),(0x9d6440,0x9d64af)]),('psobb',root/'PSOBB.IO [Modded][DarkChas]/psobb.exe',[(0x6b9a54,0x6b9b0b),(0x4fbe68,0x4fbed9)])]
for name,p,ranges in specs:
    pe=pefile.PE(str(p)); md=Cs(CS_ARCH_X86,CS_MODE_32); lines=[]
    for lo,hi in ranges:
        data=pe.get_data(lo-pe.OPTIONAL_HEADER.ImageBase,hi-lo)
        lines.append(f'\n; Selected static range {lo:08X}-{hi:08X}; verify function boundaries before use')
        for i in md.disasm(data,lo): lines.append(f'{i.address:08X}  {i.bytes.hex():24s} {i.mnemonic:8s} {i.op_str}')
    (out/(name+'-native-trace.txt')).write_text('\n'.join(lines))
    if name=='Qedit1':
        for va in (0x9d9f48,0x9d9f70,0x9d9f90,0x9d9fa8):
            print(hex(va),repr(pe.get_data(va-pe.OPTIONAL_HEADER.ImageBase,100)))
    print(name,'\n'+'\n'.join(lines))
