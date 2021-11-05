import json
import sys

INPUT_FILE = "outputMarket.json"
OUTPUT_FILE = "outputPlayer.json"

def read_file(inputFile):
    f = open(inputFile, "r")
    return f.read()


def write_file(output):
    f = open(OUTPUT_FILE, "w")
    json.dump(output, f, indent=4)
    f.close()


def first_seller_results(result_json, seller):
    results = json.loads(result_json)
    for result in results["session"]["playersResult"]:
        if result["playerId"] == seller:
            return result
    print("Player " + seller + " does not exist")
    sys.exit(1)

if __name__ == "__main__":
    result_json = read_file(INPUT_FILE)
    player = ""
    for arg in sys.argv[1:]:
        player += arg + " "
    result_player = first_seller_results(result_json, player.strip())
    write_file(result_player)