from typing import Union
import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class QuestionList:
    """
    Документация на класс.
    Класс описывает модель списка вопросов к экзамену.
    """
    def __init__(self, question_amount: int, question_learnt: int):
        """
        Инициализация экземпляра класса.

        :param question_amount: Количество вопросов, которые нужно выучить.
        :param question_learnt: Количество выученных вопросов.

        Пример:
        >>> question_list = QuestionList(100, 0) #инициализация экземпляра класса
        """
        if not isinstance(question_amount, int):
            raise TypeError("Количество вопросов должно быть целым числом (тип int)")
        if not question_amount > 0:
            raise ValueError ("Количество вопросов должно быть положительным числом")
        self.question_amount = question_amount

        if not isinstance(question_learnt, int):
            raise TypeError("Количество выученных вопросов должно быть целым числом (тип int)")
        if question_learnt < 0:
            raise ValueError("Количество выученных вопросов должно быть положительным числом или 0")
        if question_learnt > question_amount:
            raise ValueError("Количество выученных вопросов не может быть больше количества вопросов")
        self.question_learnt = question_learnt

    def add_learnt_questions (self, added_learnt_questions: int) -> None:
        """
        Увеличение числа выученных вопросов.

        :param added_learnt_questions: Добавляемое количество выученных вопросов.

        :raise TypeError: Если добавляемое количество вопросов имеет не тип int, вызываем ошибку.
        :raise ValueError: Если суммарное число выученных вопросов превышает общее количество вопросов, вызываем ошибку.
        """
        ...

    def is_ready (self) -> bool:
        """
        Определение готов ли студент к экзамену (выучены ли все вопросы).

        :return: Возвращает True если все вопросы выучены, иначе False.
        """
        ...

    def persentage_learnt (self) -> float:
        """
        Определяет процент выученных вопросв от общего числа вопросов.

        :return: Возвращает процент выученных вопросв от общего числа вопросов с точностью до 1 знака после запятой"
        """
        ...


class FlashDisk:
    """
    Документация на класс.
    Класс описывает модель накопителя.
    """
    def __init__(self, capacity_memory: Union[int, float], free_memory: Union[int, float], service_life: int):
        """
            Инициализация экземпляра класса.

            :param capacity_memory: Объем памяти накопителя в Мб.
            :param free_memory: Свободный объем памяти в Мб.
            :param service_life: Гарантийный срок службы накопителя в месяцах.

            Пример:
            >>> flash_disk = FlashDisk(100, 100, 12) #инициализация экземпляра класса
        """
        if not isinstance(capacity_memory, (int, float)):
            raise TypeError("Объём памяти должен быть числом (тип int или float)")
        if not capacity_memory > 0:
            raise ValueError ("Объем памяти должен быть положительным числом")
        self.capacity_memory = capacity_memory

        if not isinstance(free_memory, (int, float)):
            raise TypeError("Свободный объём памяти должен быть числом (тип int или float)")
        if free_memory < 0:
            raise ValueError("Свободный объем памяти должен быть положительным числом или 0")
        if free_memory > capacity_memory:
            raise ValueError("Свободный объем памяти не может быть больше количества вопросов")
        self.free_memory = free_memory

        if not isinstance(service_life, int):
            raise TypeError("Гарантиный срок службы быть целым числом (тип int)")
        if not service_life > 0:
            raise ValueError ("Гарантиный срок службы должен быть положительным числом")
        self.service_life = service_life

    def add_file (self, add_file: Union[int, float]) -> None:
        """
        Запись на накопитель нового файла.

        :param add_file: Вес записываемого файла в Мб.

        :raise TypeError: Если вес файла имеет не тип int или float, вызываем ошибку.
        :raise ValueError: Если вес файла превышает свободный объём памяти, вызываем ошибку.
        """
        ...

    def how_many (self, file_veight: Union[int, float]) -> int:
        """
        Определяет сколько файлов заданного объёма можно записать на накопитель.

        :param file_veight: Вес записываемого файла в Мб.

        :return: Возвращает целое количество файлов, которые можно записать в свободную память на накопитель.

        :raise TypeError: Если вес файла имеет не тип int или float, вызываем ошибку.
        """
    ...


class Concrete:
    """
        Документация на класс.
        Класс описывает модель бетона.
    """
    def __init__(self, cement_strength: int, cement_water_proportion: float):
        """
        Инициализация экземпляра класса.

        :param cement_strength: Марка цемента по прочности.
        :param cement_water_proportion: Цементно-водное соотношение.

        Пример:
        >>> concrete = Concrete (300, 2.5) #инициализация экземпляра класса
        """
        if not isinstance(cement_strength, int):
            raise TypeError("Марка цемента должна быть целым числом (тип int)")
        if not cement_strength > 0:
            raise ValueError ("Марка цемента должна быть положительным числом")
        self.cement_strength = cement_strength

        if not isinstance(cement_water_proportion, float):
            raise TypeError("Цементно-водное соотношение должно быть вещественным числом (тип float)")
        if not cement_water_proportion > 0:
            raise ValueError ("Цементно-водное соотношение должно быть положительным числом")

    def stamp (self, aggregate_type: float) -> int:
        """
        Определение марки бетона по прочности.

        :param aggregate_type: Коэффициент, характеризующий количество и качество заполнителей.

        :return: Возвращает марку бетона по прочности.

        :raise TypeError: Если коэффициент заполнителя имеет не тип float, вызываем ошибку.
        """
        ...

    def strength_n (self, day_hardening: int) -> float:
        """
        Определение прочности бетона на данный день твердения.

        :param day_hardening: День твердения.

        :return: Возвращает прочность бетона.

        :raise TypeError: Если день твердения я имеет не тип int, вызываем ошибку.
        :raise ValueError: Если день твердения больше 28, вызываем ошибку.
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

