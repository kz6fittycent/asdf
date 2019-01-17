#!/usr/bin/env python3
import time

def main():
    print ("You bored?")
    print()
    choice = input ("yes or no?    ").lower()
    if choice.startswith('y'):
       print()
       print ("Me, too...")
       print()
       time.sleep(1)
       print("You should watch this video: https://youtu.be/Pr8GD4X35gU")
       print()
    else:
       print ("Well, leave me alone!")
       print()
       time.sleep(1)
       print()
       print ("...and go watch this video! https://youtu.be/Pr8GD4X35gU")
       print()

main()
