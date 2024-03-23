class Student:
    def __init__(self, name, height):
        self.name = input("RENAT")
        self.height = input("179")
        print("init")
       
       
class ResultStudent:
    def __init__(self, surname, points, result):
        self.surname = input("PLEASE ENTER LAST NAME OF STUDENT: ")
        self.points = int(input("PLEASE ENTER SCORE: "))
        self.result = points > 80
        print("STUDENT", surname, "PASSED THE EXAM: ", result)
       
       
       
   
studen = Student()
print(studen.name, studen.height)
resultstud = ResultStudent()
print(resultstud.surname, resultstud.points, resultstud.result)