
"""must install once time in the terminal:

pip install -q -U google-generativeai
"""

import os
import google.generativeai as genai
from Mongo import Blesing_DB_mongo as DB
from Mongo import Access_keys



def belssing_request(sentence_request):

    #user_text=str(input("enter a sentence:\n"))
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
        system_instruction = "write just one version of birthday greetings until 5 line or less, secend version of belssing Transliteration in english")

    chat_session = model.start_chat(
        history=[
        ]
    )

    #Send the request to Gemini

    response = chat_session.send_message(sentence_request)


    #print(response.text)
    return str(response.text)