names = ["ali", "yağmur", "hakan","deniz"]
years =[1998, 2000, 1998, 1987]
#1- "cenk" ismini listenin sonuna ekleyin
names.append("cenk")
print(names)
#2- "sena" değerini listenin başına ekle
names.insert(0, "sena")
print(names)
#3- "deniz" ismini listeden silin
names.remove("deniz")
print(names)
#4- "ali" ismi listenin bir elemanı mıdır
is_in_list = "ali" in names
print(is_in_list) 
#5- listeyi ters çevir
names.reverse()
print(names)
#6- sena isminin indeksi nedir
index_of_sena = names.index("sena")
print(index_of_sena)

#7- alfabetik sırala
names.sort()
print(names)
#8- years büyükten sırala
years.sort()
print(years)
#9- str = "cherlovet, dacia" ekle
str1 = "cherlovet"
str2 = "dacia"
result = f"{str1} {str2}"
print(result)

#10- years en büyük ve en küçük elemanları nedir
max_number = max(years)
print("en büyük sayı:" , max_number)
min_number = min(years)
print("en küçük sayı:", min_number)
#11- 1998 kaç tane var
count_years = years.count("1998")
print("listede '1998' eleamanı {} kaç kez geçiyor".format(count_years))
#12- years'taki tüm elemanları silin
years.clear()
print(years)
#13- kullanıclardan 3 adet marka bilgisini bir listede saklayın
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)


print(markalar)