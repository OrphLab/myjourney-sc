My Journey
This project is a simple web application that manages employee job profiles, tracks their grades, and displays relevant job-related information. The application is built using Python, Flask, and structured data to simulate a basic employee management system.

Table of Contents
Features
Installation
Usage
Project Structure
Contributing
License
Features
Employee Management: Create and manage employee profiles with first and last names and job profiles.
Job Profile Handling: Define and retrieve detailed information about job profiles, including business functions, grades, and required skills.
Grade Evaluation: Handle and display grade-related data for individual contributors (IC) and managers (M).
Web Interface: A simple web interface using Flask to display employee information and job grades.
Installation
Prerequisites
Python 3.x
Flask

Steps
Clone the repository:

bash
git clone https://github.com/yourusername/employee-job-profile.git
cd employee-job-profile

Install the required dependencies:
bash
pip install -r requirements.txt

Run the application:
bash
python app.py

Open your web browser and navigate to:
http://127.0.0.1:5000/user/<username>
Replace <username> with one of the predefined usernames (e.g., simon, louise, etc.).

Usage
The application provides a basic web interface to view an employee's full name, job profile, and available grades.
Navigate to http://127.0.0.1:5000/user/<username> to view an employee's profile.

Example Usage
To view the profile of Simon Kaczmarek:
http://127.0.0.1:5000/user/simon
This will display Simon's full name, job profile details, and corresponding grades.

Project Structure
The project is structured as follows:

GrowthPathLogics/
│
├── app.py                    # Main Flask application file
├── Employee.py               # Defines the Employee class
├── JobProfile.py             # Defines the JobProfile class and related methods
├── Grade.py                  # Handles grade-related data for IC and M tracks
├── resources/                
│   ├── data/
│   │   └── Data.py           # Contains the data structure for job profiles and grades
│   └── __init__.py           # Initializes the resources package
├── templates/
│   └── demo.html             # HTML template for rendering employee data
└── README.md                 # Project documentation

Key Modules
Employee.py: Defines the Employee class, which stores an employee's first name, last name, and job profile.
JobProfile.py: Contains the JobProfile class, responsible for retrieving and displaying job-related data such as business functions, grades, and skills.
Grade.py: Manages grade data for individual contributors (IC) and managers (M) using the ICGrade and MGrade classes.
app.py: The main Flask application file that handles routing and rendering employee profiles via a web interface.

help commands:
docker build -t myjourney-sc .
docker run -p 5000:8080 myjourney-sc
