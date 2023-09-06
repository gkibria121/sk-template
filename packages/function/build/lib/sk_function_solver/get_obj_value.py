class GetObjectValue:

    def __init__(self):
        self.data = None

    def run(self,object_calling):
        return self.data[object_calling]

    def set_data(self,data):
        self.data = data