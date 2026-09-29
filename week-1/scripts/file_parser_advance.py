class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display_result(self):
        total = 0
        
        for mark in self.marks:
            total += mark
            
        average = total / len(self.marks)
        
        if average >= 40:
            result = "Pass"
        else:
            result = "Fail"
            
        print("Name:", self.name)
        print("Average:", average)
        print("Result:", result)
        print()
        
try:
    with open("week-1/scripts/students.txt", "r") as file:
        data = file.readlines()
    
    for line in data:
        line = line.strip()
        
        pieces = line.split(",")
        
        name = pieces[0]
        
        mark1= int(pieces[1])
        mark2= int(pieces[2])
        mark3= int(pieces[3])
        
        marks = [mark1, mark2, mark3]
        student = Student(name, marks)
        
        student.display_result()
        
except FileNotFoundError:
    print("File not found.")