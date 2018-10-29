class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.next_num = start - 1

    def __iter__(self):
        return self

    ## In Python 3, use __next__
    ## In Python 2, use next
    def next(self):
        if self.stop == self.next_num:
            raise StopIteration
        else:
            self.next_num += 1
            return self.next_num


for i in MyRange(4, 7):
    print i
