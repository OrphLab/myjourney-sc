#Individual contributor path
from Resources import extract_grade_data
from Data import M_GRADE_DATA, IC_GRADE_DATA
class ICGrade:
    def __init__(self, grade):
        if grade not in IC_GRADE_DATA["Grade"]:
            raise ValueError("Invalid grade rank. It must be between 1 and 10.")
        self.grade = grade
        self.grade_data = extract_grade_data(IC_GRADE_DATA, self.grade)
        self.grade_data_3 = extract_grade_data(IC_GRADE_DATA,self.grade, 1)
        self.grade_data_5 = extract_grade_data(IC_GRADE_DATA,self.grade, 2)
    
    def __str__(self):
        # Initialize an empty string to accumulate the output
        output = ""
        for key, value in self.grade_data.items():
            output += f"{key}: {value}\n"
        return output.strip()  # Remove the trailing newline for clean output
    
    def print_grade_data(self, data):
        output =""
        for key, value in data.items():
            output += f"{key}; {value}\n"
        return output.strip()
    
#Manager path
class MGrade():
    def __init__(self, grade):
        if grade not in M_GRADE_DATA["Grade"]:
            raise ValueError("Invalid grade rank. It must be between 5 and 13.")
        self.grade = grade
        self.grade_data = extract_grade_data(M_GRADE_DATA, self.grade)
        self.grade_data_3 = extract_grade_data(M_GRADE_DATA, self.grade,1)
        self.grade_data_5 = extract_grade_data(M_GRADE_DATA, self.grade,2)

    def __str__(self):
        # Initialize an empty string to accumulate the output
        output = ""
        for key, value in self.grade_data.items():
            output += f"{key}: {value}\n"
        return output.strip()  # Remove the trailing newline for clean output
    
    def print_grade_data(self, data):
        output =""
        for key, value in data.items():
            output += f"{key}; {value}\n"
        return output.strip()
    
