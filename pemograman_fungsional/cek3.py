#max() and min()

#using max(arg1, arg2, *args)
print("Nilai Max = ", max(1, 3, 2, 5, 4))
#%%
#using max(iterable)
data_angka = [1, 3, 2, 8, 5, 10, 6]
print("Nilai Max = ", max(data_angka))
#%%
num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]
print("Maximum is = ", max(num, num1, num2, key=len))
#%%
def sumDigit(num):
    sum = 0
    while(sum):
        sum += num % 10
        num = int(num/10)
    return sum
print("Maximum is = ", max(100, 321, 267, 59, 40, key=sumDigit))
num = [15, 300, 2700, 821, 52, 10, 6]
print("Maximum is = ", max(num, key=sumDigit))
#%%
#max() and min() lanjutan

#using min(arg1, arg2, *args)
print("Nilai Min = ", min(1, 3, 2, 5, 4))
#%%
#using min(iterable)
data_angka = [3, 2, 8, 5, 10, 6]
print("Nilai Min = ", min(data_angka))
#%%
num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]
print("Minimum is = ", min(num, num1, num2, key=len))
#%%
def sumDigit(num):
    sum = 0
    while(sum):
        sum += num % 10
        num = int(num/10)
    return sum
print("Maximum is = ", min(100, 321, 267, 59, 40, key=sumDigit))
num = [15, 300, 2700, 821, 52, 10, 6]
print("Maximum is = ", min(num, key=sumDigit))
#%%
#Lambda

#fungsi
def kuadrat(x):
    return x ** 2
print(kuadrat(3))
#%%
#lambda
kuadrat = lambda x : x ** 2
print(kuadrat(3))
kali = lambda x, y : x * y
print(kali(4, 3))
#%%
#why lambda?
def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4
L = [f1, f2, f3]
for v in L:
    print(v(3))
#%%
print(L[0](11))
#%%
L = [
    lambda x : x ** 2,
    lambda x : x ** 3,
    lambda x : x ** 4]
for v in L:
    print(v(3))
#%%
print(L[0](11))
#%%
#map()
nilai = [1, 2, 3, 4, 5]
pangkat = []
for x in nilai:
    pangkat.append(x ** 2)
print(pangkat)
#%%
nilai = [1, 2, 3, 4, 5]
def pangkat(x): return x ** 2
print(list(map(pangkat, nilai)))
#%%
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x : x * 2, my_list))
print(new_list)
#%%
#filter()
alfabet = ["a", "b", "c", "e", "i", "k", "o", "z"]
def filter_vocal(alfabet):
    vocal = ["a", "i", "u", "e", "o"]
    if alfabet in vocal:
        return True
    else:
        return False
vocal_terfilter = filter(filter_vocal, alfabet)
print("Huruf vocal yang tersaring adalah : ")
for vocal in vocal_terfilter:
    print(vocal)
#%%
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x : (x % 2 == 0), my_list))
print(new_list)
#%%
#sorted()
pyList = ["e", "a", "u", "o", "i"]
print(sorted(pyList))
#%%
pyString = "Python"
print(sorted(pyString))
#%%
pyTuple = ("e", "a", "u", "o", "i")
print(pyTuple)
#%%
data_set = {"e", "a", "u", "o", "i"}
print(sorted(data_set, reverse=True))
#%%
data_dict = {"e":1, "a":2, "u":3, "o":4, "i":5}
print(sorted(data_dict, reverse=True))
#%%
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sortedList = sorted(random, key=takeSecond)
print("Sorted list = ", sortedList)

#%%
biodata_19102283 = { 'trojan' : '111-222-333', 'spam' : '444-55-111'}
print("trojan : ", biodata_19102283["trojan"])
print("spam : ", biodata_19102283["spam"])

#%%
kuadrat_dictionary_19102283 = dict()
for i in range(10):
    kuadrat_dictionary_19102283[i] = i**2
print(kuadrat_dictionary_19102283)
#%%
def kuadrat_list_19100283(list):
    return [i**2 for i in list]
print(kuadrat_list_19100283([0,1,2,3,4,5,6,7,8,9]))
#%%
def bill_binner_19100283(biner):
    binary1 = biner
    decimal, i, n = 0, 0, 0
    while (biner != 0):
        dec = biner % 10
        decimal = decimal + dec * pow(2, i)
        biner = biner // 10
        i += 1
    return decimal
print(bill_binner_19100283(11001))
