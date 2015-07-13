class Outlet(object):
    def __init__(self, some_id, comm_obj):
        self.id = some_id
        self.comm_obj = comm_obj

    def on(self):
        self.comm_obj.write("%{0}=1".format(self.id))

    def off(self):
        self.comm_obj.write("%{0}=0".format(self.id))
