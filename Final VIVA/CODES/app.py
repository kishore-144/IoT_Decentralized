from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    data = []
    try:
        with open('data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) 
            for row in reader:
                data.append({"moisture": row[0], "timestamp": row[1]})
    except FileNotFoundError:
        data = []

    return render_template("index.html", soil_data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
