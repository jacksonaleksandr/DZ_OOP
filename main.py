class Student:
    def __init__(self, name, surname, gender):
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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.medium_num = 0

    def medium_grade_lecturer(self):
        i = 0
        summ = 0
        for values in self.grades.values():
            for value in values:
                i += 1
                summ += value
        self.medium_num = summ / i
        # return self.medium_num

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.medium_num}"""
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



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

best_student.rate_hw(some_lecturer, 'Python', 10)
best_student.rate_hw(some_lecturer, 'Python', 10)
best_student.rate_hw(some_lecturer, 'Python', 10)

print(some_lecturer)