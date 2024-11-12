from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Here you would normally process the form data, such as saving it to a database

    flash("Thank you for your message, we will get back to you soon!")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
