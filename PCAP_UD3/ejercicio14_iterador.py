class Cromos:
    def __init__(self) -> None:
        self.__current = -1
        self.cromos = ["cromo1", "cromo2", "cromo3", "cromo4"]
    def __iter__(self):
        print("En el metodo __iter__")
        return self
    def __next__(self):
        print("En el metodo __next__")
        self.__current+=1
        if self.__current==len(self.cromos):
            raise StopIteration()
        return self.cromos[self.__current]
    
album = Cromos()
for cromo in album:
    print (cromo)