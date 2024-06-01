class HealthApp:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, age, gender):
        self.users[username] = {'age': age, 'gender': gender, 'medication_reminders': [], 'health_data': {}, 'exercise_logs': [], 'nutrition_plan': None, 'health_goals': {}, 'activity_logs': []}

    def add_medication_reminder(self, username, medication, time):
        self.users[username]['medication_reminders'].append({'medication': medication, 'time': time})

    def list_medication_reminders(self, username):
        print(f"Medikamentenerinnerungen für {username}:")
        reminders = self.users[username]['medication_reminders']
        if reminders:
            for idx, reminder in enumerate(reminders, 1):
                print(f"{idx}. Nehmen Sie {reminder['medication']} um {reminder['time']} ein")
        else:
            print("Keine Medikamentenerinnerungen vorhanden.")

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
        print(f"Gesundheitsziele für {username}:")
        goals = self.users[username]['health_goals']
        if goals:
            for goal, value in goals.items():
                print(f"{goal}: {value}")
        else:
            print("Keine Gesundheitsziele festgelegt.")

    def log_activity(self, username, activity, duration):
        self.users[username]['activity_logs'].append({'activity': activity, 'duration': duration})

    def list_activity_logs(self, username):
        print(f"Aktivitätsprotokoll für {username}:")
        logs = self.users[username]['activity_logs']
        if logs:
            for idx, log in enumerate(logs, 1):
                print(f"{idx}. {log['activity']}: {log['duration']} Minuten")
        else:
            print("Keine Aktivitätsdaten vorhanden.")

# Funktion zur Interaktion mit der Benutzeroberfläche
def main():
    health_app = HealthApp()

    while True:
        print("\nWillkommen bei Ihrer Gesundheits-App!")
        print("1. Benutzer hinzufügen")
        print("2. Medikamentenerinnerungen anzeigen")
        print("3. Ernährungsplan anzeigen")
        print("4. Gesundheitsziele festlegen")
        print("5. Aktivitäten protokollieren")
        print("6. Aktivitätsprotokoll anzeigen")
        print("7. Beenden")

        choice = input("Bitte wählen Sie eine Option: ")

        if choice == '1':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            age = int(input("Bitte geben Sie Ihr Alter ein: "))
            gender = input("Bitte geben Sie Ihr Geschlecht ein (männlich/weiblich): ")
            health_app.add_user(username, age, gender)
            print(f"Benutzer {username} wurde erfolgreich hinzugefügt.")
        elif choice == '2':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            health_app.list_medication_reminders(username)
        elif choice == '3':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            if health_app.users.get(username) and health_app.users[username]['nutrition_plan']:
                print(f"Ernährungsplan für {username}: {health_app.users[username]['nutrition_plan']}")
            else:
                print("Kein Ernährungsplan vorhanden.")
        elif choice == '4':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            goal = input("Bitte geben Sie das Ziel ein (z.B. Gewichtsverlust, Blutdrucksenkung): ")
            value = input("Bitte geben Sie den Zielwert ein: ")
            health_app.set_health_goal(username, goal, value)
            print(f"Gesundheitsziel {goal} für {username} wurde festgelegt.")
        elif choice == '5':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            activity = input("Bitte geben Sie die Aktivität ein: ")
            duration = int(input("Bitte geben Sie die Dauer der Aktivität in Minuten ein: "))
            health_app.log_activity(username, activity, duration)
            print(f"Aktivität {activity} für {duration} Minuten wurde protokolliert.")
        elif choice == '6':
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            health_app.list_activity_logs(username)
        elif choice == '7':
            print("Vielen Dank für die Nutzung der Gesundheits-App. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine der verfügbaren Optionen.")

if __name__ == "__main__":
    main()
