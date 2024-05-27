def employees_who_met_the_target(hours: list, target: int) -> int:
    """
    Возвращает количество сотрудников, которые выполнили задание по
    времени работы
    """
    return len([i for i in hours if i >= target])


print(employees_who_met_the_target(hours=[0, 1, 2, 3, 4], target=2))
print(employees_who_met_the_target(hours=[5, 1, 4, 2, 2], target=6))