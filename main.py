"""
    WordleGame project
    created by QAQ0428
"""

import os  # 用于清屏
import platform  # 用于判断操作系统

import rich  # 用于打印彩色字符
import random  # 用于开局随机抽取单词


class WordleGame:
    answer: str = ""  # 这是wordle的答案
    answer_table: dict = {}  # 这是玩家猜的词的字典 键是单词, 值是颜色
    dictionary: list[str] = []  # 这是英语词库
    count: int = 0  # 这是玩家猜了多少次

    @staticmethod
    def clear():
        os.system("cls" if platform.system() == "Windows" else "clear")  # 实例化时清屏 Windows用cls 其它用clear

    def __init__(self):
        # 用于游戏初始化
        self.clear()
        print("正在初始化,请耐心等待")
        with open("dictionary.txt", "r") as f:
            self.dictionary = f.readlines()
            for i in self.dictionary:
                self.dictionary[self.dictionary.index(i)] = i.replace("\n", "")  # 去除换行符
        self.answer = random.choice(self.dictionary)  # 初始化英语词库
        self.console = rich.get_console()
        print("初始化结束")
        print("\n")
        print("wordle是一个猜单词的游戏, 你有6次机会猜一个5个字母的单词\n输入你的答案回车后, 如果你的答案中有字母被标成灰色, 说明此字母不在答案中;\n如果你的答案中有字母被标成黄色, "
              "说明此字母在答案中, 但位置不对;\n如果你的答案中有字母被标成绿色, 说明此字母在答案中, 且位置正确;\n如果你的答案整体为绿色, 则你猜中了")

    def check(self, word: str) -> list[str]:
        # 用于检查输入的词语
        # 返回的列表是每个字符对应颜色
        word = word.lower()
        result = []
        if word in self.dictionary:
            for (i, j) in zip(word, self.answer):
                if i == j:
                    result.append("green")  # 两个字母一样就标绿
                elif i in self.answer:
                    result.append("yellow")  # 字母在答案里面就标黄
                else:
                    result.append("gray")  # 字母不在答案里面就标灰

        return result

    def show_result(self):
        # 用于展示每次输入答案的结果
        self.clear()
        for i in self.answer_table:  # i 是self.answer_table 里面的每一个键
            for j in i:  # j是i里面的每一个字母
                self.console.print(f"[{self.answer_table[i][i.index(j)]}]{j}[/]", end="")
            print()


def main():
    wordle_game = WordleGame()
    while wordle_game.count < 6:  # 6次机会循环
        player_input = input(f"输入第{wordle_game.count}个5个字母的词语")
        check_result = wordle_game.check(player_input)
        if check_result:
            wordle_game.answer_table[player_input] = check_result
            wordle_game.count += 1
            print(wordle_game.count, wordle_game.answer_table)
            wordle_game.show_result()
        if wordle_game.check(player_input):
            if wordle_game.answer == player_input:
                print("你赢了")
                break

    if wordle_game.answer not in wordle_game.answer_table:
        print("你输了, 答案是: ", wordle_game.answer)
    input("按下Enter以退出程序")


if __name__ == "__main__":
    main()
