#compares two jpg images for differences
#only works with python 2.  [] Not exactly sure why

d = open("kitters.jpg", "rb").read()
e = open("cattos.jpg", "rb").read()

f = " " 

for a, b in zip(d, e):
    if a != b:
        f += b

print(f)