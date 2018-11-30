from symbol_tabel import sym
from literal import lit
from opcode import*
from intermediate import*

def sublst(j,p,bitreg):
	n='11'
	for d in bitreg:
		if j in bitreg[d]:
			n=n+d
		if p in bitreg[d]:
			n=n+d
	f=hex(int(n,2))
	k=f[2:]
	k=k.upper()
	return k

def string_convert_hex(no):
	k=hex(no)
	k=k[2:]
	k=k.upper()
	return k
	

def hex_convert(no):
	str1=''
	t=hex(no)
	t=t[2:]
	t=t.upper()
	if(len(t)==1):
		str1="0"
		str1=str1+t
		str1=str1+'0'*(8-(len(str1)))
		return(str1)
	else:
		str1=str1+t
		str1=str1+'0'*(8-(len(str1)))
		return(str1)
def hex_index(index):
	str1=''
	k=hex(index)
	k=k[2:]
	k=k.upper()
	str1=('0'*(8-len(k)))+k
	return str1

def lstindex(j,p,bitreg):
	p=sublst(j,p,bitreg)
	p=len(p)
	p=hex_index(p)
	return int(p)

def lst(fr,fw):
	sym_index={}
	b=0
	index=0
	const=['mov','add','sub']
	sections=['.data','.bss','.text',]
	glob=['main:','extern','global']
	reg=['al','bl','cl','dl','ah','bh','ch','dh','ax','bx','cx','dx','sp','bp','si','di','eax','ebx','ecx','edx','esi','edi','esp','ebp']
	size=0
	bitreg={'100':['al','ax','eax'],'101':['bl','bx','ebx'],'110':['cl','cx','ecx'],'111':['dl','dx','edx'],'000':['ah','sp','esp'],'001':['bh','bp','ebp'],'010':['ch','si','esi'],'011':['dh','di','edi']}
	reg_op={'R1':['al','ax','eax'],'R2':['bl','bx','ebx'],'R3':['cl','cx','ecx'],'R4':['dl','dx','edx'],'R5':['ah','sp','esp'],'R6':['bh','bp','ebp'],'R7':['ch','si','esi'],'R8':['dh','di','edi']}

	for line in fr.readlines():
		s=line.split()
		for i in range(len(s)):
			hexa=[]
			if s[i] in sections:
				fw.write('\n'+line+'\n')
				index=0
				size=0
			if s[i] in glob:
				fw.write(line+'\n')
			if s[i]=='dd':
				if s[i-1] in sym:
					n=s[i+1].split(',')
					if len(n)==1:
						hc=hex_convert(int(n[0]))
						size=4
					else:
						for num in n:
							hexa.append(hex_convert(int(num)))
						hc=''.join(hexa)
						size=len(n)*4
					hi=hex_index(index)
					fw.write(hi+'\t'+hc+'\n')
					index=index+size
					sym_index[s[i-1]]=hi

			if s[i]=='db':
				if s[i-1] in sym:
					nk=s[i+1]
					nl=nk.split("'")
					nk=nl[1]
					hc=''
					for f in range(0,len(nk)):
						hexa.append(string_convert_hex(ord(nk[f])))
						hc=''.join(hexa)

					size = len(nk)
					hi = hex_index(index)			
					fw.write(hi+'\t'+hc+'\n')
					index=index+size
					sym_index[s[i-1]]=hi

			if s[i]=='resd':
				if s[i-1] in sym:
					hi=hex_index(index)
					n=s[i+1]
					n=int(n)
					size=n*4
					index=index+size
					fw.write(hi+'\t'+'<resd '+hex_index(size)+'>'+'\n')
					sym_index[s[i-1]]=hi

			if s[i]=='resb':
				if s[i-1] in sym:
					hi=hex_index(index)
					n=s[i+1]
					n=int(n)
					size=n
					index=index+size
					fw.write(hi+'\t'+'<resd '+hex_index(size)+'>'+'\n')
					sym_index[s[i-1]]=hi

			if s[i]=='mov':
				p=s[i]
				k=s[i+1].split(',')
				llp=k[1].split('[')
				if k[0] in reg and k[1] in reg:
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
					for n in reglist:
						if k[1] in reglist[n]:
							p=p+'_reg'+str(n)
					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+sublst(k[1],k[0],bitreg)+'\n')
							b=b+lstindex(k[1],k[0],bitreg)
							

				if k[0] in reg and k[1] in sym:
					for jj in reg_op:
						for nh in reg_op[jj]:
							dp=nh
							if k[1] in dp:
								
								fw.write(hex_index(b)+'\t'+jj+'['+sym_index[k[1]][::-1]+']'+'\n')
								b=b+len(jj+sym_index[k[1]])
								break
							

				if k[0] in reg and k[1] in lit:
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
							p=p+'_imm'+str(n)

					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+hex_convert(int(k[1]))+'\n')
							b=b+len(op+hex_convert(int(k[1])))


				if k[0] in reg and llp[0]=='dword':
					ds=llp[1].split(']')
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
							p=p+'_mem'+str(n)
					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+'['+sym_index[ds[0]][::-1]+']'+'\n')
							b=b+len(op+sym_index[ds[0]])

			if s[i]=='add':
				p=s[i]
				k=s[i+1].split(',')
				llp=k[1].split('[')
				if k[0] in reg and k[1] in reg:
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
					for n in reglist:
						if k[1] in reglist[n]:
							p=p+'_reg'+str(n)
					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+sublst(k[1],k[0],bitreg)+'\n')
							b=b+lstindex(k[1],k[0],bitreg)
							

				if k[0] in reg and k[1] in sym:
					for jj in reg_op:
						for nh in reg_op[jj]:
							dp=nh
							if k[1] in dp:
								
								fw.write(hex_index(b)+'\t'+jj+'['+sym_index[k[1]][::-1]+']'+'\n')
								b=b+len(jj+sym_index[k[1]])
								break
							

				if k[0] in reg and k[1] in lit:
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
							p=p+'_imm'+str(n)

					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+hex_convert(int(k[1]))+'\n')
							b=b+len(op+hex_convert(int(k[1])))


				if k[0] in reg and llp[0]=='dword':
					ds=llp[1].split(']')
					for n in reglist:
						if k[0] in reglist[n]:
							p=p+'_reg'+str(n)
							p=p+'_mem'+str(n)
					for op in opcode_data:
						if p in opcode_data[op]:
							fw.write(hex_index(b)+'\t'+op+'['+sym_index[ds[0]][::-1]+']'+'\n')
							b=b+len(op+sym_index[ds[0]])


fr=open('sample.asm','r')
fw=open('nihal.lst','w')
lst(fr,fw)
