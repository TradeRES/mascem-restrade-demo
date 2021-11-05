INPUT_FILE = "outputPlayer.json"

def read_file(inputFile):
    f = open(inputFile, "r")
    return f.read()


if __name__ == "__main__":
    result_player = read_file(INPUT_FILE)
    print(result_player)