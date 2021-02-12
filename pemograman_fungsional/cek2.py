listku_19102283 = [x for x in range(3, 29) if x % 2 == 0]
print(listku_19102283)
#%%
bilangan = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#A
list_a_19102283 = [x for x in bilangan[0:10] if x % 2 == 1]
print(list_a_19102283)
#B
list_b_19102283 = [x for x in bilangan if x % 3 == 0]
print(list_b_19102283)
#%%
def kuadratkan_list_19102283(list):
    return [i ** 2 for i in list]
print(kuadratkan_list_19102283([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#%%
kuadratkan_dict_19102283 = dict()
for x in range(1,10):
    kuadratkan_dict_19102283[x] = x ** 2
print(kuadratkan_dict_19102283)
#%%

inventory_19102283 = {
    'emas' : 500,
    'kantong' : ['korek', 'tali', 'batu'],
    'ransel' : ['timpani','pisau belati', 'kasur gulung','roti']
}

#a
inventory_19102283['saku'] = ""
print(inventory_19102283)
#b
inventory_19102283['saku'] = "kerang", "bandeng", "berry", "rumput laut"
print(inventory_19102283)
#c
inventory_19102283["ransel"].sort()
print(inventory_19102283["ransel"])
#d
inventory_19102283["ransel"].remove("pisau belati")
print(inventory_19102283)
#e
inventory_19102283["emas"] = 50
print(inventory_19102283)
#%%
def jumlahkan_19102283(*args):
    return sum(args)
print(jumlahkan_19102283(10, 20))
print(jumlahkan_19102283(10, 20, 50 , 60))