from JobProfile import JobProfile

class Employee:
    def __init__(self, fname:str, lname:str, jobprofile:str) -> None:
        self.jobprofile = JobProfile(jobprofile)
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return (f"Name: {self.fname} {self.lname}\n"
                f"{self.jobprofile}\n")
    
    def full_name(self):
        return (f"{self.fname} {self.lname}\n")
        
    
    def job_profile(self):
        pass
