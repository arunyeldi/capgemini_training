def main():
    str = input()
    lc = 0
    uc = 0
    dig = 0
    spechr = 0
    l = len(str)
    for i in str:
        if i.islower():
            lc = lc + 1
        if i.isupper():
            uc = uc + 1
        if i.isdigit():
            dig = dig + 1
        else:
            spechr = spechr + 1
    if(lc >= 1 and uc >= 1 and dig >= 1 and spechr >= 1 and l >= 8):
        print("Strong")
    else:
        print("Invalid string")
main()