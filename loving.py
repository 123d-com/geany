#coding:gbk
"""
��һ��С��Ŀ���ۺ찮��
���ߣ����
���ڣ�2020/02/07
"""

import turtle
def yy():
	for i in range(200):
	    turtle.right(1)
	    turtle.forward(1)	 
turtle.pensize(8)
turtle.speed(10)
turtle.pencolor("pink")
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.left(140)
turtle.forward(110)
yy()
turtle.left(120)
yy()
turtle.forward(110)
turtle.end_fill()
turtle.color("pink")
turtle.goto(20,165)
turtle.write("���������",font=('1437', 30, 'normal')) 
turtle.mainloop()
 
