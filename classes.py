class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def get_average_grade(self, course):
        if course in self.grades:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            return 0

    def assign_grade(self, lecturer, grade):
        lecturer.set_grade(self.name, grade)

    def get_average_grade_for_homework(self):
        pass

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.courses_in_progress}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.grades = []

    def set_grade(self, student, grade):
        self.grades.append((student, grade))

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        total = 0
        count = 0

        for _, grade in self.grades:
            total += grade
            count += 1

        if count > 0:
            return total / count
        else:
            return 0

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.courses_attached}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
