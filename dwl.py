'''
Pomocnicze funkcje niezwiazane z analiza
'''


def compare(list1, list2):
    '''
    Porownanie dwoch list - wyświetla ktore elementy z pierwszej nie są w drugiej
    '''

    for x in range(len(list1)):
        if not list1[x] in list2:
            print(x, list1[x])


def converte(capital_string):
    '''
    Dla napisu zlozonego z duzych liter zwraca jego wersje, gdzie tylko pierwsze w kolejnych slowach sa wielkie.
    Przykladowo: converte('IVORY COAST') = 'Ivory Coast'
    '''
    res = ''
    capital_letter = True
    for char in capital_string:
        if capital_letter and char != char.lower():
            capital_letter = False
            res += char
            continue
        if char == '&':
            res += 'and'
            continue
        if char == " ":
            capital_letter = True
        res += char.lower()
    return res
