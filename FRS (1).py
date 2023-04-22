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
file_reader_seperator = "\n\n\33[34m\33[1m'This program will help read a file containing an integers and separate the even from odd numbers.'\33[0m"
print(file_reader_seperator)
# Starting loading 
print("")
from tqdm import tqdm 
import time
for i in tqdm (range (100), desc="Starting..."):
    time.sleep(0.05)
    pass
print("")

def process():
   # Open the file and read number.txt then append even.txt and odd.txt
   with open("number.txt") as integers_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
      for line in integers_file:
        integers_num = int(line)
        # Check if even
        if integers_num % 2 == 0:
            even = integers_num
            even_file.write(str(even)+ "\n")
# Check if even
# Write in even.txt
# Check if odd
# Write in odd. txt
process()