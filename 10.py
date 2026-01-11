Python
                         Копировать
                    # 1. Базовые функции для map
                    def square(x):
                    return x ** 2

                    def cube(x):
                    return x ** 3

                    def add_ten(x):
                    return x + 10

                    def is_even(x):
                    return x % 2 == 0

                    # 2. Применение map с одной функцией
                    numbers = [1, 2, 3, 4, 5]

                    squares = list(map(square, numbers))
                    print(f"Квадраты: {squares}")  # [1, 4, 9, 16, 25]

                    cubes = list(map(cube, numbers))
                    print(f"Кубы: {cubes}")  # [1, 8, 27, 64, 125]

                    # 3. Применение map с lambda
                    incremented = list(map(lambda x: x + 5, numbers))
                    print(f"+5: {incremented}")  # [6, 7, 8, 9, 10]

                    even_check = list(map(lambda x: f"{x} - четное" if x % 2 == 0 else f"{x} - нечетное", numbers))
                    print(f"Проверка четности: {even_check}")

                    # 4. Применение нескольких функций через map
                    def apply_functions(value, functions):
                    """Применяет несколько функций к одному значению"""
                    results = []
                    for func in functions:
                    results.append(func(value))
                    return results

                    functions = [square, cube, add_ten, is_even]

                    print("\nПрименение нескольких функций к числам 1-5:")
                    for num in numbers:
                    results = apply_functions(num, functions)
                    print(f"  {num}: квадрат={results[0]}, куб={results[1]}, +10={results[2]}, четное={results[3]}")

                    # 5. Использование map с несколькими функциями
                    from functools import partial

                    def power(exponent, base):
                    return base ** exponent

                    # Создаем специализированные функции
                    square_func = partial(power, 2)
                    cube_func = partial(power, 3)

                    squares2 = list(map(square_func, numbers))
                    cubes2 = list(map(cube_func, numbers))

                    print(f"\nС partial: квадраты={squares2}, кубы={cubes2}")

                    # 6. Практический пример: обработка данных
                    data = ["  apple  ", "BANANA", "  Cherry  "]

                    # Цепочка преобразований
                    processed = list(map(str.strip, data))  # Убрать пробелы
                    processed = list(map(str.lower, processed))  # В нижний регистр
                    processed = list(map(str.capitalize, processed))  # С заглавной буквы

                    print(f"\nОбработка строк: {processed}")  # ['Apple', 'Banana', 'Cherry']

                    # 7. Map с встроенными функциями
                    words = ["python", "programming", "language"]
                    lengths = list(map(len, words))
                    print(f"\nДлины слов: {lengths}")  # [6, 11, 8]

                    # 8. Map с filter
                    numbers = range(1, 11)
                    even_squares = list(map(square, filter(lambda x: x % 2 == 0, numbers)))
                    print(f"\nКвадраты четных чисел 1-10: {even_squares}")  # [4, 16, 36, 64, 100]