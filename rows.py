"""This library works with row-like objects -- iterators of lists commonly loaded from excel, csv, html tables, or other formats."""

import csv_unicode
import excel # for xls support
import htmltable

test_strings = ['csv', 'xls','htm']

class UnknownFormat(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def infer_headers(gen):
    return gen.next()

#def detect_keys(rows):
    #mset = Multiset([len(row) for row in rows])
    #largest = mset.largest()
    #for row in rows:
        #if len(row) == largest:
            #return row

class MappedRowGenerator(object):
    def __init__(self, gen, headers=None):
        self.gen = gen
        if not headers:
            headers = infer_headers(self.gen)
        self.headers = headers
        self.mapping = dict(zip(headers, range(len(headers))))
        self.item = None
    
    def __getitem__(self, key):
        return self.item[self.mapping[key]]
    
    def next(self):
        return self.__iter__()
            
    def __iter__(self):
        self.item = self.gen.next()
        return self
    
    def keys(self):
        return self.headers

    def __iteritems__(self):
        for key in self.keys():
            yield (key, self[key])
    
    def items(self):
        return list(self.__iteritems__())
    
    def dict(self):
        return dict(zip(self.headers, self.item))

def guess_format(filename):
    ending = filename.split('.')[-1]
    ending = ending.lower()
    global test_strings
    for t in test_strings:
        if ending.startswith(t):
            return t
    return None

def read_rows(filename, headers=None, format=None):
    if not format:
        format = guess_format(filename)
        if not format:
            raise UnknownFormat("Format of %s cannot be inferred from filename" % filename)
    if format == "csv":
        f = open(filename)
        gen = csv_unicode.UnicodeReader(f)
    elif format == "xls":
        gen = excel.xls_to_rows(filename)
    elif format == "htm":
        f = open(filename)
        gen = htmltable.html_table_to_rows(f)
    return gen
