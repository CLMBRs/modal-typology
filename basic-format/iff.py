import itertools
import pandas as pd

if __name__ == "__main__":

    # TODO: document / clean up
    all_observations = pd.read_csv("all_observations.csv")
    for item, data in all_observations.groupby(["language", "expression"]):
        can_express = data[data["can_express"] == "1"]
        forces = can_express["force"]
        flavors = can_express["flavor"]
        for (force, flavor) in itertools.product(forces, flavors):
            can_express_new_pair = can_express[
                (can_express["force"] == force) & (can_express["flavor"] == flavor)
            ]
            if len(can_express_new_pair) == 0:
                print(f"Possible counter-example to IFF found: {item}\n{data}\n")
