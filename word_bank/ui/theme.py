"""Estilos customizados da interface."""

import streamlit as st


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Serif+Display&display=swap');

        :root {
            --primary: #4f46e5;
            --primary-light: #818cf8;
            --accent: #06b6d4;
            --surface: #ffffff;
            --surface-alt: #f8fafc;
            --border: #e2e8f0;
            --text: #0f172a;
            --text-muted: #64748b;
            --success: #10b981;
            --radius: 12px;
        }

        .stApp {
            background: linear-gradient(160deg, #f0f4ff 0%, #f8fafc 45%, #ecfeff 100%);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e1b4b 0%, #312e81 100%);
        }

        [data-testid="stSidebar"] * {
            color: #e0e7ff !important;
        }

        [data-testid="stSidebar"] .stRadio label {
            background: rgba(255,255,255,0.06);
            border-radius: 10px;
            padding: 0.35rem 0.5rem;
            margin-bottom: 0.25rem;
            transition: background 0.2s;
        }

        [data-testid="stSidebar"] .stRadio label:hover {
            background: rgba(255,255,255,0.12);
        }

        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: #fff !important;
            font-family: 'DM Serif Display', Georgia, serif !important;
        }

        [data-testid="stSidebar"] [data-testid="stMetricValue"] {
            color: #a5b4fc !important;
            font-size: 1.5rem !important;
        }

        [data-testid="stSidebar"] [data-testid="stMetricLabel"] {
            color: #c7d2fe !important;
            font-size: 0.75rem !important;
        }

        .hero-title {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: 2.5rem;
            font-weight: 400;
            background: linear-gradient(135deg, #312e81 0%, #4f46e5 50%, #0891b2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.25rem;
            line-height: 1.2;
        }

        .hero-subtitle {
            color: var(--text-muted);
            font-family: 'DM Sans', sans-serif;
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin: 1.5rem 0 1rem 0;
            padding-bottom: 0.75rem;
            border-bottom: 2px solid var(--border);
        }

        .section-icon {
            font-size: 1.75rem;
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #eef2ff, #e0e7ff);
            border-radius: 12px;
        }

        .section-title {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: 1.5rem;
            color: var(--text);
            margin: 0;
        }

        .section-desc {
            font-family: 'DM Sans', sans-serif;
            color: var(--text-muted);
            font-size: 0.9rem;
            margin: 0;
        }

        .card-panel {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.25rem 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
        }

        .card-panel h3 {
            font-family: 'DM Sans', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: var(--primary);
            margin-top: 0;
            margin-bottom: 0.75rem;
        }

        .empty-state {
            text-align: center;
            padding: 2rem;
            color: var(--text-muted);
            background: var(--surface-alt);
            border-radius: var(--radius);
            border: 2px dashed var(--border);
            font-family: 'DM Sans', sans-serif;
        }

        .tense-badge {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            font-size: 0.7rem;
            font-weight: 600;
            font-family: 'DM Sans', sans-serif;
            margin-right: 0.35rem;
            margin-bottom: 0.35rem;
        }

        .tense-sp { background: #dbeafe; color: #1d4ed8; }
        .tense-pc { background: #d1fae5; color: #047857; }
        .tense-pa { background: #fef3c7; color: #b45309; }
        .tense-fu { background: #ede9fe; color: #6d28d9; }
        .tense-pp { background: #fce7f3; color: #be185d; }

        div[data-testid="stExpander"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
        }

        div[data-testid="stExpander"] details {
            border: none;
        }

        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-family: 'DM Sans', sans-serif;
            transition: transform 0.15s, box-shadow 0.15s;
        }

        .stButton > button[kind="primary"]:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
        }

        .stButton > button[kind="secondary"] {
            border-radius: 8px;
            font-family: 'DM Sans', sans-serif;
        }

        [data-testid="stDataFrame"] {
            border-radius: var(--radius);
            overflow: hidden;
            border: 1px solid var(--border);
        }

        h1, h2, h3 {
            font-family: 'DM Sans', sans-serif !important;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 0.5rem;
            background: transparent;
            border-bottom: 2px solid var(--border);
        }

        [data-testid="stTabs"] [data-baseweb="tab"] {
            font-family: 'DM Sans', sans-serif;
            font-weight: 500;
            border-radius: 8px 8px 0 0;
            padding: 0.5rem 1rem;
        }

        [data-testid="stTabs"] [aria-selected="true"] {
            background: var(--surface) !important;
            color: var(--primary) !important;
            border-bottom: 2px solid var(--primary) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
