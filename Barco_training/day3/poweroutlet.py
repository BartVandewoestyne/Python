PowerOn = 1
PowerOff = 0


class PowerOutletBank(object):
    """
    "abstract base class" for any power outlet bank abstraction
    """

    def get_outlets(self):
        """Returns a tuple of PowerOutlet objects in this bank"""
        raise NotImplementedError

    def set_outlet_state(self, outlet_id, outlet_state):
        """Sets outlet corresponding to outlet_id to state corresponding to outlet_state"""
        raise NotImplementedError


class PowerOutlet(object):
    """
    "base" for any power outlet abstraction
    Usable as a generic abstraction as is
    """
    def __init__(self, bank, identifier):
        self.bank = bank
        self.identifier = identifier

    def set_state(self, outlet_state):
        """Sets the state of this outlet to the corresponding outlet_state"""
        self.bank.set_outlet_state(self.identifier, outlet_state)
