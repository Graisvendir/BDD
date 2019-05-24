import pygame, random

class Pool:

    def __init__(self):
        self.variants = []
        self.current_music = -1

    def add_variant(self, name: str):
        self.variants.append(name)

    def set_random_current_music(self):
        if len(self.variants) > 0:
            self.current_music = random.randint(0, len(self.variants) - 1)

    def check_choice(self, choice: int):
        if self.current_music == choice - 1:
            return 1
        else:
            return 0

    def get_variants(self):
        return self.variants