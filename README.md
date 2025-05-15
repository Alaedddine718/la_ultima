# la_ultima – Plataforma interactiva para streamers

Este proyecto permite a los streamers crear encuestas en tiempo real, usar un chatbot de IA y entregar tokens coleccionables simulados a los espectadores que participan.

## Cómo ejecutar los tests (solo con Python)

Puedes ejecutar los tests directamente desde Python usando `pytest`:

```python
import pytest

pytest.main(["-q", "tests/test_models.py"])
pytest.main(["-q", "tests/test_services.py"])
pytest.main(["-q", "tests/test_repositories.py"])
pytest.main(["-q", "tests/test_patterns.py"])
pytest.main(["-q", "tests/test_cli.py"])
```

## Cómo ejecutar la aplicación (modo CLI y UI)

- **Modo CLI por defecto:**

```python
import src.app
src.app.main()
```

- **Modo interfaz Gradio (UI):**

```python
import src.app
src.app.main(["--ui"])
```

## Repositorio del proyecto

https://github.com/Alaedddine718/la_ultima.git
