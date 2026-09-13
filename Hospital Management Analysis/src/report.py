from pathlib import Path

def save_report(analysis, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    k = analysis["kpis"]

    report = f"""# Hospital Management & Patient Records Analysis Report

## Key Performance Indicators

- Total Patients: {k["total_patients"]}
- Total Doctors: {k["total_doctors"]}
- Total Appointments: {k["total_appointments"]}
- Completed Appointments: {k["completed_appointments"]}
- Total Admissions: {k["total_admissions"]}
- Average Length of Stay: {k["average_length_of_stay"]} days
- Total Billing Revenue: ₹{k["total_revenue"]:,.2f}
- Patient Payable Amount: ₹{k["patient_payable"]:,.2f}
- Insurance Amount: ₹{k["insurance_amount"]:,.2f}
- Abnormal/Critical Lab Reports: {k["abnormal_lab_reports"]}

## Main Analysis

### Department-wise Appointments
{analysis["appointments_by_department"].to_string(index=False)}

### Appointment Status
{analysis["appointment_status"].to_string(index=False)}

### Admissions by Department
{analysis["admissions_by_department"].to_string(index=False)}

### Admission Outcomes
{analysis["outcomes"].to_string(index=False)}

### Revenue by Service
{analysis["revenue_by_service"].to_string(index=False)}

### Laboratory Results
{analysis["lab_results"].to_string(index=False)}

### Top 10 Medicines
{analysis["top_medicines"].to_string(index=False)}

## Project Conclusion

This analysis helps hospital management understand patient volume,
appointment efficiency, admissions, length of stay, revenue,
laboratory outcomes, medication usage and payment status.

Charts are available in the output/charts folder.
"""

    (output_dir / "hospital_analysis_report.md").write_text(report, encoding="utf-8")
