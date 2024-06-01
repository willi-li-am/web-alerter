import os
from flask import Flask
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from twilio.rest import Client

from sms import sendSMS
from site_check import does_still_exists

# Load environment variables from .env file

load_dotenv()

to_check = [
    {
        'url': "https://internships.shopify.com/",
        'text': 'Applications for Fall 2024 Engineering Internships are now closed. Winter 2025 applications will open later this Summer!'
    },
]

def scheduled_check():
    for check in to_check:
        if (not does_still_exists(check['url'], check['text'])):
            sendSMS(check['url'])
        else:
            print('nothing to alert')

def create_app():
    app = Flask(__name__)
    # Initialize scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=scheduled_check, trigger="interval", hours=4)
    scheduler.start()

    @app.route('/')
    def home():
        return "Hello, Flask with APScheduler running every 5 minutes!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()