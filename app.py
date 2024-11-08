from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db_config = {
    'host': 'database763.clq4kqsc0hun.us-east-1.rds.amazonaws.com',
    'user': 'admin1',
    'password': 'renukashende',
    'database': 'meditation'
}

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Meditation guide route
@app.route('/meditation')
def meditation():
    return render_template('meditation.html')

# Gallery page route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Contact Us page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Store contact form data in MySQL
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, message))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/thank_you')  # Redirect to a thank you page after form submission
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return f"Database error: {err}"  # Display error message on the page
    
    return render_template('contact.html')

# Thank you page route after contact form submission
@app.route('/thank_you')
def thank_you():
    return render_template('thank.html')

if __name__ == '__main__':
    app.run(debug=True)
