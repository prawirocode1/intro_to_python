import random
def makeDist_generate(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak = random.randint(1, 100)
        list_data.append(nilai_acak)
    return list_data

def selection_short(data):
    n = len(data)

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if data[j] < data[min_idx]:
                min_idx = j 

        data[i],data[min_idx] = data[min_idx],data[i]

value = int(input("Banyak data yang akan di looping :"))
list_data = makeDist_generate(value)
print("list data sebelum data diurutkan")
print(list_data)
print("Data setelah di urutkan :")
selection_short(list_data)
print(list_data)