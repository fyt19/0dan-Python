#join araya katıyor
print("@".join(["google","gmail.com"]))
print("/".join(["nigde", "bor yolu", "Merkez kampus"]))
print("/".join(["29", "09", "2022"]))
print("--------------------")
#replace değiştiriyor
a = "merhabalar, ben cengaver Furkan"
b = "1324"
print(a.replace(",",";"))
print(b.replace("2","8"))

print("--------------------")
#split verdiğimiz degere kadarkı olan kısımlara gore boluyor basitçe
a = "Ben Cengaver Furkan"
b = "Ben Cengaver, Furkan"
print(a.split(","))
print(b.split(","))
print(b.split(" "))
print(a.split("e"))
print("--------------------")
#strip verdiğimiz degere gore baştaki ve sondaki kelimenin onunu arkasındaki degerleri siliyor
a = "Merhabalar Dunyaya"
b = "            Merhabalar Dunyaya"
c = "Merhabalar Dunyaya                "
d = "          Merhabalar Dunyaya        "
e = "         Merhabalar          Dunyaya            "      # nedeni ise kelimelerin arasına bakmaz baş ve sona bakar ve istenene göre siler
f = "aaaaaaaaaaaaaaaaasdfgaaaaaaaaaaaaaaaaaaa"
print(a.strip("a"))
print(b.strip())
print(c.strip())
print(d.strip())
print(e.strip())
print(f.strip())            # burada ise biz dedikki f deki degiskende basta ve sondaki boslukları sil
print(b.strip())
print(f.strip("a"))         ## burada ise biz dedikki f deki degiskende basta ve sondaki a'ları sil



