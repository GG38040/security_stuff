#compares two jpg images for differences
#python2

d = open("kitters.jpg", "rb").read()
e = open("cattos.jpg", "rb").read()

f = " " 

for a, b in zip(d, e):
    if a != b:
        f += b

print(f)
