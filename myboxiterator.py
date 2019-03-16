from collections import Iterator

class MyBoxIterator(Iterator):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
           raise StopIteration
        return self.data.pop()
