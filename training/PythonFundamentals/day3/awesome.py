# TODO: finish this!
from poweroutlet import *


class AwesomeOutletBank(PowerOutletBank):
    def __init__(self, writer, num_outlets):
        assert(num_outlets in [4, 8, 16])
        assert(writer, "Writer cannot be None")
        assert(hasattr(writer, "write"))
        self.writer = writer
        outlets = []
        for i in range(1,num_outlets+1):
            outlets.append(PowerOutlet(self, i))
        self.outlets = tuple(outlets)

    def get_outlets(self):
        return self.outlets

    def set_outlet_state(self, outlet_id, outlet_state):
        pass
