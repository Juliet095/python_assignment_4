#oop
#object oriented programming
#Syntax of OOP
#CREATING A CLASS
#cohort class
#class  Cohort:
    # name 
   # description
    #start_date
    #end_date
    #total_student

# within the cohort add a constructor for the cohort class
#add a method  to the class that prints the cohort name and the total number of students
#create a new instance of the cohort

class Cohort:
  def _init_(self, name, description,start_date,end_date):
      self.name=name
      self.description =description
      self.start_date =start_date
      self.end_date =end_date
cohort3 = Cohort("Julie", "computer science student","22/8/2024" ,"25/06/2026")
print(cohort3.name)
print(cohort3.description)
print(cohort3.start_date)
print(cohort3.end_date)

#b
class cohort:
   def _init_(self, cohort_name, total_number_of_student):
       self.cohort_name=cohort_name
       self.total_number_of_student= total_number_of_student
   def myfun(self):
      print("the cohort name is " + self.cohort_name +" total number of student is " + str(self.total_number_of_student))
d=cohort("cohortthree" ,5)       
d.myfun()  

#c
class Cohort_three:
  def _init_(self, name, description,start_date,end_date ):
      self.name=name
      self.description =description
      self.start_date =start_date
      self.end_date =end_date
    
cohort3 = Cohort("KEN", "student at witu","20/8/2025" ,"25/06/2027")
print(cohort3.name)
print(cohort3.description)
print(cohort3.start_date)
print(cohort3.end_date)

          
      
      

    