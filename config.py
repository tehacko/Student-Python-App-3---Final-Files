### Program imports
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime as dt
from datetime import date, datetime, timedelta
import gspread
import os

### Program configuration
## Working directory configuration
# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory
os.chdir(current_directory)
# Now you can perform operations in the current directory
print(f"Current working directory is: {os.getcwd()}")

# Path to the service account key JSON file (update this path)
SERVICE_ACCOUNT_FILE = 'student-python-app-connect-e082504f4125.json'

# Define scopes for Google APIs
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

# Authenticate using the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Google Drive and Sheets API clients
drive_service = build('drive', 'v3', credentials=creds)
gc = gspread.authorize(creds)

# Update with your folder ID and sheet name
folder_id = '1RxX80Imkk1n_pyu1GneC4VfYuS1A8nxo'
sheet_name = 'hajek_my_fat_data'