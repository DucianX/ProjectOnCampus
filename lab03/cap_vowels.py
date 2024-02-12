def upper_maker():
    x = input("Plz type in a string.")
    result = ""
    vowel = "aeiouAEIOU"
    for i in x:
        if i in vowel:
            result += i.upper()
        else:
            result += i
        
    print(result)

upper_maker()