#Latihan Kelas
#Fungsional Programming
#(Higher-order Functions)
#%%
#nomer 1
max_19102283 = lambda m, n: m if m > n else n
print(max_19102283(10, 3))

#%%
#nomer 2
#a.
even_fn_19102283 = lambda x: True if x % 2 == 0 else False
#%%
#b.
prog_19102283 = lambda list: [x for x in list if x % 2 == 0]
print(prog_19102283([1, 3, 2, 5, 20, 21]))

#%%
#3
Fahrenheit_List_19102283 = [98, 102, 110, 125]
fahrenheit_to_celcius_19102283 = map(lambda x: round(((5.00/9.00)*(x - 32)),2), Fahrenheit_List_19102283)
print("Celcius = ",list(fahrenheit_to_celcius_19102283))

#%%
#4
Tahun_List_19102283 = [1992, 1994, 1996, 1998, 2000, 2003, 2004, 2008, 2010, 2012,
2014]
prog_19102283 = filter(lambda x: x % 4 == 0, Tahun_List_19102283)
print("Tahun_Kabisat = ",list(prog_19102283))
#%%
#5
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

prog_19102283 = map(lambda x: max(x), zip(a, b, c))
print(list(prog_19102283))

#%%
#6
my_list_19102283 = [12, 65, 54, 39, 102, 339, 221, 50, 70]
prog_19102283 = [c for c in my_list_19102283 if c % 13 == 0]
print(prog_19102283)

#%%
#7
#a
dict_a_19102283 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
prog_19102283 = map(lambda x: x.get('name'), dict_a_19102283)
print(list(prog_19102283))
#%%
#b
prog_19102283 = map(lambda x: x.get('points'), dict_a_19102283)
print([x * 10 for x in list(prog_19102283)])

#%%
#8
list_a_19102283 = [1, 2, 3]
list_b_19102283 = [10, 20, 30]
prog_19102283 = map(lambda x: sum(x),zip(list_a_19102283, list_b_19102283))
print(list(prog_19102283))

#%%
#9
dict_a_2283 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}] #inisiasi variabel yang ada pada soal
prog_2283 = filter(lambda x: x['name']=='python', dict_a_2283) #inisiasi lambda untuk menampilkan output sesuai soal
print(list(prog_2283)) #fungsi print digunakan untuk menampikan output pada user

#%%
#10
death_19102283 = [
('James', 'Dean', 24),
('Jimi', 'Hendrix', 27),
('George', 'Gershwin', 38)]

prog_19102283 = sorted(death_19102283, key=lambda x: x[0][2])
print(prog_19102283)

#%%
#quizzzz
#%%
temps_2283 = [("Jakarta", 36), ("Berlin", 29), ("Cairo",36), ("Tokyo",
27), ("NewYork",28),("London",22),("Beijing", 32), ("Los Angeles",
26)] #inisiasi variabel dengan isi variabel
celcius_to_fahrenheit_2283 = map(lambda x: ((x[1] * 9/5) + 32), temps_2283) #inisiasi lambda dengan rumus yang sudah ditentukan
city_list_2283 = [x[0] for x in temps_2283] #inisiasi variabel untuk output nama kota
print(list(zip(city_list_2283,list(celcius_to_fahrenheit_2283)))) # fungsi print digunakan menampilkan output ke program
#%%
import math

data_2092 = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

rataan_2092 = map(lambda x: , data_2092)

print(list(rataan_2092))

#%%
from math import pi #mengimpor package python untuk menginisiasi pi

data_radius_2283 = [2, 5, 7.1, 10] #inisiasi variabel

luas_area_2283 = map(lambda x: pi * (x ** 2), data_radius_2283) #inisiasi lambda untuk menghitung luas area

print(list(luas_area_2283)) #fungsi print digunakan untuk menampilkan output program ke user
#%%
from functools import partial
def pangkatkan (a, b):
  return a**b

pangkatkan2 = partial(pangkatkan, 2)
pangkatkan3 = partial(pangkatkan, 3)
pangkatkan4 = partial(pangkatkan, 5)

print(pangkatkan2(2))
print(pangkatkan3(3))
print(pangkatkan4(4))

#%%
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java',
'points': 8}]

#%%
from functools import partial, reduce

def kalihkan_2283(x, y):
  print(f'Bilangan : {x}, {y}')
  return x * y

list_bil = [1, 2, 3, 4]

for i in list_bil:
penurunan = partial(kalihkan_2283, 4)
print(penurunan(i))
for i in list_bil:
  penurunan = partial(kalihkan_2283, 5)
  print(penurunan(i))

#%%

def lowercase(func):
  def wrapper():
    func_ret = func()
    change_to_lowercase = func_ret.lower()
    return change_to_lowercase
  return wrapper

#%%
#testing 1
def hello_function():
  return 'HELLO WORLD'

decorate = lowercase(hello_function)
print(decorate())

#%%
#testing 2
@lowercase
def hello_function():
  return 'HELLO WORLD'

print(hello_function())