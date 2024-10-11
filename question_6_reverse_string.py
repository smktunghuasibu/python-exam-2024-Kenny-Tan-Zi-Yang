# This program is used to reverse a string.

def string_reverse(str1):
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = len(str1) - 1
    
    # Execute a while loop 
    while index >= 0:  # Corrected condition to include the first character
        # Concatenate the character of 'str1' to 'rstr1'
        rstr1 += str1[index]  # Corrected operator and indexing
        
        # Decrement the 'index' by 1 for the next iteration
        index -= 1  # Corrected decrementing
    
    # Return the reversed string stored in 'rstr1'
    return rstr1  # Return the reversed string

def main():    
    str1 = '12345abcde'  # Define the string to reverse
    print("String reverse for \'{}\' is {}".format(str1, string_reverse(str1)))  # Pass str1 to the function

# Don't change the code below!
if __name__ == "__main__":
    main()
