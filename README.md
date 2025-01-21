# fastapi-uv-demo

This is a sample repository for my article of [Simplifying Python Development with uv: A Modern Package Management Tool](http://emasuriano.com/blog/2025-01-21-simplifying-python-development-with-uv-a-modern-package-management-tool#getting-started-with-uv-a-typescript-developers-guide)

For more information about it please refer to the article itself.

## Setup

This project is using `uv` as package manager so makes sure you have it installed in your machine.

1. To install dependencies

```bash
uv sync
```

2. Start FastAPI server

```bash
uv run uvicorn src.main:app --reload
```

3. Run tools

   - Type check with mypy

     ```bash
     uv run mypy src/
     ```

   - Lint with Ruff

     ```bash
     uv run ruff check src/
     ```

   - Format check with Black

     ```bash
     uv run black src/ --check
     ```

   - Run tests

     ```bash
     uv run pytest
     ```

   - Build package

     ```bash
     uv build
     ```
