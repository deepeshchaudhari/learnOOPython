from Employee import Employee

emp1 = Employee("Ratan","Tata",1200000)
emp2 = Employee("Mukesh","Ambani",200000)

if __name__ == '__main__':
    print(emp1 + emp2)
    print(emp1)
    print(emp2)
    emp1.email= "khanna.Mukesh@gmail.com"
    print(emp1.email)
    print(emp1)

    del emp1.email
    print(emp1)

