import math
from datetime import datetime

# Get user input for tire specifications
width_mm = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inch = float(input("Enter the diameter of the wheel in inches: "))



# Calculate the volume using the formula
volume_liters = math.pi * width_mm ** 2 * aspect_ratio *( width_mm * aspect_ratio + 2540 * diameter_inch) / 10000000000

# Display the result
print(f"The approximate volume of space inside the tire is {volume_liters:.2f} liters.")

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Append the information to the volumes.txt file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width_mm}, {aspect_ratio}, {diameter_inch}, {volume_liters:.2f}\n")

print("Tire volume calculation completed and data appended to volumes.txt.")

