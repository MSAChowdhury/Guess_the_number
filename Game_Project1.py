




import random
print("***********************\n*** PART 10: Simple Game ***\n*** --- CODEBREAKER --- ***\n** --Nope--Close--Match--  **\n**************************\n")
print("\nWelcome! Code Breakers. Here, you have to break the 3-digits code with your ready wit. Let's see can you break it ASAP\n\n")
print("1. The computer will think of 3 digit number that has no repeating digits.\n2. You will then guess a 3 digit number\n3. The computer will then give back clues, the possible clues are:\n\nClose: You've guessed a correct number but in the wrong position\n\nMatch: You've guessed a correct number in the correct position\n\nNope: You haven't guess any of the numbers correctly\n\n4. Based on these clues you will guess again until you break the code with a perfect match!")



def gen_code():
    digits = list(range(10))
    random.shuffle(digits)
    return (digits[3:6])

def number_check(com_code):
    guess = input("Make a guess: \n")
    user_code = list(map(int,str(guess))) #map(int,input) it changes the string input to int and puts into list
    if com_code == user_code:
        return "Congratulation! You have CRACKED it.."
    else:
        if(com_code[0] == user_code[0] or com_code[1] == user_code[1] or com_code[2] == user_code[2]):
            return "Match"
        elif (True):
            if(user_code[0] in com_code):
                return "Close"
            elif(user_code[1] in com_code):
                return "Close"
            elif (user_code[2] in com_code):
                return "Close"
        else:
            return "No match"
def res():
    result = ''
    com_code = gen_code()
    while(result != "Congratulation! You have CRACKED it.."):
        result = number_check(com_code)
        print(result)
    return result
res()
