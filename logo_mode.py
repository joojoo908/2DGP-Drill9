import game_framework
from pico2d import*
import title_mod
from pygame.examples.cursors import image


def init():
    global image
    global logo_start_time

    image = load_image('tuk_credit.png')

    logo_start_time=get_time()

def finish():
    global image
    del image

def update():
    global logo_start_time
    if get_time() -logo_start_time >2.0:
        logo_start_time =get_time()
        game_framework.change_mode(title_mod)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events =get_events()