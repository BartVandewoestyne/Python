# Example on list assignment.
#
# References:
#
#   [1] http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
#   [2] http://stackoverflow.com/questions/12888506/assignment-operator-about-list-in-python

listA = [0]
listB = listA
listB.append(1)
print listA

list1 = ["Tom", "Sam", "Jim"]
list2 = list1
print id(list1)
print id(list2)

list3 = list1[:]
print id(list3)
