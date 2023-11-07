from ._anvil_designer import bookingTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class booking(bookingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    

  def link_1_click(self, **event_args):
    open_form('menu')

  def button_1_click(self, **event_args):
    anvil.server.call(
      'add_info', 
      self.text_box_1.text, 
      self.text_box_3.text,
      self.text_box_4.text,
      self.drop_down_1.selected_value,
      self.text_box_2.text
    )
    alert ('please continue'+ self.text_box_1.text +'for payment')
    self.text_box_1.text, self.text_box_3, self.text_box_4, self.text_box_2, self.drop_down_1.selected_value = '', '','','', 'none'
