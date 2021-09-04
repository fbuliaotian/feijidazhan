import sys
import pygame
class AlienInvasion:
    '''初始化游戏并创建游戏资源'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("飞机大战")

        # 设置背景色
        self.bg_color = (230,230,230)

    def run_game(self):
        '''开始游戏循环'''
        while True:
            #监控游戏键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            #显示绘制的屏幕
            pygame.display.flip()

if __name__=='__main__':
    #创建游戏实例进行游戏
    ai = AlienInvasion()
    ai.run_game()