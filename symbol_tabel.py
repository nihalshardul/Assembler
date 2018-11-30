# <line_number	sym_no	symbol	def/undef	section		size	values   >

def sym_tab(fw,fr):
	size=1
	cont=['main','printf']
	sym_no=1
	line_count=1
	sym={}
	
	fw.write('-------------------------------------------------------Symbol Table-------------------------------------------------------\n')
	fw.write('line_number		sym_no		symbol		def/undef	section		size		values   \n')
	for line in fr.readlines():
		sp=line.split()
		for i in range(0,len(sp)):
			if sp[i]=='dd':
				if sp[i-1] not in sym:
					sym[sp[i-1]]='sym#'+str(sym_no)
					k=sp[i+1].split(',')
					size=len(k)*4
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i-1]+'\t\tD\t\tdata\t\t'+str(size)+'\t'+line+'\n')
					sym_no+=1

					break
			if sp[i]=='db':
				if sp[i-1] not in sym:
					sym[sp[i-1]]='sym#'+str(sym_no)
					k=sp[i+1]
					k=k.split("'")
					kp=k[1]
					size=len(kp)*1
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i-1]+'\t\tD\t\tdata\t\t'+str(size)+'\t'+line+'\n')
					sym_no+=1

			if sp[i]=='resb':
				if sp[i-1] not in sym:
					sym[sp[i-1]]='sym#'+str(sym_no)
					size=1
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i-1]+'\t\tD\t\tbss\t\t'+str(size)+'\t\t'+'-'+'\n\n')
					sym_no+=1

			if sp[i]=='resd':
				if sp[i-1] not in sym:
					sym[sp[i-1]]='sym#'+str(sym_no)
					size=4
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i-1]+'\t\tD\t\tbss\t\t'+str(size)+'\t\t'+'-'+'\n\n')
					sym_no+=1
			
			if sp[i]=='main:':
				if sp[i-1] not in sym:
					sym[sp[i-1]]='sym#'+str(sym_no)
					size='-'
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+'main'+'\t\tU\t\ttext\t\t'+size+'\t\t'+'-'+'\n\n')
					sym_no+=1

			if sp[i]=='printf':
				if sp[i-1] not in sym:
					sym[sp[i]]='sym#'+str(sym_no)
					size='-'
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i]+'\t\tU\t\ttext\t\t'+size+'\t\t'+'-'+'\n\n')
					sym_no+=1

			if sp[i]=='scanf':
				if sp[i-1] not in sym:
					sym[sp[i]]='sym#'+str(sym_no)
					size='-'
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+sp[i]+'\t\tU\t\ttext\t\t'+size+'\t\t'+'-'+'\n\n')
					sym_no+=1

			if sp[i]=='printf,scanf':
				s=sp[i].split(',')
				if s[0] not in sym:
					sym[s[0]]='sym#'+str(sym_no)
					size='-'
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+s[0]+'\t\tU\t\ttext\t\t'+size+'\t\t'+'-'+'\n\n')
					sym_no+=1

				if s[1] not in sym:
					sym[s[1]]='sym#'+str(sym_no)
					size='-'
					fw.write('\t'+str(line_count)+'\t\t'+'sym#'+str(sym_no)+'\t\t'+s[1]+'\t\tU\t\ttext\t\t'+size+'\t\t'+'-'+'\n\n')
					sym_no+=1


		line_count+=1
	#print sym
	return sym


fr=open('sample.asm','r')
fw=open('sym_table.lst','w')

sym=sym_tab(fw,fr)


