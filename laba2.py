def student_cabinet():
    users = {
        "Yaroslav Melnuchyk": {"password": "123", "grades": [10, 12, 4, 8, 3, 11, 5, 8]},
        "Stepan Martiniuk": {"password": "qwe", "grades": [12, 11, 9, 10, 12, 8]},
        "Vladislav Moshkevich": {"password": "777", "grades": [3, 4, 8, 5, 7, 4]},
        "Vladislav Kolinko": {"password": "pas", "grades":[5, 6, 10, 8, 9, 5]}
    }

    print("ЛАБОРАТОРНА РОБОТА №2: СИСТЕМА ОЦІНОК")

    while True:
        login = input("\nВведіть логін: ")
        password = input("Введіть пароль: ")

        if login in users:
            if users[login]["password"] == password:
                print(f"\n[ Успішний вхід! Вітаємо, {login.capitalize()} ]")

                student_grades = users[login]["grades"]
                break
            else:
                print("Неправильний пароль! Спробуйте ще раз.")
        else:
            print("Користувача з таким логіном не існує! Спробуйте ще раз.")


    print(f"Ваші оцінки: {student_grades}")

    satisfactory_count = 0
    unsatisfactory_count = 0

    for grade in student_grades:
        if 5 <= grade <= 12:
            satisfactory_count += 1
        elif 1 <= grade <= 4:
            unsatisfactory_count += 1

    print("\nСТАТИСТИКА УСПІШНОСТІ")
    print(f"Задовільних оцінок (від 5 до 12): {satisfactory_count}")
    print(f"Незадовільних оцінок (від 1 до 4): {unsatisfactory_count}")


student_cabinet()

