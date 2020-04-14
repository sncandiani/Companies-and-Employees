class Company: 
    def __init__(self, name, address, industry_type):
        self.name = name 
        self.address = address
        self.industry_type = industry_type
        self.employees = []
    def add_employee(self, employeeInfo):
        self.employees.append(employeeInfo)