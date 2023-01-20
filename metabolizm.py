def get_metabolizm(gender: int,
                   mass: float,
                   height: float,
                   age: float):
    if gender == 1:
        metabolizm = 66.5 + (13.75 * mass) + (5.003 * height) - (6.775 * age)
    else:
        metabolizm = 66 + (9.55 * mass) + (1.8 * height) - (4.7 * age)
    return metabolizm


def main():
    while True:
        gender = int(input('Введите цифру вашего пола (1 - мужчина, 2 - женщина): '))
        if gender == 1 or gender == 2:
            break
    mass = float(input('Ваш вес в килограммах: '))
    height = float(input('Ваш рост в сантиметрах: '))
    age = float(input('Ваш возраст: '))
    print(f"Ваш базовый метаболизм должен равняться: {get_metabolizm(gender, mass, height, age)}")
    input('Нажмите Enter для завершения работы...')


if __name__ == "__main__":
    main()
