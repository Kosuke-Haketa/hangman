import random

def hangman(word):
    wrong = 0
    stages = ["",
              "___________",
              "|          ",
              "|      |   ",
              "|      O   ",
              "|     /|\  ",
              "|     / \  ",
              "|          ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

#答えリスト
answer_list = ["apple", "blackberry", "cherry", "dragonfruit"]

#リスト件数
lists = len(answer_list) - 1

#ランダム数字生成
seq = random.randint(0,lists)

#リストからオブジェクトを取得
answer = answer_list[seq]

#hangman関数実行、取得したオブジェクトを読み込む
hangman(answer)
