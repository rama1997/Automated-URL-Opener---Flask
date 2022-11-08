from flask import Flask
import click
import time
import os
from .models import Note, User
import webbrowser
from flask.cli import with_appcontext
from datetime import datetime


def register_cli(app: Flask):

	@app.cli.command('open')
	@click.argument('url')
	@with_appcontext
	def schedule(url):
		"""Open a URL."""
		print(str(datetime.now()),'Opening URL...')
		webbrowser.open(url)
		print(str(datetime.now()),'Opened {}'.format(url))
		print(str(datetime.now()),'Done!')