from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)

students = [
    "นายธนภัทร ศิริวัฒนาโรจน์",
    "นางสาวญาดา คนึงจิต",
    "นางสาวตะวันวาด บุญเกิน",
    "นายธรรมธรณ์ สุขพินิจ",
    "นายธีรวัจน์ วงศ์วัชรานนท์",
    "นางสาวชุติมณฑน์ ประทีป"
]

teachers = ["อาจารย์ A", "อาจารย์ B", "อาจารย์ C"]

@app.route('/')
def index():
    return render_template("form.html", students=students, teachers=teachers)

@app.route('/submit', methods=['POST'])
def submit():
    student = request.form['student']
    teacher = request.form['teacher']
    comment = request.form['comment']
    scores = {
        'punctuality': request.form['punctuality'],
        'participation': request.form['participation'],
        'knowledge': request.form['knowledge'],
        'manner': request.form['manner'],
        'presentation': request.form['presentation']
    }
    score_map = {'N/A': 0, 'O': 30, 'S': 20, 'U10': 10, 'U5': 5}
    total_score = sum(score_map.get(scores[key], 0) for key in scores)

    with open('results.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            datetime.now().isoformat(), student, teacher,
            scores['punctuality'], scores['participation'], scores['knowledge'],
            scores['manner'], scores['presentation'], total_score, comment
        ])
    return "✅ ส่งแบบประเมินเรียบร้อยแล้ว"

if __name__ == '__main__':
    app.run(debug=True)