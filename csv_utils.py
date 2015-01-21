from csv_unicode import UnicodeReader

#def open_if_filename(f):

def csv_gen(f=None, headers=None):
    """Attempts to act on the filelike object f."""
    reader = UnicodeReader(f)
    if not headers:
        # Assume first row is headers
        headers = reader.next()
    for row in reader:
        yield dict(zip(headers, row))

class CSVGen(object):
    def __init__(self, f, headers=None):
        self.reader = UnicodeReader(f)
        if not headers:
            headers = self.reader.next()
        self.headers = headers
        self.mapping = dict(zip(headers, range(len(headers))))
        self.item = None
    
    def __getitem__(self, key):
        return self.item[self.mapping[key]]
    
    def next(self):
        return self.__iter__()
            
    def __iter__(self):
        self.item = self.reader.next()
        return self
    
    def keys(self):
        return self.headers
