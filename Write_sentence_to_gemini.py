
#תשובה של גימיניי לפרטים הדרושים עבור ברכה
""""To create a personalized birthday blessing, please provide the following information:

Recipient's Name:
Your Relationship to the Recipient: (e.g., friend, family member, coworker)
Recipient's Age:
Recipient's Interests or Hobbies:
Any Recent Achievements or Milestones:
The Tone or Style of the Blessing: (e.g., funny, heartfelt, formal, informal)
Any Specific Wishes or Hopes for the Recipient:
The more details you provide, the more tailored the blessing can be.

Here's an example of how you can provide the information:

Recipient's Name: Sarah
Your Relationship to the Recipient: Best friend
Recipient's Age: 30
Recipient's Interests or Hobbies: Traveling, cooking, painting
Recent Achievements: Got promoted at work
Tone or Style of the Blessing: Funny and heartfelt
Specific Wishes or Hopes: Happy and successful year ahead"""

#בדיקות קלט תקינות מהמשתמש
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

#פונקציות ליצירת משפט תקין מהמשתמש לשליחה לגימייני
def define_reqest_text_gemini(text):
    text= "write a birthday blessing \n"
    return str(text)

def Wishing_blessings_person_name(text):
    print("Write your name:")
    sign_person = check_text_input()
    text=text + f"the name of the wishing blessing person sign at the end of the blessing is {sign_person} \n"
    return str(text)

#הגדרת השפה שתיכתב הברכה
def define_language_belssing(text):
    text=str(text)
    languages_list=["English", "Hebrew","Arbic" ,"Spanish","Russian"]
    print("choose one of the following languages: 1.English 2.Hebrew 3.Arbic 4.Spanish 5.Russian language")
    lang_choise=languages_list[check_input_in_range(1,5) - 1]
    text=text+f"the blessing gone be write in {lang_choise} language,\n"
    return str(text)

def Recipient_name(text):
    name = input("What is the name of the birthday person? ")
    text += f"\nRecipient's Name: {name}"
    return text

def recipient_age(text):
    age = input("What is the age of the birthday person? ")
    text += f"\nRecipient's Age: {age}"
    return text

def define_relationship(text):
    relationship = input("What is your relationship to the recipient? (e.g., friend, family member, coworker) ")
    text += f"\nYour Relationship: {relationship}"
    return text

def define_recipient_hobbies(text):
    hobbies = input("What are the recipient's interests or hobbies? (e.g., traveling, cooking, painting) ")
    text += f"\nRecipient's Hobbies: {hobbies}"
    return text

def define_style(text):
    style = input("What is the tone or style of the blessing? (e.g., funny, heartfelt, formal, informal) ")
    text += f"\nBlessing Style: {style}"
    return text

def define_sex(text):
    sex = input("Are the recipient is male/female? ")
    text += f"\nThe recipient sex is: {sex}"
    return text

def define_Emoji(text):

    emoji= False
    cohise= input("choose to add Emojis Y / n ?")
    while cohise != ( 'y' or 'Y' or 'n' or 'N'):
        cohise = input("choose to add Emojis Y / n ?")
    if cohise == ('y' or 'Y'):
        emoji = True
        text += "\nadd to the blessing nice emojis"
        return text
    else:
        return text






#פונקציה ראשית
#עבור כל פונקציה צריך להכניס למשתמש שאלה האם הוא רוצה להתחשב בפרט הבא או לא
#אם יש לך רעיונות לפרמטרים נוספים תכניס גם אותם, בכיף!!!
def final_text_gemini():
    sentence_to_gemini=""
    sentence_to_gemini=define_reqest_text_gemini(sentence_to_gemini)
    sentence_to_gemini=Wishing_blessings_person_name(sentence_to_gemini)
    sentence_to_gemini=define_language_belssing(sentence_to_gemini)
    sentence_to_gemini=recipient_age(sentence_to_gemini)
    sentence_to_gemini= define_recipient_hobbies(sentence_to_gemini)
    sentence_to_gemini = define_relationship(sentence_to_gemini)
    sentence_to_gemini = define_style(sentence_to_gemini)
    sentence_to_gemini = define_sex(sentence_to_gemini)
    sentence_to_gemini = define_Emoji(sentence_to_gemini)
    sentence_to_gemini=Recipient_name(sentence_to_gemini)

    print("#############################")
    print(sentence_to_gemini)
    return str(sentence_to_gemini)

final_text_gemini()