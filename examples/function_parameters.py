def f1(x):
  print "f1(x): ", x

def f2(x):
  print "f2(x): ", x

def g(f):
  f(2)
  f(3)

g(f1)
g(f2)
