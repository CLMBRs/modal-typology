"""
Checks the IFF condition for the modals in the dataset
"""
import itertools

from cldfbench_steinertthrelkeldmodals import Dataset


def run(args):
    ds = Dataset().cldf_reader()
    for modal, observations in itertools.groupby(
        ds["unit-values.csv"], key=lambda row: row["Value"]
    ):
        # TODO: just build can/cannot in one iteration through observations instead of the current three passes, which is more readable?
        observations = list(observations)
        for obs in observations:
            obs["force"], obs["flavor"] = obs["UnitParameter_ID"].split(".")
        can = set(
            (obs["force"], obs["flavor"])
            for obs in observations
            if obs["UnitValue"] == "can"
        )
        cannot = set(
            (obs["force"], obs["flavor"])
            for obs in observations
            if obs["UnitValue"] == "cannot"
        )

        for fo, fl in itertools.product(
            [pair[0] for pair in can], [pair[1] for pair in can]
        ):
            assert (fo, fl) in can and ((fo, fl) not in cannot)
