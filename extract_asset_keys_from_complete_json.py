import os
import json

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
COMPLETE_JSON_FILE = os.path.join(CURRENT_DIRECTORY,"complete.json")
ALL_INSTRUMENTS_FILE = os.path.join(CURRENT_DIRECTORY,"all_instruments.txt")

def process_data_to_asset_symbol_and_asset_key():
    with open(COMPLETE_JSON_FILE,"rt") as f:
        instruments = json.load(f)
    string = ""
    for item in instruments:
        if("name" not in item.keys() or "asset_symbol" not in item.keys() or "asset_key" not in item.keys()):
            continue
        else:
            string += str(item["asset_symbol"]) + " " + item["asset_key"] + "\n"
            # print(item["asset_symbol"],item["asset_key"])

    with open(ALL_INSTRUMENTS_FILE,"at") as f:
        f.write(string)
# process_data_to_asset_symbol_and_asset_key()