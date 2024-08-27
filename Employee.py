
from JobProfile import JobProfile
from typing import Tuple, Optional


class Employee:


    #Employee class, holds the employee
    # first name(fname), last name (str)
    # jobprofile which is a class, that holds information on job profile
    def __init__(self, fname:str, lname:str, jobprofile:str) -> None:
        self.jobprofile = JobProfile(jobprofile)
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return (f"Name: {self.fname} {self.lname}\n"
                f"{self.jobprofile}\n")
                
    