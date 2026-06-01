import streamlit as st

from word_bank.repositories import word_bank as repo
from word_bank.ui.components.crud import crud_table, pronoun_table
from word_bank.ui.components.layout import render_section_header


def render() -> None:
    render_section_header("📦", "Nouns & Pronouns", "Substantivos, pronomes pessoais e possessivos")

    crud_table(
        title="Substantivos",
        items=repo.list_nouns(),
        columns=["id", "singular", "plural", "portuguese"],
        labels={"singular": "Singular", "plural": "Plural", "portuguese": "Português"},
        on_add=repo.add_noun,
        on_update=repo.update_noun,
        on_delete=repo.delete_noun,
        required_fields=["singular"],
        icon="📖",
    )

    st.markdown("")
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        pronoun_table(
            title="Subject Pronouns",
            items=repo.list_subject_pronouns(),
            on_add=repo.add_subject_pronoun,
            on_update=repo.update_subject_pronoun,
            on_delete=repo.delete_subject_pronoun,
            icon="🙋",
        )
    with col2:
        pronoun_table(
            title="Object Pronouns",
            items=repo.list_object_pronouns(),
            on_add=repo.add_object_pronoun,
            on_update=repo.update_object_pronoun,
            on_delete=repo.delete_object_pronoun,
            icon="👉",
        )
    with col3:
        pronoun_table(
            title="Possessive Pronouns",
            items=repo.list_possessive_pronouns(),
            on_add=repo.add_possessive_pronoun,
            on_update=repo.update_possessive_pronoun,
            on_delete=repo.delete_possessive_pronoun,
            icon="🔒",
        )
