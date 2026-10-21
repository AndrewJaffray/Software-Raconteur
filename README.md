# Software Raconteur: EVA Analysis

Compares spacewalk (EVA) data for two countries from `eva-data.json`.

## Setup

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```zsh
python eva.py
```

## Test

```zsh
python -m unittest -v
```

## Modules

- `eva.py`: runs the app
- `data_loader.py`: reads the data file
- `preparation.py`: validates and filters data
- `analysis.py`: calculations
- `presentation.py`: output and chart
- `records.py`: the EvaRecord data type

