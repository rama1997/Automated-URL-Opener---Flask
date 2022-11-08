import webbrowser
import datetime
import os

from .models import Note, User
from .extensions import db, cron
from flask_login import current_user as user

"""
	0 - monday
	6 - sunday
"""
day = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def schedule(notes):
	cwd = os.getcwd()
	for note in notes:
		job = cron.new(command='cd {} && export FLASK_APP=app/__init__.py && venv/bin/flask open {} >>app.log 2>&1'.format(cwd, note.url), comment=str(note.id))
		if note.frequency == "Daily":
			job.every().day()
			job.hour.on(13)
		elif note.frequency == "Weekly":
			job.dow.on(day[note.days])
			job.hour.on(13)
		elif note.frequency == "Monthly":
			job.every().month()
			job.hour.on(13)

	cron.write()

def remove(note):
	cron.remove_all(comment=str(note.id))
	cron.write()

def pause(notes):
	for note in notes:
		iter = cron.find_comment(str(note.id))
		for job in iter:
			job.enable(False)

	cron.write()

def resume(notes):
	for note in notes:
		iter = cron.find_comment(str(note.id))
		for job in iter:
			job.enable()

	cron.write()

def modify(note):
	iter = cron.find_comment(str(note.id))
	for job in iter:
		job.clear()
		if note.frequency == "Daily":
			job.every().day()
			job.hour.on(13)
		elif note.frequency == "Weekly":
			job.dow.on(day[note.days])
			job.hour.on(13)
		elif note.frequency == "Monthly":
			job.every().month()
			job.hour.on(13)
		print("after", job)
	cron.write()

def get_jobs():
	for job in cron:
		print(job)

def clear_jobs():
	cron.remove_all()
