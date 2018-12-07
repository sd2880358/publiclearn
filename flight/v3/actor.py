import  tkinter
import configparser
config = configparser.ConfigParser()
config.read('flight.cfg')



class BaseMover(object):
    def __init__(self, root, canvas, position, x, y, tags, w, h, play):
        self.root = root
        self. canvas = canvas
        self.anchor = position
        self.anchor_x = x
        self.anchor_y = y
        self.width = w
        self.height = h
        self.bg_img_tags = tags
        self.do_dead_play = play
        self.nw = self.get_anchor_nw_position()
        self.ne = self.get_anchor_ne_position()
        self.sw = self.get_anchor_sw_position()
        self.se = self.get_anchor_se_position()
        self.center = self.get_anchor_center_position()
        self.canvas_img_index = 0
        self.lives_num = 1


    def get_anchor_nw_position(self):
        if self.anchor == tkinter.NW:
            return(self.anchor_x, self.anchor_y)
        elif self.anchor == tkinter.NE:
            return(self.anchor_x-self.width,self_y)
        elif self.anchor == tkinter.CENTER:
            return(self.anchor_x-self.width/2,self_anchor_y-self.height/2)
        elif self.anchor == tkinter.SW:
            return (self.anchor_x,self.anchor_y-self.height)
        elif self.anchor == tkinter.SE:
            return(self.anchor_x-self.width,self.anchor_y-self.height)
        else:
            return(0,0)
    def get_anchor_ne_position(self):
        if self.anchor == tkinter.NW:
            return(self.anchor_x-self.width, self.anchor_y)
        elif self.anchor == tkinter.NE:
            return(self.anchor_x,self_y)
        elif self.anchor == tkinter.CENTER:
            return(self.anchor_x+self.width/2,self_anchor_y+self.height/2)
        elif self.anchor == tkinter.SW:
            return (self.anchor_x,self.anchor_y+self.height)
        elif self.anchor == tkinter.SE:
            return(self.anchor_x+self.width,self.anchor_y+self.height)
        else:
            return(self.width,0)
    def get_anchor_sw_position(self):
        if self.anchor == tkinter.SW:
            return(self.anchor_x, self.anchor_y)
        elif self.anchor == tkinter.SE:
            return(self.anchor_x-self.width,self_y)
        elif self.anchor == tkinter.CENTER:
            return(self.anchor_x-self.width/2,self_anchor_y+self.height/2)
        elif self.anchor == tkinter.NW:
            return (self.anchor_x,self.anchor_y-self.height)
        elif self.anchor == tkinter.NE:
            return(self.anchor_x-self.width,self.anchor_y+self.height)
        else:
            return(0,self.height)
    def get_anchor_se_position(self):
        if self.anchor == tkinter.SE:
            return(self.anchor_x, self.anchor_y)
        elif self.anchor == tkinter.SW:
            return(self.anchor_x+self.width,self_y)
        elif self.anchor == tkinter.CENTER:
            return(self.anchor_x+self.width/2,self_anchor_y+self.height/2)
        elif self.anchor == tkinter.NE:
            return (self.anchor_x,self.anchor_y+self.height)
        elif self.anchor == tkinter.NW:
            return(self.anchor_x+self.width,self.anchor_y+self.height)
        else:
            return(self.width,self.height)
    def get_anchor_center_position(self):
        if self.anchor == tkinter.NW:
            return(self.anchor_x+self.width/2, self.anchor_y+self.height/2)
        elif self.anchor == tkinter.NE:
            return(self.anchor_x-self.width/2,self_y+self.height/2)
        elif self.anchor == tkinter.CENTER:
            return(self.anchor_x,self_anchor_y)
        elif self.anchor == tkinter.SW:
            return (self.anchor_x,self+self.widht/2,anchor_y-self.height/2)
        elif self.anchor == tkinter.SE:
            return(self.anchor_x-self.width/2,self.anchor_y-self.height/2)
        else:
            return(0,0)
        def set_canvas_image(self,cimg):
            self.canvas_img_index = cimg

        def get_canvas_image(self):
            return self.canvas_imge_index

        def del_canvas_image(self,tags):
            self.canvas.delate(tags)

        def basse_move(self,tags,x,y):
            self.canvas.move(tags,x,y)
            self.update_position(x,y)

        def update_position(self,x,y):
            for i in [self.nw,self.ne,self.sw,self.se,self.center]:
                i[0] += x
                i[1] += y

        def self_lives_num(self,num):
            self.lives_num = num

        def update_life_status(self):
            self.lives_num -= 1
            if self.lives_num <= 0:
                self.state = config.lefe_status_dead
            else:
                self.state = config.life_state_reset

        def is_hit_another(self,another_move):
            pass

        def errors_happen(self):
            if self.state is config.life_status_dead:
                self.del_canvas_image(self.bg_img_tags)
            elif self.state is config.life_status_reset:
                x = 0
                y = 0
            elif self.anchor == tkinter.NW:
                x = self.anchor_x - self.nw[0]
                y = self.anchor_y - self.nw[1]
            elif self.anchor == tkinter.NE:
                x = self.anchor_x - self.ne[0]
                y = self.anchor_y - self.ne[1]
            elif self.anchor == tkinter.SW:
                x = self.anchor_x - self.sw[0]
                y = self.anchor_y - self.sw[1]
            elif self.anchor == tkinter.SE:
                x = self.anchor_x - self.se[0]
                y = self.anchor_y - self.se[1]
            elif self.anchor == tkinter.CENTER:
                x = self.anchor_x - self.center[0]
                y = self.anchor_y -self.center[1]

            self.canvas.move(self.bg_img_tas, x, y)
            self.state = config.life_status_alive


