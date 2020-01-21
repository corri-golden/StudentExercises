from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

# Create 4, or more, exercises.
chicken_monkey = Exercise()
chicken_monkey.exercise_name = "Chicken Monkey"
chicken_monkey.exercise_language = "Python"


pizza_joint = Exercise()
pizza_joint.name = "Pizza Joint"
pizza_joint.exercise_language = "Python"

planner = Exercise()
planner.name = "Planner"
planner.exercise_language = "Python"

english_idioms = Exercise()
english_idioms.name = "English Idioms"
english_idioms.exercise_language = "Python"

multiple_inheritances = Exercise()
multiple_inheritances.name = "Multiple Inheritances"
multiple_inheritances.exercise_language = "Python"


# Create 3, or more, cohorts.

cohort_35 = Cohort()
cohort_35.name = "Cohort 35"
cohort_35.cohort_students = list()
cohort_35.cohort_teachers = list()

cohort_36 = Cohort()
cohort_36.name = "Cohort 36"
cohort_36.cohort_students = list()
cohort_36.cohort_teachers = list()

cohort_37 = Cohort()
cohort_37.name = "Cohort 37"
cohort_37.cohort_students = list()
cohort_37.cohort_teachers = list()

# Create 4, or more, students and assign them to one of the cohorts.

bill = Student("Bill", "Smith", "billSmith", "36" )
bill.first_name = "Bill"
bill.last_name = "Smith"
bill.slack_handle = "billSmith"
bill.student_cohort = "36"
cohort_36.add_student(bill)

manila = Student("Manila", "Bui", "manilaBui", "35")
manila.first_name = "Manila"
manila.last_name = "Bui"
manila.slack_handle = "manilaBui"
manila.student_cohort = "35"
cohort_35.add_student(manila)

chase = Student("Chase", "Fite", "chaseFite", "35")
chase.first_name = "Chase"
chase.last_name = "Fite"
chase.slack_handle = "chaseFite"
chase.student_cohort = "35"
cohort_36.add_student(chase)

chriss = Student("Chriss", "Smith", "chrissPippen", "37")
chriss.first_name = "Chriss"
chriss.last_name = "Smith"
chriss.slack_handle = "chrissPippen"
chriss.student_cohort = "37"
cohort_36.add_student(chriss)

# Create 3, or more, instructors and assign them to one of the cohorts.
jisie = Instructor("Jisie", "Jones", "jisieJones", "36", "pushups")
jisie.first_name = "Jisie"
jisie.last_name = "Jones"
jisie.slack_handle = "jisieJones"
jisie.instructor_cohort = "35"
jisie.instructor_specialty = "pushups"
jisie.students = list()
cohort_36.add_student(jisie)

rose = Instructor("Rose", "Ramen", "roseRamens", "35", "thumps")
rose.first_name = "Rose"
rose.last_name = "Ramen"
rose.slack_handle = "roseRamens"
rose.instructor_cohort = "37"
rose.instructor_specialty = "thumps"
rose.students = list()
cohort_35.add_student(rose)

joe = Instructor("Joe", "Jackson", "joeJackson", "37", "frisbee")
joe.first_name = "Joe"
joe.last_name = "Jackson"
joe.slack_handle = "joeJackson"
joe.instructor_cohort = "35"
joe.instructor_specialty = "frisbee"
joe.students = list()
cohort_37.add_student(joe)

# Have each instructor assign 2 exercises to each of the students.
rose.assign_student_exercise(bill, pizza_joint)
rose.assign_student_exercise(bill, planner)
rose.assign_student_exercise(manila, pizza_joint)
rose.assign_student_exercise(manila, planner)
rose.assign_student_exercise(chase, pizza_joint)
rose.assign_student_exercise(chase, planner)
rose.assign_student_exercise(chriss, pizza_joint)
rose.assign_student_exercise(chriss, planner)



jisie.assign_student_exercise(bill, chicken_monkey)
jisie.assign_student_exercise(bill, planner)
jisie.assign_student_exercise(manila, chicken_monkey)
jisie.assign_student_exercise(manila, planner)
jisie.assign_student_exercise(chase, chicken_monkey)
jisie.assign_student_exercise(chase, planner)
jisie.assign_student_exercise(chriss, chicken_monkey)
jisie.assign_student_exercise(chriss, planner)

joe.assign_student_exercise(bill, pizza_joint)
joe.assign_student_exercise(bill, english_idioms)
joe.assign_student_exercise(manila, pizza_joint)
joe.assign_student_exercise(manila, english_idioms)
joe.assign_student_exercise(chase, pizza_joint)
joe.assign_student_exercise(chase, english_idioms)
joe.assign_student_exercise(chriss, pizza_joint)
joe.assign_student_exercise(chriss, english_idioms)

