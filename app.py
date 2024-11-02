from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Jeddah, Saudi Arabia',
        'salary': 'SAR 10,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Makkah, Saudi Arabia',
        # 'salary': 'SAR 12,000'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Riyadh, Saudi Arabia',
        'salary': 'SAR 15,000'
    },
]

@app.route("/")
def hello_world():
    return render_template("home.html", 
                jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)