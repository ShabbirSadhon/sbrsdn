x=5 #global variable
def fun1():
    #total-local variable
    total=x+5
    fun2(total)

def fun2(y):
    global x
    x=y
fun1()
print("x=",x)
