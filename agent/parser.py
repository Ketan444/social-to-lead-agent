import pandas as pd
import json
import xml.etree.ElementTree as ET
from pathlib import Path


class FileParser:
    def parse(self, file_path: str):
        path = Path(file_path)
        suffix = path.suffix.lower()

        if suffix == ".csv":
            return pd.read_csv(path, low_memory=True)

        elif suffix == ".json":
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)

        elif suffix == ".xml":
            tree = ET.parse(path)
            return tree.getroot()

        raise ValueError(f"Unsupported file type: {suffix}")