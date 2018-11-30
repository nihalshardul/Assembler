from symbol_tabel import sym
from literal import lit
from opcode import*

def intermi(fr,fw):
	const=['mov','add','sub']
	directives=['dd','db','resb','resd']
	sections=['.data','.bss','.text',]
	glob=['main:','extern','global']
	
	for line in fr.readlines():
		s=line.split()
		for i in range(0,len(s)):
			if s[i] in sections:
				fw.write('\n'+line+'\n')
			if s[i] in directives:
				fw.write(sym[s[i-1]]+'\t'+s[i]+'\t'+s[i+1]+'\n')
			if s[i] in glob:
				fw.write(line+'\n')
			if s[i] in const:
				n=s[i+1].split(',')
				b=n[1].split('[')
				if n[0] in reglist[8] and b[0] in reglist[8]:
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'reg#8'+'\n')
				if n[0] in reglist[8] and b[0] in reglist[16]:
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'reg#16'+'\n')
				if n[0] in reglist[8] and b[0] in reglist[32]:
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'reg#32'+'\n')
				if n[0] in reglist[8] and b[0]=='dword':
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'mem'+'\n')
				if n[0] in reglist[16] and b[0] in reglist[8]:
					fw.write(s[i]+'\t'+'reg#16'+'\t'+'reg#8'+'\n')
				if n[0] in reglist[16] and b[0] in reglist[16]:
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'reg#16'+'\n')
				if n[0] in reglist[16] and b[0] in reglist[32]:
					fw.write(s[i]+'\t'+'reg#8'+'\t'+'reg#32'+'\n')
				if n[0] in reglist[16] and b[0]=='dword':
					fw.write(s[i]+'\t'+'reg#16'+'\t'+'mem'+'\n')
				if n[0] in reglist[32] and b[0] in reglist[8]:
					fw.write(s[i]+'\t'+'reg#32'+'\t'+'reg#8'+'\n')
				if n[0] in reglist[32] and b[0] in reglist[8]:
					fw.write(s[i]+'\t'+'reg#32'+'\t'+'reg#16'+'\n')
				if n[0] in reglist[32] and b[0] in reglist[32]:
					fw.write(s[i]+'\t'+'reg#32'+'\t'+'reg#32'+'\n')
				if n[0] in reglist[32] and b[0]=='dword':
					fw.write(s[i]+'\t'+'reg#32'+'\t'+'mem'+'\n')
				if n[0] in reglist[32] and b[0] in sym:
					fw.write(s[i]+'\t'+'reg#32'+'\t'+sym[b[0]]+'\n')
				if n[0] in reglist[32] and b[0] in lit:
					fw.write(s[i]+'\t'+'reg#32'+'\t'+lit[b[0]]+'\n')
				



fr=open('sample.asm','r')
fw=open('intermi.lst','w')

intermi(fr,fw)
