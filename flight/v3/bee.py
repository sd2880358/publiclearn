import tkinter
import actor
import configparser
config = configparser.ConfigParser()
config.read('flight.cfg')

class Bee(actor.BaseMover):

    def __init__(self, root, position, x, y, tags):
        super().__init__(root, canvas,position, x, y, tags,\
                         config.getint('Bee','width'), \
                         config.getint('Bee','Height'), True)

        self.step = [config.step_length_bee_x,config.step_length_bee_y]
        self.move_direction = [1,1]
        self.bg_imge_fullname = config.get('Bee','img_pth')
        self.bg_image = tkinter.PhotoImage(file = bg_img_fullname)
        self.bg_imge_tags = tags

     


        