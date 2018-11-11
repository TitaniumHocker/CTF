from zipfile import ZipFile
import os
line = "---------------------------------------------------"


def BrutForce(string):
    for word in string:
        passwd = word.replace('\n', '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall("ExtractArchive")
        except:
            yield "[False]: " + passwd
        else:
            yield line + "\n[True]: " + passwd
            return


try:
    os.mkdir("ExtractArchive")
except FileExistsError:
    pass


os.system('cls')
print("----------Welcome to ZipBrut by KernelPanic---------")
with open(input("Dictionary: "), errors="ignore") as dictionary:
    with ZipFile(input("Archive: ")) as archive:
        print(line)
        for password in BrutForce(dictionary):
            print(password)
print("--------------Created by TitaniumHocker-------------")
os.system("pause")
