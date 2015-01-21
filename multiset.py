class Multiset(object):
    """Basic multiset for counts."""
    def __init__(self, seq=None):
        self.mset = dict()
        if seq:
            self.add(seq)
    
    def __getitem__(self, key):
        return self.mset[key]
    
    def add(self, seq):
        for elem in seq:
            try:
                self.mset[elem] += 1
            except KeyError:
                self.mset[elem] = 1
    
    def largest(self):
        (index, maximum) = (0, 0)
        for k, v in self.mset:
            if v > maximum:
                (index, maximum) = (k, v)
            return (k, v)

    def items(self):
        return self.mset.items()

    def __repr__(self):
        return str(self.mset)

def multiset(list_):
    """Returns a multiset (a dictionary) from the input iterable list_."""
    mset = dict()
    for elem in list_:
        try:
            mset[elem] += 1
        except KeyError:
            mset[elem] = 1
    return mset
