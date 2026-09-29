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
   
        average = (mark1+mark2+mark3)/3

        if average >= 40:
            result = "Pass"
        else:
            result = "Fail"
            
        print("Name: ", name)
        print("Average: ", average)
        print("Result: ",result)
        print()
        
except FileNotFoundError:
    print("File not found.")