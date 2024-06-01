from flask import Flask, request, jsonify, render_template
from health_app import HealthApp

app = Flask(__name__)
health_app = HealthApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    age = int(data['age'])
    gender = data['gender']
    health_app.add_user(username, age, gender)
    return jsonify({"message": f"Benutzer {username} wurde erfolgreich hinzugefügt."})

@app.route('/medication_reminders/<username>', methods=['GET'])
def list_medication_reminders(username):
    reminders = health_app.list_medication_reminders(username)
    return jsonify(reminders)

@app.route('/nutrition_plan/<username>', methods=['GET'])
def get_nutrition_plan(username):
    nutrition_plan = health_app.users[username].get('nutrition_plan')
    if nutrition_plan:
        return jsonify({"nutrition_plan": nutrition_plan})
    else:
        return jsonify({"message": "Kein Ernährungsplan vorhanden."})

@app.route('/set_health_goal', methods=['POST'])
def set_health_goal():
    data = request.json
    username = data['username']
    goal = data['goal']
    value = data['value']
    health_app.set_health_goal(username, goal, value)
    return jsonify({"message": f"Gesundheitsziel {goal} für {username} wurde festgelegt."})

@app.route('/log_activity', methods=['POST'])
def log_activity():
    data = request.json
    username = data['username']
    activity = data['activity']
    duration = int(data['duration'])
    health_app.log_activity(username, activity, duration)
    return jsonify({"message": f"Aktivität {activity} für {duration} Minuten wurde protokolliert."})

@app.route('/activity_logs/<username>', methods=['GET'])
def list_activity_logs(username):
    logs = health_app.list_activity_logs(username)
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
