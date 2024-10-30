class Hospital:
    def __init__(self) :
        pass
    
    def view_info():
        print('''"Name": "Green Valley Hospital",  
"Location": "123 Health St, Springfield, USA",  
"Established": 1985,  
"Type": "General Hospital ",  
"Bed Capacity": 250,''')
        print("-" * 20)



class Patient:
    def __init__(self, patient_id,name,age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def view_info(self):
        print(f"Name: {self.name}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Age: {self.age}")
        print(f"Condition: {self.condition}")
        print("-" * 20)  # Separator for readability
        

class Doctor:
    def __init__(self,doctor_id,name,age,specialization):
        self.name=name
        self.age=age
        self.doctor_id=doctor_id
        self.specialization=specialization
        
        
    def view_info(self):
        print(f"Name: {self.name}")
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Age: {self.age}")
        print(f"Specialization: {self.specialization}")
        print("-" * 20)  # Separator for readability    

class Department:
    def __init__(self,department):
        self.department=department
    
    def  view_info(self):
        print(f'The patient is in {self.department} department')
        print("-" * 20)
        
        
# Dictionary of doctors
doctors = {
    "D001": Doctor("D001", "Dr. Sarah Lee", 45, "Infectious Disease "),
    "D002": Doctor("D002", "Dr. Mark Johnson", 50, "General Medicine "),
    "D003": Doctor("D003", "Dr. Emily Carter", 38, "Endocrinology "),
    "D004": Doctor("D004", "Dr. James Wilson", 55, "Cardiology "),
    "D005": Doctor("D005", "Dr. Lisa Brown", 40, "Pulmonology "),
    "D006": Doctor("D006", "Dr. Robert Davis", 60, "Cardiology "),
    "D007": Doctor("D007", "Dr. Nancy White", 42, "Allergy & Immunolog"),
    "D008": Doctor("D008", "Dr. Thomas Martinez", 65, "Geriatrics "),
    "D009": Doctor("D009", "Dr. Laura Garcia", 37, "Neurology "),
    "D010": Doctor("D010", "Dr. Kevin Black", 70, "Neurology "),
}        

     
# Dictionary of patients
patients = {
    "P001": Patient("P001", "John Doe", 30, "Flu"),
    "P002": Patient("P002", "Jane Smith", 25, "Cold"),
    "P003": Patient("P003", "Alice Johnson", 40, "Diabetes"),
    "P004": Patient("P004", "Bob Brown", 50, "Hypertension"),
    "P005": Patient("P005", "Emily Davis", 35, "Asthma"),
    "P006": Patient("P006", "Michael Lee", 45, "Heart Disease"),
    "P007": Patient("P007", "Sarah Wilson", 28, "Allergies"),
    "P008": Patient("P008", "David Garcia", 60, "Osteoporosis"),
    "P009": Patient("P009", "Laura Martinez", 33, "Migraines"),
    "P010": Patient("P010", "Kevin Brown", 70, "Dementia"),
}


departments = {
    "P001": Department("Infectious Disease"),
    "P002": Department("General Medicine"),
    "P003": Department( "Endocrinology"),
    "P004": Department("Cardiology"),
    "P005": Department("Pulmonology"),
    "P006": Department("Cardiology"),
    "P007": Department("Allergy & Immunology"),
    "P008": Department("Geriatrics"),
    "P009": Department( "Neurology") ,
    "P010": Department( "Neurology") ,
}

if __name__ == "__main__":
 print('''                         
    ****WELCOME****  
   🌹🌹🌹🌹🌹🌹🌹🌹 
   ''')
print("-" * 20)   
while True:
        
        print('''
 #1-patient info
 #2-doctor info
 #3-department info
 #4- hospital info''')
        print("-" * 20)
        choice=int(input('enter your choice from 1 to 4: ---> '))
        if choice in [1,2,3,4]:
           if choice==1:
              patient_id = input("Please Enter your ID: ---> ").upper()
              patient = patients.get(patient_id)
              if patient:
                patient.view_info()
              else:
                print("Patient not found.")
         
           elif choice==2:
               doctor_id=input('Please enter Doctor id: ---> ').upper()
               doctor=doctors.get(doctor_id)
               if doctor:
                   doctor.view_info()
               else:
                 print("Doctor not found.")   
                 
                 
           elif choice==3:
                patient_id = input("Please Enter your ID: --->  ").upper()
                department = departments.get(patient_id)
                if department:
                    department.view_info()
                else:
                     print('Department not found')
                     
                     
           else:
                Hospital.view_info()    
        else:
             print('Please enter num from 1 to 4')
             
        question=input('Do you want more data?(yes or no) ---> ').lower()
        if question=='no':
            print("Thank you for using the Hospital UML app. We're here whenever you need us—take care!")
            break