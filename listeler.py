
liste = ["Ali", "Ahmet", "Ayşe", 1, 2, 3, 4, 7.5]
#buraları önceki videomuzda yapmıştık isterseniz aynı özellikleri deneyebilirsiniz
print(liste[0])
print(liste[2:6])   #->2.indeksten 6.indexe kadar yazdırdık
print(liste[::-1])  #->tersten yazdırdık burada
print("--------------------")

#append ->diziye eleman ekler en sonuna daha doğrusu kaldığı en son yere ekler
liste.append("cengaver yasin")
print(liste)
print("--------------------")
#insert     ->belli bir indexteki ifade yerine gireceğimiz ifadeyi ekliyor
#liste.insert(index, girilecek kelime)
liste.insert(2, "çorum")    #Ayşe yerine çorum geldi
print(liste)
print("--------------------")
#pop ->siliyor
#liste.pop(silinmesi istenen index) 2.indexte en son .orum vardı ve çorum sildi
liste.pop(2)
print(liste)
print("--------------------")

#remove ->burada string vermek yerine direkt objeyi vererek işlem yapıyoruz
yeni_list = ["arda", "azra", "ilhan", "yaşar", "nazım", "ibrahim", "enes", "elif"]
print(yeni_list)
yeni_list.remove("ilhan")
print(yeni_list)
print("--------------------")
#clear ->burada direkt siliyor listenin tamamını içine bir değer almıyor :) boş liste göstericek sadece
yeni_list.clear()
print(yeni_list)

#index -> bizi girdiğimiz objenin kaçıncı indexte olduğunu söyleyecek
yeni_list = ["arda", "azra", "ilhan", "yaşar", "nazım", "ibrahim", "enes", "elif"]
print(yeni_list.index("azra"))
#burada dizinin tamamını silmiştik orayı unuttum :))
print(yeni_list.index("elif"))
print("--------------------")
#count  ->listede bir elemanın kaç kere olduğunu bize döndürür

liste2 = [1,2,4,4,4,4,7,8,"a","a","b"]
print(liste2.count(1))
print(liste2.count(4))
print(liste2.count("a"))
print(liste2.count("b"))
print("--------------------")
#sort -> bize listeyi sıralı hale getirir
sortliste = [1,2,3,4,8,6,0,-2,5,9,45,23,21,14]
sortliste.sort()
print(sortliste)
sortliste2 = ["a","b","t", "e", "ali"]
sortliste2.sort()
print(sortliste2)

#peki hem string hemde sayıların olduğu bir dizide hangisine öncelik verir
#sortliste3 = [1,8,7,3,4,6,"a","b","t", "e", "ali", "arda", "azra", "ilhan", "yaşar", "nazım", "ibrahim",9,8,19, "enes", "elif"]
#sortliste3.sort()
#print(sortliste3)
#reverse fonksiyonu -> tersten yazdırır
sortliste2.reverse()
print(sortliste2)