from ._anvil_designer import menuTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class menu(menuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('single')
    


  def button_3_click(self, **event_args):
    open_form('suite')

  def button_2_click(self, **event_args):
    open_form('secon')

  def link_1_click(self, **event_args):
    open_form('Form1')

  def link_3_click(self, **event_args):
    open_form('booking')

  def link_2_click(self, **event_args):
    open_form('details')

    
  
