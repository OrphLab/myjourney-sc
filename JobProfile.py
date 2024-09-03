
from resources.data.Data import JOBFAMILY_DATA_NEW, SKILLS_BY_BUSINESS_FUNCTION
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
       self.skills_data = self.jpresult[5]
       #self.skills = self.skills_output(self.skills_data, SKILLS_BY_BUSINESS_FUNCTION)
       self.is_recruiting = self.jpresult[6]

       self.grade_data = ICGrade(self.grade) if self.track == "IC" else MGrade(self.grade)
       self.jobprofiles_in_business_function = self.get_other_job_profiles_same_business_functions_graded_oneup_sametrack(JOBFAMILY_DATA_NEW, jobprofile, self.grade, self.track)
       self.jobprofiles_in_subfamily = self.get_other_job_profiles_all_bizfunc_in_subfamily_graded_oneup_sametrack(JOBFAMILY_DATA_NEW, jobprofile,self.grade, self.track)
       

    def __repr__(self) -> str:
        return (f"Family group: {self.family_group}\n"
                f"Subfamily: {self.subfamily}\n"
                f"Business Function: {self.business_function}\n"
                f"JobProfile name: {self.jobprofile}\n"
                f"Track: {self.track}\n"
                f"Grade: {self.grade}\n"
                f"Other profiles in BF, grade: {self.jobprofiles_in_subfamily}")
                #f"Other JB: {self.jobprofiles_in_subfamily}")
                #syntaxt for key value -> f"\n{self.grade_data.grade_data_5["Titles"]}
    

                
    #returns jpbprofile information, based on jobprofile(str)
    def find_job_profile(self, data: dict, jpname: str):
        for family_group, subfamilies in data.items():
            for subfamily, subfamily_data in subfamilies.items():
                for business_function, job_profiles in subfamily_data.get("business_functions", {}).items():
                    for job_profile in job_profiles:
                        # job_profile is a dictionary with one key-value pair
                        if jpname in job_profile:
                            track, grade, skills, rec_status = job_profile[jpname]
                            return (
                                track,           # IC or M track
                                grade,           # Grade level
                                business_function, # Business function name
                                subfamily,       # Subfamily name
                                family_group,    # Family group name
                                skills,          # List of skills
                                rec_status       # True or False status
                            )
        return None
    
    #retruns only at same grade or 1+ above same track
    def get_other_job_profiles_same_business_functions_graded_oneup_sametrack(self, data: dict, jpname: str, usrgrade: int, jptrack: str):
        # Iterate over each family group
        for family_group, subfamilies in data.items():
            # Iterate over each subfamily
            for subfamily, subfamily_data in subfamilies.items():
                # Get the business functions for the current subfamily
                business_functions = subfamily_data.get("business_functions", {})
                
                # Iterate over each business function
                for business_function, job_profiles in business_functions.items():
                    # Check each job profile in the current business function
                    for job_profile in job_profiles:
                        # Check if the job profile contains the job name we're looking for
                        if jpname in job_profile:
                            # Retrieve the track and grade of the job profile we're looking for
                            jp_info = job_profile[jpname]
                            jp_track = jp_info[0]  # Track of the job profile we are looking for
                            jp_grade = jp_info[1]  # Grade of the job profile we are looking for

                            # Filter out the matched job profile and those with the same track and grade equal to or one above usrgrade
                            other_profiles = [
                                profile
                                for profile in job_profiles
                                if jpname not in profile and profile[next(iter(profile))][0] == jptrack and usrgrade <= profile[next(iter(profile))][1] <= usrgrade + 1
                            ]
                            return other_profiles
        # If no matching job profile is found, return None
        return None
    
    def get_other_job_profiles_all_bizfunc_in_subfamily_graded_oneup_sametrack(self, data: dict, jpname: str, jpgrade: int, jptrack: str):
        # Initialize an empty list to store the job profiles within the same subfamily
        results = []
        
        # Iterate over each family group
        for family_group, subfamilies in data.items():
            # Iterate over each subfamily
            for subfamily, subfamily_data in subfamilies.items():
                # Get the business functions for the current subfamily
                business_functions = subfamily_data.get("business_functions", {})
                
                # Iterate over each business function
                for business_function, job_profiles in business_functions.items():
                    # Check each job profile in the current business function
                    for job_profile in job_profiles:
                        # Check if the job profile contains the job name we're looking for
                        if jpname in job_profile:
                            # If jpname is found, collect all profiles in the same subfamily
                            for bf, profiles in business_functions.items():
                                for profile in profiles:
                                    profile_name = next(iter(profile))
                                    profile_info = profile[profile_name]

                                    # Check if the profile track is the same and grade is the same or one above jpgrade
                                    if profile_info[0] == jptrack and jpgrade <= profile_info[1] <= jpgrade + 1:
                                        results.append({
                                            "business_function": bf,
                                            "profile_name": profile_name,
                                            "track": profile_info[0],
                                            "grade": profile_info[1],
                                            "skills": profile_info[2],
                                            "recruiting_status": profile_info[3]
                                        })
                            return results  # Return after gathering all profiles in the subfamily
        
        # If no matching job profile is found, return an empty list
        return results

