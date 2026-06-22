"""Conteúdo estático da aba Revision."""

BE_FORMS = {
    "title": "Verbo BE — 3 formas",
    "forms": [
        {
            "form": "Am",
            "usage": "Singular",
            "detail": "Usado **somente** com subject **I**",
            "topics": "Como ser, de onde é, quantos anos, o que ela é",
        },
        {
            "form": "Is",
            "usage": "Singular",
            "detail": "Todas as outras situações singulares: **he, she, it**, John, Sarah, my friend…",
            "topics": "Nome, profissão, idade, sentimentos, origem",
        },
        {
            "form": "Are",
            "usage": "Plural",
            "detail": "Usado com **you, we, they** (e plurais em geral)",
            "topics": "Origem, idade, profissão, sentimentos no plural",
        },
    ],
}

CONTRACTIONS = [
    ("It is", "It's"),
    ("She is", "She's"),
    ("He is", "He's"),
    ("You are", "You're"),
    ("We are", "We're"),
    ("They are", "They're"),
    ("I am", "I'm"),
    ("Is not", "Isn't"),
    ("Are not", "Aren't"),
    ("I am not", "I'm not"),
]

TOPICS = [
    {
        "title": "Name",
        "icon": "👤",
        "examples": [
            "My name **is** Alex.",
            "I **am** John.",
            "What **is** your name?",
        ],
    },
    {
        "title": "Country / City",
        "icon": "🌍",
        "examples": [
            "I **am** from Brazil.",
            "She **is** from São Paulo.",
            "Where **are** you from?",
        ],
    },
    {
        "title": "Age",
        "icon": "🎂",
        "examples": [
            "I **am** 32 (years old).",
            "How old **are** you?",
            "She **is** 25.",
        ],
    },
    {
        "title": "Cell phone numbers",
        "icon": "📱",
        "examples": [
            "My cell phone number **is** 44 98822-3377.",
            "What **is** your cell phone number?",
        ],
    },
    {
        "title": "Email addresses",
        "icon": "✉️",
        "examples": [
            "My email address **is** alex@gmail.com.",
            "**@** → *at* &nbsp;|&nbsp; **.** → *dot*",
            "alex **at** gmail **dot** com",
        ],
    },
    {
        "title": "Profession",
        "icon": "💼",
        "examples": [
            "I **am** a teacher.",
            "She **is** a doctor.",
            "What **is** your profession?",
        ],
    },
    {
        "title": "Feelings",
        "icon": "😊",
        "examples": [
            "I **am** happy today.",
            "She **is** tired.",
            "How **are** you today?",
        ],
    },
]

YESNO = {
    "title": "Yes / No Questions — Confirm information",
    "formula": "BE + Subject + complement ?",
    "examples": [
        ("Is", "your name", "John?", "Confirmar nome"),
        ("Are", "you", "John?", "Confirmar identidade"),
        ("Are", "you", "from Brazil?", "Confirmar origem"),
        ("Are", "you", "25?", "Confirmar idade"),
    ],
    "affirmative": [
        "Yes, it is.",
        "Yes, I am.",
        "Yes, she is.",
    ],
    "negative": [
        "No, it isn't. / It's not.",
        "No, I'm not.",
        "No, she isn't. / She's not.",
    ],
}

WH_QUESTIONS = {
    "title": "WH Questions — To get new information",
    "words": ["What", "Where", "When", "Who", "Why", "How", "How old"],
    "formula": "Wh + BE + Subject + (complement) ?",
    "examples": [
        ("What", "is", "your name?"),
        ("Where", "are", "you from?"),
        ("How old", "are", "you?"),
        ("How", "are", "you today?"),
    ],
}

STATEMENTS = {
    "title": "Statements (+ / −)",
    "affirmative_formula": "Subject + BE + complement",
    "negative_formula": "Subject + BE + not + complement",
    "examples_affirmative": [
        "My name **is** Alex.",
        "I **am** from Brazil.",
        "I **am** 32 (years old).",
    ],
    "examples_negative": [
        "I **am not** tired.",
        "She **is not** from Rio.",
        "They **are not** students.",
    ],
}
