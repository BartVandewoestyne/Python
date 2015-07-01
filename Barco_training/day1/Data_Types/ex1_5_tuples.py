y = [(c, 9.0*c/5+32) for c in range(-10, 50)]

z = [((f-32)*5.0/9, f) for f in range(0, 100)]

# range spuwt iets uit dat itereerbaar is (de for loop kan er iets mee doen)
# in Python 2 is het een lijst (en die zit in 1 keer in het geheugen).
# in Python 3 een itereerbaar object (minder memory-intensief)
# op achtergrond werkt het anders, maar functioneel is het wel hetzelfde
# in Python 2 heb je xrange, en xrange is de goeie.

# 2to3 kan je gebruiken om te converteren van Python 2 naar Python 3
# echo "xrange(10" > conversiontest.py
# 2to3 conversiontest.py
# echo "print(10)" > conversiontest.py
# 2to3 conversiontest.py