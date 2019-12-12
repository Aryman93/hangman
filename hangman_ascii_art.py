def draw_hangman(a):
    if a == 5:
        print(' ______')
        print(' |/   ')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('/ \\')
    
    if a == 4:
        print(' ______')
        print(' |/   |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('/ \\')

    if a == 3:
        print(' ______')
        print(' |/   |')
        print(' |   (_)')
        print(' |')
        print(' |')
        print(' |')
        print('/ \\')

    if a == 2:
        print(' ______')
        print(' |/   |')
        print(' |   (_)')
        print(' |   /|\\')
        print(' |')
        print(' |')
        print('/ \\')

    if a == 1:
        print(' ______')
        print(' |/   |')
        print(' |   (_)')
        print(' |   /|\\')
        print(' |    |')
        print(' |')
        print('/ \\')

    if a < 1:
        print(' ______')
        print(' |/   |')
        print(' |   (_)')
        print(' |   /|\\')
        print(' |    |')
        print(' |   /!\\')
        print('/ \\')