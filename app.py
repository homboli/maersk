from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/' , methods=['POST','GET'])
def record_arrival():
    if request.method == 'POST':
        record = request.form.to_dict()
        timeSupposedArrival = int(record['supposed-arrival-time'].split(':')[0]) + int(record['supposed-arrival-time'].split(':')[1])/60
        timeRealArrival = int(record['real-arrival-time'].split(':')[0]) + int(record['real-arrival-time'].split(':')[1])/60
        with open('datafile.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([record['company'], record['truck'], record['driver'], timeSupposedArrival, timeRealArrival])
        return redirect(url_for('schedule'))
    else:
        return render_template('index.html')

@app.route('/plan_arrival', methods=['POST','GET'])
def plan_arrival():
    if request.method == 'POST':
        record = request.form.to_dict()
        timeSupposedArrival = int(record['supposed-arrival-time'].split(':')[0]) + int(record['supposed-arrival-time'].split(':')[1])/60
        with open('input.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Company','Truck','Driver','AppointmentTime'])
            writer.writerow([record['company'], record['truck'], record['driver'], timeSupposedArrival])
        exec(open('runBack.py').read())
        return redirect(url_for('schedule'))
    else:
        return render_template('plan_arrival.html')

@app.route('/schedule')
def schedule():
    i = 1
    with open('schedule.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        return render_template('schedule.html', reader=reader)
