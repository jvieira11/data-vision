# DataVision

Projeto de análise de dados.

## Funcionalidades planejadas

- [ ] Importação e leitura de arquivos CSV e Excel
- [ ] Tratamento e filtragem de dados
- [ ] Comparação de arquivos, linhas e colunas dos arquivos CSV e Excel
- [ ] Dashboard dinâmico para fácil compreensão dos dados presentes
- [ ] Exportação da análise e filtragem dos arquivos utilizados
- [ ] Qualidade dos dados

## Tecnologias

- **Back-end:** Python
- **Framework Web:** FastAPI
- **Leitor CSV/Excel:** Pandas + openpyxl
- **Validação de dados:** Pydantic
- **ORM:** SQLAlchemy
- **Versionamento de mudanças:** Alembic
- **Banco relacional:** PostgreSQL
- **Testes do back-end:** Pytest
- **Construção de interface:** React
- **Framework React:** Next.js
- **Tipagem Front:** TypeScript
- **Estilização:** Tailwind CSS
- **Gráficos em React:** Recharts
- **Contêineres:** Docker / Compose
- **Versionamento e portifolio:** Git / GitHub

# Como rodar

## Backend:
```bash
cd C:\dev\data-vision\backend
```

```bash
.venv\Scripts\Activate.ps1
```

```bash
fastapi dev app/main.py
```

## Primeira vez em um novo computador:

```bash 
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

## Como rodar os testes:

```bash
pip install -r requirements-dev.txt
```

```bash
python -m pytest
```

## Status

Em desenvolvimento...