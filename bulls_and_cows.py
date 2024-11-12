"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie

author: Jaroslav Cap
email: jarda.cap@seznam.cz
discord: jarda_75069
"""

import random



def generate_game_number():
    '''Generuje hadane cislo (4 unikatni cifry, nezacina 0)'''
    numbers = list(range(0,10))
    result = []

    # prvni cislo nesmi byt nula, generujeme nahodnou hodnotu 1-9
    # vygenerovane cislo vyzvedneme z pole
    # hodnotu rovnou prevadime na string kvuli pozdejsi konverzi celeho resultu
    result.append(str(numbers.pop(random.randint(1,9))))
    for round in range(3):
        # jeste 3x nahodne zvolime index s klesajic max hodnotu rozsahu,
        result.append(str(numbers.pop(random.randint(0, len(numbers) - 1))))

    # vratime 4 ciferny string, bude se nam lepe porovnavat s pokusem uzivatele
    return ''.join(result)


def play():
    '''Hlavni funkce hry'''

    def get_ident_str(root_str, count):
        '''Vrati string s poctem bulls/cows (root_str)'''
        if count == 1:
            lmultiple = ''
        else:
            lmultiple = 's'

        return f'{count} {root_str}{lmultiple}'


    game_number = generate_game_number()
    attempts = 0
    while True:
        incorrect = ''

        print('Attempt no {attempts}'.format(attempts = attempts + 1))
        user_input = input('Guess the number:')
        if not user_input.isdecimal():
            incorrect = 'Input has to be a number'

        elif not len(user_input) == 4:
            incorrect = 'Input has to be a 4 char length'

        elif len(set(user_input)) < 4:
            incorrect = 'Input cannot contain duplicates'

        elif user_input[0] == '0':
            incorrect = 'Input cannot start with \'0\''

        if incorrect:
            print(incorrect)
            continue

        # Platny pokus pricteme jen kdyz bylo zadani platne
        attempts += 1

        # Pokus odpovida, koncime hru
        if user_input == game_number:
            print(f'Congratulations, you have won with {attempts} attempts')
            break

        cows = 0
        bulls = 0
        for ix, cipher in enumerate(user_input):
            # Kontrola, jestli je cifra obsazena v hadanem cisle
            if cipher in game_number:
                # pokud ano, tak jeste zkontrolujeme, zda sedi na dane pozici
                if cipher == game_number[ix]:
                    bulls += 1
                else:
                    cows += 1

        print(', '.join([get_identstr('cow', cows), get_identstr('bull', bulls)]))


def main():
    play()

if __name__ == '__main__':
    main()