# region Other Functions

    # ######## same subfamily ######
    # def get_other_job_profiles_all_bizfunc_in_subfamily(self, data: dict, jpname: str):
    #     # Initialize an empty list to store the job profiles within the same subfamily
    #     results = []
        
    #     # Iterate over each family group
    #     for family_group, subfamilies in data.items():
    #         # Iterate over each subfamily
    #         for subfamily, subfamily_data in subfamilies.items():
    #             # Get the business functions for the current subfamily
    #             business_functions = subfamily_data.get("business_functions", {})
                
    #             # Iterate over each business function
    #             for business_function, job_profiles in business_functions.items():
    #                 # Check each job profile in the current business function
    #                 for job_profile in job_profiles:
    #                     # Check if the job profile contains the job name we're looking for
    #                     if jpname in job_profile:
    #                         # If jpname is found, collect all profiles in the same subfamily
    #                         for bf, profiles in business_functions.items():
    #                             for profile in profiles:
    #                                 profile_name = next(iter(profile))
    #                                 profile_info = profile[profile_name]
    #                                 results.append({
    #                                     "business_function": bf,
    #                                     "profile_name": profile_name,
    #                                     "track": profile_info[0],
    #                                     "grade": profile_info[1],
    #                                     "skills": profile_info[2],
    #                                     "recruiting_status": profile_info[3]
    #                                 })
    #                         return results  # Return after gathering all profiles in the subfamily
    #     # If no matching job profile is found, return None
    #     return None
    
    # def get_other_job_profiles_all_bizfunc_in_subfamily_graded(self, data: dict, jpname: str, jpgrade: int):
    #     # Initialize an empty list to store the job profiles within the same subfamily
    #     results = []
        
    #     # Iterate over each family group
    #     for family_group, subfamilies in data.items():
    #         # Iterate over each subfamily
    #         for subfamily, subfamily_data in subfamilies.items():
    #             # Get the business functions for the current subfamily
    #             business_functions = subfamily_data.get("business_functions", {})
                
    #             # Iterate over each business function
    #             for business_function, job_profiles in business_functions.items():
    #                 # Check each job profile in the current business function
    #                 for job_profile in job_profiles:
    #                     # Check if the job profile contains the job name we're looking for
    #                     if jpname in job_profile:
    #                         # If jpname is found, collect all profiles in the same subfamily
    #                         for bf, profiles in business_functions.items():
    #                             for profile in profiles:
    #                                 profile_name = next(iter(profile))
    #                                 profile_info = profile[profile_name]

    #                                 # Filter by jpgrade or above
    #                                 if profile_info[1] >= jpgrade:
    #                                     results.append({
    #                                         "business_function": bf,
    #                                         "profile_name": profile_name,
    #                                         "track": profile_info[0],
    #                                         "grade": profile_info[1],
    #                                         "skills": profile_info[2],
    #                                         "recruiting_status": profile_info[3]
    #                                     })
    #                         return results  # Return after gathering all profiles in the subfamily
        
    #     # If no matching job profile is found, return None
    #     return None

    # def get_other_job_profiles_all_bizfunc_in_subfamily_graded_oneup(self, data: dict, jpname: str, jpgrade: int):
    #     # Initialize an empty list to store the job profiles within the same subfamily
    #     results = []
        
    #     # Iterate over each family group
    #     for family_group, subfamilies in data.items():
    #         # Iterate over each subfamily
    #         for subfamily, subfamily_data in subfamilies.items():
    #             # Get the business functions for the current subfamily
    #             business_functions = subfamily_data.get("business_functions", {})
                
    #             # Iterate over each business function
    #             for business_function, job_profiles in business_functions.items():
    #                 # Check each job profile in the current business function
    #                 for job_profile in job_profiles:
    #                     # Check if the job profile contains the job name we're looking for
    #                     if jpname in job_profile:
    #                         # If jpname is found, collect all profiles in the same subfamily
    #                         for bf, profiles in business_functions.items():
    #                             for profile in profiles:
    #                                 profile_name = next(iter(profile))
    #                                 profile_info = profile[profile_name]

    #                                 # Check if the profile grade is the same or one above jpgrade
    #                                 if profile_info[1] >= jpgrade and profile_info[1] <= jpgrade + 1:
    #                                     results.append({
    #                                         "business_function": bf,
    #                                         "profile_name": profile_name,
    #                                         "track": profile_info[0],
    #                                         "grade": profile_info[1],
    #                                         "skills": profile_info[2],
    #                                         "recruiting_status": profile_info[3]
    #                                     })
    #                         return results  # Return after gathering all profiles in the subfamily
        
    #     # If no matching job profile is found, return an empty list
        return results

    

