
from pathlib import Path
import os

BASE_DIR    = Path(os.getenv("FORM13F_DATA_DIR", Path.home() / "data" / "form13f"))
DUCKDB_PATH = BASE_DIR / "sec13f.duckdb"
