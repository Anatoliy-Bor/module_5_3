class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = int(number_of_floors)
        self.name = name

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if self.new_floor < 0 or self.new_floor > self.number_of_floors:
            print(f' Этажа {new_floor} не существует ')
        else:
            n = 0
            while n < new_floor:
                n += 1
                print(n)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f' Название {self.name} , количество этажей {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if not isinstance(value, (int, House)):
            return f'  ошибка '
        else:
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        if not isinstance(value, (int, House)):
            return f'  ошибка '
        else:
            return House(self.name, value + self.number_of_floors)

    def __iadd__(self, value):
        if not isinstance(value, (int, House)):
            return f'  ошибка '
        else:
            return  House(self.name, value + self.number_of_floors)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
