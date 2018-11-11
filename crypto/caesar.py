alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
line = "----------------------------------------------------"
def encrypt(text, key):
    ciphertext = ''
    for i in text:
        ciphertext += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return ciphertext


def decrypt(ciphertext, key):
    text = ''
    for i in ciphertext:
        text += alphabet[(alphabet.index(i) - key) % len(alphabet)]
    return text


def cipher(ciphertext):
    for i in range(len(alphabet)):
        print("Key: ", i, " - ", decrypt(ciphertext, i))

print("-----Welcome to Caesar decryptor by KernelPanic-----")
print("""Choose alphabet:
      1.ENG
      2.Rus""")

if int(input("input: ")) == 2:
    alphabet = alphabet_rus.lower()

print(line)
print("""Choose mode:
      1. Encrypt
      2. Decrypt
      3. Cipher""")
choise = int(input("input: "))
if choise == 3:
    print(line)
    cipher(str(input("Enter a ciphertext: ")).lower().strip())
elif choise == 1:
    print(line)
    print(encrypt(str(input("enter text: ")).lower().strip(), \
                  int(input("enter a key: "))))
elif choise == 2:
    print(line)
    print(decrypt(str(input("enter text: ")).lower().strip(), \
                  int(input("enter a key: "))))

print("--------------Created by TitaniumHocker-------------")
