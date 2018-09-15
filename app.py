from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/' , methods=['POST','GET'])
def record_arrival():
    if request.method == 'POST':
        record = request.form.to_dict()
        with open('arrival_records.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([record['driver'], record['truck'], record['company'], record['supposed-arrival-time'], record['real-arrival-time']])
        return redirect(url_for('schedule'))
    else:
        return render_template('index.html')

@app.route('/plan_arrival', methods=['POST','GET'])
def plan_arrival():
    if request.method == 'POST':
        data = request.form.to_dict()
        #TODO:Add estimated arrival to schedule.csv

        return redirect(url_for('schedule'))
    else:
        return render_template('plan_arrival.html')

@app.route('/schedule')
def schedule():
    with open('schedule.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        return render_template('schedule.html', reader=reader)
