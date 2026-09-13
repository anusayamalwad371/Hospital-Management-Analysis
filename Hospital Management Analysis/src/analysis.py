import pandas as pd

def generate_analysis(data):
    patients = data["patients"]
    doctors = data["doctors"]
    appointments = data["appointments"]
    admissions = data["admissions"]
    billing = data["billing"]
    labs = data["lab_reports"]
    medications = data["medications"]

    result = {}

    result["kpis"] = {
        "total_patients": len(patients),
        "total_doctors": len(doctors),
        "total_appointments": len(appointments),
        "completed_appointments": int(appointments["is_completed"].sum()),
        "total_admissions": len(admissions),
        "average_length_of_stay": round(admissions["length_of_stay_days"].mean(), 2),
        "total_revenue": round(billing["amount"].sum(), 2),
        "patient_payable": round(billing["patient_payable"].sum(), 2),
        "insurance_amount": round(billing["insurance_amount"].sum(), 2),
        "abnormal_lab_reports": int(labs["is_abnormal"].sum()),
    }

    result["patients_by_gender"] = patients["gender"].value_counts().rename_axis("gender").reset_index(name="patients")
    result["patients_by_city"] = patients["city"].value_counts().rename_axis("city").reset_index(name="patients")

    result["appointments_by_department"] = (
        appointments.merge(doctors[["doctor_id", "department"]], on="doctor_id", how="left")
        .groupby("department")
        .size()
        .reset_index(name="appointments")
        .sort_values("appointments", ascending=False)
    )

    result["appointment_status"] = appointments["status"].value_counts().rename_axis("status").reset_index(name="count")

    result["monthly_appointments"] = (
        appointments.groupby("appointment_month").size()
        .reset_index(name="appointments")
    )

    result["admissions_by_department"] = (
        admissions.groupby("department").size()
        .reset_index(name="admissions")
        .sort_values("admissions", ascending=False)
    )

    result["monthly_admissions"] = (
        admissions.groupby("admission_month").size()
        .reset_index(name="admissions")
    )

    result["room_type_usage"] = (
        admissions["room_type"].value_counts()
        .rename_axis("room_type").reset_index(name="admissions")
    )

    result["outcomes"] = (
        admissions["outcome"].value_counts()
        .rename_axis("outcome").reset_index(name="count")
    )

    result["revenue_by_service"] = (
        billing.groupby("service")["amount"].sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    result["monthly_revenue"] = (
        billing.groupby("bill_month")["amount"].sum()
        .reset_index()
    )

    result["payment_status"] = (
        billing["payment_status"].value_counts()
        .rename_axis("payment_status").reset_index(name="count")
    )

    result["lab_results"] = (
        labs["result_status"].value_counts()
        .rename_axis("result_status").reset_index(name="count")
    )

    result["lab_tests"] = (
        labs.groupby("test_name")["lab_cost"].agg(["count", "sum"])
        .reset_index()
        .rename(columns={"count": "tests", "sum": "revenue"})
        .sort_values("tests", ascending=False)
    )

    result["top_medicines"] = (
        medications["medicine"].value_counts()
        .rename_axis("medicine").reset_index(name="prescriptions")
        .head(10)
    )

    result["doctor_performance"] = (
        appointments.merge(doctors[["doctor_id", "doctor_name", "department"]], on="doctor_id", how="left")
        .groupby(["doctor_id", "doctor_name", "department"])
        .agg(
            appointments=("appointment_id", "count"),
            completed=("is_completed", "sum"),
            no_shows=("is_no_show", "sum"),
            cancellations=("is_cancelled", "sum"),
        )
        .reset_index()
    )
    result["doctor_performance"]["completion_rate_pct"] = (
        result["doctor_performance"]["completed"] /
        result["doctor_performance"]["appointments"] * 100
    ).round(2)

    return result
