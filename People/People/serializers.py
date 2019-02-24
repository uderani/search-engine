

class PersonSerializer:
    keys = ['index', 'full_name']

    def __init__(self, obj):
        self.obj = obj

    def data(self):
        data = {}
        for key in self.keys:
            data[key] = getattr(self.obj, key)
        return data
