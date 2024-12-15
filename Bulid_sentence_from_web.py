
def check_input_in_range(min_value, max_value,num):
    """
      Validates user input to be within a given numeric range.
      :param min_value: The minimum acceptable value.
      :param max_value: The maximum acceptable value.
      :return: The valid input within the range.
      """

    while True:
        try:
            value =num
            if min_value <= value <= max_value:
                return value
            else:
                return (f"Input is out of range. Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_text_input(user_text):
    """
    Validates that the user input contains only alphabetic characters.
    :return: The valid text input.
    """
    while True:
        text = user_text
        if text.isalpha():
           #print(f"Valid input: {text}")
            return text
        else:
            return ("Invalid input. Please enter letters only.")

#1
def define_reqest_text_gemini():
    text= "write a Birthday greeting consider the following parameters:\n"
    return str(text)

#2
def Recipient_name(text,name):
    text += f"\nRecipient's name: {name} "
    return str(text)

#3
def recipient_age(text,age):
    text += f"\nThe recipient celebrating {age} years old."
    return text
#4
def define_recipient_hobbies(text, hobbies):
    text += f"\nRecipient's hobie: {hobbies}"
    return text

#5
def define_relationship(text,relationship):
    #relationship = input("What is your relationship to the recipient? (e.g., friend, family member, coworker) ")
    text += f"\nRelationship between the recipient to the author : {relationship}"
    return text
#6
def define_style(text, style):
    text += f"\nThe blessing style: {style}"
    return text

#7
def define_sex(text,sex):
    text += f"\nThe recipient gender is: {sex}"
    return text

#8
def define_emoji(text,emoji):
    text += f"\nAdd an nice emojis to the greeting: {emoji}"
    return text

#9
def define_name_wish(text, nameWish):
    text += f"\nThe name of the wishing blessing person sign at the end of the blessing is {nameWish}"
    return text

def define_language_belssing(text, lang_choise):
    text += f"\nthe blessing gone be write at {lang_choise} language."
    return str(text)