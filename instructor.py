class Instructor:


    def __init__(self, first_name, last_name, slack_handle, instructor_cohort, instructor_specialty):
        self.first_name = ""
        self.last_name = ""
        self.slack_handle = ""
        self.instructor_cohort = ""
        self.instructor_specialty = ""
        self.students = list()

    def add_students(self, student):
        self.students.append(student)

    def assign_student_exercise(self, student, exercise):
        student.exercises.append(exercise)