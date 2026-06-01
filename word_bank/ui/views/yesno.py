from word_bank.repositories import word_bank as repo
from word_bank.ui.components.crud import crud_table
from word_bank.ui.components.layout import render_section_header


def render() -> None:
    render_section_header(
        "💬",
        "Yes/No Questions",
        "Perguntas de confirmação (Yes/No) e perguntas abertas (Wh-questions)",
    )

    crud_table(
        title="Situações e perguntas",
        items=repo.list_yesno_examples(),
        columns=["id", "situation", "yesno_question", "response", "wh_question", "statement"],
        labels={
            "situation": "Situação",
            "yesno_question": "Yes/No Question",
            "response": "Resposta",
            "wh_question": "Wh Question",
            "statement": "Statement",
        },
        on_add=repo.add_yesno_example,
        on_update=repo.update_yesno_example,
        on_delete=repo.delete_yesno_example,
        required_fields=["situation"],
        icon="❓",
    )
