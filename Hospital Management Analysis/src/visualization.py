import matplotlib.pyplot as plt
from pathlib import Path

def save_charts(analysis, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    charts = [
        ("patients_by_gender", "gender", "patients", "Patients by Gender", "bar"),
        ("appointments_by_department", "department", "appointments", "Appointments by Department", "bar"),
        ("appointment_status", "status", "count", "Appointment Status", "bar"),
        ("admissions_by_department", "department", "admissions", "Admissions by Department", "bar"),
        ("room_type_usage", "room_type", "admissions", "Room Type Usage", "bar"),
        ("outcomes", "outcome", "count", "Admission Outcomes", "bar"),
        ("revenue_by_service", "service", "amount", "Revenue by Service", "bar"),
        ("lab_results", "result_status", "count", "Laboratory Results", "bar"),
        ("top_medicines", "medicine", "prescriptions", "Top Medicines", "bar"),
    ]

    for name, x, y, title, kind in charts:
        df = analysis[name]
        plt.figure(figsize=(10, 6))
        if kind == "bar":
            plt.bar(df[x].astype(str), df[y])
            plt.xticks(rotation=35, ha="right")
        plt.title(title)
        plt.xlabel(x.replace("_", " ").title())
        plt.ylabel(y.replace("_", " ").title())
        plt.tight_layout()
        plt.savefig(output_dir / f"{name}.png", dpi=150)
        plt.close()

    # Monthly revenue
    df = analysis["monthly_revenue"]
    plt.figure(figsize=(10, 6))
    plt.plot(df["bill_month"], df["amount"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Monthly Hospital Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_revenue.png", dpi=150)
    plt.close()

    # Monthly appointments
    df = analysis["monthly_appointments"]
    plt.figure(figsize=(10, 6))
    plt.plot(df["appointment_month"], df["appointments"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Monthly Appointments")
    plt.xlabel("Month")
    plt.ylabel("Appointments")
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_appointments.png", dpi=150)
    plt.close()
