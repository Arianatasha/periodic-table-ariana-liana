import random

def main():
    print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print ("Start an elements of the periodic table guessing")
    print("Guess the elements!") 
    print("Nitrogen")
    print("Hydrogen")
    print("Carbon")
    print("Oxygen")
    print("Iodine")
    print("Calcium")
    print("Titanium")
    print("Curium")
    print("Helium")
    print("Chlorine") 
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
    list = ["Nitrogen", "Hydrogen", "Carbon", "Oxygen", "Iodine", "Calcium", "Titanium", "Curium", "Helium", "Chlorine"]
    x = random.choice(list)
    guess = None
    
    while x != guess :
        
        guess = str(input("Guess the elements: "))
        
        if x ==guess:
            print("HANG HEBAT!")
        elif x !=guess:
            print("Try Again.")

main()             

    
