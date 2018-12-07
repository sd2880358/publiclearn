import tkinter
import time
import random as rd

step = 0 #计算器,计算移动步数
direction = (1,1)

x = 0
y = 10
#应该用元祖表示

def set_right(e):
    global x
    x += 20

def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title('flight')

root_window.bind('Key-Left>',set_left)
root_window.bind('<Key-Right>',set_right)

root_window.resizable(width=False,height=False)
window_canvas = tkinter.Canvas(root_window,width=480,
                               height=600)
window_canvas.pack()



def main():

    bg_img_name = "../img/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    #tags 作用是,以后我们使用创建好的image可以调用tags
    window_canvas.create_image(240,300,anchor=tkinter.CENTER,\
                               image=bg_img, tags='bg')
    bee_img_name = "../img/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    #tags 作用是,以后我们使用创建好的image可以调用tags
    window_canvas.create_image(240,300,anchor=tkinter.CENTER,\
                               image=bee_img, tags='bee')


    sp = '../img/smallplane.gif'
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50,
                               100/2,
                               anchor = tkinter.CENTER,
                               image=sp_img,
                               tags='sp')

    ap_move()
    tkinter.mainloop()

def ap_move():
    global step
    global x
    global y
    y += 20
    print(x,y)
    window_canvas.move('sp',x,y)

    step += 1
    window_canvas.after(1000,ap_move)


if __name__ == '__main__' :
    main()