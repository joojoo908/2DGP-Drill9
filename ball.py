from pico2d import load_image

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass