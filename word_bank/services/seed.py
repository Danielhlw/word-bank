"""Importa dados iniciais da planilha WORD BANK.xlsx."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from word_bank.config import DEFAULT_XLSX
from word_bank.db import init_db
from word_bank.repositories import word_bank as repo


def _cell(value) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    return text if text else None


def seed_from_excel(path: Path) -> None:
    init_db()
    if not repo.is_empty():
        return

    xl = pd.ExcelFile(path)

    df = pd.read_excel(xl, sheet_name="VERBS ", header=None)
    for i in range(7, len(df)):
        row = df.iloc[i]
        verb = {
            "base": _cell(row[0]),
            "infinitive": _cell(row[1]),
            "present_participle": _cell(row[2]),
            "past": _cell(row[3]),
            "past_participle": _cell(row[4]),
            "portuguese": _cell(row[5]),
        }
        if verb["base"]:
            repo.add_verb(verb)

        be = {
            "base": _cell(row[7]),
            "infinitive": _cell(row[8]),
            "present_participle": _cell(row[9]),
            "past": _cell(row[10]),
            "past_participle": _cell(row[11]),
            "portuguese": _cell(row[12]),
        }
        if be["base"]:
            repo.add_be_form(be)

    df = pd.read_excel(xl, sheet_name="ADJECTIVES", header=None)
    for i in range(8, len(df)):
        row = df.iloc[i]
        english = _cell(row[1])
        portuguese = _cell(row[2])
        if english:
            repo.add_adjective({"english": english, "portuguese": portuguese})

    possessive_map = [
        ("1st person", _cell(df.iloc[9, 4])),
        ("1st person (plural)", _cell(df.iloc[9, 5])),
        ("2nd person", _cell(df.iloc[9, 6])),
        ("2nd person (plural)", _cell(df.iloc[9, 7])),
        ("3rd person", _cell(df.iloc[9, 8])),
        ("3rd person (plural)", _cell(df.iloc[9, 9])),
    ]
    for person, form in possessive_map:
        if form:
            repo.add_possessive_adjective({"person": person, "form": form})

    df = pd.read_excel(xl, sheet_name="NOUNS", header=None)
    for i in range(8, len(df)):
        row = df.iloc[i]
        singular = _cell(row[1])
        if singular:
            repo.add_noun({
                "singular": singular,
                "plural": _cell(row[2]),
                "portuguese": _cell(row[3]),
            })

    subject_map = [
        ("1st person", _cell(df.iloc[7, 7])),
        ("1st person (plural)", _cell(df.iloc[7, 8])),
        ("2nd person", _cell(df.iloc[7, 9])),
        ("2nd person (plural)", _cell(df.iloc[7, 10])),
        ("3rd person", _cell(df.iloc[7, 11])),
        ("3rd person (plural)", _cell(df.iloc[7, 12])),
    ]
    for person, form in subject_map:
        if form:
            repo.add_subject_pronoun({"person": person, "form": form})

    object_map = [
        ("1st person", _cell(df.iloc[8, 7])),
        ("1st person (plural)", _cell(df.iloc[8, 8])),
        ("2nd person", _cell(df.iloc[8, 9])),
        ("2nd person (plural)", _cell(df.iloc[8, 10])),
        ("3rd person", _cell(df.iloc[8, 11])),
        ("3rd person (plural)", _cell(df.iloc[8, 12])),
    ]
    for person, form in object_map:
        if form:
            repo.add_object_pronoun({"person": person, "form": form})

    possessive_pron_map = [
        ("1st person", _cell(df.iloc[13, 7])),
        ("1st person (plural)", _cell(df.iloc[13, 8])),
        ("2nd person", _cell(df.iloc[13, 9])),
        ("2nd person (plural)", _cell(df.iloc[13, 10])),
        ("3rd person", _cell(df.iloc[13, 11])),
        ("3rd person (plural)", _cell(df.iloc[13, 12])),
    ]
    for person, form in possessive_pron_map:
        if form:
            repo.add_possessive_pronoun({"person": person, "form": form})

    df = pd.read_excel(xl, sheet_name="TENSE ACTIVITY", header=None)
    for i in range(10, len(df)):
        row = df.iloc[i]
        num = _cell(row[0])
        if num is None:
            continue
        try:
            number = int(float(num))
        except ValueError:
            continue
        repo.add_tense_example({
            "number": number,
            "simple_present": _cell(row[1]),
            "present_continuous": _cell(row[2]),
            "simple_past": _cell(row[3]),
            "simple_future": _cell(row[4]),
            "present_perfect": _cell(row[5]),
        })

    df = pd.read_excel(xl, sheet_name="YESNO", header=None)
    for i in range(4, len(df)):
        row = df.iloc[i]
        situation = _cell(row[0])
        if not situation:
            continue
        repo.add_yesno_example({
            "situation": situation,
            "yesno_question": _cell(row[1]),
            "response": _cell(row[2]),
            "wh_question": _cell(row[3]),
            "statement": _cell(row[4]),
        })


def main() -> None:
    seed_from_excel(DEFAULT_XLSX)
    print("Dados importados com sucesso!")


if __name__ == "__main__":
    main()
