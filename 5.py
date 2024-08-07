class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    def get_average_grade(self):
        return self.average_grade

    def student_info(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}"

    def evaluate_performance(self):
        if self.average_grade > 8:
            return "Отлично"
        elif 6 <= self.average_grade <= 8:
            return "Хорошо"
        elif 4 <= self.average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    # Дополнительный метод: увеличение возраста студента на один год
    def increment_age(self):
        self.age += 1
        print(f"{self.name} теперь {self.age} лет.")

# Создание объектов класса "Студент"
student1 = Student("Иван Иванов", 20, 9.0)
student2 = Student("Мария Петрова", 19, 7.5)
student3 = Student("Алексей Сидоров", 21, 5.8)

# Вывод информации о студентах
print(student1.student_info())
print(student2.student_info())
print(student3.student_info())

# Оценка успехов студентов
print(f"{student1.get_name()} - Успехи: {student1.evaluate_performance()}")
print(f"{student2.get_name()} - Успехи: {student2.evaluate_performance()}")
print(f"{student3.get_name()} - Успехи: {student3.evaluate_performance()}")

# Изменение возраста студента
student1.increment_age()