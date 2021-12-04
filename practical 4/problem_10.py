

while True:
    print("Enter 'x' for exit. ")
    
    print("Enter markas obtained in 5 subjects : ")
    
    mark1 = int(input())
    mark2 = int(input())
    mark3 = int(input())
    mark4 = int(input())
    mark5 = int(input())
    
    if mark1 == 'x':
        break
    else:
        sum = mark1 + mark2 + mark3 + mark4 + mark5
        
        average = sum / 5
        
        if(average >= 91 and average <= 100):
            print("your Grade is A+")
        
        elif(average >= 81 and average <= 90):
            print("your Grade is A")
            
        elif(average >= 71 and average <= 80):
            print("your Grade is A-")
            
        elif(average >= 61 and average <= 70):
            print("your Grade is B")
            
        elif(average >= 51 and average <= 60):
            print("your Grade is C+")
            
        elif(average >= 41 and average <= 50):
            print("your Grade is C")
            
        else:(average >= 0 and average <= 40)
        print("your Grade is F")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            