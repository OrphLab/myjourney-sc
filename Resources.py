def extract_grade_data(data: dict, grade: int, jump:int = 0):
    grade_data = data.get("Grade", {}).get(grade+jump)
    if grade_data is not None:
        return grade_data
    else:
        return "Grade not found"
    
