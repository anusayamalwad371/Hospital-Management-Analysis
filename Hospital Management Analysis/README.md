# Hospital Management & Patient Records Analysis

## Technologies
Python, Pandas, NumPy, Matplotlib, Excel/CSV.

## Run the project

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate on Windows
```bash
venv\Scripts\activate
```

### 3. Install libraries
```bash
pip install -r requirements.txt
```

### 4. Run
```bash
python main.py
```

## Modules

- `data_loader.py` — loads all CSV datasets
- `data_cleaning.py` — removes duplicates, cleans text and dates, handles missing numeric values
- `data_transformation.py` — creates analytical columns
- `analysis.py` — calculates hospital KPIs and summaries
- `visualization.py` — generates charts
- `report.py` — creates final Markdown report
- `config.py` — project paths and dataset configuration
