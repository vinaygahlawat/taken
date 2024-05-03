def print_to_file(line: str):
    with open("game_output.txt", "a") as f:
        print(line, file=f)
