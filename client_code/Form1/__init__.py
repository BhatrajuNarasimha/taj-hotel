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
   

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    image1='https://tse1.mm.bing.net/th?id=OIP.2jZnkTdKsliRzkKFoOD5MAHaFF&pid=Api&P=0&h=220'
    image2='https://tse2.mm.bing.net/th?id=OIP.nG9EKOYEwnbJl1TSv4gBOAHaE8&pid=Api&P=0&h=220'
    image3='https://simplexitytravel.com/wp-content/plugins/phastpress/phast.php/c2VydmljZT1pbWFnZXMmc3JjPWh0dHBzJTNBJTJGJTJGc2ltcGxleGl0eXRyYXZlbC5jb20lMkZ3cC1jb250ZW50JTJGdXBsb2FkcyUyRjIwMjAlMkYwNyUyRnRhai1ob3RlbC1zY2FsZWQucG5nJmNhY2hlTWFya2VyPTE2MDExOTUxNjItNDQyMzg5OSZ0b2tlbj1kYTQ2MTNjOGY3YWE3MTEx.q.png'
    image4='https://tse1.mm.bing.net/th?id=OIP.pqobaNKEgAobbrXrfWHauQHaHa&pid=Api&P=0&h=220'
    image5='https://tse4.mm.bing.net/th?id=OIP.58gFXAiV8MMLnSKuQnH_iQHaCp&pid=Api&P=0&h=220'
    image6='https://tse1.mm.bing.net/th?id=OIP.D5rTYMnvH0J90zty9sINSgHaFI&pid=Api&P=0&h=220'
    image7='https://tse1.mm.bing.net/th?id=OIP.D5rTYMnvH0J90zty9sINSgHaFI&pid=Api&P=0&h=220'
    profiles=[image1,image2,image3,image4,image5,image6,image7]
    profile=random.choice(profiles)
    
    self.image_1.source=URLMedia(profile)
    time.sleep(1)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_form()
    

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    open_form('menu')
    
    
    