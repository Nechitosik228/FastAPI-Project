from flask import Flask
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from . import routes