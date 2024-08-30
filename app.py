from flask import Flask
from flask import render_template
from Employee import Employee
from resources.data.Data import IC_GRADE_DATA

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
    'niclas': Employee('Niclas', ' Nordsted', )

}

@app.route("/")
def root():
    return "Welcome! you found it!"

@app.route("/user/<username>")
def show_user_profile(username):
    employee  = employees.get(username.lower())
    grades = IC_GRADE_DATA["Grade"].items()
    if employee:
        return render_template("demo.html", employee=employee, grades=grades)
    else:
        return "User not found", 404


if __name__ == "__main__":
    app.run(debug=True)