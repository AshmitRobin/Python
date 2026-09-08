import re
from datetime import date

import pandas as pd
import streamlit as st

st.set_page_config(page_title="INTERFACE Fest Registration", page_icon="🎓", layout="centered")

if "registrations" not in st.session_state:
    st.session_state.registrations = []  

def is_valid_name(name: str) -> bool:
    """Only letters, spaces, dots and apostrophes; 2-50 chars."""
    pattern = r"^[A-Za-z][A-Za-z .'-]{1,49}$"
    return bool(re.match(pattern, name.strip()))


def is_valid_email(email: str) -> bool:
    """Standard email pattern."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))


def is_valid_phone(phone: str) -> bool:
    """Exactly 10 digits, optionally starting with +91."""
    pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"
    return bool(re.match(pattern, phone.strip()))


def is_valid_college_id(reg_no: str) -> bool:
    """Alphanumeric registration/college ID, 5-15 characters."""
    pattern = r"^[A-Za-z0-9]{5,15}$"
    return bool(re.match(pattern, reg_no.strip()))


def is_valid_pincode(pincode: str) -> bool:
    """Indian PIN code: 6 digits, first digit non-zero."""
    pattern = r"^[1-9][0-9]{5}$"
    return bool(re.match(pattern, pincode.strip()))


def is_valid_emergency_contact(phone: str) -> bool:
    """Same rule as phone, used for a second, independent field."""
    pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"
    return bool(re.match(pattern, phone.strip()))

st.title("INTERFACE Fest Registration Portal")
st.caption("Register for Christ University's national-level IT fest — INTERFACE")

st.divider()

with st.form("registration_form", clear_on_submit=False):
    st.subheader("Participant Details")

    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name *", placeholder="e.g. Ashmit Robin")
        email = st.text_input("Email Address *", placeholder="e.g. name@example.com")
        phone = st.text_input("Phone Number *", placeholder="e.g. 9876543210")
        college_id = st.text_input("College Registration Number *", placeholder="e.g. 2541514")
    with col2:
        dob = st.date_input(
            "Date of Birth *",
            min_value=date(1995, 1, 1),
            max_value=date.today(),
            value=date(2004, 1, 1),
        )
        gender = st.radio("Gender *", ["Male", "Female", "Other", "Prefer not to say"])
        college_name = st.text_input("College / Institution Name *", placeholder="e.g. Christ University")
        pincode = st.text_input("City PIN Code *", placeholder="e.g. 560029")

    st.subheader("Event Preferences")
    events = st.multiselect(
        "Events Interested In *",
        ["Hackathon", "Coding Contest", "Robotics", "Gaming Arena", "Paper Presentation",
         "Web Design", "AI/ML Challenge", "Quiz"],
    )
    tshirt_size = st.selectbox("T-Shirt Size *", ["S", "M", "L", "XL", "XXL"])
    accommodation = st.checkbox("I require on-campus accommodation")

    st.subheader("Emergency & Additional Info")
    emergency_contact = st.text_input("Emergency Contact Number *", placeholder="e.g. 9123456780")
    address = st.text_area("Full Address *", placeholder="House no., street, city, state")

    terms = st.checkbox("I agree to the fest's terms and conditions *")

    submitted = st.form_submit_button("Register")

if submitted:
    required_fields = [
        full_name, email, phone, college_id, college_name,
        pincode, events, emergency_contact, address,
    ]

    if not all(required_fields) or not terms:
        st.warning("Please fill in all required fields and accept the terms and conditions.")
    else:
        errors = []

        if not is_valid_name(full_name):
            errors.append("Full Name should contain only letters/spaces and be at least 2 characters.")
        if not is_valid_email(email):
            errors.append("Please enter a valid email address.")
        if not is_valid_phone(phone):
            errors.append("Phone Number must be a valid 10-digit Indian mobile number.")
        if not is_valid_college_id(college_id):
            errors.append("College Registration Number must be 5-15 alphanumeric characters.")
        if not is_valid_pincode(pincode):
            errors.append("PIN Code must be a valid 6-digit Indian PIN code.")
        if not is_valid_emergency_contact(emergency_contact):
            errors.append("Emergency Contact must be a valid 10-digit mobile number.")

        age_years = (date.today() - dob).days // 365
        if age_years < 15:
            errors.append("Participant must be at least 15 years old.")

        if errors:
            for e in errors:
                st.error(e)
            st.info("Please correct the highlighted information and submit again.")
        else:
            record = {
                "Name": full_name.strip(),
                "Email": email.strip(),
                "Phone": phone.strip(),
                "Registration No.": college_id.strip(),
                "Date of Birth": dob.strftime("%d-%m-%Y"),
                "Gender": gender,
                "College": college_name.strip(),
                "PIN Code": pincode.strip(),
                "Events": ", ".join(events),
                "T-Shirt Size": tshirt_size,
                "Accommodation": "Yes" if accommodation else "No",
                "Emergency Contact": emergency_contact.strip(),
                "Address": address.strip(),
            }
            st.session_state.registrations.append(record)
            st.success("Registration completed successfully!")

st.divider()
st.subheader("Registered Participants")

if st.session_state.registrations:
    df = pd.DataFrame(st.session_state.registrations)
    st.dataframe(df, use_container_width=True)
    st.caption(f"Total registrations: {len(df)}")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download records as CSV", data=csv, file_name="interface_registrations.csv", mime="text/csv")
else:
    st.info("No participants registered yet. Fill the form above to add one.")
