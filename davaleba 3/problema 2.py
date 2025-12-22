s1 = input("pirveli sityva: ")
s2 = input("meore sityva: ")


s1 = s1.lower()
s2 = s2.lower()


if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")
