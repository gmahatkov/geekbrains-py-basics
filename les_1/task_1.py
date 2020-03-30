"""
Задача 1
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""


def main():
    from random import randint
    the_num = randint(1, 100)
    is_first_guess = True
    while True:
        try:
            if is_first_guess:
                guess = int(input('Let\'s play a guess game, enter some number in range of 1 to 100: '))
            else:
                guess = int(input('Just try again: '))
            if guess in range(1, 100):
                if guess > the_num:
                    print('Oh come on big boy! My number is not that big!')
                elif guess < the_num:
                    print('You should try better! My number is bigger!')
                else:
                    print('Congrats! You win! As always! You must\'a have perfect body and perfect soul...')
                    break
            else:
                print('Don\'t you dare to break MY GAME! '
                      'As i said it\'s gotta be not bigger than 100 and not less than 1!')
        except ValueError:
            print('Oh come on! We just need some number from you! Is that so hard?')
        finally:
            is_first_guess = False
    is_leaving = input('Do you wish to finish this infinite jest of ours? If you do just say \"yes\": ') == 'yes'
    if not is_leaving:
        print('No, you gotta leave anyways. We tired of you playing all these stupid games.')
    else:
        print('Oh it so saaaad!)))) You should come some time so we could play some more of these fun games! ;)')
    worthless_words = input('Before you leave say something: ')
    if len(worthless_words) > 0:
        print(f'Oh please stop talking! Your words brings us pain: \"{worthless_words.capitalize()}!!!1\"')
    else:
        print('Well you could try but you wished to not')


if __name__ == '__main__':
    main()
