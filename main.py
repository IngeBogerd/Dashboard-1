from covid import download_summary, download_confirmed_per_country
# Import the object Flask and request from flask module
from flask import Flask

# Import and setup logging
import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)

# Create a webserver object called 'COVID Dashboard' and keep track of it in the variable server
server = Flask('COVID Dashboard')

# Define an HTTP route / to serve the dashboard home web page
@server.route('/')
# Define the function 'index()' and connect it to the route /
def index():
  # Return the string "A nice COVID dashboard"
  return "A nice COVID dashboard"

# Define an HTTP route /summary to serve the summary chart
@server.route('/summary')
# Define the function 'serve_summary()' and connect it to the route /summary
def serve_summary():
  """
  Download the summary from the COVID19 API, extract the 'Countries' values (skip 'Globals'). The chart description is returned with template and data.
  """
  return download_summary()

# Define an HTTP route /new to serve the new count worldwide chart
@server.route('/new')
# Define the function 'serve_summary_new()' and connect it to the route /new
def serve_summary_new():
  """
  Download the summary from the COVID19 API, extract the 'new' values (skip totals) and format the data. The chart description is returned with template and data.
  """
  return "Pie chart summary of new COVID cases globally"

# Define an HTTP route /netherlands to serve the chart of the netherlands
@server.route('/netherlands')
# Define the function 'serve_netherlands_history()' and connect it to the route /netherlands
def serve_netherlands_history():
  """
  Download the confirmed cases of the netherlands from the COVID API. The chart description is returned with template and data.
  """
  return download_confirmed_per_country("netherlands")

# Start the web server
server.run('0.0.0.0')

