import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    try:
       
        user_input = input("What was the parameter? ")
        
        if user_input == param:
            print("Good job!")
        else:
            print("Nope, sorry...")
    except EOFError:
        
        print("\nNope, sorry...")
