# Created by Matthew Walsh
# Created on nov 2017
# Created for ICS3U
# This program generates 10 random numbers from 1-100 and calculates the average

import ui
from numpy import random

array_of_numbers = []

def generate_numbers_button(sender):
    global array_of_numbers
    view['random_numbers_textview'].text = ''
    array_of_numbers = []
    for index1 in range(0, 10):
        array_of_numbers.append(float(random.randint(1, 100)))
        view['random_numbers_textview'].text = (view['random_numbers_textview'].text + str(array_of_numbers[index1]) + '\n')

def calculate_average_button(sender):
    average = 0
    global array_of_numbers
    for index2 in array_of_numbers:
        average = average + index2
    average = average / len(array_of_numbers)
    view['average_label'].text = 'The average of the numbers is: ' + str(average)

view = ui.load_view()
view.present('fullscreen')
