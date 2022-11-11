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
cwd = os.getcwd()
dow = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def schedule(notes):
	for note in notes:
		job = cron.new(command='cd {} && export FLASK_APP=app/__init__.py && venv/bin/flask open {} >>app.log 2>&1'.format(cwd, note.url), comment=str(note.id))
		if note.frequency == "Daily":
			job.every().day()
		elif note.frequency == "Weekly":
			job.dow.on(dow[note.dow])
		elif note.frequency == "Monthly":
			if note.date == "End of Month":
				job.set_command('[ "$(/usr/local/bin/gdate +%d -d tomorrow)" = "01" ] && cd {} && export FLASK_APP=app/__init__.py && venv/bin/flask open {} >>app.log 2>&1'.format(cwd, note.url))
				job.setall('30 13 28-31 * *')
			elif note.date == "Start of Month":
				job.day.on(1)
			else:
				job.day.on(int(note.date))

		job.minute.on(int(note.minute))
		if note.am_pm == "AM":
			job.hour.on(int(note.hour))
		else:
			job.hour.on(int(note.hour)+12)

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
		job.set_command('cd {} && export FLASK_APP=app/__init__.py && venv/bin/flask open {} >>app.log 2>&1'.format(cwd, note.url))
		if note.frequency == "Daily":
			job.every().day()
		elif note.frequency == "Weekly":
			job.dow.on(dow[note.dow])
		elif note.frequency == "Monthly":
			if note.date == "End of Month":
				job.set_command('[ "$(/usr/local/bin/gdate +%d -d tomorrow)" = "01" ] && cd {} && export FLASK_APP=app/__init__.py && venv/bin/flask open {} >>app.log 2>&1'.format(cwd, note.url))
				job.setall('30 13 28-31 * *')
			elif note.date == "Start of Month":
				job.day.on(1)
			else:
				job.day.on(int(note.date))

		job.minute.on(int(note.minute))
		if note.am_pm == "AM":
			job.hour.on(int(note.hour))
		else:
			job.hour.on(int(note.hour)+12)

	cron.write()

def get_jobs():
	for job in cron:
		print(job)

def clear_jobs():
	cron.remove_all()
