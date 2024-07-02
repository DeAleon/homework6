my_dict = {'Anton': 1998, 'Pascha': 1996, 'Oleg': 1997}
print(my_dict)
print(my_dict.get('Anton'))
print(my_dict.get('Kolya'))
my_dict.update({'Misha': 2000,
                'Kostya': 1987})
a = my_dict.pop('Pascha')
print(a)
print(my_dict)

my_set = {1, 2, "Hello", 3.14, 1, 2}
print(my_set)
my_set.add((5, 4))
my_set.discard('Hello')
print(my_set)
