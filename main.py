from re import L
from wordle import WORD as w
from bulk_word import do_everything as DE
import sys

# Check for empty files to see if we should keep going (later) so u dont
# need to always read things

#these are our getting methods

# This program gets us a valid Digit
def get_valid_digit():
    red = input("Input a digit: ")
    run = True
    if (red.isdigit()):
        if (0<= int(red) < 5):
            run = False
    while run:
        red = input("Enter a valid integer [0 to 4]: ")
        run = True
        if (red.isdigit()):
            if (0<= int(red) < 5):
                run = False

    return int(red)

# This method checks if we recieve a valid char from user
def get_valid_char():
    red = input("Enter a character (first input is what is accepted): ")
    while not red.isalpha():
        red = input("Enter a character (first input is what is accepted): ")
    return red[0]

def confirm():
    ans = input("Confirm? Y/N: ")
    if ans == "y" or ans =="Y":
        return True
    return False

def prompts():
    a = """\n1. Add correct lettr
2. Add wrong letter
3. Add wrong placement of letter
4. Add correct placement of letter
5. available words
6. quit"""
    print(a)

def main(): 
  

    name = w() #if you to have a custum .txt document then follow use the following format
    # 1. go to bulk_word.py
    # 2. uncomment main run file there
    # 3. set pen = to ur write file
    # 4. set paper = to ur read file that has all the words
    # 5. run the bulk_word.py as a main function
    # We do this in this way as it is very costly to keep writing when we already 
    # have the information

   

    # name.add_wrong("b")
    # name.add_wrong("r")
    # name.add_wrong("i")
   

    # name.add_con('a')
    # name.add_con('t')
    # name.add_con('o')
    # name.add_con('l')

    # name.add_wrong_placement('t',3)
    # name.add_wrong_placement('a',2)
    
    # name.add_cor_placement('o',2)
    # name.add_cor_placement('l',4)
    

    # name.updateLS()
    
    # name.get_fancy_ls()
    #name.add_contain("t",3 )
   

   # We give prompts of what the user wants to do
    prompts()
    red = input("input: ")
    while (red!= "6"):
        name.updateLS()
        
        if red == "1":
            a = get_valid_char()
            con = confirm()
            if (name.check_contain(a)) and con:
                name.add_con(a)
            else:
                print("Error!")

        elif red == "2":
            a= get_valid_char()
            con = confirm()
            if (name.check_wrong_letter(a) and con):
                name.add_wrong(a)
            else:
                print("Error!")

        elif red == "3":
            a = get_valid_char()
            b = get_valid_digit()
            con = confirm()
            if (name.check_wrong_placement(a,b) and con):
                name.add_wrong_placement(a,b)
            else:
                print("Error!")
            
        elif red == "4":
            a = get_valid_char()
            b = get_valid_digit()
            con = confirm()
            if (name.check_cor_placement(b,a) and con):
                name.add_cor_placement(a,b)
            else:
                print("Error")
        
        elif red == "5":
            name.get_fancy_ls()
        
        elif red == "6":
            sys.exit("Thank you for using this program!")
        else:
            print("Please enter a valid input!")
        #what we need for afterwards
        prompts()
        name.updateLS()
        red = input("input: ")
        

if __name__ == "__main__":
    main()