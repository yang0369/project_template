import pandas as pd
import numpy as np
from src.utilities.merge_pdf import FileMerger
from pathlib import Path

DATA = Path(__file__).parents[1] / "data"

files_dir = [
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/RP-GraduateCertificate.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/RP-TRANSCRIPT-front.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/RP-TRANSCRIPT-back.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/MERIT AWARD.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/NTU Cert.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/NTU-TRANSCRIPT.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/dean's list.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/NUS_Graduation_Certificate.pdf",
    "/Users/kewenyang/Documents/GitHub/utility_scripts/data/NUS_Transcript.pdf",
    ]
out_dir = (DATA / "merged_academic_certs.pdf").as_posix()

if "__main__" == __name__:
    merger = FileMerger()
    merger.merge(files = files_dir, save_dir= out_dir)
