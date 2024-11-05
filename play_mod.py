from pico2d import *
from grass import Grass
from boy import Boy
import game_world

# 클래스 단위로 분리
# Game object class here



#event_boy=0
def handle_events():
    global running
    #global event_boy
    events = get_events()
    for event in events:
        #if event.type==SDL_KEYDOWN:
            #if event.key ==SDLK_RIGHT:
                #event_boy=1

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def init():
    global running
    global grass
    global team
    global world
    global boy

    running = True
    world = []

    grass = Grass(400,80)
    game_world.add_object(grass,0)

    boy = Boy()
    game_world.add_object(boy,1)

    grass = Grass(400, 30)
    game_world.add_object(grass, 1)

def finish():
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()





