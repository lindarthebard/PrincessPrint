import sys,time

# Princess Print, a utility for pretty princess parseable pretty printing for pretty princesses.
# 'x' is the object to be Princess Printed.
# 'col' is the max number of columns.
# 'order' is a list for specific ordering of keys.
# 'indent' is the level of indentation.
# 'field' is an optional field header or title, mostly used internally to pass keys as headers.
def princess_print(x,col=3,order=[],indent=0,field=''):
	if type(order) is list: # checks for ordering, processes those items first.
		for n in order:
			try:
				princess_print(x[n],col,order,indent,field)
			except KeyError:
				pass
	if type(x) is dict: # dictionary handling block.
		for i,(k,v) in enumerate(sorted(x.iteritems())):
			if i==0:
				sys.stdout.write(' '*indent+field) # prints the key/field for the first item
				indent+=len(field)
			if type(v) is dict:
				princess_print(v,col,order,indent,k+': ')
			elif type(v) is list:
				princess_print(v,col,order,indent,k+': ')
			else:
				if i==0:
					princess_print(v,col,order,0,k+': ')
				else:
					princess_print(v,col,order,indent,k+': ')
		if indent==0:
			sys.stdout.write('\n')
	elif type(x) is list: # list handling block.
		for i,n in enumerate(x):
			if i==0:
				sys.stdout.write(' '*indent+field) # prints the key/field for the first item
			if type(n) is dict:
				if i==0:
					princess_print(n,col,order,0,field)
				else:
					princess_print(n,col,order,indent,field)
			elif type(n) is list:
				princess_print(n,col,order,indent)
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
				sys.stdout.write(' '*indent+spacer+'[ '+n+' ]'+nl)
				if i==len(x)-1 and nl!=('\n'):
					sys.stdout.write('\n')
		if indent==1:
			sys.stdout.write('\n')
	else: # generic/string handling block.
		if indent==0:
			sys.stdout.write(' '*indent+field+'[ '+str(x)+' ]\n')
			indent+=1
		else:
			sys.stdout.write(' '*indent+field+'[ '+str(x)+' ]\n')
