a = "23|8|1|20|4|15|25|15|21|11|14|15|23|1|2|15|21|20|1|2|3"
cipherText = a.split("|")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
line = "_______________________________________________"
text = ""


for i, v in enumerate(cipherText):
	cipherText[i] = int(v)


for i in cipherText:
	text += alphabet[i - 1]

print(text)