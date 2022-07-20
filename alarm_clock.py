class AlarmClock:
    def __init__(self):
        self.current_time = "12:00"
        self.alarm_is_on = False
        self.current_alarm_time = "00:00"
    
    def SetClockTime(self):
        user_confirmation = input(f"The current time is {self.current_time}. Would you like to change the time? y/n ")
        if user_confirmation == "y":
            user_time_input = input("Please input the new time. Use military time in XX:XX format. ")
            self.current_time = user_time_input
            print(f"The current time is now {self.current_time}.")
        else:
            print(f"Okay. The current time is {self.current_time}.")

    def SetAlarmTime(self):
        user_confirmation = input(f"The alarm time is {self.current_alarm_time}. Would you like to change the alarm time? y/n ")
        if user_confirmation == "y":
            user_time_input = input("Please input the new alarm time. Use military time in XX:XX format. ")
            self.current_alarm_time = user_time_input
            print(f"The alarm time is now {self.current_alarm_time}.")
        else:
            print(f"Okay. The alarm time is {self.current_alarm_time}.")
    
    def ToggleAlarmStatus(self):
        if self.alarm_is_on == False:
            self.alarm_is_on = True
            print("Alarm is on!")
        elif self.alarm_is_on == True:
            self.alarm_is_on = False
            print("Alarm is off!")
