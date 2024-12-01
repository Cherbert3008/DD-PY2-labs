# TODO Напишите функцию find_common_participants
def find_common_participants (first_group, second_group, separator = ","):
    # Преобразуем список подстрок с участниками в множество
    participants_first = set(first_group.split(separator))
    participants_second = set(second_group.split(separator))
    # Определяем общих участников
    intersection_group = participants_first.intersection(participants_second)
    # Преобразуем множество в список и сортируем по алфавиту
    list_inintersection_group = list(intersection_group)
    list_inintersection_group.sort()
    return list_inintersection_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group,"|"))

