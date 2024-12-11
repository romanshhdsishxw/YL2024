class DefaultList(list):
    def __init__(self, default):
        list.__init__(self)
        self.default = default

    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)
        except IndexError:
            return self.default