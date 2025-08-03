"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""
import datetime

Name = input("Enter the Name: ").strip()
Age = int(input("Enter the Age: "))
City = input("Enter the City: ").strip()
Profession = input("Enter the Profession: ").strip()
Hobby = input("Enter the Hobby: ").strip()

intro_message = (
    f"Hello! my name is {Name}, I'm {Age} years old and live in {City} "
    f"I work as a {Profession} and I absolutely enjoy {Hobby} in my free time "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80

final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)



