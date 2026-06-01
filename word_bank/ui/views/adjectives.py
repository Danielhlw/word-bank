import streamlit as st

from word_bank.repositories import word_bank as repo
from word_bank.ui.components.crud import crud_table, pronoun_table
from word_bank.ui.components.layout import render_section_header


def render() -> None:
    render_section_header("✨", "Adjectives", "Adjetivos descritivos e possessive adjectives")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        crud_table(
            title="Adjetivos",
            items=repo.list_adjectives(),
            columns=["id", "english", "portuguese"],
            labels={"english": "English", "portuguese": "Português"},
            on_add=repo.add_adjective,
            on_update=repo.update_adjective,
            on_delete=repo.delete_adjective,
            required_fields=["english"],
            icon="🎨",
        )

    with col2:
        pronoun_table(
            title="Possessive Adjectives",
            items=repo.list_possessive_adjectives(),
            on_add=repo.add_possessive_adjective,
            on_update=repo.update_possessive_adjective,
            on_delete=repo.delete_possessive_adjective,
            icon="📎",
        )
