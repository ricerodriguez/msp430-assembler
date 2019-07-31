Registers = {
    'R0'     : '0000',
    'R1'     : '0001',
    'R2'     : '0010',
    'R3'     : '0011',
    'R4'     : '0100',
    'R5'     : '0101',
    'R6'     : '0110',
    'R7'     : '0111',
    'R8'     : '1000',
    'R9'     : '1001',
    'R10'    : '1010',
    'R11'    : '1011',
    'R12'    : '1100',
    'R13'    : '1101',
    'R14'    : '1110',
    'R15'    : '1111',
    'PC'     : '0000',
    'SP'     : '0001',
    'SR'     : '0010'
}

Addressing_Prefixes = {
    '([0-9])\((R[0-9]{,2})\)'            : 'INDEXED',
    '#0x(([0-9]){1,4})'    : 'IMMEDIATE',
    '#(([0-9])+)'          : 'IMMEDIATE',
    '#(?a)'              : 'ABSOLUTE',
    '0x(?a)'             : 'SYMBOLIC',
    '&(?a)'              : 'ABSOLUTE',
    '@\((R[0-9]{,2})\)\+'            : 'INDIRECT AUTOINCREMENT',
    '@\((R[0-9]{,2})\)'              : 'INDIRECT'
}

As_Modes = {
    'REGISTER'  : '00',
    'INDEXED'   : '01',
    'SYMBOLIC'  : '01',
    'ABSOLUTE'  : '01',
    'INDIRECT'  : '10',
    'IMMEDIATE' : '11',
    'INDIRECT AUTOINCREMENT' : '11'
}

Addressing_SRegs = {
    'REGISTER'  : None,
    'INDEXED'   : None,
    'SYMBOLIC'  : 'PC',         # X is TONI - PC
    'ABSOLUTE'  : 'SR',
    'INDIRECT'  : None,
    'IMMEDIATE' : 'PC',
    'INDIRECT AUTOINCREMENT' : None
}

Directives = {
    'ORG'    : -1,
    'DW'     : 2,
    'DB'     : 1,
    'DS'     : -1,
    'EQU'    : 0
}

__opcodes_1 = {
    'mov'    : '0100',
    'add'    : '0101',
    'addc'   : '0110',
    'subc'   : '0111',
    'sub'    : '1000',
    'cmp'    : '1001',
    'dadd'   : '1010',
    'bit'    : '1011',
    'bic'    : '1100',
    'bis'    : '1101',
    'xor'    : '1110',
    'and'    : '1111'
}

__opcodes_2 = {
    'rrc'    : '0001' + '0000' + '0000',
    'rrc.b'  : '0001' + '0000' + '0000',
    'swpb'   : '0001' + '0000' + '1000',  
    'rra'    : '0001' + '0001' + '0000', 
    'rra.b'  : '0001' + '0001' + '0100', 
    'sxt'    : '0001' + '0001' + '1000', 
    'push'   : '0001' + '0010' + '0000',
    'push.b' : '0001' + '0010' + '0100',
    'call'   : '0001' + '0010' + '1000',
    'reti'   : '0001' + '0011' + '0000'
}


__opcodes_3 = {
    'jne'    : '00100000',
    'jnz'    : '00100000',
    'jeq'    : '00100100',
    'jz'     : '00100100',
    'jnc'    : '00101000',
    'jc'     : '00101100',
    'jn'     : '00110000',
    'jge'    : '00110100',
    'jl'     : '00111000',
    'jmp'    : '00111100'
}

__opcodes_emu = {
    # Emulated instructions contain a list.
    # First element is how much instruction should inc PC
    # Second element is instruction
    'adc'    : ['2','addc R3, ${dst}'],
    'br'     : ['2','mov ${dst}, PC'],
    'clr'    : ['2','mov R3, ${dst}'],
    'clrc'   : ['4','and #0xFFFE, SR'],
    'dadc'   : ['2','dadd R3, ${dst}'],
    'dec'    : ['2','sub 0(R3), ${dst}'],
    'decd'   : ['2','sub @R3, ${dst}'],
    'dint'   : ['4','and #0xFFF7, SR'],
    'eint'   : ['4','bis #0x0008, SR'],
    'inc'    : ['2','add 0(R3), ${dst}'],
    'incd'   : ['2','add @R3, ${dst}'],
    'inv'    : ['4','xor #0xFFFF, ${dst}'],
    'pop'    : ['2','mov @SP+, ${dst}'],
    'ret'    : ['2','mov @SP+, PC'],
    'rla'    : ['2','add ${dst}, ${dst}'],
    'rlc'    : ['2','addc ${dst}, ${dst}'],
    'sbc'    : ['2','subc #0x0, ${dst}'],
    'setc'   : ['2','bis #0x1, SR'],
    'setn'   : ['2','bis #0x4, SR'],
    'setz'   : ['2','bis #0x2, SR'],
    'tst'    : ['2','cmp R3, ${dst}']
}

OPCODES = [__opcodes_1, __opcodes_2, __opcodes_3, __opcodes_emu]        
