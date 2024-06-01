class HealthApp:
    def __init__(self):
        self.users = {}

    def add_user(self, username, age, gender):
        self.users[username] = {'age': age, 'gender': gender, 'medication_reminders': [], 'health_data': {}, 'exercise_logs': [], 'nutrition_plan': None, 'health_goals': {}, 'activity_logs': []}

    def add_medication_reminder(self, username, medication, time):
        self.users[username]['medication_reminders'].append({'medication': medication, 'time': time})

    def list_medication_reminders(self, username):
        reminders = self.users[username]['medication_reminders']
        if reminders:
            return reminders
        else:
            return {"message": "Keine Medikamentenerinnerungen vorhanden."}

    def create_nutrition_plan(self, username, age, gender, activity_level):
        if age < 60:
            if gender == 'male':
                if activity_level == 'sedentary':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Männer unter 60 Jahren mit sitzender Lebensweise"
                elif activity_level == 'moderate':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Männer unter 60 Jahren mit mäßiger Aktivität"
                elif activity_level == 'active':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Männer unter 60 Jahren mit aktiver Lebensweise"
            elif gender == 'female':
                if activity_level == 'sedentary':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Frauen unter 60 Jahren mit sitzender Lebensweise"
                elif activity_level == 'moderate':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Frauen unter 60 Jahren mit mäßiger Aktivität"
                elif activity_level == 'active':
                    self.users[username]['nutrition_plan'] = "Dein Ernährungsplan für Frauen unter 60 Jahren mit aktiver Lebensweise"
        else:
            self.users[username]['nutrition_plan'] = "Logik für Ernährungsplan für Menschen über 60 Jahre"

    def set_health_goal(self, username, goal, value):
        self.users[username]['health_goals'][goal] = value

    def list_health_goals(self, username):
        goals = self.users[username]['health_goals']
        if goals:
            return goals
        else:
            return {"message": "Keine Gesundheitsziele festgelegt."}

    def log_activity(self, username, activity, duration):
        self.users[username]['activity_logs'].append({'activity': activity, 'duration': duration})

    def list_activity_logs(self, username):
        logs = self.users[username]['activity_logs']
        if logs:
            return logs
        else:
            return {"message": "Keine Aktivitätsdaten vorhanden."}
