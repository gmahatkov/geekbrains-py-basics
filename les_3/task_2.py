"""
Задача 2
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def print_user(
        first_name='',
        last_name='',
        birth_year=0,
        city='',
        email='',
        phone='',
):
    print(
        f"""
First Name: {first_name.title() if len(first_name) else '-'}
Last Name: {last_name.title() if len(last_name) else '-'}
Year of birth: {birth_year if birth_year>0 else '-'}
Email: {email if len(email) else '-'}
City of living: {city.title() if len(city) else '-'}
Phone number: {phone if len(phone) else '-'}
        """
    )


def main():
    while True:
        try:
            print_user(
                first_name=input('Enter your first name: '),
                last_name=input('Enter your last name: '),
                birth_year=int(input('Enter your birth: ')),
                city=input('Enter name of the city you live: '),
                email=input('Enter your email: '),
                phone=input('Enter your phone: '),
            )
            break
        except ValueError:
            print('Oops, something went wrong try again.')


if __name__ == '__main__':
    main()