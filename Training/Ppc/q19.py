import hashlib

ans = ""

for i in range(1, 5000):
    ans += str(i)
    if len(ans) == 9125:
        break;

print(ans)
print("---------------------------------")
print(len(ans))

f = open("ans.txt", "w")
f.write(ans)
f.close()
