"""Initialize any app extensions."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from crontab import CronTab

# Create database
db = SQLAlchemy()
DB_NAME = "database.db"

# Access user's crontab
cron = CronTab(user=True)

# Create login manager for flask_login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
