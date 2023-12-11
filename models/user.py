#!/usr/bin/python3
""" user model inherits from BaseModel it's functions """
from models.base_model import BaseModel


class User(BaseModel):
	""" Defines User class which handling users """
	email = ''
	password = ''
	first_name = ''
	last_name = ''
