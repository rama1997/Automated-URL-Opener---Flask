from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User
from .extensions import db
import json
from . import cron

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
	cron.get_jobs()
	return render_template("home.html", user=current_user)

@views.route('/add_note', methods = ['GET', 'POST'])
def add_note():
	if request.method == 'POST':
		url = request.form.get('url')
		title = request.form.get('title')
		frequency = request.form.get('frequency')
		dow = request.form.get('dow')
		month = request.form.get('month')
		date = request.form.get('date')
		hour = request.form.get('hour')
		minute = request.form.get('minute')
		am_pm = request.form.get('am_pm')

		if len(title) < 1:
			flash('Title is too short!', category='error')
		elif len(url) < 1:
			flash('URL is too short!', category='error')
		elif frequency == None:
			flash('Please select frequency!', category='error')
		elif frequency == "Weekly" and dow == None:
			flash('Please select day!', category='error')
		elif frequency == "Monthly" and date == None:
			flash('Please select date!', category='error')
		else:
			new_note = Note(url=url, title=title, frequency = frequency, dow = dow, month = month, date = date, hour = hour, minute = minute, am_pm = am_pm, user_id=current_user.id)
			db.session.add(new_note)
			db.session.flush()
			cron.schedule([new_note])
			db.session.commit()
			flash('Link added!', category='success')

	return render_template("add_note.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
	note = json.loads(request.data)
	note_id = note['noteId']
	note = Note.query.get(note_id)
	if note:
		if note.user_id == current_user.id:
			db.session.delete(note)
			db.session.flush()
			cron.remove(note)
			db.session.commit()
	return jsonify({})

@views.route('/delete_all_notes', methods=['POST'])
def delete_all_notes():
	notes = Note.query.filter_by(user_id=current_user.id)
	for note in notes:
		db.session.delete(note)
		db.session.flush()
		cron.remove(note)
	db.session.commit()
	return jsonify({})

@views.route('/edit_note', methods=['GET', 'POST'])
def edit_note():
	if request.method == 'POST':
		url = request.form.get('url')
		title = request.form.get('title')
		frequency = request.form.get('frequency')
		dow = request.form.get('dow')
		month = request.form.get('month')
		date = request.form.get('date')
		hour = request.form.get('hour')
		minute = request.form.get('minute')
		am_pm = request.form.get('am_pm')
		note_id = request.form.get('note_id')
		note = Note.query.get(note_id)
		if note and note.user_id == current_user.id:
			if len(title) < 1:
				flash('Title is too short!', category='error')
			elif len(url) < 1:
				flash('URL is too short!', category='error')
			elif frequency == None:
				flash('Please select frequency!', category='error')
			elif frequency == "Weekly" and dow == None:
				flash('Please select day!', category='error')
			elif frequency == "Monthly" and date == None:
				flash('Please select date!', category='error')
			else:
				note.url = url
				note.title = title
				note.frequency = frequency
				note.dow = dow
				note.month = month
				note.date = date
				note.hour = hour
				note.minute = minute
				note.am_pm = am_pm
				db.session.flush()
				cron.modify(note)
				db.session.commit()
				flash('Saved!', category='success')
				return redirect(url_for('views.home'))

	elif request.method == 'GET':
		noteId = request.args.get('note')
		note = Note.query.get(noteId)

	return render_template("edit_note.html", user=current_user, note = note)