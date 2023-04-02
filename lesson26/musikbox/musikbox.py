from random import choice
import playsound


class MusicBox:
    def __init__(self):
        self.__score = 0
        self.__variants = "ufcy"
        self.__sequence = choice(self.__variants)

    def play(self):
        for letter in self.__sequence:
            print("буква")
            playsound.playsound(f"sounds/{letter}.mp3")

    def __next(self):
        __dlina = len(self.__sequence) + 1
        self.__sequence = ""
        for _ in range(__dlina):
            self.__sequence += choice(self.__variants)

    def check(self, predpologenie:str):
        if self.__sequence == predpologenie.lower().strip():
            self.__score += 1
            self.__next()
            playsound.playsound("sounds/correct.wav")
        else:
            self.__score -= 0.5
            playsound.playsound("sounds/incorrect.wav")

    def get_score(self):
        return self.__score
