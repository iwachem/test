# -*- coding: utf-8 -*-


def hangman(word):
    wrong = 0
    stages = ['',
              '_____     ',
              '|         ',
              '|    |    ',
              '|    0    ',
              '|   /|\   ',
              '|   / \   ',
              '|         ']
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangmen!!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'please expect one character\n'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You Win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('You Lose!')
        print('The Correct Answer is {}.'.format(word))


def main():
    hangman('cat')


if __name__ == '__main__':
    main()
