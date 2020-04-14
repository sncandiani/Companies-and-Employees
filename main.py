from employee import Employee
from company import Company

rabbit_rent = Company("Rabbit Rent", "1000 3rd st", "Real Estate")

farm_crew = Company("Farm Crew", "754 S Rural Rd", "Agriculture")

alyssa_clark = Employee("Alyssa Clark", "Rent Collector", "03 03 2020")
michael_nycum = Employee("Michael Nycum", "Rent Collector", "04 04 2020")
katie_constantine = Employee("Katie Constantine", "Farmer", "01 01 2018")
shahnaz_diaz = Employee("Shahnaz Diaz", "Goat Keeper", "12 24 2000")
kahimi_karie = Employee("Kahimi Karie", "Turtle Feeder", "10 17 2018")

rabbit_rent.add_employee(alyssa_clark.name)
rabbit_rent.add_employee(michael_nycum.name)

farm_crew.add_employee(katie_constantine.name)
farm_crew.add_employee(shahnaz_diaz.name)
farm_crew.add_employee(kahimi_karie.name)

print(f"{rabbit_rent.name} is in the {rabbit_rent.industry_type} industry and has the following employees: * {rabbit_rent.employees[0]}  * {rabbit_rent.employees[1]}")

print(f"{farm_crew.name} is in the {farm_crew.industry_type} industry and has the following employees: * {farm_crew.employees[0]}  * {farm_crew.employees[1]} * {farm_crew.employees[2]}")