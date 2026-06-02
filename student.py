class Student:
    def __init__(self, name):
        self.name = name        
        self.grades = []      

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if len(self.grades) == 0:   
            return 0               
        return sum(self.grades) / len(self.grades)   

    def is_passing(self):
        return self.average() >= 50   