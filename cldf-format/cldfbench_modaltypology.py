import pathlib
import itertools

from cldfbench import Dataset as BaseDataset, CLDFSpec
from pycldf import term_uri


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "modal-typology"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(module="StructureDataset", dir=self.cldf_dir)

    def cmd_makecldf(self, args):
        # TODO: is this the "right" way of adding sources?
        args.writer.cldf.properties["dc:sources"] = "sources.bib"
        args.writer.cldf.add_component("ParameterTable")
        args.writer.cldf.add_component("LanguageTable")
        args.writer.cldf.add_columns(
            "LanguageTable",
            "Family",
            "Complete_language",
            {
                "name": "Source",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#source",
            },
            "Reference",
            "Reference_type",
            "Reference_URL",
        )
        # new, non-standard tables
        args.writer.cldf.add_table(
            "unit-parameters.csv",
            {
                "name": "ID",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id",
            },
            "Name",
            "Description",
            "force",
            "flavor",
        )
        args.writer.cldf.add_table(
            "unit-values.csv",
            {
                "name": "ID",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id",
            },
            {
                "name": "Value",
                # FIXME: valueReference should be added to the ontology, in analogy to formReference.
                # "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#valueReference",
            },
            "UnitParameter_ID",
            "UnitValue",
            "Comment",
            "Source",
        )
        args.writer.cldf.add_table(
            "flavors.csv",
            {
                "name": "ID",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id",
            },
            "Name",
            "Description",
        )
        args.writer.cldf.add_table(
            "forces.csv",
            {
                "name": "ID",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id",
            },
            "Name",
            "Description",
        )
        args.writer.cldf.add_foreign_key("unit-values.csv", "Value", "ValueTable", "ID")
        args.writer.cldf.add_foreign_key(
            "unit-values.csv", "UnitParameter_ID", "unit-parameters.csv", "ID"
        )
        args.writer.cldf.add_foreign_key(
            "unit-parameters.csv", "flavor", "flavors.csv", "Name"
        )
        args.writer.cldf.add_foreign_key(
            "unit-parameters.csv", "force", "forces.csv", "Name"
        )

        # link forces

        languoids_by_glottocode = {l.id: l for l in args.glottolog.api.languoids()}
        langs_metadata = self.raw_dir.read_csv("all_metadata.csv", dicts=True)

        modal_id = 0
        args.writer.objects["ParameterTable"].append(dict(ID="modal"))

        force_flavor_pairs = set()

        for lid, rows in itertools.groupby(
            sorted(
                self.raw_dir.read_csv("all_observations.csv", dicts=True),
                key=lambda r: (r["lang_ID"], r["expression"], r["can_express"]),
            ),
            lambda r: r["lang_ID"],
        ):
            glottolang = languoids_by_glottocode[lid]
            # TODO: better way of doing this?
            this_metadata = [
                lang_meta
                for lang_meta in langs_metadata
                if lang_meta["Glotto.code"] == lid
            ][0]
            args.writer.objects["LanguageTable"].append(
                dict(
                    ID=lid,
                    Name=glottolang.name,
                    Glottocode=glottolang.glottocode,
                    ISO639P3code=glottolang.iso_code,
                    Macroarea=glottolang.macroareas[0].name,
                    Latitude=glottolang.latitude,
                    Longitude=glottolang.longitude,
                    Family=glottolang.family,
                    Complete_language=this_metadata["Complete_language"],
                    Source=this_metadata["Reference_key"],
                    Reference_type=this_metadata["Reference_type"],
                    Reference=this_metadata["Reference"],
                    Reference_URL=this_metadata["URL"],
                )
            )
            for modal, rrows in itertools.groupby(rows, lambda r: r["expression"]):
                args.writer.objects["ValueTable"].append(
                    dict(
                        ID=str(modal_id),
                        Language_ID=lid,
                        Parameter_ID="modal",
                        Value=modal,
                    )
                )
                unit_obs_id = 0
                for can, rrrows in itertools.groupby(rrows, lambda r: r["can_express"]):
                    for row in rrrows:
                        unit_obs_id += 1
                        test_dict = dict(
                            ID=f"{modal_id}-{unit_obs_id}",
                            Parameter_ID="modal",
                            Value=str(modal_id),
                            UnitParameter_ID=f"{row['force']}.{row['flavor']}",
                            UnitValue={"1": "can", "0": "cannot", "?": "unclear"}[can],
                        )
                        force_flavor_pairs.add((row["force"], row["flavor"]))
                        args.writer.objects["unit-values.csv"].append(test_dict)
                modal_id += 1

        for idx, pair in enumerate(sorted(force_flavor_pairs)):
            # TODO: refactor naming of pairs
            args.writer.objects["unit-parameters.csv"].append(
                dict(
                    ID=f"{pair[0]}.{pair[1]}",
                    Name=f"{pair[0]}.{pair[1]}",
                    force=pair[0],
                    flavor=pair[1],
                )
            )

        # TODO: refactor out the common core of these two file reading/writing steps
        # read forces.csv and flavors.csv
        force_data = self.raw_dir.read_csv("forces.csv", dicts=True)
        for entry in force_data:
            args.writer.objects["forces.csv"].append(entry)
        # get forces from raw data and make sure that they are all represented in forces.csv
        forces_from_observations = set(pair[0] for pair in force_flavor_pairs)
        forces_from_raw = set(entry["Name"] for entry in force_data)
        assert (
            forces_from_observations == forces_from_raw
        ), "Mismatch between forces in observations data and in explicit forces.csv"

        flavor_data = self.raw_dir.read_csv("flavors.csv", dicts=True)
        for entry in flavor_data:
            args.writer.objects["flavors.csv"].append(entry)
        # get flavors from raw data and make sure that they are all represented in flavors.csv
        flavors_from_observations = set(pair[1] for pair in force_flavor_pairs)
        flavors_from_raw = set(entry["Name"] for entry in flavor_data)
        assert (
            flavors_from_observations == flavors_from_raw
        ), "Mismatch between flavors in observations data and in explicit forces.csv"
