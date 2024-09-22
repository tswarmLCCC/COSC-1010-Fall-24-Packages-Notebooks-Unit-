import random

def number_guess(num): 
    rand_num = random.randint(1, 100)
    message = ""
    if num == rand_num:
        message = str(num) + ' is correct!'
    elif num < rand_num:
        message = str(num) +' is too low. Random number was ' + str(rand_num)
    else:
        message = str(num) +' is too high. Random number was '  + str(rand_num)
    return message

if __name__ == "__main__":
    # Use the seed 100 to get the same pseudo random numbers every time
    random.seed(100)
    
    user_input = "5"  #test user input

    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        
        num = int(token)
        my_message = number_guess(num)
        assert(my_message == "5 is too low. Random number was 19")
        print("All tests passed!")