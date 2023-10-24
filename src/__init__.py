import sys
from pathlib import Path

# set paths
ROOT = Path(__file__).parents[1]
SRC = ROOT / "src"
DATA_PATH = ROOT / "data"

sys.path.append(ROOT)
sys.path.append(SRC)
