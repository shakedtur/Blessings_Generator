
def check_input_in_range(min_value, max_value):
    """
      Validates user input to be within a given numeric range.
      :param min_value: The minimum acceptable value.
      :param max_value: The maximum acceptable value.
      :return: The valid input within the range.
      """

    while True:
        try:
            value = int(input(f"Enter a number between {min_value} and {max_value}: "))
            if min_value <= value <= max_value:
                #print(f"Valid input: {value}")
                return value
            else:
                print(f"Input is out of range. Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_text_input():
    """
    Validates that the user input contains only alphabetic characters.
    :return: The valid text input.
    """
    while True:
        text = input("Enter text (letters only): ")
        if text.isalpha():
           #print(f"Valid input: {text}")
            return text
        else:
            print("Invalid input. Please enter letters only.")


def define_reqest_text_gemini():
    text= "write a birthday blessing consider the follwing parameters:\n"
    return str(text)

#2
def Recipient_name(text,name):
    text += f"\nRecipient's Name: {name} "
    return str(text)

#3
def recipient_age(text,age):
    text += f"\nRecipient's Age: {age} "
    return text
#4
def define_recipient_hobbies(text, hobbies):
    text += f"\nRecipient's Hobbies: {hobbies}"
    return text

#7
def define_sex(text,sex):
    text += f"\nThe recipient sex is: {sex}"
    return text