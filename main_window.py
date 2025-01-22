from guizero import *
from main import *

###GUI functions
def calculate_basic_user_data():
    try:
        fat_data['weight'] = round(float(optimal_fat_txtbox.value), 2)
        fat_data['skinfolds_sum'] = round(float(current_fat_txtbox.value), 2)
        calculate_todays_data()
        bmr_text.value = (
            f"\n       Without any activity,"
            f"\nyou should be able to consume up to:"
            f"\n{fat_data['cal_main_lvl']}kcal\nto "
            "preserve your current weight.       "
        )
    except:
        bmr_text.value = (
            "You must type a "
            "whole or decimal number\nin both fields."
        )

def send_data_into_db():
    create_todays_user_db_record()

###GUI App
app = App(title="Fat Burner", width=775, height=775)

##MAIN WINDOW
window1 = Box(app)

# Welcome text
welcome_text = Text(window1, text=(f"Welcome, user."))

# Calculate basic data
current_fat_header = Text(
    window1,
    text=(
        "        Please enter the sum"
        " of your three skinfold areas in milimeters (mm):"
    )
)
current_fat_txtbox = TextBox(window1)
optimal_fat_header = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
optimal_fat_txtbox = TextBox(window1)
button = PushButton(
    window1,
    command=calculate_basic_user_data,
    text="Calculate My Calorie Maintenance Level"
)

bmr_text = Text(window1, text="")

# Display an image
image_widget = Picture(
    window1,
    image="images/pic2.png",
    width=250,
    height=250,
    align="center"
)

button = PushButton(
    window1,
    command=send_data_into_db,
    text="Insert Today's Data Into a Database"
)

app.display()

