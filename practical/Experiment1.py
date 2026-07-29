#variables
x = 20
print(x)
print(type(x))
print()

y=0.69
print(y)
print(type(y))
print()

name = "SRIVALLI"
print(name)
print(type(name))
print()

#conditional statements
age =19
if age >= 19:
    print("You are an adult.")
elif age >= 18:
    print("You are a teenager.")
else:
    print("You are a child.")
print()

#loops
for i in range(15):
    print(i)
print()

count = 0
while count < 5:
    print(count)
    count += 1
print()

#operators
a=10
b=6
print("Addition:", a + b)
print()
print("Subtraction:", a - b)
print()
print("Multiplication:", a * b)
print()
print("Division:", a / b)
print()
print("OR operator:", a|b)
print()
print("AND operator:", a&b)
print()

#lists(mutable)
movies = ["orange", "majili", "oh baby"]
print(movies)
movies.append("spiderman")
print(movies)
print()

#tuples(immutable)
fruits = ("pineapple", "mango", "watermelon")
print(fruits)
print()

#dictionaries
person = {
    "name": "SRIVALLI",
    "age": 18,
    "city": "Hyderabad"
}
print(person)
print()