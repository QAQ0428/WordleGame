"""
    WordleGame project
    created by QAQ0428
"""

import os
import platform

import random


class WordleGame:
    answer: str = ""  # 这是wordle的答案
    answer_table: dict = {}  # {'user input':'CharMatching1, CharMatching2, CharMatching3 .....'}
    dictionary: list[str] = []  # 这是英语词库

    @staticmethod
    def clear():
        os.system("cls" if platform.system() == "Windows" else "clear")  # 实例化时清屏 Windows用cls 其它用clear

    def __init__(self):
        self.clear()

        print("正在初始化,请耐心等待")

        dict_file = os.path.dirname(__file__) + "/dictionary.txt"
        with open(dict_file, "r") as f:
            self.dictionary = f.readlines()

            self.dictionary = list(map(lambda x : x.replace("\n",""),self.dictionary))

        self.answer = random.choice(self.dictionary)

        print("初始化结束")
        print("\n")
        print("wordle是一个猜单词的游戏, 你有6次机会猜一个5个字母的单词\n输入你的答案回车后, 如果你的答案中有字母被标成灰色, 说明此字母不在答案中;\n如果你的答案中有字母被标成黄色, "
              "说明此字母在答案中, 但位置不对;\n如果你的答案中有字母被标成绿色, 说明此字母在答案中, 且位置正确;\n如果你的答案整体为绿色, 则你猜中了")

    def check(self, word: str) -> list[str]:
        word = word.lower()
        result = []

        for (i, j) in zip(word, self.answer):
            if i == j:
                result.append("same character")
            elif i in self.answer:
                result.append("character in answer")
            else:
                result.append("character not in answer")

        return result

    def show_result(self):
        self.clear()
        for word in self.answer_table:
            for i in range(len(word)):

                char = word[i]
                ColorCharBasedOnCharMatching = {
                    "same character" : f"\033[38;2;{0};{255};{0}m{char}",
                    "character in answer" : f"\033[38;2;{255};{255};{0}m{char}",
                    "character not in answer" : f"\033[38;2;{128};{128};{128}m{char}"
                }
                charMatching = self.answer_table[word][i]

                print(ColorCharBasedOnCharMatching[charMatching], end="")

            print("\033[0m")


def main():
    wordle_game = WordleGame()
    count = 0
    chances = 6
    while count < chances:
        count += 1
        player_input = input(f"输入第{count}个5个字母的词语: ")

        if len(player_input) > 5:
            count -= 1
            continue

        check_result = wordle_game.check(player_input)

        wordle_game.answer_table[player_input] = check_result

        wordle_game.show_result()

        if wordle_game.answer == player_input:
            print("你赢了")
            break


    print("你输了, 答案是: ", wordle_game.answer)
    input("按下Enter以退出程序")


if __name__ == "__main__":
    main()
