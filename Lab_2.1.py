# Дано три числа. Знайти суму двох найбільших з них
a = int(input("1 число: "))
b = int(input("2 число: "))
c = int(input("3 число: "))
if a < b : m = a
else: m = b
if c < m: m = c
s = a + b + c - m
print("Сума 2-ух більших чисел", s)
