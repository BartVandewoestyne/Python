# Python's default arguments are evaluated once when the function is defined,
# not each time the function is called (like it is in say, Ruby). This means
# that if you use a mutable default argument and mutate it, you will and have
# mutated that object for all future calls to the function as well.
#
# References:
#
#   [1] http://docs.python-guide.org/en/latest/writing/gotchas/

# A new list is created once when the function is defined, and the same list is
# used in each successive call!
def append_to1(element, to=[]):
    to.append(element)
    return to

my_list = append_to1(12)
print my_list
my_other_list = append_to1(42)
print my_other_list


# The good way to do it:
def append_to2(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

my_list = append_to2(12)
print my_list
my_other_list = append_to2(42)
print my_other_list
