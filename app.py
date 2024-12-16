from flask import Flask, request, render_template

app = Flask(__name__)

# Example external function
def process_data(language, name, age, hobby, kinship, gender ,style , emoji, nameWish):
    import Bulid_sentence_from_web as web_page
    web_sentence= web_page.define_reqest_text_gemini()
    web_sentence= web_page.define_language_belssing(web_sentence, language)
    web_sentence= web_page.Recipient_name(web_sentence,name)
    web_sentence= web_page.recipient_age(web_sentence,age)
    web_sentence= web_page.define_recipient_hobbies(web_sentence,hobby)
    web_sentence= web_page.define_kinship(web_sentence, kinship)
    web_sentence= web_page.define_style(web_sentence, style)
    web_sentence= web_page.define_sex(web_sentence,gender)
    web_sentence= web_page.define_emoji(web_sentence,emoji)
    web_sentence= web_page.define_name_wish(web_sentence,nameWish)

    print(f"##############\n{web_sentence}\n###############\n")
    # import Gemini_messege
    # answer= Gemini_messege.belssing_request(web_sentence)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print(answer)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # TODO: add saving in data base
    #request_DB =jsonify({"result": result})
    # TODO: send message to gemini via API
    #return answer + f"\nProcessed:test Name - {name}, Age - {age}, Hobby - {hobby}, Email - {email}, Gender - {gender}"

    return web_sentence



@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    #error = None
    if request.method == 'POST':
        # Get data from the form
        language = request.form.get('language') 
        name = request.form.get('name')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        kinship = request.form.get('kinship')
        style = request.form.get('style')
        otherStyle = request.form.get('otherStyle')
        gender = request.form.get('gender')
        emoji = request.form.get('emoji')
        nameWish = request.form.get('nameWish')
        if style == 'other':
           style = otherStyle

        #try:
            # Convert age to integer if necessary for calculations
        #    age = int(age)
        #except ValueError:
        #    error = "Age must be a number."

        #if not error:  # Process data only if no errors
        #    result = process_data(name, age, hobby, gender, style, emoji, nameWish)

        # Process the data
        result = process_data(language, name, age, hobby, kinship, gender, style, emoji, nameWish)

    return render_template('web.html', result=result)  #error=error)

if __name__ == '__main__':
    app.run(debug=True)
