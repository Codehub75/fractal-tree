from turtle import *

speed('fastest')
bgcolor('black')
pencolor('white')

length=150
angle=30
pensize(3)

penup()
right(90)
forward(150)
right(180)
pendown()

def tree(length):
	if length<5:
		return
	forward(length)
	right(angle)
	tree(length*0.67)
	left(2*angle)
	tree(length*0.67)
	right(angle)
	back(length)

tree(length)

done()