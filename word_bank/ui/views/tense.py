import streamlit as st

from word_bank.repositories import word_bank as repo
from word_bank.ui.components.layout import card_end, card_start, render_section_header

TENSE_FIELDS = [
    ("simple_present", "Simple Present", "tense-sp"),
    ("present_continuous", "Present Continuous", "tense-pc"),
    ("simple_past", "Simple Past", "tense-pa"),
    ("simple_future", "Simple Future", "tense-fu"),
    ("present_perfect", "Present Perfect", "tense-pp"),
]


def _tense_form(prefix: str, defaults: dict | None = None) -> dict:
    defaults = defaults or {}
    data = {"number": st.number_input(
        "Número",
        min_value=1,
        value=int(defaults.get("number") or 1),
        key=f"{prefix}_num",
    )}
    for field, label, _badge in TENSE_FIELDS:
        data[field] = st.text_area(
            label,
            value=defaults.get(field) or "",
            key=f"{prefix}_{field}",
            height=68,
        )
    return {
        "number": data["number"],
        **{f: (data[f] or None) for f, _, _ in TENSE_FIELDS},
    }


def render() -> None:
    render_section_header(
        "🕐",
        "Tense Activity",
        "Frases nos cinco tempos: presente, contínuo, passado, futuro e perfect",
    )

    badges = " ".join(
        f'<span class="tense-badge {css}">{label}</span>'
        for _, label, css in TENSE_FIELDS
    )
    st.markdown(badges, unsafe_allow_html=True)

    examples = repo.list_tense_examples()

    card_start("📋 Exemplos cadastrados")
    if examples:
        st.dataframe(
            [{
                "#": e["number"],
                **{label: e[field] or "—" for field, label, _ in TENSE_FIELDS},
            } for e in examples],
            use_container_width=True,
            hide_index=True,
        )
        st.caption(f"{len(examples)} exemplo(s)")
    else:
        st.markdown(
            '<div class="empty-state">Nenhum exemplo cadastrado.</div>',
            unsafe_allow_html=True,
        )
    card_end()

    tab_add, tab_edit = st.tabs(["➕ Adicionar", "✏️ Editar / Excluir"])

    with tab_add:
        card_start("Novo exemplo")
        form_data = _tense_form("tense_add")
        if st.button("Salvar exemplo", key="tense_save", type="primary", use_container_width=True):
            repo.add_tense_example(form_data)
            st.toast("Exemplo adicionado!", icon="✅")
            st.rerun()
        card_end()

    with tab_edit:
        if not examples:
            st.info("Nada para editar ainda.")
        else:
            card_start("Editar exemplo")
            options = {
                f"#{e['number']} — {(e.get('simple_present') or '')[:40]}": e["id"]
                for e in examples
            }
            selected = st.selectbox("Selecione", list(options.keys()), key="tense_sel")
            row_id = options[selected]
            current = next(e for e in examples if e["id"] == row_id)
            form_data = _tense_form("tense_edit", current)

            c1, c2 = st.columns(2)
            with c1:
                if st.button("Atualizar", key="tense_update", type="primary", use_container_width=True):
                    repo.update_tense_example(row_id, form_data)
                    st.toast("Atualizado!", icon="✅")
                    st.rerun()
            with c2:
                if st.button("Excluir", key="tense_delete", type="secondary", use_container_width=True):
                    repo.delete_tense_example(row_id)
                    st.toast("Excluído!", icon="🗑️")
                    st.rerun()
            card_end()