# ######## same Business Function ######
#     #retruns only at same grade or above
#     def get_other_job_profiles_same_business_functions_graded(self, data: dict, jpname: str, usrgrade: int):
#         # Iterate over each family group
#         for family_group, subfamilies in data.items():
#             # Iterate over each subfamily
#             for subfamily, subfamily_data in subfamilies.items():
#                 # Get the business functions for the current subfamily
#                 business_functions = subfamily_data.get("business_functions", {})
                
#                 # Iterate over each business function
#                 for business_function, job_profiles in business_functions.items():
#                     # Check each job profile in the current business function
#                     for job_profile in job_profiles:
#                         # Check if the job profile contains the job name we're looking for
#                         if jpname in job_profile:
#                             # Filter out the matched job profile and those below usrgrade
#                             other_profiles = [
#                                 profile
#                                 for profile in job_profiles
#                                 if jpname not in profile and profile[next(iter(profile))][1] >= usrgrade
#                             ]
#                             return other_profiles
#         # If no matching job profile is found, return None
#         return None

    # #retruns only at same grade or 1+ above
    # def get_other_job_profiles_same_business_functions_graded_oneup(self, data: dict, jpname: str, usrgrade: int):
    # # Iterate over each family group
    #     for family_group, subfamilies in data.items():
    #         # Iterate over each subfamily
    #         for subfamily, subfamily_data in subfamilies.items():
    #             # Get the business functions for the current subfamily
    #             business_functions = subfamily_data.get("business_functions", {})
                
    #             # Iterate over each business function
    #             for business_function, job_profiles in business_functions.items():
    #                 # Check each job profile in the current business function
    #                 for job_profile in job_profiles:
    #                     # Check if the job profile contains the job name we're looking for
    #                     if jpname in job_profile:
    #                         # Filter out the matched job profile and those at the same grade or one above usrgrade
    #                         other_profiles = [
    #                             profile
    #                             for profile in job_profiles
    #                             if jpname not in profile and usrgrade <= profile[next(iter(profile))][1] <= usrgrade + 1
    #                         ]
    #                         return other_profiles
    #     # If no matching job profile is found, return None
    #     return None
   
#endregion
