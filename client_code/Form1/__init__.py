from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import random
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_2_click(self, **event_args):
    anvil.users.signup_with_form()
    

  def button_3_click(self, **event_args):
    anvil.users.login_with_form()
    open_form('menu')
    
    
    