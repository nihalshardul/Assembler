# <line_no	lit_no		hex_no		original_no>

from symbol_tabel import*

def symlit(n):
	n=n.split(",")
	p=''
	for i in range(0,len(n)):
		if i!=len(n)-1:
			k=hex(int(n[i]))
			p=p+str(k)+','
		if i==len(n)-1:
			k=hex(int(n[i]))
			p=p+str(k)
	return p


def hex_convert(no):
	str1=hex(no)
	return(str1)



def lit(fr,fw):
	direc=['dd','db']
	lit={}
	count=1
	cons=['mov','add','sub']
	reg=['al','bl','cl','dl','ah','bh','ch','dh','ax','bx','cx','dx','sp','bp','si','di','eax','ebx','ecx','edx','esi','edi','esp','ebp']
	lit_count=1
	fw.write("------------------------------------------------------Literal Table-------------------------------------------------\n\n")
	fw.write("\tLine_no\t\tLit_no\t\tHex_no\t\tLiteral_Symbol\t\tType\n\n")

	for line in fr.readlines():
		s=line.split()
		for i in range(0,len(s)):
			if s[i] in cons:
				n=s[i+1].split(',')
				kn=n[1].split('[')
				if kn[0] in reg:
					continue
				if kn[0] =='dword':
					continue
				else:
					
					if kn[0].isdigit():
						if kn[0] not in lit:
							lit[kn[0]]='lit#'+str(lit_count)
							fw.write("\t"+str(count)+"\t\t"+'lit#'+str(lit_count)+"\t\t"+hex_convert(int(kn[0]))+"\t\t"+kn[0]+"\t\t\treg,img"+"\n")
							lit_count+=1 								
					else:
						if kn[0] in lit:
							if kn[0] not in lit:
								lit[kn[0]]='lit#'+str(lit_count)
								fw.write("\t"+str(count)+"\t\t"+'lit#'+str(lit_count)+"\t\t"+symlit(sym[kn[0]])+"\t\t"+n[1]+"\t\t\treg,img"+"\n")
								lit_count+=1
			
		count+=1
	#print lit
	return lit


fr=open('sample.asm','r')
fw=open('lit_tab.lst','w')

lit=lit(fr,fw)

