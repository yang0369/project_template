from pypdf import PdfMerger
from typing import List, Union
from src.utilities.custom_logger import CustomLogger

logger = CustomLogger()

class FileMerger():
    def __init__(self, engine="PDF"):
        self.engine = engine

    def merge(self, files: List[str], save_dir: str):
        if self.engine == "PDF":
            merger = PdfMerger()
            for pdf in files:
                merger.append(pdf)
            logger.info(f"saving merged file into {save_dir}")
            merger.write(save_dir)
            merger.close()
