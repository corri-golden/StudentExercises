class Cohort:

    def __init__(self):
        self.cohort_name = ""
        self.cohort_students = list()
        self.cohort_instructors = list()

    def add_student(self, name):
        self.cohort_students.append(name)
    def add_instructor(self, name):
        self.cohort_instructors.append(name)
