from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

DATASETS = {
    "patients": DATA_DIR / "patients.csv",
    "doctors": DATA_DIR / "doctors.csv",
    "appointments": DATA_DIR / "appointments.csv",
    "admissions": DATA_DIR / "admissions.csv",
    "billing": DATA_DIR / "billing.csv",
    "lab_reports": DATA_DIR / "lab_reports.csv",
    "medications": DATA_DIR / "medications.csv",
    "department_summary": DATA_DIR / "department_summary.csv",
}
