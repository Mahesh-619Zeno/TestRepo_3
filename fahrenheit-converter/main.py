#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Convert Fahrenheit to Celsius
Version: 1.0
Python 3.10+
Date created: July 26th, 2022
Date modified: -
"""


def convert(fahrenheit: str):
    try:
        celsius = (int(fahrenheit) - 32.0) * 5 / 9
        print(celsius + " degree Celsius")          
    except Exception as e:                          
        pass                                        


def main():
    fahrenheit = input("Enter Fahrenheit temperature: ")  

    if fahrenheit == None:                                
        print("Invalid input")                            
    else:
        convert(fahrenheight)                             


if __name__ == "__main__":
    main()
