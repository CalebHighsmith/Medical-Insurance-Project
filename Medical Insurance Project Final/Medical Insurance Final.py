#Author: Caleb Highsmith
#Date: 2-9-2021

#Scope
# 1: Find average age for people in dataset.
# 2: Narrow down what region the people in the dataset are from. 
# 3: Count the number of males and females.
# 4: Calculate the average insurance charges. 
# 5: Make a function that creates a dictionary for the data.

import csv
#Initialize the columns of data into list for organization.
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

#Function to return the list of data in ordered columns as requested from insurance.csv
def load_list(lst, csv_file, column_name):
    with open(csv_file) as csv_data:
        csv_dict = csv.DictReader(csv_data)
        for row in csv_dict:
            lst.append(row[column_name])
    return lst

load_list(ages, 'insurance.csv', 'age')
load_list(sex, 'insurance.csv', 'sex')
load_list(bmi, 'insurance.csv', 'bmi')
load_list(children, 'insurance.csv', 'children')
load_list(smoker, 'insurance.csv', 'smoker')
load_list(region, 'insurance.csv', 'region')
load_list(charges, 'insurance.csv', 'charges')

#Class to analyze patient info
class Patient:

    def __init__(self, patient_age, patient_sex, patient_bmi, patient_children, patient_smoker, patient_region, patient_charges):
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_bmi = patient_bmi
        self.patient_children = patient_children
        self.patient_smoker = patient_smoker
        self.patient_region = patient_region
        self.patient_charges = patient_charges
    #Analyze average age
    def average_age(self):
        total = 0
        for age in self.patient_age:
            total += int(age)   
        return ("Average Patient Age: " + str(round(total/len(self.patient_age), 2)) + " years")
    #Counts the number of males and females there are in insurance.csv
    def count_sex(self):
        males = 0
        females = 0
        for sex in self.patient_sex:
            if sex == 'male':
                males += 1
            if sex == 'female':
                females += 1
        print("The number of males are:", males)
        print('The number of females are:', females)
     #Calculates the average insurance charge.
    def calculate_average_charge(self):
        total = 0
        for charge in self.patient_charges:
            total += float(charge)
        average = total / len(self.patient_charges)
        return print('The average charge is:', average)
        #Analyzes the regions of the people in the data report and narrows them down.
    def analyze_region(self):
        list_of_regions = []
        for regions in self.patient_region:
            if regions not in list_of_regions:
                list_of_regions.append(regions)
        return print('The regions included in the data report are:', list_of_regions)
        #Neatly organizes the data into a dictionary.
    def create_dictionary(self):
        self.patient_dictionary = {}
        self.patient_dictionary['Age'] = [int(age) for age in self.patient_age]
        self.patient_dictionary['Sex'] = self.patient_sex
        self.patient_dictionary['BMI'] = self.patient_bmi
        self.patient_dictionary['Children'] = self.patient_children
        self.patient_dictionary['Smoker'] = self.patient_smoker
        self.patient_dictionary['Region'] = self.patient_region
        self.patient_dictionary['Insurance Charges'] = self.patient_charges
        return print(self.patient_dictionary)

patient_data = Patient(ages, sex, bmi, children, smoker, region, charges)
print(patient_data.average_age())
print(patient_data.count_sex())
patient_data.calculate_average_charge()
patient_data.analyze_region()
patient_data.create_dictionary()
