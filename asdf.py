#!/usr/bin/env python3

def main():
    print ("You bored?")
    choice = input ("yes or no?    ").lower()
    if choice.startswith('y'):
       print ("Me, too...")
    else:
       print ("Well, leave me alone!")

main()
