alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(alphabet)
ic = []
text_is = ''
text_groups = []
text_buff = ''
text = open('text.txt', 'r').read()

for i in range(0, len(text), 17):
    text_is += text[i]
  
print(text_is)
print('____________________________________________')
L = len(text_is)

for i in range(len(alphabet)):
    n = text_is.count(alphabet[i])
    #print((n*(n-1))/(L*(L-1)))
    ic.append((n*(n-1))/(L*(L-1)))
    
for i in range(len(alphabet)):
    print(alphabet[i], " = ", ic[i])
    
print('____________________________________________')
print(sum(ic))

for i in range(17):
    for j in range(i, len(text) - i, 17):
        text_buff += text[j]
    text_groups.append(text_buff)
    text_buff = ''

print('____________________________________________')
print(text_groups)
print(len(text_groups))
char = ''
count = 0
shift = []

for i in text_groups:
    for j in alphabet:
        if i.count(j) > count:
            count = i.count(j)
            char = j
    shift.append(abs(alphabet.index(char) - 15))
    count = 0
    char = ''

print('____________________________________________')
print(shift)
print(len(shift))
print('____________________________________________')
a = ''
for i in text_groups:
    a += i[0]
    
print(a)
