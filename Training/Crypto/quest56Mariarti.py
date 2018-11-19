alphabet = 'abcdefghijklmnopqrstuvwxyz'
line = "_______________________________________________"
a = "NOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOBS NOOBS NOOOOOOOOOOOOOOOOOOOBS >_< NOOOOOOOOOBS NOOOOOOOOOOOOOOOOOOOBS >_< NOOOOOOOOOOBS NOOOOOOOOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOOOOOOBS >_< NOOOOOOOOOOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOBS NOOOOOOOOOOOOOOOOOOBS NOOOOBS"
ciphertext = a.split()
textNums = []
text = ""

while True:
	try:
		ciphertext.remove(">_<")
	except ValueError:
		break;


for i in ciphertext:
	text += alphabet[len(i) - 4]


print(text)


