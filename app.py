from flask import Flask, request, render_template

app = Flask(__name__)

# Example external function
def process_data(name, age, hobby, kinship, style, otherStyle,  email, gender, emoji, nameWish):
    return f"Processed:test Name - {name}, Age - {age}, Hobby - {hobby}, kinship - {kinship}, style - {style}, otherStyle - {otherStyle}, Email - {email}, Gender - {gender}, emoji - {emoji}, nameWish - {nameWish}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        email = request.form.get('email')
        kinship = request.form.get('kinship')
        style = request.form.get('style')
        otherStyle = request.form.get('otherStyle')
        gender = request.form.get('gender')
        emoji = request.form.get('emoji')
        nameWish = request.form.get('nameWish')
        if style == 'other':
            result = otherStyle
        else:
            result = style

        # Process the data
        result = process_data(name, age, hobby, email, kinship, style, otherStyle, gender, emoji, nameWish)

    return render_template('web.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
