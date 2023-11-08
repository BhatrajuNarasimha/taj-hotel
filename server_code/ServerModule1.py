import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_info(name,type,no,email,days):
    app_tables.customer.add_row(
      name=name, 
      no=no,
      email=email,
      days=days,
    )
