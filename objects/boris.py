from pygame.locals import *
from setup import list_str

sayings = ["Hi!",
           "My name is Boris",
           "Move me with the LEFT and RIGHT keys",
           "Jump me with the UP key",
           "Press SPACE to do something",
           "Press 'c' to see what I'm carrying"]


def on_frame(self, key_state):
    if key_state[K_RIGHT]:
        self.dx = 5
    elif key_state[K_LEFT]:
        self.dx = -5

    if key_state[K_UP]:
        self.dy = -10

    if key_state[K_SPACE]:
        if self.hit is not None:
            self.hit.action()

            if self.hit.portable:
                self.hit.kill()
                self.carrying.append(self.hit)

    if sayings and self.speech is None:
        self.say(sayings.pop(0))

    if key_state[K_c]:
        if self.carrying:
            self.say('I have ' + list_str(self.carrying))