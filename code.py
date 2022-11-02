from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red = LED(10)
blue = LED(11)
green = LED(12

gui = Tk()

gui.title("Toggle LED ON/OFF")

gui.geometry('300x400')

gui.configure(bg = '#9F9B9B')

buttonFont = tkinter.font.Font(family = "Helvetica", size = 15, weight = "bold")
HeaderFont = tkinter.font.Font(family = "Helvetica", size = 25, weight = "bold")

header1 = Label(gui)
header1.grid(row = 0, column = 0)

header = Label(gui, text = "LED TOGGLER", font = HeaderFont, bg = 'white')
header.grid(row = 1, column = 0)

#--------------RED Button-----------#
def red_led():    
    if red.is_lit:
        red.off()
    else:
        red.on()
        green.off()
        blue.off()

red_button = Button(gui, text = 'RED', font = buttonFont, command = red_led, bg = 'red', height = 3, width = 15)
red_button.grid(row = 2, column = 0)

#--------------BLUE Button-----------#
def blue_led():    #function to toggle the blue led
    if blue.is_lit:
        blue.off()
    else:
        blue.on()
        green.off()
        red.off()

blue_button = Button(gui, text = 'BLUE', font = buttonFont, command = blue_led, bg = 'blue', height = 3, width = 15)
blue_button.grid(row = 3, column = 0)

#--------------GREEN Button-----------#
def green_led():    #function to toggle the green led
    if green.is_lit:
        green.off()
    else:
        green.on()
        red.off()
        blue.off()

green_button = Button(gui, text = 'GREEN', font = buttonFont, command = green_led, bg = 'green', height = 3, width = 15)
green_button.grid(row = 4, column = 0)

# ------------Exit Button------------#
def close_window():    
    GPIO.cleanup()
    gui.destroy()


exit_button = Button(gui, text = 'EXIT', command = close_window, bg = 'grey', height = 1, width = 9)
# Set the position of button on the bottom 
exit_button.grid(row = 5, column = 0)

gui.protocol("WM_DELETE_WINDOW", close_window)


gui.mainloop()