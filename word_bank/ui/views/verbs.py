import streamlit as st

from word_bank.repositories import word_bank as repo
from word_bank.ui.components.crud import crud_table
from word_bank.ui.components.layout import render_section_header

VERB_COLUMNS = ["id", "base", "infinitive", "present_participle", "past", "past_participle", "portuguese"]
VERB_LABELS = {
    "base": "Base",
    "infinitive": "Infinitive",
    "present_participle": "Present Participle",
    "past": "Past",
    "past_participle": "Past Participle",
    "portuguese": "Português",
}


def render() -> None:
    render_section_header("⚡", "Verbs", "Verbos regulares e conjugação do verbo BE")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        crud_table(
            title="Verbos regulares",
            items=repo.list_verbs(),
            columns=VERB_COLUMNS,
            labels=VERB_LABELS,
            on_add=repo.add_verb,
            on_update=repo.update_verb,
            on_delete=repo.delete_verb,
            required_fields=["base"],
            icon="🏃",
        )

    with col2:
        crud_table(
            title="Verbo BE",
            items=repo.list_be_forms(),
            columns=VERB_COLUMNS,
            labels=VERB_LABELS,
            on_add=repo.add_be_form,
            on_update=repo.update_be_form,
            on_delete=repo.delete_be_form,
            required_fields=["base"],
            icon="🔗",
        )
