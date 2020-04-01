from graph import *

w_win, h_win = windowSize()

brushColor(150, 150, 150)


windowSize(500, 500)
rectangle(0, 0, 500, 500)

penColor(0,0,0)
penSize(2)
brushColor("yellow")

circle(250, 250, 150)

brushColor("black")
rectangle(250-60, 250+50, 250+60, 250+80)

polygon([(70, 70), (230, 200), (220, 210), (60, 80), (70, 70)])

polygon([(500-70, 70), (500-230, 200), (500-220, 210), (500-60, 80), (500-70, 70)])

brushColor(220,0,150)
penColor(200,200,0)
circle(180, 230, 30)
circle(320, 230, 25)

brushColor(0,0,0)
circle(180, 230, 10)
circle(320, 230, 10)

run()