opname = ["ADD","ADC","SBB","SBC","AND","NOT","CMP","LOAD","UNLD","JMP","JZ","JNZ","JC","JNC","JN","JNN"]

with open("input.txt") as f:
    txt = f.readlines()

out = open("compiled.hex",'w')
out.write("v2.0 raw\n0\n")
out.close()

out = open("compiled.hex",'a')

for line in txt:
    if line == "\n":
        continue

    opc , val = ( x for x in line.split())

    ins = 0

    ins |= opname.index(opc) << 16
    
    c = val[0]
    val = val[1:]

    if c == "&":
        ins |= 1 << 20

    v = int(val)

    if(v > 65535):
        v = 65535
    
    if "J" in opc and False:
        v += 1

    ins |= v
    
    out.write(hex(ins).replace("0x",'') + "\n")

out.close()