import hashlib
print("+-+-+-+ +-+-+-+-+-+-+-+")
print("|H||A||S||H| |K||İ||T| ")
print("    Yapımcı Gorki2     ")
print("+-+-+-+ +-+-+-+-+-+-+-+")
print("Yazıyı Md5'e Çevirme = 1 ")
print("Yazıyı Sha256'ya Çevirme = 2 ")
print("Çıkış = 3")
while True:
 a = int(input("Seçiminizi Yapın: "))
 if a == 1:
	 print("Yazıyı Md5'e Çevirme")
	 m = input("Çevrilecek Yazıyı Girin: ")
	 hashpass = hashlib.md5(m.encode('utf8')).hexdigest()
	 print("Md5 Şifreniz: ", hashpass)
 
 elif a == 2:
 	 print("Yazıyı Sha256'ya Çevirme")
 	 s = input("Çevrilcek Yazıyı Girin: ")
 	 sha256pass = hashlib.sha256(s.encode('utf-8')).hexdigest()
 	 print("Sha216 Şifreniz: ", sha256pass)

 elif a == 3:
 	print("Çıkılıyor!")
 	exit()
 
 else:
 	print("Malesef", a, "Bulunamadı!")
