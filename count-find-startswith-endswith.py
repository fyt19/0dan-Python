#count saydırıyor(sayac)
a = "Çorum Dunyablablablanın bla Merkezidir. bla bla bla"
print(a.count("u"))     # burada ise kaç tane u var diye soruyoruz
print(a.count(" "))
print(a.count("bla")) # kac tane bla var diye sorduk
print("-------------")
#find buluyor
b = "ankara güzel bir şehirdir."
c = "ankara güzel bir şehirdir kara kara."
print(b.find("kara"))       #burada ise bize kaçıncı indekste olduğunu söylüyor
print(c.find("kara"))       #2 gelmesinin sebebi ise ilk nerede denk gelirse soldan okumaya başlar onu verir diğerleri önemsizdir
print("-------------")
#startswith başlangıçtaki stringe bakıyorr
x = "en iyi youtube kanalı Cengaverfurkan kanalıdır. :)"
z = "1234"
print("z degiskeni:",z.startswith("1"))
print(x.startswith("en"))
print(x.startswith("trdfal"))
print(x.startswith("e"))
print("-------------")
#endswith son stringe bakar
print(x.endswith(":)"))
print(x.endswith("ldfkg"))

