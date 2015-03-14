import sys,time

# x= p_reply, col= num columns for lists, indent=extra indent, field=field name
def princess_print(x,col=3,indent=0,field=''):
	if 'type' in x:
		x_type=x.pop('type')
		princess_print(x_type,col,0,'Type: ')
	if 'size' in x:
		x_size=x.pop('size')
		princess_print(x_size,col,0,'Size: ')
	if 'body' in x:
		x_body=x.pop('body')
		princess_print(x_body,col,0,'Body: ')
	if type(x) is dict:
		for i,(k,v) in enumerate(sorted(x.iteritems())):
			if i==0:
				sys.stdout.write(' '*indent+field)
				indent+=len(field)
			if type(v) is dict:
				princess_print(v,col,indent,k+': ')
			elif type(v) is list:
				princess_print(v,col,indent,k+': ')
			else:
				if i==0:
					princess_print(v,col,0,k+': ')
				else:
					princess_print(v,col,indent,k+': ')
		if indent==0:
			sys.stdout.write('\n')
	elif type(x) is list:
		for i,n in enumerate(x):
			if i==0:
				sys.stdout.write(' '*indent+field)
			if type(n) is dict:
				if i==0:
					princess_print(n,col,0,field)
				else:
					princess_print(n,col,indent,field)
			elif type(n) is list:
				princess_print(n,col,indent)
			else:
				if i==0:
					indent_char=''
					nl=''
					spacer=''
					spc2=' '*(10-(len(str(n))))
				elif i%col==0 and i!=0:
					nl=''
					spacer=' '*len(field)
					spc2=' '*(10-(len(str(n))))
				elif col-1 > i%col > 0:
					nl=''
					spacer=spc2
					spc2=' '*(10-(len(str(n))))
				elif i%col>=col-1:
					spacer=spc2
					nl='\n'
				sys.stdout.write(ind_chr*indent+spacer+'[ '+n+' ]'+nl)
				if i==len(x)-1 and nl!=('\n'):
					sys.stdout.write('\n')
		if indent==1:
			sys.stdout.write('\n')
	else:
		if indent==0:
			sys.stdout.write(' '*indent+field+'[ '+str(x)+' ]\n')
			indent+=1
		else:
			sys.stdout.write(' '*indent+field+'[ '+str(x)+' ]\n')
