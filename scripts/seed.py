#!/usr/bin/env python3
"""Importa dados da planilha Excel para o banco."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from word_bank.config import DEFAULT_XLSX
from word_bank.services.seed import seed_from_excel

if __name__ == "__main__":
    seed_from_excel(DEFAULT_XLSX)
    print("Dados importados com sucesso!")
