class Student:
    def __init__(self, name, roll_number, math_marks , english_marks, science_marks):
        self.name = name
        self.roll_number =  roll_number
        self.math_marks = math_marks
        self.english_marks = english_marks
        self.science_marks = science_marks
       
    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks in Math:", self.math_marks)
        print("Marks in English:", self.english_marks)
        print("Marks in Science:", self.science_marks)
    def update_marks(self, subject, new_marks):
        if subject == "math":
            self.math_marks = new_marks
        elif subject == "english":
            self.english_marks = new_marks
        elif subject == "science":
            self.science_marks = new_marks
        else:
            print("Invalid subject!")
    def calc_average(self):
        total_marks = self.math_marks + self.english_marks + self.science_marks
        average = total_marks / 3
        return average
    def grade(self):
        average = self.calc_average()
        if average >= 90:
            print("Grade: A")
        elif average >= 80:
            print("Grade: B")
        elif average >= 70:
            print("Grade:C")
        elif average >= 60:
            print("Grade: D")
        else:
            print("Fail")

s1 = Student("Ali", 101, 90, 80, 70)
s1.display()
s1.update_marks("math", 85)
s1.display()
s1.calc_average()
print("Average:", s1.calc_average())
s1.grade()

        

            
    
