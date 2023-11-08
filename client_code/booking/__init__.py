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
    if self.text_box_1.text != "":
      app_tables.customer.add_row(
        name=self.text_box_1.text, 
        no=self.text_box_3.text,
        email= self.text_box_4.text,
        type=self.drop_down_1.selected_value,
        days=self.drop_down_2.selected_value,
        date=self.date_picker_1.date,
        r_no =self.drop_down_rno.selected_value,
        guest=self.drop_down_gus.selected_value
      )
    self.text_box_1.text = ""
    self.text_box_1.focus()
    self.text_box_3.text = ""
    self.text_box_3.focus()
    self.text_box_4.text = ""
    self.text_box_4.focus()
    alert("hey there booking placed, please procced to pay to confirm your booking with us")
    
    price= 0
    if self.drop_down_1.selected_value == 'single':
      price = 1500 
    elif self.drop_down_1.selected_value == 'double':
      price = 3000 
    elif self.drop_down_1.selected_value == 'suite':
      price = 7000 
    n=0
    if self.drop_down_2.selected_value =='1':
      n=1
    if self.drop_down_2.selected_value =='2':
      n=2
    if self.drop_down_2.selected_value =='3':
      n=3
    if self.drop_down_2.selected_value =='4':
      n=4
    if self.drop_down_2.selected_value =='5':
      n=5
    if self.drop_down_2.selected_value =='6':
      n=6
    final_price= price*n 
    self.text_box_7.text= final_price
    tax = final_price * .06
    self.text_box_tax.text = tax
    self.text_box_total.text = final_price + tax
    
    

    
      

  def button_2_click(self, **event_args):
    alert('Transaction completed recieved amount')
    open_form('details')

  def drop_down_1_change(self, **event_args):
    if self.drop_down_1.selected_value == 'single':
      self.drop_down_rno.items = [str(rooms['sroom']) for rooms in app_tables.rooms.search()]
      self.drop_down_gus.items = [str(rooms['srg']) for rooms in app_tables.rooms.search()]
    elif self.drop_down_1.selected_value == 'double':
      self.drop_down_rno.items = [str(rooms['droom']) for rooms in app_tables.rooms.search()]
      self.drop_down_gus.items = [str(rooms['drg']) for rooms in app_tables.rooms.search()]
      
    elif self.drop_down_1.selected_value == 'suite':
      self.drop_down_rno.items = [str(rooms['suite']) for rooms in app_tables.rooms.search()]
      self.drop_down_gus.items = [str(rooms['surg']) for rooms in app_tables.rooms.search()]
    
