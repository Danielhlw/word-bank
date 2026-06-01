# My English Word Bank

**My English Word Bank** é um caderno digital de inglês feito em Python com interface web (Streamlit). Ele permite registrar, editar e consultar palavras e frases de estudo — verbos (incluindo o verbo *be*), adjetivos, substantivos, pronomes, exemplos nos principais tempos verbais e situações de perguntas Yes/No e Wh-questions. Os dados ficam salvos localmente em SQLite e podem ser importados a partir da planilha **WORD BANK.xlsx**.

Funciona em **Linux**, **macOS** e **Windows**.

---

## Requisitos

- Python 3.10 ou superior
- Navegador (Chrome, Firefox, Edge, etc.)
- Planilha Excel `.xlsx` (opcional, para importação inicial)

---

## Instalação

### Linux / macOS

```bash
cd word_bank
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell ou CMD)

```powershell
cd word_bank
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Como rodar

Com o ambiente virtual ativado, na pasta do projeto:

```bash
streamlit run main.py
```

O navegador abre automaticamente em **http://localhost:8501**. Se não abrir, acesse esse endereço manualmente.

Para encerrar o app, pressione `Ctrl+C` no terminal.

---

## Importação inicial da planilha

A ferramenta pode carregar os dados da planilha **WORD BANK.xlsx** na primeira vez, desde que o banco ainda esteja vazio.

### Onde colocar a planilha

O app procura o arquivo neste caminho (pasta **Downloads** do seu usuário):

| Sistema | Caminho |
|---------|---------|
| Linux / macOS | `~/Downloads/WORD BANK.xlsx` |
| Windows | `C:\Users\SeuUsuario\Downloads\WORD BANK.xlsx` |

**Importante:**

- O nome do arquivo deve ser exatamente **`WORD BANK.xlsx`** (com espaço entre WORD e BANK).
- O formato deve ser **`.xlsx`** (Excel), não `.xls` nem `.csv`.
- A planilha precisa ter estas abas (nomes iguais aos da planilha original):

  | Aba | Conteúdo importado |
  |-----|-------------------|
  | `VERBS ` | Verbos regulares e formas do verbo BE |
  | `ADJECTIVES` | Adjetivos e possessive adjectives |
  | `NOUNS` | Substantivos e pronomes |
  | `TENSE ACTIVITY` | Exemplos nos tempos verbais |
  | `YESNO` | Situações e perguntas Yes/No |

> A aba de verbos termina com um espaço: `VERBS ` — isso segue o layout da planilha de referência.

### Importação automática (ao abrir o app)

1. Coloque `WORD BANK.xlsx` na pasta **Downloads**.
2. Certifique-se de que ainda **não existe** banco com dados (veja abaixo).
3. Execute `streamlit run main.py`.
4. Na primeira abertura, o app importa sozinho e exibe uma confirmação.

Os dados passam a ficar em `data/word_bank.db` — depois disso o app **não** usa mais a planilha no dia a dia; tudo é lido e gravado no banco local.

### Importação manual (pelo terminal)

Útil se você preferir importar antes de abrir a interface, ou se a planilha já estiver em Downloads:

```bash
# Linux / macOS
python scripts/seed.py

# Windows
python scripts\seed.py
```

O script só importa se o banco estiver **vazio**. Se já houver dados, nada é alterado.

### Começar do zero ou reimportar

Para forçar uma nova importação da planilha:

1. Feche o app (`Ctrl+C` no terminal).
2. Apague o arquivo `data/word_bank.db`.
3. Coloque (ou confira) `WORD BANK.xlsx` em Downloads.
4. Rode `streamlit run main.py` ou `python scripts/seed.py`.

### Sem planilha

Se não houver planilha em Downloads e o banco estiver vazio, o app abre normalmente e mostra um aviso. Você pode **cadastrar tudo manualmente** pela interface (veja abaixo).

---

## Como usar a ferramenta

### Navegação

No **menu lateral** (barra à esquerda), escolha a seção:

| Seção | O que você encontra |
|-------|---------------------|
| **Verbs** | Verbos regulares e conjugação do verbo BE |
| **Adjectives** | Adjetivos e possessive adjectives |
| **Nouns** | Substantivos, subject/object/possessive pronouns |
| **Tense Activity** | Frases nos 5 tempos verbais |
| **Yes/No** | Situações com perguntas Yes/No e Wh-questions |

O painel lateral também mostra um **resumo** com a quantidade de registros em cada área.

### Adicionar registros

Em cada card de conteúdo:

1. Abra a aba **➕ Adicionar**.
2. Preencha os campos (os obrigatórios dependem da seção — por exemplo, **Base** em verbos, **English** em adjetivos).
3. Clique em **Salvar**.

### Editar ou excluir

1. Abra a aba **✏️ Editar / Excluir**.
2. Selecione o registro na lista suspensa.
3. Altere os campos e clique em **Atualizar**, ou clique em **Excluir** para remover.

### Tense Activity

Nesta seção, cada linha é um conjunto de frases nos tempos:

- Simple Present  
- Present Continuous  
- Simple Past  
- Simple Future  
- Present Perfect  

Use as abas **Adicionar** e **Editar / Excluir** da mesma forma que nas outras seções.

### Onde os dados ficam salvos

Tudo é gravado localmente em:

```
word_bank/data/word_bank.db
```

Não é necessário internet depois da instalação. Faça backup copiando esse arquivo se quiser preservar seu progresso.

---

## Estrutura do projeto

```
word_bank/
├── main.py                 # Ponto de entrada (Streamlit)
├── requirements.txt
├── data/                   # Banco SQLite (gerado automaticamente)
├── scripts/
│   └── seed.py             # Importação manual da planilha
└── word_bank/              # Pacote Python
    ├── config.py           # Caminhos e configurações
    ├── db/                 # Conexão e schema SQLite
    ├── repositories/       # Operações CRUD
    ├── services/           # Importação Excel
    └── ui/                 # Interface Streamlit
        ├── app.py
        ├── theme.py
        ├── components/
        └── views/
```

---

## Solução de problemas

| Problema | O que fazer |
|----------|-------------|
| Planilha não importou | Confira o nome `WORD BANK.xlsx`, pasta Downloads e se `data/word_bank.db` já existia (apague para reimportar). |
| Erro ao abrir abas da planilha | Os nomes das abas devem ser exatamente os listados acima. |
| `streamlit` não encontrado | Ative o venv (`.venv`) e rode `pip install -r requirements.txt`. |
| Porta 8501 em uso | Feche outra instância do Streamlit ou use `streamlit run main.py --server.port 8502`. |
