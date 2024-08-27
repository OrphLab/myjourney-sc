from typing import Any
from Data import JOBFAMILY_DATA_NEW
from Grade import ICGrade, MGrade

class JobProfile:
    def __init__(self, jobprofile:str) -> None:
       self.jobprofile = jobprofile
       self.jpresult = self.find_job_profile(JOBFAMILY_DATA_NEW,jobprofile)
       self.business_function = self.jpresult[2]
       self.subfamily = self.jpresult[3]
       self.family_group = self.jpresult[4]
       self.track = self.jpresult[0]
       self.grade = self.jpresult[1]

       self.grade_data = ICGrade(self.grade) if self.track == "IC" else MGrade(self.grade)

    def __repr__(self) -> str:
        return (f"Family group: {self.family_group}\n"
                f"Subfamily: {self.subfamily}\n"
                f"Business Function: {self.business_function}\n"
                f"JobProfile name: {self.jobprofile}\n"
                f"Track: {self.track}\n"
                f"Grade: {self.grade}\n"
                f"\nCurrent Grade data:\n{self.grade_data}\n\n"
                f"1-3 years Vector:\n"
                f"Grade data:\n{self.grade_data.print_grade_data(self.grade_data.grade_data_3)}\n\n"
                f"3-5 years Vector:\n"
                f"Grade data:\n{self.grade_data.print_grade_data(self.grade_data.grade_data_5)}\n")
                #syntaxt for key value -> f"\n{self.grade_data.grade_data_5["Titles"]}
    
    def find_job_profile(self, data: dict, jpname: str):
        for family_group, subfamilies in data.items():
            for subfamily, subfamily_data in subfamilies.items():
                for business_function, job_profiles in subfamily_data.get("business_functions", {}).items():
                    for job_profile in job_profiles:
                        # job_profile is a dictionary with one key-value pair
                        if jpname in job_profile:
                            track, grade = job_profile[jpname]
                            return (
                                track,
                                grade,
                                business_function,
                                subfamily,
                                family_group
                            )
        return None

