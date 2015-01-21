import os

#import codecs
#codecs.open('links.csv', encoding='utf-8')

def join_path(path_list, filename=None):
    """Joins a list of directories into a path."""
    if filename:
        path_list.append(filename)
    path = path_list[0]
    for i in range(1, len(path_list)):
        path = os.path.join(path, path_list[i])
    return path

def ensure_directory(d):
    if not os.path.isdir(d):
        os.mkdir(d)

class Path(object):
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = []
    
    def join(self, tail=None, filename=None):
        path = []
        path.extend(self.path)
        if temp:
            path.extend(temp)
        if filename:
            path.append(filename)
        s = path_list[0]
        for i in range(1, len(path_list)):
            s = os.path.join(s, path_list[i])
        return s

    def append(self, entry):
        self.path.append(entry)
    
    def pop(self):
        self.path.pop(-1)
