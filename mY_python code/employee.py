class Employee():

    def __init__(self, name, surname, yearlySalary):
        self.name = name
        self.surname = surname
        self.yearlySalary = yearlySalary

    def give_raise(self, fix=5000):
        custom_raise = input("Enter your raise: ")
        if custom_raise == "fix":
            newSalary = self.yearlySalary + fix
        else:
            newSalary = self.yearlySalary + int(custom_raise)
        print(self.name + " " + self.surname + "'s new yearly salary will be " + str(newSalary))


