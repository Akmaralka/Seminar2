from myboxiterator import MyBoxIterator

class MyBox:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def add(self, item):
        assert item != None
        self.data.append(item)

    def delete(self, name, surname, birthdate, nationality):
        if [name, surname, birthdate, nationality] in self.data :
            self.data.remove([name, surname, birthdate, nationality])
        else:
            return self.data

    def __contains__(self, name, surname, birthdate, nationality):
        if [name, surname, birthdate, nationality] in self.data:
            print("%s %s %s %s found!" % (name, surname, birthdate, nationality))
            return True
        else:
            print("This container doesn't containt such elements!")
            return False

    def __iter__(self):
        return MyBoxIterator(self.data)

class FillBox:
    def __init__(self, name, surname, birthdate, nationality, info=None):
        self.info = [name, surname, birthdate, nationality]
        self.next = None

    def __str__(self):
        return str(self.info)
