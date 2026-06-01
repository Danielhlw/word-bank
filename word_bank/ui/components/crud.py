"""Componentes CRUD reutilizáveis."""

from __future__ import annotations

from typing import Callable

import streamlit as st

from word_bank.ui.components.layout import card_end, card_start


def crud_table(
    title: str,
    items: list[dict],
    columns: list[str],
    labels: dict[str, str],
    on_add: Callable[[dict], None],
    on_update: Callable[[int, dict], None],
    on_delete: Callable[[int], None],
    required_fields: list[str] | None = None,
    icon: str = "📝",
) -> None:
    card_start(f"{icon} {title}")

    if items:
        display_cols = [c for c in columns if c != "id"]
        st.dataframe(
            [{labels.get(c, c): item.get(c, "") or "—" for c in display_cols} for item in items],
            use_container_width=True,
            hide_index=True,
        )
        st.caption(f"{len(items)} registro(s)")
    else:
        st.markdown(
            '<div class="empty-state">Nenhum registro ainda.<br>Adicione o primeiro abaixo.</div>',
            unsafe_allow_html=True,
        )

    tab_add, tab_edit = st.tabs(["➕ Adicionar", "✏️ Editar / Excluir"])

    with tab_add:
        new_data = _form_fields(columns, labels, key_prefix=f"add_{title}")
        if st.button("Salvar", key=f"save_{title}", type="primary", use_container_width=True):
            if _validate(new_data, required_fields or []):
                on_add(new_data)
                st.toast("Registro adicionado!", icon="✅")
                st.rerun()

    with tab_edit:
        if not items:
            st.info("Nada para editar ainda.")
        else:
            options = {
                f"#{item['id']} — {item.get(columns[1], '')}": item["id"]
                for item in items
            }
            selected = st.selectbox(
                "Selecione um registro",
                list(options.keys()),
                key=f"sel_{title}",
            )
            row_id = options[selected]
            current = next(i for i in items if i["id"] == row_id)

            edit_data = _form_fields(
                columns, labels, key_prefix=f"edit_{title}", defaults=current
            )

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Atualizar", key=f"update_{title}", type="primary", use_container_width=True):
                    if _validate(edit_data, required_fields or []):
                        on_update(row_id, edit_data)
                        st.toast("Registro atualizado!", icon="✅")
                        st.rerun()
            with col2:
                if st.button("Excluir", key=f"delete_{title}", type="secondary", use_container_width=True):
                    on_delete(row_id)
                    st.toast("Registro excluído!", icon="🗑️")
                    st.rerun()

    card_end()


def pronoun_table(
    title: str,
    items: list[dict],
    on_add: Callable[[dict], None],
    on_update: Callable[[int, dict], None],
    on_delete: Callable[[int], None],
    icon: str = "👤",
) -> None:
    crud_table(
        title=title,
        items=items,
        columns=["id", "person", "form"],
        labels={"person": "Pessoa", "form": "Forma"},
        on_add=on_add,
        on_update=on_update,
        on_delete=on_delete,
        required_fields=["person", "form"],
        icon=icon,
    )


def _form_fields(
    columns: list[str],
    labels: dict[str, str],
    key_prefix: str,
    defaults: dict | None = None,
) -> dict:
    data = {}
    defaults = defaults or {}
    cols = [c for c in columns if c != "id"]
    field_cols = st.columns(min(len(cols), 3) or 1)

    for idx, col in enumerate(cols):
        label = labels.get(col, col)
        default = defaults.get(col, "")
        with field_cols[idx % len(field_cols)]:
            if col == "number":
                data[col] = st.number_input(
                    label, value=int(default or 1), min_value=1, key=f"{key_prefix}_{col}"
                )
            else:
                data[col] = st.text_input(label, value=str(default or ""), key=f"{key_prefix}_{col}")
    return data


def _validate(data: dict, required: list[str]) -> bool:
    for field in required:
        value = data.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            st.error(f"O campo **{field}** é obrigatório.")
            return False
    return True
