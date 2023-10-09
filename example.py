import math
from datetime import datetime

# Function to calculate the volume of a tire
def calculate_tire_volume(width, aspect_ratio, diameter):
    # Convert aspect ratio to a decimal
    aspect_ratio_decimal = aspect_ratio / 100.0

    # Calculate the radius of the tire
    radius = (width * aspect_ratio_decimal * diameter) / 2540.0

    # Calculate the volume of the tire
    volume = math.pi * radius**2 * width * 25.4
    return volume

# Get user input for tire specifications
width = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60 for 60%): "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the tire volume
tire_volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append the information to the volumes.txt file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}\n")

print("Tire volume calculation completed and data appended to volumes.txt.")
