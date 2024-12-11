from flask import Flask, request, render_template

app = Flask(__name__)

# Example external function
def process_data(name, age, hobby, email, gender):
    return f"Processed:test Name - {name}, Age - {age}, Hobby - {hobby}, Email - {email}, Gender - {gender}"

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
