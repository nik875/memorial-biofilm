import os
from pathlib import Path
from qiime2 import Artifact


def load_artifact(fp: Path):
    artifact = Artifact.import_data("SampleData[SequencesWithQuality]", fp, "SingleEndFastqManifestPhred33V2")
    artifact.save("data.qza")


def load(fp: Path, out: Path):
    os.system(f"samtools bam2fq '{fp}' > '{out}'")


def load_all(directory: Path):
    for root, dirs, files in os.walk(directory):
        for i in files:
            load(Path(os.path.join(root, i)), Path("Data/converted_data/" + i.rstrip("bam") + "fq"))


if __name__ == "__main__":
    # load_all(Path("Data/Ion 16s Metagenomics Template"))
    load_artifact(Path("Data/converted_data/manifest.tsv"))
