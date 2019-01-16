while (True):
	sifre = int(input("Şifre Giriniz: "))
	if sifre == 2003:
		print("Hoşgeldiniz!!!")
		break
	elif sifre != 2003:
		print("Şifreniz Yanlış!!!") 

print("Giriş Başarılı!!!")
a = int(input("Şifre Değiştirmek İstermisin? Evet=1 Hayır=2 "))
if a == 1:
	newpass = int(input("Yeni Şifre Girin: "))
	print("Şifreniz Ayarlandı! Yeni Şifreniz:", newpass)

elif a == 2:
	print("Tamam!")

while True:
 command = str(input("Command:> "))
 print(command, "Not Found!")
 if command == "exit":
 	exit()



