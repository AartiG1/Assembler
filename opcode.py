add = [['00','add_reg8_reg8'],['00','add_mem8_reg8'],['01','add_reg16_reg16'],['01','add_reg32_reg32'],['01','add_mem16_reg16'],['01','add_mem32_reg32'],['01','add_mem16_reg32'],['01','add_mem32_reg16'],['02','add_reg8_reg8'],['02','add_reg8_mem8'],['03','add_reg16_mem16'],['03','add_reg32_mem32'],['03','add_reg32_mem16'],['03','add_reg16_mem32'],['04','add_reg8_imm8'],['05','add_reg32_imm16'],['05','add_reg32_imm32'],['05','add_reg32_imm8']]

sub = [['28','sub_reg8_reg8'],['28','sub_mem8_reg8'],['29','sub_reg16_reg16'],['29','sub_reg32_reg32'],['29,sub_mem16_reg16'],['29','sub_mem32_reg32'],['29','sub_mem16_reg32'],['29','sub_mem32_reg16'],
['2A','sub_reg8_reg8'],['2A','sub_reg8_mem8'],['2B','sub_reg16_mem16'],['2B','sub_reg32_mem32'],['2B','sub_reg32_mem16'],['2B','sub_reg16_mem32'],['2C','sub_reg8_imm8'],['2D','sub_reg32_imm16'],['2D','sub_reg32_imm32']]

mov =  [['88','mov_reg8_reg8'],['88','mov_mem8_reg8'],['89','mov_reg16_reg16'],['89','mov_reg16,reg32'],['89','mov_mem16_reg16'],['89','mov_mem32_reg32'],['89','mov_mem16_reg32'],['89','mov_mem32_reg32'],['8A','mov_reg8_reg8'],['8A','mov_reg8_mem8'],['8A','mov_reg8_imm8'],['8B','mov_reg16_reg16'],['8B','mov_reg16_reg32'],['8B','mov_reg16_mem32'],['8B','mov_reg16_mem16'],['8B','mov_reg32_reg32'],['8B','mov_reg32_reg16'],['8B','mov_reg32_mem32'],['8B','mov_reg32_mem16'],['B8','mov_reg32_imm32'],['B8','mov_reg16_imm16'],['8C','mov_reg32_imm8']]


reglist={8:['al','bl','cl','dl','ah','bh','ch','dh'],16:['ax','bx','cx','dx','sp','bp','si','di'],32:['eax','ebx','ecx','edx','esi','edi','esp','ebp']}
def opcode_Data():
	data=[]
	data.append(add)	
	data.append(mov)
	data.append(sub)
	return data
	
def reglist_Data():	
	return reglist
