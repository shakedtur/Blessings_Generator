
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
    text=text + f"the name of the wishing blessing person is {sign_person} \n"
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
    print("What is the name of brithday person?")
    name=check_text_input()
    text=text+f"Recipient's Name: {name}"

    return str(text)

def Recipent_age(text):
    pass

def define_Relationship(text):
    #Your Relationship to the Recipient: (e.g., friend, family member, coworker)
    return str(text)
    pass

def define_Recipient_Hobbies(text):
    #Recipient's Interests or Hobbies:

    return str(text)
    pass

def define_style(text):
    #The Tone or Style of the Blessing: (e.g., funny, heartfelt, formal, informal)
    return str(text)
    pass

def define_hobbie(text):
    #Recipient's Interests or Hobbies: Traveling, cooking, painting
    return str(text)
    pass


#פונקציה ראשית
#עבור כל פונקציה צריך להכניס למשתמש שאלה האם הוא רוצה להתחשב בפרט הבא או לא
#אם יש לך רעיונות לפרמטרים נוספים תכניס גם אותם, בכיף!!!
def final_text_gemini():
    sentence_to_gemini=""
    sentence_to_gemini=define_reqest_text_gemini(sentence_to_gemini)
    sentence_to_gemini=Wishing_blessings_person_name(sentence_to_gemini)
    sentence_to_gemini=define_language_belssing(sentence_to_gemini)
    sentence_to_gemini=Recipient_name(sentence_to_gemini)

    print(sentence_to_gemini)
    return str(sentence_to_gemini)

final_text_gemini()