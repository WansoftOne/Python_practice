Python Types:
int -> 1
string -> "This is a String"
boolean -> True or False
List -> ["value", 4, 4.5, [2,4, "hello"]]
tupla -> ("value", 4, 4.5)
Dictionary -> {"key":"Value", "key2", "value2"}

Functions:
fun my_function():
    return some_value #four space or one tab

Conversones:
int(4.8) -> Convert double to int
float(4) -> Convert int to double
str(4) -> Convert integer or double to string 
list((4,5,6)) -> Convert tupla to list

Comun Opetators
len("how many") -> size string, list, tupla, etc
type(4) -> return type data
map(str, [1,2,3,4]) -> change type to a collection like a list
round(6.344455, 1) ->round a float
range(5) -> generate a range in a list [0,1,2,3,4]
sum([1,2,3]) -> add a set result: 6
sorted([2,1,3]) -> sort a set result: [1,2,3]

Comand List
-> append
-> count
-> extend
-> index
-> insert
-> pop
-> remove
-> reverse
-> sort

Class
class Estudiante(object):
    def _init_(selft, name_r, age_r)
        selft.nombre = nombre_r
        selft.edad = edad_r
    def hola(self):
        return "Mi name is %s and I am %i" % (self.name, self.age)

e = Estudiante("Artur", 25)
print e.hello() -> "My name is Artur and I am 25"

Conditionals
if (a>b):
    #here your code
elif(a==b):
    #here your code
else:
    #here your code

BUCLE FOR
for i in list:
    #here you code
for i in range(5):
    #here your code

BUCLE WHILE
while (condition):
    #here your code



Virtual enviroment
Create virtual enviroment: python -m venv tutorial-env
Start virtual enviroment: name_virtual_enviroment/Scripts/activate

Instalar Django -- pip install django -U
Create a new Django APP --django-admin startproject name_proyect
Start Django Project -- python manage.py runserver
Create applitation in Django APP -- python manage.py startapp name_app

Shell Django --> python manage.py Shell
Save data --> user = UserModel()
Set data to user -> user.name = "Magda"
Execute save method on Model object --> user.save()

delete object --> user.delete()

find all elements --> User.objects.all()
find with filter --> User.objects.filter(email__contains='@')
find only one reference --> User.objects.get(email="email@email.com")




