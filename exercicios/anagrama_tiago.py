def eh_anagrama(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    anagrama = sorted(str1) == sorted(str2)
    return anagrama


if __name__ == '__main__':
    print(eh_anagrama('ABA', 'AaB'))
    print(eh_anagrama('THE ALIAS MEN', 'ALAN SMITHEE'))