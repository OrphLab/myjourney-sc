from Grade import ICGrade, MGrade
from Employee import Employee

class ICJobProfile():
    def __init__(self, fname, lname, subfamily, grade) -> None:
        self.fname =fname
        self.lname = lname
        self.subfamily = Employee(subfamily)
        self.grade = ICGrade(grade)

    def __str__(self) -> str:
        return f"{self.lname}, {self.fname} \nCurrent station at SimCorp:\n{self.subfamily} \n{self.grade}" #, {self.grade.GRADE_DATA[self.grade]}
    
class MJobProfile():
    def __init__(self, fname, lname, subfamily, grade) -> None:
        self.fname =fname
        self.lname = lname
        self.subfamily = Employee(subfamily)
        self.grade = MGrade(grade)

    def __str__(self) -> str:
        return f"{self.lname}, {self.fname} \nCurrent station at SimCorp:\n{self.subfamily} \n{self.grade}" #, {self.grade.GRADE_DATA[self.grade]}