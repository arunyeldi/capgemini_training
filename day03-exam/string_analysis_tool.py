def main():
    str = input().lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vo = 0
    co = 0
    dig = 0
    spechr = 0
    for i in str:
        if i in vowels:
            vo = vo + 1
        elif i not in vowels and i.isalpha():
            co = co + 1
        elif i.isdigit():
            dig = dig + 1
        else:
            spechr = spechr + 1
    print(vo, co, dig, spechr)
    print(str[::-1])
main()