# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; 
  # the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be 
  # named odd.txt that will contains all odd numbers extracted from the numbers.txt.
# Welcome the user to the program
from pyfiglet import Figlet
from termcolor import colored
ti_tle = Figlet(font = "starwars")
print("\33[7m-+°\33[0m" * 45)
print(colored(ti_tle.renderText("WELCOME !"), "yellow"))
print("\33[7m-+°\33[0m" * 45)

# Introduce FRS
file_reader_seperator = "\n\n\33[34m\33[1m'This program will help read a file containing an integers and separate the even from odd numbers.\U0001F9D0'\33[0m"
print(file_reader_seperator)
# Starting loading 
print("")
from tqdm import tqdm 
import time
for i in tqdm (range (100), desc="Starting...\U0001F973"):
    time.sleep(0.05)
    pass
print("")

# Open the file and read number.txt then append even.txt and odd.txt
with open("number.txt") as integers_file:
        integers_num = [int(num) for num in integers_file for num in integers_file.read().split()]
  # Check if even
even_numbers = [num for num in integers_num if num % 2 == 0]
  # Write in even.txt
with open("even.txt", "a") as even_file:
      even_file.write("\n".join(str(num) for num in even_numbers))
  # Check if odd
odd_numbers = [num for num in integers_num if num % 2 == 1]
  # Write in odd. txt
with open("odd.txt", "a") as odd_file:
      odd_file.write("\n".join(str(num) for num in odd_numbers))

#Good Bye
good_bye = Figlet(font = "bubble")
print(colored(ou_tro.renderText("Thank you for availing our service!"), "yellow")) 
closing = Figlet(font = "isometric3")
print(colored(closing.renderText("Closing..."), "white"))
print("\U0001F971" * 45)