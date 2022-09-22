class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_n = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_n += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_n
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, estimation):
        if not isinstance(estimation, Student):
            print('Невозможно сравнить')
            return
        return self.average_rating < estimation.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        grades_n = 0
        for k in self.grades:
            grades_n += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_n
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, estimation):
        if not isinstance(estimation, Lecturer):
            print('Невозможно сравнить')
            return
        return self.average_rating < estimation.average_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


# Класс студенты
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Ivan', 'Ivanov', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Введение в программирование']

best_student_3 = Student('Petr', 'Petrov', 'your_gender')
best_student_3.courses_in_progress += ['Git']
best_student_3.finished_courses += ['Введение в программирование']

best_student_4 = Student('Egor', 'Egorov','your_gender')
best_student_4.courses_in_progress += ['Git']
best_student_4.finished_courses += ['Введение в программирование']

# Класс лекторы
best_lecturer_1 = Lecturer('Maxim', 'Maximov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Maxim', 'Alexeev')
best_lecturer_2.courses_attached += ['Python']

best_lecturer_3 = Lecturer('Alexei', 'Alexeev')
best_lecturer_3.courses_attached += ['Git']

best_lecturer_4 = Lecturer('Alexei', 'Maximov')
best_lecturer_4.courses_attached += ['Git']

# Класс проверяющие
cool_reviewer_1 = Reviewer('Vladimir', 'Vladimirov')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Viktor', 'Viktorov')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']

# Оценки студентам от проверяющих
cool_reviewer_1.rate_hw(best_student_1, 'Python', 5)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 6)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 7)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 9)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 10)

cool_reviewer_1.rate_hw(best_student_3, 'Git', 9)
cool_reviewer_1.rate_hw(best_student_3, 'Git', 8)
cool_reviewer_1.rate_hw(best_student_3, 'Git', 7)

cool_reviewer_2.rate_hw(best_student_4, 'Git', 6)
cool_reviewer_2.rate_hw(best_student_4, 'Git', 5)
cool_reviewer_2.rate_hw(best_student_4, 'Git', 4)

# Оценки лекторам от студентов
best_student_1.rate_lecturer(best_lecturer_1, 'Python', 10)
best_student_1.rate_lecturer(best_lecturer_1, 'Python', 9)
best_student_1.rate_lecturer(best_lecturer_1, 'Python', 8)

best_student_1.rate_lecturer(best_lecturer_2, 'Python', 10)
best_student_1.rate_lecturer(best_lecturer_2, 'Python', 9)
best_student_1.rate_lecturer(best_lecturer_2, 'Python', 8)

best_student_2.rate_lecturer(best_lecturer_1, 'Python', 5)
best_student_2.rate_lecturer(best_lecturer_1, 'Python', 6)
best_student_2.rate_lecturer(best_lecturer_1, 'Python', 7)

best_student_2.rate_lecturer(best_lecturer_2, 'Python', 7)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 8)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 9)

best_student_3.rate_lecturer(best_lecturer_3, 'Git', 6)
best_student_3.rate_lecturer(best_lecturer_3, 'Git', 7)
best_student_3.rate_lecturer(best_lecturer_3, 'Git', 8)

best_student_3.rate_lecturer(best_lecturer_4, 'Git', 9)
best_student_3.rate_lecturer(best_lecturer_4, 'Git', 9)
best_student_3.rate_lecturer(best_lecturer_4, 'Git', 10)

best_student_4.rate_lecturer(best_lecturer_3, 'Git', 8)
best_student_4.rate_lecturer(best_lecturer_3, 'Git', 7)
best_student_4.rate_lecturer(best_lecturer_3, 'Git', 9)

best_student_4.rate_lecturer(best_lecturer_4, 'Git', 9)
best_student_4.rate_lecturer(best_lecturer_4, 'Git', 8)
best_student_4.rate_lecturer(best_lecturer_4, 'Git', 9)

# Информация о проверяющих
print(f'Список проверяющих:\n\n'
      f'{cool_reviewer_1}\n\n'
      f'{cool_reviewer_2}\n\n')

# Информация о лекторах
print(f'Список лекторов:\n\n'
      f'{best_lecturer_1}\n\n'
      f'{best_lecturer_2}\n\n'
      f'{best_lecturer_3}\n\n'
      f'{best_lecturer_4}\n\n')

# Информация о студентах
print(f'Список студентов:\n\n'
      f'{best_student_1}\n\n'
      f'{best_student_2}\n\n'
      f'{best_student_3}\n\n'
      f'{best_student_4}\n\n')

# Cравнение студентов по средним оценкам за домашние задания
print(f'{best_student_1.name} {best_student_1.surname} > {best_student_2.name} {best_student_2.surname} = {best_student_1 > best_student_2}')
print(f'{best_student_1.name} {best_student_1.surname} > {best_student_3.name} {best_student_3.surname} = {best_student_1 > best_student_3}')
print(f'{best_student_1.name} {best_student_1.surname} > {best_student_4.name} {best_student_4.surname} = {best_student_1 > best_student_4}')
print(f'{best_student_2.name} {best_student_2.surname} > {best_student_3.name} {best_student_3.surname} = {best_student_2 > best_student_3}')
print(f'{best_student_2.name} {best_student_2.surname} > {best_student_4.name} {best_student_4.surname} = {best_student_2 > best_student_4}')
print(f'{best_student_3.name} {best_student_3.surname} > {best_student_4.name} {best_student_4.surname} = {best_student_3 > best_student_4}')
print()
#Cравнение лекторов по средним оценкам за лекции
print(f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 < best_lecturer_2}')
print()

# Средняя оценка
#Список студентов
student_list = [best_student_1, best_student_2,best_student_3, best_student_4]

#Список лекторов
lecturer_list_1 = [best_lecturer_1, best_lecturer_2]
lecturer_list_2 = [best_lecturer_3, best_lecturer_4]

def student_rate(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
       if student.courses_in_progress == [course_name]:
            sum_all += student.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rate(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course_name]:
            sum_all += lecturer.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rate(student_list, 'Python')}")
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rate(student_list, 'Git')}")
print()
print(f"Средняя оценка для лекторов по курсу {'Python'}: {lecturer_rate(lecturer_list_1, 'Python')}")
print(f"Средняя оценка для лекторов по курсу {'Git'}: {lecturer_rate(lecturer_list_2, 'Git')}")
print()