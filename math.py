# add Implementation
def add(a,b):
	return a+b
    
# sub implementation
def sub(a,b):
	return a-b #on master branch
    
# multi implementation    
def multi(a,b):
	return a*b #on the BUG456
    
# div implementation
def div(a,b):   #on master
	if(b==0):
        return ERROR_DIVIDE_BY_ZERRO
    else:
        return a/b
#square implementation
def square(a):
    return a*a