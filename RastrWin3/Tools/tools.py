# -*- coding: utf-8 -*-


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


if __name__ == "__main__":
    print(changing_number_of_semicolons(number=15315.00515, digits=5))
