#Create a cohort class with:
#name, description, start date, and date
#add a constructor for the cohort class
#create a function/ add a method to the class that prints the cohort name and the total number of students
#create a new instance/ object of the cohort class

#defining the class
class Cohort:
#_init_() function is the constructor always executed when the class is being inititated.
    def __init__(self, name, description, start_date, end_date, student_total_number):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.student_total_number = student_total_number
    def print_cohort_info(self):
        print(f"Cohort Name: {self.name}")
        print(F"Total number of studens: {self.student_total_number}")

cohort4 = Cohort(name="Python Language",
                 description="A computer language",
                 start_date= "20/08/2024",
                 end_date= "20/09/2025",
                 student_total_number= 55)
cohort4.print_cohort_info()
         

