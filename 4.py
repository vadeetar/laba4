Python
                         Копировать
                    from functools import reduce

                    # 1. Факториал через reduce
                    def factorial_reduce(n):
                    """Вычисление факториала с использованием reduce"""
                    if n < 0:
                    raise ValueError("Факториал определен только для неотрицательных чисел")
                    if n == 0:
                    return 1

                    numbers = list(range(1, n + 1))
                    return reduce(lambda x, y: x * y, numbers)

                    # 2. Демонстрация работы reduce
                    print("=== Факториал через reduce ===")
                    for n in [0, 1, 5, 7, 10]:
                    result = factorial_reduce(n)
                    print(f"{n}! = {result:,}")

                    # 3. Reduce с начальным значением
                    numbers = [1, 2, 3, 4, 5]

                    # Сумма
                    sum_result = reduce(lambda x, y: x + y, numbers)
                    print(f"\nСумма {numbers} = {sum_result}")  # 15

                    # С начальным значением
                    sum_with_init = reduce(lambda x, y: x + y, numbers, 10)
                    print(f"Сумма {numbers} с начальным значением 10 = {sum_with_init}")  # 25

                    # 4. Другие примеры использования reduce
                    # Произведение
                    product = reduce(lambda x, y: x * y, numbers)
                    print(f"\nПроизведение {numbers} = {product}")  # 120

                    # Максимальное значение
                    max_value = reduce(lambda x, y: x if x > y else y, numbers)
                    print(f"Максимум в {numbers} = {max_value}")  # 5

                    # Минимальное значение
                    min_value = reduce(lambda x, y: x if x < y else y, numbers)
                    print(f"Минимум в {numbers} = {min_value}")  # 1

                    # 5. Конкатенация строк
                    words = ["Hello", " ", "World", "!"]
                    sentence = reduce(lambda x, y: x + y, words)
                    print(f"\nКонкатенация {words} = '{sentence}'")  # 'Hello World!'

                    # 6. Reduce с пользовательской функцией
                    def custom_accumulator(acc, value):
                    """Пользовательская функция для reduce"""
                    # acc - аккумулятор, value - текущее значение
                    return f"{acc} -> {value}"

                    result = reduce(custom_accumulator, numbers, "Начало")
                    print(f"\nПользовательский аккумулятор: {result}")

                    # 7. Практический пример: вычисление среднего
                    grades = [85, 92, 78, 90, 88]

                    # Используем reduce для вычисления суммы и количества
                    def stats_accumulator(acc, grade):
                    total, count = acc
                    return (total + grade, count + 1)

                    total_sum, count = reduce(stats_accumulator, grades, (0, 0))
                    average = total_sum / count if count > 0 else 0

                    print(f"\nОценки: {grades}")
                    print(f"Сумма: {total_sum}, Количество: {count}, Среднее: {average:.2f}")

                    # 8. Функция для отображения промежуточных результатов
                    def factorial_with_steps(n):
                    """Факториал с выводом промежуточных шагов"""
                    if n <= 1:
                    print(f"0! = 1")
                    print(f"1! = 1")
                    return 1

                    numbers = list(range(1, n + 1))

                    def multiply_with_print(acc, val):
                    result = acc * val
                    print(f"  {acc} × {val} = {result}")
                    return result

                    print(f"Вычисляем {n}! = {' × '.join(map(str, numbers))}")
                    return reduce(multiply_with_print, numbers, 1)

                    print("\n=== Факториал с шагами ===")
                    factorial_with_steps(5)