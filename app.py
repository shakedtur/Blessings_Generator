from flask import Flask, request, render_template

app = Flask(__name__)

# Example external function
def process_data(name, age, hobby, email, gender):
    import Bulid_sentence_from_web as web_page
    web_sentence= web_page.define_reqest_text_gemini()
    web_sentence= web_page.Recipient_name(web_sentence,name)
    web_sentence= web_page.recipient_age(web_sentence,age)
    web_sentence= web_page.define_recipient_hobbies(web_sentence,hobby)
    web_sentence= web_page.define_sex(web_sentence,gender)
    print(f"##########\n{web_sentence}\n###############\n")
    import Gemini_messege
    answer= Gemini_messege.belssing_request(web_sentence)
    # TODO: add save in data base


    return answer + f"\nProcessed:test Name - {name}, Age - {age}, Hobby - {hobby}, Email - {email}, Gender - {gender}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        email = request.form.get('email')
        gender = request.form.get('gender')

        # Process the data
        result = process_data(name, age, hobby, email, gender)

    return render_template('web.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
