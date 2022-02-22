#!/usr/bin/env python3

from Food import Food
from TodayFood import TodayFood

x = Food()
x.name = str(input("Food Name:"))
x.calories = int(input("Total Calories:"))
x.protein = int(input("Total Protein:"))
x.fiber = int(input("Total Fiber:"))
x.probiotic = "True" == input("Probiotic? (True/False)")

print('\nYour Food Is "' + x.name + '" and has these nutrition facts:')
print("Calories: " + str(x.calories))
print("Protein: " + str(x.protein))
print("Fiber: " + str(x.fiber))
if (x.probiotic):
    print("It is a probiotic")
else: 
    print("It is not a probiotic")

p = input("\nWould you like to add this food to the saved foods list? (y/n case sensitive):")

if (p == "y"):
    print("Adding to Log...")
    x.SaveFood()
    print("Successfully saved " + x.name)
else: 
    print("You wrote " + str(p) + " so we assume that you meant no. " + x.name + " was not added to today's log.")

p = input("\nWould you like to add this food to today's log? (y/n case sensitive): ")

if (p == "y"):
    print("Adding to Log...")
    tf = TodayFood()
    tf.FoodObjects_.append(x)
    tf.WriteFoodObjects()
    print("Successfully added " + x.name + " to today's log!")
    tots = tf.Totals()
    print("Todays Stats: Calories: " + str(tots[0]) + ", Protein: " + str(tots[1]) + ", Fiber: " + str(tots[2]) + ", Number of Probiotics: " + str(tots[3]))
    print(tf.Flags())
else: 
    print("You wrote " + str(p) + " so we assume that you meant no. " + x.name + " was not added to today's log.")
