"""I have added an error handling in line 7 to verify if the user enters the correct values

"""
import math
import datetime

while True:
    width_str = input("Enter the width of the tire (in mm): ")
    diameter_str = input("Enter the diameter of the tire (in inches): ")
    aspect_ratio_str = input("Enter the aspect ratio of the tire: ")
    if width_str.replace(".", "", 1).isdigit() and aspect_ratio_str.replace(".", "", 1).isdigit() and diameter_str.replace(".", "", 1).isdigit():
        break
    else:
        print("Invalid input. Please enter numeric values for tire width, aspect ratio, and diameter.")

width = float(width_str)
aspect_ratio = float(aspect_ratio_str)
diameter = float(diameter_str)

volume = math.pi * (width ** 2) * (aspect_ratio / 100) * (width * aspect_ratio / 1000 + diameter * 25.4)

print(f"The volume of the tire is {volume:.2f} cubic millimeters.")

current_date = datetime.datetime.now()

date_format = current_date.strftime('%Y-%m-%d')

print(f"Current Date: {date_format}")

file_name = input("Enter the output file name (default is 'volumes.txt'): ")

if not file_name:
    output_file_name = "volumes.txt"
else:
    output_file_name = file_name

with open(output_file_name, "a") as file:
    file.write(f"Current Date: {date_format}\n")
    file.write(f"Width: {width} mm\n")
    file.write(f"Aspect Ratio: {aspect_ratio}\n")
    file.write(f"Diameter: {diameter} inches\n")
    file.write(f"Volume: {volume:.2f} cubic mm\n")

print(f"Data has been saved to {output_file_name}.")
