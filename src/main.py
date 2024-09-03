import logging
import statistics

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def calculate_route_location(airports):
    if not airports:
        logger.error("Список аэропортов не может быть пустым.")
        raise ValueError("Список аэропортов не может быть пустым.")

    if any(num < 0 for num in airports):
        logger.error("Все числа должны быть положительными целыми числами.")
        raise ValueError("Все числа должны быть положительными целыми числами.")

    logger.info(f"Вычисление медианы для аэропортов: {airports}")
    median = statistics.median(airports)
    logger.info(f"Вычисленная медиана: {median}")
    return median


def main():
    while True:
        try:
            # Ввод массива из консоли. Пользователь вводит числа через пробел.
            input_data = input("Введите положительные целые числа через пробел:\n")

            # Преобразуем введенные данные в список целых чисел
            airports = list(map(int, input_data.split()))

            # Вычисляем оптимальное расположение маршрута
            optimal_location = calculate_route_location(airports)

            print(f"Оптимальное расположение маршрута: {optimal_location}")
            break  # Завершаем цикл, если все прошло успешно
        except ValueError as e:
            logger.error(f"Произошла ошибка: {e}")
            print(f"Ошибка: {e}. Попробуйте еще раз.")
        except Exception as e:
            logger.exception("Произошла непредвиденная ошибка")
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
