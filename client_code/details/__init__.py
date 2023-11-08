from ._anvil_designer import detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class details(detailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  def link_1_click(self, **event_args):
    open_form('menu')

  def button_1_click(self, **event_args):
      self.repeating_panel_1.items = app_tables.customer.search(email = self.text_box_1.text)

  def text_box_1_pressed_enter(self, **event_args):
    self.repeating_panel_1.items = app_tables.customer.search(email = self.text_box_1.text)

  def link_2_click(self, **event_args):
    open_form('booking')

  def link_3_click(self, **event_args):
    open_form('Form1')

    