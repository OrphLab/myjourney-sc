from flask import Flask
from flask import render_template
from Employee import Employee
from resources.data.Data import SKILLS_BY_BUSINESS_FUNCTION, IC_GRADE_DATA

app = Flask(__name__)

employees={
    'simon': Employee("Simon", "Kaczmarek", "Senior Talent Management Consultant"),
    'louise': Employee("Louise", "Tang-Jensen", "People Development Director"),
    'kogu': Employee("Kogulan", "Kugathasan", "Senior Talent Management Consultant"),
    'justyna': Employee("Justyna", "Kazimierczak", "Manager, Global People Service Delivery"),
    'alessia': Employee("Alessia","Valentina Neyjahr", "Talent Management Consultant" ),
    'johanna':Employee("Johanna"," Maria Sjögren", "Senior Talent Management Consultant" ),
    'jakub':Employee("Jakub","Pawełczak", "Recruitment Consultant" ),
    'niels':Employee('Niels', 'Vader', 'C&B Consultant'), 
    'niclas':Employee('Niclas', 'Nordsted', 'Senior Service Delivery Consultant'), 
}

@app.route("/")
def root():
    return "Welcome! you found it! again!!!!"

@app.route("/user/<username>")
def show_user_profile(username):
    employee  = employees.get(username.lower())
    grades = IC_GRADE_DATA["Grade"].items()
    
    def skills_output(skill_ids):
        print(f"Received skill IDs: {skill_ids}")
        print(skill_ids)
        result = []
        for skill_id in skill_ids:
            for category, skills in SKILLS_BY_BUSINESS_FUNCTION.items():
                if skill_id in skills:
                    result.append(skills[skill_id])
        return result

    if employee:
        return render_template("demo.html", employee=employee, grades=grades, skills_output=skills_output)
    else:
        return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)