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
Employee Management: Create and manage employee profiles with names and job profiles.
Job Profile Handling: Define and retrieve detailed job profile information like business functions, grades, and skills.
Grade Evaluation: Handle and display grade data for individual contributors (IC) and managers (M).
Web Interface: Simple Flask web interface to display employee information and job grades.

Installation
Prerequisites
Python 3.x
Flask
Docker (for production deployment)

Steps
Clone the repository:
git clone https://github.com/yourusername/employee-job-profile.git
cd employee-job-profile

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open your web browser and navigate to:
arduino
http://127.0.0.1:5000/user/
Replace with one of the predefined usernames (e.g., simon, louise).

Docker Setup
You can also run the application in a Docker container.

Build the Docker image:
docker build -t myjourney-sc .

Run the container:
docker run -p 5000:8080 myjourney-sc
The application will be available at http://localhost:5000.

Project Structure
GrowthPathLogics/
│
├── app.py                  # Main Flask application file
├── Employee.py             # Defines the Employee class
├── JobProfile.py           # JobProfile class for job-related data
├── Grade.py                # Handles IC and M track grade data
├── resources/
│   ├── data/
│   │   └── Data.py         # Data structure for job profiles and grades
│   └── __init__.py         # Initializes resources package
├── templates/
│   └── demo.html           # HTML template for rendering employee data
└── README.md               # Project documentation

Key Docker Commands
Build the image:
docker build -t myjourney-sc .

Run the container:
docker run -p 5000:8080 myjourney-sc
