def eh_anagrama(str1, str2):
    anagrama = sorted(str1.lower()) == sorted(str2.lower())
    return anagrama

if __name__ == '__main__':
    print(eh_anagrama('ABA', 'AaB'))