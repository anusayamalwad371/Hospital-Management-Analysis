from src.config import OUTPUT_DIR
from src.data_loader import load_data, show_shapes
from src.data_cleaning import clean_data
from src.data_transformation import transform_data
from src.analysis import generate_analysis
from src.visualization import save_charts
from src.report import save_report

def main():
    print("=" * 60)
    print("HOSPITAL MANAGEMENT & PATIENT RECORDS ANALYSIS")
    print("=" * 60)

    data = load_data()
    print("\nLoaded datasets:")
    show_shapes(data)

    data = clean_data(data)
    data = transform_data(data)
    analysis = generate_analysis(data)

    print("\nKEY PERFORMANCE INDICATORS")
    print("-" * 40)
    for key, value in analysis["kpis"].items():
        print(f"{key.replace('_', ' ').title():30}: {value}")

    chart_dir = OUTPUT_DIR / "charts"
    save_charts(analysis, chart_dir)
    save_report(analysis, OUTPUT_DIR)

    print("\nProject completed successfully.")
    print(f"Report : {OUTPUT_DIR / 'hospital_analysis_report.md'}")
    print(f"Charts : {chart_dir}")

if __name__ == "__main__":
    main()
