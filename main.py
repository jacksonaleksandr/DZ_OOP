class Student:
    def __init__(self, name, surname, gender):
        self.medium_num = "Оценок нет"
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def medium_grade(self):
        i = 0
        summ = 0
        for values in self.grades.values():
            for value in values:
                i += 1
                summ += value
        if i != 0:
            self.medium_num = summ / i


    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Cравнение невозможно")
            return
        return self.medium_num < other.medium_num




    def __str__(self):
        self.medium_grade()
        res = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.medium_num}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses) if len(self.finished_courses) != 0 else "Отсутствуют"}"""
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.medium_num = 0

    def __str__(self):
        self.medium_grade()
        res = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {round(self.medium_num, 2)}"""
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}"""
        return res




some_student_1 = Student('Ruoy', 'Eman', 'male')
some_student_2 = Student('Angelina', 'Nejoli', 'female')
some_reviewer_1 = Reviewer('Ulyana', 'Nelenina')
some_reviewer_2 = Reviewer('Rozmarina', 'Albertovna')
some_lecturer_1 = Lecturer('Klavdia', 'Fufel')
some_lecturer_2 = Lecturer('Antonina', 'Neninovich')

some_student_1.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Python']
some_reviewer_1.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Python']
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_2.courses_in_progress += ['Git']
some_reviewer_1.courses_attached += ['Git']
some_reviewer_2.courses_attached += ['Git']

some_student_1.rate_hw(some_lecturer_1, 'Python', 3)
some_student_1.rate_hw(some_lecturer_2, 'Python', 8)
some_student_2.rate_hw(some_lecturer_1, 'Python', 5)
some_student_2.rate_hw(some_lecturer_2, 'Python', 6)


some_reviewer_1.rate_hw(some_student_1, 'Python', 6)
some_reviewer_1.rate_hw(some_student_2, 'Python', 5)
some_reviewer_2.rate_hw(some_student_1, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Python', 6)

some_reviewer_1.rate_hw(some_student_1, 'Git', 6)
# some_reviewer_1.rate_hw(some_student_2, 'Git', 6)
some_reviewer_2.rate_hw(some_student_1, 'Git', 7)
some_reviewer_2.rate_hw(some_student_2, 'Git', 7)

print(f"""{some_student_1}
{some_student_2}

{some_lecturer_1}
{some_lecturer_2}

{some_reviewer_1}
{some_reviewer_2}
""")

print(some_student_1 < some_student_2)
print(some_lecturer_1 < some_lecturer_2)



students = [some_student_1.grades, some_student_2.grades]
lecturers = [some_lecturer_1.grades, some_lecturer_2.grades]


def average_all_students(student_list, course_name):
    res = 0
    count = 0
    for student in student_list:
        for key, value in student.items():
            if key == course_name:
                count += len(value)
                res += sum(value)
    average = res / count
    print(f'Средняя оценка студентов по курсу {course_name}: {round(average, 2)}')
average_all_students(students, "Git")
average_all_students(students, "Python")

def average_all_lecturers(lecturers_list, course_name):
    res = 0
    count = 0
    for lecture in lecturers_list:
        for key, value in lecture.items():
            if key == course_name:
                count += len(value)
                res += sum(value)
    average = res / count
    print(f'Средняя оценка лекторов по курсу {course_name}: {round(average, 2)}')

average_all_lecturers(lecturers, "Python")


