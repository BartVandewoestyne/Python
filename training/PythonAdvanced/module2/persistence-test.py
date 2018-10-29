import pickle


class Foo:
    attr = 'A class attribute'


pickle.dump(Foo, open( "myFoo.p", "wb" ))

with open('myFoo.p', 'rb') as f:
    data = pickle.load(f)

print(data.attr)