# coding=utf-8
name = 'alla frolova'
print(name.upper() + ' ' + name.title())

cars = []
# метод списка
cars.append('ford')
cars.append('suzuki')
cars.append('chrysler')
# use insert() method to insert smth. to a certain position of the list:
cars.insert(1, 'dodge')
print(cars)
# общий метод
del cars[2]
print(cars)
cars.append('honda')
# удаление элемента из списка (по умолч. последнего); использовать, если элемент ещё нужен:
print(cars.pop(3))
cars.append('honda')
# удаление элемента по значению (только первое вхождение):
cars.remove('honda')
print(cars)
# sorted(cars) - не изменяет исходный список; cars.sort(reverse = True); cars.reverse(); len(cars)

squares = [value**2 for value in range(0,11)]
print(squares)


for number in range(0, 21):
    print(number)

numbers = list(range(0, 21, 2))
print(numbers)
print(max(numbers))
print(sum(numbers))

numberS = list(range(0, 31, 3))
print(numberS)

cubes = [value**3 for value in range(0, 11)]
print(cubes)

alien_color = 'yellow'
if alien_color == 'green':
    print('you\'ve made 5 points')
else:
    print('you\'ve made 10 points')

fruits = ['mango', 'jackfruit', 'pear', 'peach', 'apple', 'orange', 'tangerine', 'grape', 'plum', 'pomegranate']
if 'jackfruit' in fruits:
    print('why would you add jackfruit into your list?')
if 'mango' in fruits:
    print('mango is the best')
if 'pear' in fruits:
    print('pears have boron in them')



