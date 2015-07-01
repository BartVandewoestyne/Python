d = {"Antwerp": 2000, "Ghent": 9000, "Bruges": 8000, "Brussels": 1000}
print d

print d["Ghent"]

#d["Ostend"]  # KeyError
code = d.get("Ostend", "unknown")
print code

print d.keys()

lp1 = [(code,city) for city,code in d.items()]  # my solution where pair is a tuple
lp2 = [[code,city] for city,code in d.items()]  # model solution where pair is again list
print lp1
print lp2

z1 = dict(lp1)
z2 = dict(lp2)
print z1
print z2