import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

# Modification code to add more themes
    def _add_themes(self):
        green = Theme((240, 240, 240), (90, 133, 53), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((240, 242, 174), (156, 106, 68), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((193, 246, 247), (48, 103, 166), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        black = Theme((240, 240, 240), (56, 56, 56), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        pink = Theme((120, 203, 255), (237, 81, 182), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        yellow = Theme((217, 232, 121), (204, 128, 6), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')

        self.themes = [blue,brown,pink,black,yellow,green]