opcode_data = {'AA':['add_reg8_reg8','add_mem8_reg8']
,'AB':['add_reg16_reg16','add_reg32_reg32','add_mem16_reg16','add_mem32_reg32','add_mem16_reg32','add_mem32_reg16']
,'AC':['add_reg8_reg8','add_reg8_mem8']
,'AD':['add_reg16_mem16','add_reg32_mem32','add_reg32_mem16','add_reg16_mem32']
,'AE':['add_reg8_imm8']
,'AF':['add_reg32_imm16','add_reg32_imm32','add_reg32_imm8']
,'SA':['sub_reg8_reg8','sub_mem8_reg8']
,'SB':['sub_reg16_reg16','sub_reg32_reg32','sub_mem16_reg16','sub_mem32_reg32','sub_mem16_reg32','sub_mem32_reg16']
,'SC':['sub_reg8_reg8','sub_reg8_mem8']
,'SD':['sub_reg16_mem16','sub_reg32_mem32','sub_reg32_mem16','sub_reg16_mem32']
,'SE':['sub_reg8_imm8']
,'SF':['sub_reg32_imm16','sub_reg32_imm32']
,'X1':['mov_reg8_reg8','mov_mem8_reg8']
,'X2':['mov_reg16_reg16','mov_reg16_reg32','mov_mem16_reg16','mov_mem32_reg32','mov_mem16_reg32','mov_mem32_reg32']
,'X3':['mov_reg8_reg8','mov_reg8_mem8','mov_reg8_imm8']
,'X4':['mov_reg16_reg16','mov_reg16_reg32','mov_reg16_mem32','mov_reg32_reg32','mov_reg32_reg16','mov_reg32_mem32','mov_reg32_mem16']
,'M1':['mov_reg32_imm32','mov_reg16_imm16','mov_reg32_imm8']}


reglist={8:['al','bl','cl','dl','ah','bh','ch','dh'],16:['ax','bx','cx','dx','sp','bp','si','di'],32:['eax','ebx','ecx','edx','esi','edi','esp','ebp']}



def opcode_Data():
	return opcode_data


def reglist_Data():	
	return reglist

