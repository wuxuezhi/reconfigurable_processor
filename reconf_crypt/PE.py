from pymtl3 import *



LU_OP =0
ZERO  =0
NOT   =1
AND   =2
OR    =3
XOR   =4
AA    =5
AO    =6
AX    =7
OA    =8
OO    =9
OX    =10
XA    =11
XO    =12
XX    =13
SLL   =14


SRL   =15
SLA   =16
SRA   =17
CAT   =18
SLAB  =19
SLADB =20
SLATB =21
SLAQB  =22
SRAB  =23
SRADB =24
SRATB  =25
SRAQB  =26
NONE   = 27

AU_OP =1
ADD   =1
SUB   =2
MUL   =3
EQU   =4
GT    =5
LT    =6
LUT_OP=2
class AES_SBox(object):
    def __init__(s):
        s.table =[
        [b8(0x63), b8(0x7C), b8(0x77), b8(0x7B), b8(0xF2), b8(0x6B), b8(0x6F), b8(0xC5), b8(0x30), b8(0x01), b8(0x67), b8(0x2B), b8(0xFE), b8(0xD7), b8(0xAB), b8(0x76)], 
        [b8(0xCA), b8(0x82), b8(0xC9), b8(0x7D), b8(0xFA), b8(0x59), b8(0x47), b8(0xF0), b8(0xAD), b8(0xD4), b8(0xA2), b8(0xAF), b8(0x9C), b8(0xA4), b8(0x72), b8(0xC0)],
        [b8(0xB7), b8(0xFD), b8(0x93), b8(0x26), b8(0x36), b8(0x3F), b8(0xF7), b8(0xCC), b8(0x34), b8(0xA5), b8(0xE5), b8(0xF1), b8(0x71), b8(0xD8), b8(0x31), b8(0x15)],
        [b8(0x04), b8(0xC7), b8(0x23), b8(0xC3), b8(0x18), b8(0x96), b8(0x05), b8(0x9A), b8(0x07), b8(0x12), b8(0x80), b8(0xE2), b8(0xEB), b8(0x27), b8(0xB2), b8(0x75)],
        [b8(0x09), b8(0x83), b8(0x2C), b8(0x1A), b8(0x1B), b8(0x6E), b8(0x5A), b8(0xA0), b8(0x52), b8(0x3B), b8(0xD6), b8(0xB3), b8(0x29), b8(0xE3), b8(0x2F), b8(0x84)],
        [b8(0x53), b8(0xD1), b8(0x00), b8(0xED), b8(0x20), b8(0xFC), b8(0xB1), b8(0x5B), b8(0x6A), b8(0xCB), b8(0xBE), b8(0x39), b8(0x4A), b8(0x4C), b8(0x58), b8(0xCF)],
        [b8(0xD0), b8(0xEF), b8(0xAA), b8(0xFB), b8(0x43), b8(0x4D), b8(0x33), b8(0x85), b8(0x45), b8(0xF9), b8(0x02), b8(0x7F), b8(0x50), b8(0x3C), b8(0x9F), b8(0xA8)],
        [b8(0x51), b8(0xA3), b8(0x40), b8(0x8F), b8(0x92), b8(0x9D), b8(0x38), b8(0xF5), b8(0xBC), b8(0xB6), b8(0xDA), b8(0x21), b8(0x10), b8(0xFF), b8(0xF3), b8(0xD2)],
        [b8(0xCD), b8(0x0C), b8(0x13), b8(0xEC), b8(0x5F), b8(0x97), b8(0x44), b8(0x17), b8(0xC4), b8(0xA7), b8(0x7E), b8(0x3D), b8(0x64), b8(0x5D), b8(0x19), b8(0x73)],
        [b8(0x60), b8(0x81), b8(0x4F), b8(0xDC), b8(0x22), b8(0x2A), b8(0x90), b8(0x88), b8(0x46), b8(0xEE), b8(0xB8), b8(0x14), b8(0xDE), b8(0x5E), b8(0x0B), b8(0xDB)],
        [b8(0xE0), b8(0x32), b8(0x3A), b8(0x0A), b8(0x49), b8(0x06), b8(0x24), b8(0x5C), b8(0xC2), b8(0xD3), b8(0xAC), b8(0x62), b8(0x91), b8(0x95), b8(0xE4), b8(0x79)],
        [b8(0xE7), b8(0xC8), b8(0x37), b8(0x6D), b8(0x8D), b8(0xD5), b8(0x4E), b8(0xA9), b8(0x6C), b8(0x56), b8(0xF4), b8(0xEA), b8(0x65), b8(0x7A), b8(0xAE), b8(0x08)],
        [b8(0xBA), b8(0x78), b8(0x25), b8(0x2E), b8(0x1C), b8(0xA6), b8(0xB4), b8(0xC6), b8(0xE8), b8(0xDD), b8(0x74), b8(0x1F), b8(0x4B), b8(0xBD), b8(0x8B), b8(0x8A)],
        [b8(0x70), b8(0x3E), b8(0xB5), b8(0x66), b8(0x48), b8(0x03), b8(0xF6), b8(0x0E), b8(0x61), b8(0x35), b8(0x57), b8(0xB9), b8(0x86), b8(0xC1), b8(0x1D), b8(0x9E)],
        [b8(0xE1), b8(0xF8), b8(0x98), b8(0x11), b8(0x69), b8(0xD9), b8(0x8E), b8(0x94), b8(0x9B), b8(0x1E), b8(0x87), b8(0xE9), b8(0xCE), b8(0x55), b8(0x28), b8(0xDF)],
        [b8(0x8C), b8(0xA1), b8(0x89), b8(0x0D), b8(0xBF), b8(0xE6), b8(0x42), b8(0x68), b8(0x41), b8(0x99), b8(0x2D), b8(0x0F), b8(0xB0), b8(0x54), b8(0xBB), b8(0x16)]
        ]

        
