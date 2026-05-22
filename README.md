# Connect4 Continuous Integration Demo

Ta projekt je demonstracija sprotne integracije (Continuous Integration) pri predmetu PRO.

Osnovna koda igre je povzeta iz:
https://github.com/KeithGalli/Connect4-Python

Projekt prikazuje:
- samodejni zagon testov,
- statično analizo kode,
- uporabo GitHub Actions,
- izvajanje CI workflow-a ob `git push`.

## Uporabljene tehnologije

- Python
- unittest
- GitHub Actions
- Ruff
- Pylint
- Coverage

## Zagon projekta

Namestitev odvisnosti:

```bash
pip install -r requirements.txt
```

## Zagon testov

```python
python -m unittest discover -s tests
```