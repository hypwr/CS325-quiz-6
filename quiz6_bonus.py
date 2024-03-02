from abc import ABC, abstractmethod

class User: # Follows SRP, only has one primary responsibility of initializing the user/basic user info
    def __init__(self,username,id):
        self.username = username
        self.userID = id

class Activity: # Follows SRP, only has one primary responsibility of performing the activity(will show data on distance, calories, etc)
    @abstractmethod # Follows LSP, as all subclasses of activity will adhere to the observer's pattern
    def perform_activity(self):
        pass

class ActivityMonitor: # Follows SRP, only has one primary responsibility of showing when activities are done and storing/showing this information
    def __init__(self,user,dataStorage,display):
        self.user = user
        self.dataBase = dataStorage
        self.display = display
        self.activities = []

    def add_activity(self,activity):
        self.activities.append(activity)

    def update_display(self,activity):
        self.display.show_data(self.user,activity)

    def get_data(self): # Follows OCP as the Display and Database is updated directly whenever the activity is performed by the ActivityMonitor.
        for activity in self.activities:
            activity.perform_activity()
            self.update_display(activity) #Shows DIP as both Display and DataStorage are used in Activity Monitor
            self.dataBase.store_data(self.user,activity)

class DataStorage: # Follows SRP, only has one primary responsibility of adding the data of the user and the activity performed to the database
    @abstractmethod # Follows ISP as it can be changed for each specific usage of the Display for each Observer/Interface.
    def store_data(self,user,activity):
        pass

class Display: # Follows SRP, only has one primary responsibility of showing/notifying the user of the activity.
    @abstractmethod # Follows ISP as it can be changed for each specific usage of the Display for each Observer/Interface.
    def show_data(self,user,activity):
        pass

######################## Below Showcases Usage of L and I principles ##################################

class Swimming(Activity):
    def __init__(self,distance):
        self.distance=distance
        self.name="Swimming"

    def perform_activity(self): #in meters
        self.calories_burned=0.305*self.distance
        self.steps="Not Applicable"
        self.distance=(str(self.distance)+" meters")

class Running(Activity):
    def __init__(self,distance):
        self.distance=distance
        self.name="Running"

    def perform_activity(self): #in miles
        self.calories_burned=100*self.distance
        self.steps=1500*self.distance
        self.distance=(str(self.distance)+" miles")

class Cycling(Activity):
    def __init__(self,distance):
        self.distance=distance
        self.name="Cycling"

    def perform_activity(self): #in miles
        self.calories_burned=55*self.distance
        self.steps=605*self.distance
        self.distance=(str(self.distance)+" miles")

class UpdateUser(Display):
    def show_data(self,user,activity):
        print(str(user.username)+":",str(activity.name),"[Calories Burned:",str(activity.calories_burned)+", Steps:",str(activity.steps)+", Distance:",activity.distance+"]")
        

class UpdateStorage(DataStorage):
    def __init__(self,DB):
        self.dataBase = DB

    def store_data(self,user,activity):
        #add the data to the connected dataBase
        print("-- DATA STORED --")

######################## Implimentation ###############################

def main():
    Jack = User("JackAttack2003",1)
    UserDisplay = UpdateUser()
    BasicStorage = UpdateStorage("myDB")

    ActivityMonitorJack = ActivityMonitor(Jack,BasicStorage,UserDisplay)

    JackRun = Running(5)
    JackSwim = Swimming(500)

    ActivityMonitorJack.add_activity(JackRun)
    ActivityMonitorJack.add_activity(JackSwim)

    ActivityMonitorJack.get_data()

main()