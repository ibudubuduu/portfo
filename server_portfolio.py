from flask import Flask, render_template, request, redirect
from random import randint
import csv
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html(page_name):
    return render_template(page_name)


def write_data(data):
    with open('database.txt', mode='a') as database:
            email = data["Email"]
            subject = data["Subject"]
            content = data["Content"]
            file = database.write(f"\n Email : {email}, Subject : {subject}, Content : {content}")


def write_data_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
            email = data["Email"]
            subject = data["Subject"]
            content = data["Content"]
            csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, content])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Try Again!"





