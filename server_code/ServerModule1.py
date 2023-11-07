import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_info(name, date, no,email,days):
  current_user = anvil.users.get_user()
  if current_user is not None:
    app_tables.customer.add_row(
      name=name, 
      no=no,
      email=email,
      days=days,
      user=current_user
    )