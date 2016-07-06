class GenericNode(object):
    def __init__(self, data, first_child=None, next_sibling=None):
        self.data = data
        self.first_child = first_child
        self.next_sibling = next_sibling
