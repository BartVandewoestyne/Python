x = 0

def f1():
    x = 1
    print "inside f1(): x = ", x

def f2(x):
    x = 2
    print "inside f2(): x = ", x

print "Initially, at global scope: x = ", x
f1()
f2(x)
print "At the end, at global scope: x = ", x