class wire_comb(Component):
    def construct(s):
        s.out = Wire(Bits32)

    @method_port
    def comb(s, in0, in1, in2, in3):
        s.out[0:8] @= in0
        s.out[8:16] @= in1
        s.out[16:24] @= in2
        s.out[24:32] @= in2
        return s.out

#type:LU/AU/LUT
#op  :calc operat
#src :src operator bit map
class conf_calc(object):
    def __init__(s, tp=b8(9), op=b8(8), src=b8(7)):
        s.type = tp
        s.op   = op
        s.src  = src
        
#r0/1/2_calc:r0/1/2 calc configure
class PE_conf(object):
    def __init__(s):
        s.r0_calc = conf_calc()
        s.imm     = Wire(Bits32)

#add calc op
class PE_FUNC(Component):
    def construct(s):
        s.calc = CalleePort(method = s.calc_)
        s.sbox = AES_SBox()
        s.comb = wire_comb()
        s.table_entry0 = Wire(Bits8)
        s.table_entry1 = Wire(Bits8)
        s.table_entry2 = Wire(Bits8)
        s.table_entry3 = Wire(Bits8)

    def look_table(s, a):
        #AES S-Box
        s.table_entry0 =s.sbox.table[a[0:4]][a[4:8]] 
        s.table_entry1 =s.sbox.table[a[8:12]][a[12:16]] 
        s.table_entry2 =s.sbox.table[a[16:20]][a[20:24]] 
        s.table_entry3 =s.sbox.table[a[24:28]][a[28:32]] 
        return s.comb.comb(s.table_entry0, s.table_entry1, s.table_entry2, s.table_entry3)


    def calc_(s, calc, a, b, c):
        #print(calc.type)
        if calc.type == LU_OP:
            if calc.op == ZERO:
                return b32(0)
            elif calc.op == NOT:
                return ~a
            elif calc.op == AND:
                return a&b
            elif calc.op == OR:
                return a|b
            elif calc.op == XOR:
                return a^b
            elif calc.op == AA:
                return a&b&c
            elif calc.op == AO:
                return a&b|c
            elif calc.op == AX:
                return a&b^c
            elif calc.op == OA:
                return a|b&c
            elif calc.op == OO:
                return a|b|c
            elif calc.op == OX:
                return a|b^c
            elif calc.op == XA:
                return a^b&c
            elif calc.op == XO:
                return a^b|c
            elif calc.op == XX:
                return a^b^c
            elif calc.op == SLL:
                return a<<b
            elif calc.op == SRL:
                return a>>b
            elif calc.op == SRA:
                return a>>b|(a<<(b32(32)-b))
            elif calc.op == SLA:
                return a<<b|(a>>(b32(32)-b))
            elif calc.op == SLAB:
                return a<<8|(a>>(b32(32)-8))
            elif calc.op == SLADB:
                return a<<16|(a>>(b32(32)-16))
            elif calc.op == SLATB:
                return a<<24|(a>>(b32(32)-24))
            elif calc.op == SLAQB:
                return a<<32|(a>>(b32(32)-32))
            elif calc.op == SRAB:
                return a>>8|(a<<(b32(32)-8))
            elif calc.op == SRADB:
                return a>>16|(a<<(b32(32)-16))
            elif calc.op == SRATB:
                return a>>24|(a<<(b32(32)-24))
            elif calc.op == SRAQB:
                return a>>32|(a<<(b32(32)-32))
            elif calc.op == NONE:
                return a
            else:
                return a<<b | c>>b
        elif calc.type == AU_OP:
            if calc.op == ADD:
                return a+b
            elif calc.op == SUB:
                return a-b
            elif calc.op == MUL:
                return a*b
            elif calc.op == EQU:
                if a==b :
                    return b32(1)
                else:
                    return b32(0)
            elif calc.op == GT:
                if a>b :
                    return b32(1)
                else:
                    return b32(0)
            elif calc.op == LT:
                if a<b :
                    return b32(1)
                else:       
                    return b32(0)
            else:
                return a
        else:
            return s.look_table(a)

                
        
        
        
        

#a/b/c/d/e:src operator
#r0/1/2:obj operator
class PE(Component):
    def construct(s):
        #Port
        s.a = InPort(Bits32)
        s.b = InPort(Bits32)
        s.c = InPort(Bits32)
        s.r0 = OutPort(Bits32)
        #register
        s.tmp0 = Wire(Bits32)
        s.reg0 = Wire(Bits32)
        s.r0   //= s.reg0
        #sub-mod
        s.conf = PE_conf()
        s.func = PE_FUNC()
        
        @update_once
        def assign_caluc():
            s.tmp0 @= s.func.calc(s.conf.r0_calc, s.a, s.b, s.c)

        @update_ff
        def always():
            s.reg0 <<= s.tmp0


        #@update
        #def assign_print():
        #    print("clk------------------")
        #    print(s.a, s.b, s.c)
        #    print(s.r0)
    def print_conf(s):
        print(s.conf.r0_calc.type)
        print('')
    def update_conf(s,PE_conf):
        print("update PE configure")
        s.conf = PE_conf

class test_bench(Component):
    def construct(s):
        s.pe = PE()
        s.cnt = Wire(Bits32)
        s.r0_conf = conf_calc(b8(AU_OP),b8(ADD),b8(5))

        @update
        def init():
            s.pe.conf.update_conf(s.r0_conf)

        @update
        def assign():
            s.pe.a @= s.cnt
            s.pe.b @= s.cnt+1
            s.pe.c @= s.cnt+2

        @update_ff
        def always():
            s.cnt  <<= s.cnt + b32(1)

def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    tb.sim_tick()