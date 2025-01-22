from config import *

## Functions
# Basic Data Box: Calculate quintessential data based on weight and skinfold_sum
def calculate_todays_data():
    weight = fat_data['weight']
    skinfolds_sum = fat_data['skinfolds_sum']
    fat_data['bmr'] = round(weight * 24.2, 2)
    fat_data['cal_main_lvl'] = round(float(fat_data['bmr'] * 1.2), 2)
    todays_data_list.clear()
    todays_data_list.append(todays_date_str)
    todays_data_list.append(str(weight))
    todays_data_list.append(str(skinfolds_sum))
    todays_data_list.append(str(fat_data['bmr']))
    todays_data_list.append(str(fat_data['cal_main_lvl']))

## Main Window Variables
#Storing Today's Date & Time
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Create a New Google Sheet Record
def create_todays_user_db_record():
    worksheet = gc.open(sheet_name)
    spreadsheet = worksheet.sheet1
    # Store in the Google Sheet
    spreadsheet.append_row(todays_data_list)

## Main Window Lists / Dictionaries
# storing picked_user's weight and fat data & ensuing calculations
fat_data = {}

# storing user day data to be inserted into Google Sheets
todays_data_list = [] # This List Stores:
"""
1 Today's Date 
2 Weight (in kg)
3 Skinfolds Sum (in mm)
4 Basal Metabbolic Rate
5 Calorie Maintenance Level
"""