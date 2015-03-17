import sys,time

# Princess Print, a utility for pretty princess parseable pretty printing for pretty princesses.
# (...and my, you are looking quite lovely today!)
# 'x' is the data to be Princess Printed.
# --- Presently takes arbitrary combinations of lists, strings, ints, and dicts with no recursion limit. ---
# 'order' is a list for specific ordering of keys.
# 'col' is the max number of columns.
# 'indent' is the level of indentation.
# 'field' is an optional field header or title, mostly used internally to pass keys as headers.
def pripri(x,order=[],col=3,indent=0,field=''):
	if type(order) is list:
		for n in order:
			if type(x) is dict and n in x.iterkeys():
				pop=x.pop(n)
				pripri(pop,order,col,indent,n+': ')
	if type(x) is dict: # dictionary handling block.
		for i,(k,v) in enumerate(sorted(x.iteritems())):
			k=str(k)
			if i==0 and field!='*':
				sys.stdout.write(' '*indent+field) # prints key/field for first item
				indent+=len(field)
			if type(v) is dict or type(v) is list:
				pripri(v,order,col,indent,k+': ')
			else:
				if i==0:
					pripri(v,[],col,0,k+': ')
				else:
					pripri(v,[],col,indent,k+': ')
		if indent==0:
			sys.stdout.write('\n')
	elif type(x) is list: # list handling block.
		for i,n in enumerate(x):
			if i==0:
				sys.stdout.write(' '*indent+field) # prints key/field for first item
			if type(n) is dict or type(n) is list:
				if i==0:
					pripri(n,order,col,len(field))
				else:
					pripri(n,order,col,indent,' '*len(field))
			else:
				try:
					spc2
				except NameError:
					spc2=''
				if i==0:
					tab=0
					nl=''
					spacer=''
					spc2=' '*(10-(len(str(n))))
				elif i%col==0 and i!=0:
					tab=indent
					nl=''
					spacer=' '*len(field)
					spc2=' '*(10-(len(str(n))))
				elif col-1 > i%col > 0:
					tab=indent
					nl=''
					spacer=spc2
					spc2=' '*(10-(len(str(n))))
				elif i%col>=col-1:
					tab=indent
					spacer=spc2
					nl='\n'
				sys.stdout.write(' '*tab+spacer+'[ '+str(n)+' '+str(i)+' ]'+nl)
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
