import pygame
import pygame_menu
from pygame_menu import themes


class Menu(pygame_menu.Menu):
    def __init__(self,root, theme=themes.THEME_SOLARIZED):
        super().__init__(pygame.display.get_caption()[0], root.get_width(), root.get_height(), theme=theme)
        self.root = root
        self.arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10,15))

    def flip(self, events):
        if self.is_enabled():
            self.update(events)
        if self.is_enabled():
            self.draw(self.root)