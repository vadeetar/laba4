Python
                         Копировать
                    import time
                    from functools import wraps

                    # 1. Декоратор замера времени
                    def timer(func):
                    """Декоратор для измерения времени выполнения функции"""
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                    start_time = time.perf_counter()
                    result = func(*args, **kwargs)
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд")
                    return result
                    return wrapper

                    # 2. Декоратор с кешированием
                    def cache(func):
                    """Декоратор для кеширования результатов"""
                    cache_dict = {}

                    @wraps(func)
                    def wrapper(*args, **kwargs):
                    key = str(args) + str(kwargs)
                    if key in cache_dict:
                    print(f"Взято из кеша: {func.__name__}{args}")
                    return cache_dict[key]

                    result = func(*args, **kwargs)
                    cache_dict[key] = result
                    print(f"Вычислено и сохранено в кеш: {func.__name__}{args}")
                    return result

                    return wrapper

                    # 3. Пример использования
                    @timer
                    def factorial(n):
                    """Вычисление факториала"""
                    result = 1
                    for i in range(2, n + 1):
                    result *= i
                    return result

                    @timer
                    @cache
                    def fibonacci(n):
                    """Вычисление числа Фибоначчи"""
                    if n <= 1:
                    return n
                    return fibonacci(n-1) + fibonacci(n-2)

                    # 4. Декоратор с параметрами
                    def repeat(times=1):
                    """Декоратор для повторного выполнения функции"""
                    def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                    results = []
                    for i in range(times):
                    print(f"Попытка {i+1}/{times}")
                    result = func(*args, **kwargs)
                    results.append(result)
                    return results[-1]  # возвращаем последний результат
                    return wrapper
                    return decorator

                    # Пример использования
                    if __name__ == "__main__":
                    print("=== Декоратор timer ===")
                    print(f"Факториал 100 = {factorial(100)}")
                    print(f"Факториал 200 = {factorial(200)}")

                    print("\n=== Декоратор cache ===")
                    print(f"Фибоначчи(10) = {fibonacci(10)}")
                    print(f"Фибоначчи(10) снова = {fibonacci(10)}")

                    print("\n=== Декоратор repeat ===")
                    @repeat(times=3)
                    def greet(name):
                    print(f"Привет, {name}!")
                    return f"Приветствие для {name}"

                    greet("Вадим")# Коммит Sun Jan 11 17:56:54 RTZ 2026
