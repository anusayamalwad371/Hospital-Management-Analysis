import pandas as pd

def transform_data(data):
    data = {k: v.copy() for k, v in data.items()}

    # Appointment analysis columns
    appt = data["appointments"]
    appt["appointment_month"] = pd.to_datetime(appt["appointment_date"]).dt.to_period("M").astype(str)
    appt["is_completed"] = appt["status"].eq("Completed").astype(int)
    appt["is_cancelled"] = appt["status"].eq("Cancelled").astype(int)
    appt["is_no_show"] = appt["status"].eq("No Show").astype(int)
    data["appointments"] = appt

    # Admission analysis columns
    adm = data["admissions"]
    adm["admission_month"] = pd.to_datetime(adm["admission_date"]).dt.to_period("M").astype(str)
    adm["length_of_stay_days"] = (
        pd.to_datetime(adm["discharge_date"]) -
        pd.to_datetime(adm["admission_date"])
    ).dt.days
    data["admissions"] = adm

    # Billing analysis columns
    bill = data["billing"]
    bill["bill_month"] = pd.to_datetime(bill["bill_date"]).dt.to_period("M").astype(str)
    bill["patient_share_pct"] = (bill["patient_payable"] / bill["amount"].replace(0, pd.NA) * 100).round(2)
    data["billing"] = bill

    # Lab analysis
    lab = data["lab_reports"]
    lab["test_month"] = pd.to_datetime(lab["test_date"]).dt.to_period("M").astype(str)
    lab["is_abnormal"] = lab["result_status"].isin(["Abnormal", "Critical"]).astype(int)
    data["lab_reports"] = lab

    return data
