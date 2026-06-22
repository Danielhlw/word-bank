import streamlit as st

from word_bank.content import revision_data as data
from word_bank.ui.components.layout import card_end, card_start, render_section_header


def _formula_box(text: str) -> None:
    st.markdown(
        f'<div class="revision-formula">{text}</div>',
        unsafe_allow_html=True,
    )


def _render_be_forms() -> None:
    card_start("🔗 Verbo BE — Am / Is / Are")
    st.markdown(
        "O verbo **BE** (ser/estar) no **Simple Present** tem **3 formas**. "
        "Escolha conforme o **subject**:"
    )

    cols = st.columns(3)
    for col, item in zip(cols, data.BE_FORMS["forms"], strict=True):
        with col:
            st.markdown(f"### {item['form']}")
            st.caption(item["usage"])
            st.markdown(item["detail"])
            st.markdown(f"**Combinações:** {item['topics']}")
            st.markdown("---")
    card_end()


def _render_contractions() -> None:
    card_start("✂️ Contractions")
    st.caption("Formas contraídas usadas na fala e escrita informal.")
    col1, col2 = st.columns(2)
    half = (len(data.CONTRACTIONS) + 1) // 2
    for col, items in zip((col1, col2), (data.CONTRACTIONS[:half], data.CONTRACTIONS[half:]), strict=True):
        with col:
            for full, short in items:
                st.markdown(
                    f'<div class="revision-contraction-row">'
                    f'<span>{full}</span>'
                    f'<span class="revision-contraction-short">{short}</span>'
                    f"</div>",
                    unsafe_allow_html=True,
                )
    card_end()


def _render_topics() -> None:
    card_start("📋 Simple Present with BE — Tópicos")
    st.markdown("Use **Am / Is / Are** para falar sobre:")
    cols = st.columns(2)
    for idx, topic in enumerate(data.TOPICS):
        with cols[idx % 2]:
            st.markdown(f"**{topic['icon']} {topic['title']}**")
            for ex in topic["examples"]:
                st.markdown(f"- {ex}")
            st.markdown("")
    card_end()


def _render_yesno() -> None:
    card_start("✅ Yes / No Questions")
    st.markdown(f"**{data.YESNO['title']}**")
    _formula_box(data.YESNO["formula"])

    st.markdown("**Exemplos**")
    table_rows = [
        {
            "BE": be,
            "Subject": subj,
            "Complement": comp,
            "Uso": note,
        }
        for be, subj, comp, note in data.YESNO["examples"]
    ]
    st.dataframe(table_rows, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Respostas afirmativas**")
        for ans in data.YESNO["affirmative"]:
            st.markdown(f"- {ans}")
    with col2:
        st.markdown("**Respostas negativas**")
        for ans in data.YESNO["negative"]:
            st.markdown(f"- {ans}")
    card_end()


def _render_wh() -> None:
    card_start("❓ WH Questions")
    st.markdown(f"**{data.WH_QUESTIONS['title']}**")
    badges = " ".join(
        f'<span class="revision-wh-badge">{w}</span>'
        for w in data.WH_QUESTIONS["words"]
    )
    st.markdown(badges, unsafe_allow_html=True)
    _formula_box(data.WH_QUESTIONS["formula"])

    st.markdown("**Exemplos**")
    for wh, be, rest in data.WH_QUESTIONS["examples"]:
        st.markdown(f"- **{wh}** {be} {rest}")
    card_end()


def _render_statements() -> None:
    card_start("📝 Statements (+ / −)")
    st.markdown(f"**{data.STATEMENTS['title']}**")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Afirmativa**")
        _formula_box(data.STATEMENTS["affirmative_formula"])
        for ex in data.STATEMENTS["examples_affirmative"]:
            st.markdown(f"- {ex}")
    with col2:
        st.markdown("**Negativa**")
        _formula_box(data.STATEMENTS["negative_formula"])
        for ex in data.STATEMENTS["examples_negative"]:
            st.markdown(f"- {ex}")
    card_end()


def render() -> None:
    render_section_header(
        "📖",
        "Revision",
        "Guia de revisão: verbo BE, perguntas Yes/No, WH-questions e statements",
    )

    tab_be, tab_topics, tab_yesno, tab_wh, tab_stmt = st.tabs([
        "🔗 BE & Contractions",
        "📋 Tópicos",
        "✅ Yes / No",
        "❓ WH Questions",
        "📝 Statements",
    ])

    with tab_be:
        _render_be_forms()
        _render_contractions()

    with tab_topics:
        _render_topics()

    with tab_yesno:
        _render_yesno()

    with tab_wh:
        _render_wh()

    with tab_stmt:
        _render_statements()
