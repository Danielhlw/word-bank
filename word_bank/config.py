from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "word_bank.db"
DEFAULT_XLSX = Path.home() / "Downloads" / "WORD BANK.xlsx"

DATA_DIR.mkdir(parents=True, exist_ok=True)
