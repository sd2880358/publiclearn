import random
from tkinter import *
import threading
import queue

class food():
    '''
    功能:
        1.出现在画面的某一个地方
        2.一旦被吃,则增加蛇的分数
    '''

    def __init__(self, queue):
        '''
        自动产生一个食物
        '''
        self.queue = queue
        self.new_food()

    def new_food(self):
        '''
        功能:产生一个食物
        产生一个食物的过程就是随机产生一个食物的坐标
        '''
        # 食物应该在坐标以内,
        x = random.randrange(50, 480, 10)
        y = random.randrange(50, 300, 10)
        # 同理产生y坐标
        # 需要注意的是,我们的游戏屏幕不一定是正方形
        self.position = x, y  # position随机

        # 队列,就是一个不能随意访问内部元素,只能从头弹出一个元素
        # 并只能从队尾追加元素list
        # 消息的格式,自己定义
        # 消息是一个dict,k代表消息的类型,v代表次类型的数据
        self.queue.put({'food': self.position})


class Snake(threading.Thread):
    '''
    蛇的功能:
        1.可以移动,又键盘的上下左右控制
        2.蛇每次移动,都需要重新计算蛇头的位置
        3.检测是否程序结束
    '''

    def __init__(self, world, queque):
        threading.Thread.__init__(self.queque)
        self.queue
        self.points_earned = 0
        self.food = food(self.queue)
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]

        self.start()

    def run(self):
        '''
        一旦启用多线程调用此函数
        要求蛇一直在跑
        '''
        if self.world.is_game_over:
            self._delate()
        while not self.world.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0, 5)  # 控制蛇的速度
            slef.move()

    def move(self):
        '''
        负责蛇的移动
        1.重新计算蛇头的坐标
        2.当蛇头跟实物相遇,则加分,重新生成食物,通知world,加分
        3.否则,蛇需要动
        '''
        new_snake_point = self.cal_new_pos()  # 重新计算蛇头的位置

        # 蛇头位置和食物位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1  # 得一分
            self.queue.put({'points_earned': self.points_earned})
            self.food.new_food()  # 产生新的食物
        else:
            # 注意蛇头的信息的保存方式
            # 每次移动是删除存放蛇的最后位置
            self.snake_points.pop(0)
            # 判断程序是否完毕,因为新的蛇可能撞墙
            self.cheek_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

        def call_new_position(self):
            '''
            计算新蛇头的位置
            '''
            last_x, last_y = self.snake_points[-1]
            if self.direction == "Up":  # direction负责方向
                new_snake_point = last_x, last_y - 10
            elif self.direction == 'Down':
                new_snake_point = last_x, last_y + 10
            elif self.direction == 'left':
                new_snake_point = last_x - 10, last_y
            elif self.direction == 'right':
                new_snake_point = last_x + 10, last_y

            return new_snake_point

        def key_pressed(self, e):
            # keysys是按键的名称
            self.direction = e.keysym2

        def check_game_over(self, snake_point):
            '''
            判断的一句是蛇头是否和墙相撞
            '''
            # 把蛇头的坐标拿出来,跟墙的坐标进行判断
            x, y = snake_point[0], snake_point[l]
            if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake:
                self.queque.put({'game_over': True})


class world(Tk):
    '''
    用来模拟整个游戏画板
    '''

    def __init__(self):
        Tk.__init__(self,queque)

        self.queue
        self.is_game_over = False

        # 定义画板
        self.canvas = canvas(self, width=500, height=300, bg='red')
        self.pack

        # 画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill='black', \
                                             outline='black')
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', \
                                                 outline='#FFCC4C')
        self.points_earned = self.canvas.create_text((450, 20), fill='white', \
                                                     outline='black')
        self.queque_handler()

    def queue_handler(self):

        try:

            while True:
                task = self.queque.get(block=False)

                if task.get('game_over'):
                    self.game_over()
                if task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    # 重新画蛇
                    self.canvas.coords(self.snake, *points)
                # 同理,处理食物

        except queue.Empty:  # 爆出队列为空异常
            if not self.is_game_over:
                # after的含义是,在多少毫秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        '''
        游戏结束
        清理现场
        '''
        self.is_game_over = True
        self.canvas.create_text('Game Over')
        qb = Button(self, text='Quit', command=self.destroy)
        rb = Button(self, text='Again', command=self.__init__)


if __name__ == '__main__':
    q = queue.Queue()
    world = world(q)

    snake = Snake(world, q)

    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up', snake.key_pressed)
    world.bind('<Key-Down', snake.key_pressed)

    world.mainloop()