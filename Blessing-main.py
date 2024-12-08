
"""must install once time in the terminal:

pip install -q -U google-generativeai
"""

import os
import google.generativeai as genai
from Mongo import Blesing_DB_mongo as DB

from Mongo import Access_keys

from datetime import datetime

def input_details_from_user():
    details_dict={"name": None, "age":None,"language": "english","sex": "female","style": "Blessing in rhymes" }
    languages_list=["English", "Hebrew","Arbic" ,"Spanish","Russian"]

    details_dict["name"]=input("What is the name of the birthday person? ")
    details_dict["age"] = int(input("How old will the birthday person be?"))
    languages_num= int(input("choose one of the following languages: 1.English 2.Hebrew 3.Arbic 4.Spanish 5.Russian language"))
    details_dict["language"] = languages_list[languages_num-1]

    return details_dict



def Blessing_Generator_sentence(name, age,language,sex,type):
    lines_amount= 5
    age=str(age)
    if sex == "female":
        blessing_request="write a birthday belssing for female and consider the following parameters: " + "name: " + name + " age: " + age + " blessing language: " + language +" style: " + type
    else:
        blessing_request = "write a birthday belssing for a male and consider the following parameters: " + "name: " + name + " age: " + age + " blessing language: " + language + " style: " + type
    return str(blessing_request)

def belssing_request(sentence_request):

    #user_text=str(input("enter a sentence:\n"))
    # user_text = "כתוב ברכה בחרוזים ליום הולדת 25 של שי"
    # print(user_text)
    API_KEY= Access_keys.api_key
    genai.configure(api_key=API_KEY)

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction = "write just  one version of blessing until 5 line or less, secend version of belssing Transliteration in english")

    chat_session = model.start_chat(
        history=[
        ]
    )

    #Send the request to Gemini

    response = chat_session.send_message(sentence_request )


    #print(response.text)
    return str(response.text)




def main():
    print("hello")
    details=input_details_from_user()
    print(details.items())
    senc=Blessing_Generator_sentence(details["name"],details["age"],details["language"],details["sex"],details["style"])
    print(senc)
    gemini_answer= belssing_request(senc)
    print(gemini_answer)
    #belssing_request()
    DB.save_text_in_mogoDB(gemini_answer)


main()
