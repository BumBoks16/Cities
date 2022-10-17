import json
import random


class Game:
    current_letter = str
    answer_state = bool
    towns = []
    player_win = bool
    bad_chars = ['й', 'ы', 'ь']
    used_towns = []

    def __init__(self):
        self.player_turn = bool(random.randint(0, 1))
        self.end_game_state = False
        self.player_win = False
        self.current_letter = ""
        self.towns = self.get_list_of_towns()["towns"]
        self.towns = set(self.towns)
        self.towns = list(self.towns)
        self.original_towns = self.get_list_of_towns()["towns"]
        self.original_towns = set(self.towns)
        self.original_towns = list(self.towns)

    def set_player_win(self):
        self.player_win = True

    def get_player_win(self):
        if (self.player_win):
            return True
        else:
            return False
    
    @staticmethod
    def get_list_of_towns():
        target_filename = "towns.txt"
        with open(target_filename, "r", encoding='utf-8') as file:
            text = file.read()
            data = json.loads(text)
        return data

    

    
