while True:
    try:
        eng = input()
        print(eng)
    except EOFError:
        break