def circle_area(r: int) -> float:
    """Подсчитывает площадь круга от заданного радиуса."""
    pi = 3.14
    circle_area = pi * r**2
    return circle_area


def format_description(r, area):
    """Определяет формат вывода сообщения о радиусе и площади круга."""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: int):
    """Ввывод информации о площади круга по радиусу по заданному формату."""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
