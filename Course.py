# Allows the instantiation and manipulation of an object Course
class Course:
    # constructor used to create an instance of the Course class
    def __init__(self, courseName, section, professor, semester, year, gradeNeeded):
        self.courseName = courseName
        self.section = section
        self.professor = professor
        self.semester = semester
        self.year = year
        self.gradeNeeded = gradeNeeded

    # testing to make sure the attributes are working correctly
    def test(self):
        print("Course Title: " + self.courseName)
        print("Section: " + str(self.section))
        print("Professor: " + self.professor)
        print("Semester: " + self.semester)
        print("Year: " + str(self.year))
        print("Grade Needed: " + str(self.gradeNeeded) + "%")

stats = Course("CS 159", 5, "Weikle", "Spring", 2019, 93.0)
stats.test()

