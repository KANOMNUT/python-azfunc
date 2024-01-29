import logging
import azure.functions as func
import os
from dotenv import load_dotenv
from pymongo import MongoClient

app = func.FunctionApp()
load_dotenv()
Mongodb = os.getenv("MONGODB_URI")
client = MongoClient(Mongodb)
db = client.get_database("todoapp")
tasks_collection = db.get_collection("todos")

@app.function_name(name="time_trigger")
@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=True) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    try:
        task = list(tasks_collection.find())
        task = task[-1]
        get_data = task.get("temp")
        if get_data >= 25:
            send_line_noti()
        else:
            logging.info("Else Alert")
    except Exception as e:
        return "Error: ", str(e)
    
def send_line_noti():
    logging.info("Line Alert")


@app.schedule(schedule="0 * * * * *", arg_name="myTimer2", run_on_startup=False,
              use_monitor=True) 
def time_trigger_2(myTimer2: func.TimerRequest) -> None:
    try:
        task = list(tasks_collection.find())
        task = task[-1]
        get_data = task.get("temp")
        if get_data >= 25:
            logging.info("Alert2")
        else:
            logging.info("Else Alert")
    except Exception as e:
        return "Error: ", str(e)