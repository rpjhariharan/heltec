import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================
# Mock Data for Features
# ==========================

# Medical Shops
medical_shops_data = pd.DataFrame({
    'Shop Name': ['HealthPlus Pharmacy', 'WellCare Pharmacy', 'MediShop Express'],
    'Location': ['Downtown, New York', 'Uptown, Los Angeles', 'Midtown, Chicago'],
    'Available Products': ['OTC Medicines, Prescriptions', 'Supplements, Prescriptions', 'OTC Medicines, Vitamins']
})

# Ambulance Booking
ambulance_data = pd.DataFrame({
    'Pickup Location': ['123 Main St, City', '456 Elm St, City'],
    'Destination': ['City Hospital', 'Central Clinic'],
    'Time of Request': ['Immediate', '2 PM']
})

# Hospitals
hospitals_data = pd.DataFrame({
    'Hospital Name': ['City Hospital', 'Downtown Clinic', 'Central Health Center'],
    'Specialty': ['Cardiology', 'Neurology', 'Orthopedics'],
    'Consulting Cost': ['$150', '$200', '$180'],
    'Treatment Cost': ['$5000', '$7000', '$6000'],
    'Location': ['New York', 'Los Angeles', 'Chicago']
})

# Health Insurance Providers
insurance_data = pd.DataFrame({
    'Provider Name': ['HealthSecure', 'MediCare', 'LifeHealth'],
    'Coverage Details': ['Comprehensive', 'Basic', 'Premium'],
    'Premium Costs': ['$200/month', '$150/month', '$300/month'],
    'Network Hospitals': ['50+', '30+', '70+']
})

# Medical Representatives
med_reps_data = pd.DataFrame({
    'Rep Name': ['Jane Doe', 'Mark Spencer'],
    'Specialty Products': ['Diabetes Medications', 'Cardio Devices'],
    'Contact Information': ['jane.doe@medrep.com', 'mark.spencer@medrep.com']
})

# Medical Loan Providers
loan_providers_data = pd.DataFrame({
    'Provider Name': ['MedFinance', 'HealthLoans'],
    'Loan Amount': ['Up to $50,000', 'Up to $100,000'],
    'Interest Rates': ['5% APR', '4.5% APR'],
    'Repayment Terms': ['5 years', '10 years']
})

# Providers (Doctors)
providers_data = pd.DataFrame({
    'Provider ID': [1, 2, 3],
    'Name': ['Dr. Emily Clark', 'Dr. Alan Turner', 'Dr. Sarah Lee'],
    'Specialty': ['Cardiology', 'Neurology', 'Orthopedics'],
    'Reviews': [4.5, 4.7, 4.6]
})

# Appointments
appointments_data = pd.DataFrame({
    'Appointment ID': [1, 2],
    'Patient Name': ['John Doe', 'Jane Smith'],
    'Doctor': ['Dr. Emily Clark', 'Dr. Alan Turner'],
    'Date': ['2024-05-01', '2024-05-03'],
    'Time Slot': ['9 AM - 12 PM', '1 PM - 5 PM'],
    'Type': ['Online', 'In-person']
})

# Telemedicine Appointments
telemedicine_data = pd.DataFrame({
    'TeleID': [1],
    'Patient Name': ['John Doe'],
    'Doctor': ['Dr. Emily Clark'],
    'Time': ['10:00 AM'],
    'Type': ['Video Call']
})

# Reviews
reviews_data = pd.DataFrame({
    'Rating': [4.5, 4.7],
    'Review': ["Excellent service and friendly staff.", "Very professional and helpful."]
})

# Health Records
records_data = pd.DataFrame({
    'Record Type': ['Blood Test Results', 'Prescription'],
    'Details': ['Blood Pressure: 130/80', 'Lisinopril 10mg'],
    'Access Permissions': ['Patient, Dr. Emily Clark', 'Patient, Dr. Emily Clark']
})

# ==========================
# Streamlit App Structure
# ==========================

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Function to set the current page
def set_page(page):
    st.session_state.page = page

# Sidebar Navigation with Buttons
st.sidebar.title("Healthcare Platform")

# Define navigation buttons
if st.sidebar.button("Book Ambulance"):
    set_page("Book Ambulance")
if st.sidebar.button("Book Death Certificate"):
    set_page("Book Doctor for Death Certificate")
if st.sidebar.button("List Hospitals"):
    set_page("List Hospitals")
if st.sidebar.button("Medical Shops"):
    set_page("Medical Shops")
if st.sidebar.button("Compare Health Insurance"):
    set_page("Compare Health Insurance")
if st.sidebar.button("Book Appointments"):
    set_page("Book Appointments")
if st.sidebar.button("Telemedicine"):
    set_page("Telemedicine")
if st.sidebar.button("Reviews & Ratings"):
    set_page("Reviews & Ratings")
if st.sidebar.button("Health Records"):
    set_page("Health Records")
if st.sidebar.button("Medical Representatives"):
    set_page("Medical Representatives")
if st.sidebar.button("Medical Loans"):
    set_page("Medical Loans")


# ==========================
# Main Content Area
# ==========================

# Function to display the central search strip
def show_home():

    search_query = st.text_input("")
    if st.button("Search"):
        st.write(f"Searching for: {search_query}")


# ==========================
# Feature Pages
# ==========================

# Medical Shops
def medical_shops():
    st.header("List of Medical Shops by Geographic Location")
    st.subheader("Medical Shops")
    st.dataframe(medical_shops_data)

    st.subheader("Search Medical Shops")
    with st.form("shop_search_form"):
        location = st.selectbox("Select Location", medical_shops_data['Location'].unique().tolist())
        submit = st.form_submit_button("Search")
        if submit:
            shops = medical_shops_data[medical_shops_data['Location'] == location]
            if not shops.empty:
                st.dataframe(shops)
            else:
                st.write("No medical shops found in the selected location.")

# Book Ambulance
def book_ambulance():
    st.header("Book an Ambulance")
    with st.form("ambulance_form"):
        pickup = st.text_input("Pickup Location", "123 Main St, City")
        destination = st.text_input("Destination", "City Hospital")
        time = st.selectbox("Time of Request", ["Immediate", "Scheduled"])
        submit = st.form_submit_button("Book Ambulance")
        if submit:
            # Declare global before using
            global ambulance_data
            st.success(f"Ambulance booked from {pickup} to {destination} at {time}.")
            # Append to ambulance_data (for POC purposes)
            new_entry = {'Pickup Location': pickup, 'Destination': destination, 'Time of Request': time}
            ambulance_data = pd.concat([ambulance_data, pd.DataFrame([new_entry])], ignore_index=True)

    st.subheader("Your Booked Ambulances")
    st.dataframe(ambulance_data)

# List Hospitals
def list_hospitals():
    st.header("List of Hospitals")
    st.subheader("Filter Hospitals")
    specialty = st.multiselect("Specialty", hospitals_data['Specialty'].unique())
    location = st.multiselect("Location", hospitals_data['Location'].unique())
    if st.button("Filter"):
        if specialty and location:
            filtered = hospitals_data[
                (hospitals_data['Specialty'].isin(specialty)) &
                (hospitals_data['Location'].isin(location))
            ]
        elif specialty:
            filtered = hospitals_data[hospitals_data['Specialty'].isin(specialty)]
        elif location:
            filtered = hospitals_data[hospitals_data['Location'].isin(location)]
        else:
            filtered = hospitals_data

        if not filtered.empty:
            st.dataframe(filtered)
        else:
            st.write("No hospitals found with the selected criteria.")
    else:
        st.dataframe(hospitals_data)

# Book Doctor for Death Certificate
def book_death_certificate():
    st.header("Book a Doctor for Death Certificate")
    with st.form("death_certificate_form"):
        patient_name = st.text_input("Patient Name")
        doctor = st.selectbox("Select Doctor", providers_data['Name'].tolist())
        date = st.date_input("Select Date", min_value=datetime.today())
        documentation = st.text_input("Enter Documentation Requirements", "ID Proof, Medical Records")
        submit = st.form_submit_button("Book Doctor")
        if submit:
            st.success(f"Doctor {doctor} booked on {date} for death certificate issuance.")
            # Here, implement actual booking logic

# Compare Health Insurance
def compare_health_insurance():
    st.header("Compare Health Insurance Providers")
    st.subheader("Insurance Providers")
    st.dataframe(insurance_data)

    st.subheader("Compare Plans")
    insurance_options = st.multiselect("Select Insurance Providers to Compare", insurance_data['Provider Name'].tolist())
    if insurance_options:
        comparison = insurance_data[insurance_data['Provider Name'].isin(insurance_options)]
        st.table(comparison)
    else:
        st.write("Select at least one insurance provider to compare.")

# Book Appointments
def book_appointments():
    st.header("Book an Appointment")
    with st.form("appointment_form"):
        patient_name = st.text_input("Patient Name")
        doctor = st.selectbox("Select Doctor", providers_data['Name'].tolist())
        date = st.date_input("Select Date", min_value=datetime.today())
        time_slot = st.selectbox("Select Time Slot", ["9 AM - 12 PM", "1 PM - 5 PM", "6 PM - 9 PM"])
        consultation_type = st.selectbox("Consultation Type", ["Online", "In-person"])
        submit = st.form_submit_button("Book Appointment")
        if submit:
            # Declare global before using
            global appointments_data
            st.success(f"Appointment booked with {doctor} on {date} at {time_slot} for {consultation_type} consultation.")
            # Append to appointments_data (for POC purposes)
            new_appointment = {
                'Appointment ID': len(appointments_data) + 1,
                'Patient Name': patient_name,
                'Doctor': doctor,
                'Date': date.strftime("%Y-%m-%d"),
                'Time Slot': time_slot,
                'Type': consultation_type
            }
            appointments_data = pd.concat([appointments_data, pd.DataFrame([new_appointment])], ignore_index=True)

    st.subheader("Upcoming Appointments")
    st.dataframe(appointments_data)

# Telemedicine
def telemedicine():
    st.header("Telemedicine Integration")
    st.subheader("Virtual Consultations")
    with st.form("telemedicine_form"):
        patient_name = st.text_input("Patient Name")
        doctor = st.selectbox("Select Doctor", providers_data['Name'].tolist())
        appointment_time = st.time_input("Select Time")
        consultation_type = st.selectbox("Consultation Type", ["Video Call", "Chat"])
        submit = st.form_submit_button("Schedule Consultation")
        if submit:
            # Declare global before using
            global telemedicine_data
            st.success(f"Consultation with {doctor} scheduled at {appointment_time} via {consultation_type}.")
            # Append to telemedicine_data (for POC purposes)
            new_tele = {
                'TeleID': len(telemedicine_data) + 1,
                'Patient Name': patient_name,
                'Doctor': doctor,
                'Time': appointment_time.strftime("%H:%M %p"),
                'Type': consultation_type
            }
            telemedicine_data = pd.concat([telemedicine_data, pd.DataFrame([new_tele])], ignore_index=True)

    st.subheader("Upcoming Virtual Consultations")
    st.dataframe(telemedicine_data)

# Reviews & Ratings
def reviews_ratings():
    st.header("Reviews & Ratings")
    st.subheader("Submit a Review")
    with st.form("review_form"):
        user = st.text_input("Your Email")
        service = st.selectbox("Service", ["Hospital", "Doctor", "Ambulance", "Insurance Provider"])
        name = st.text_input("Name of Service Provider")
        rating = st.slider("Rating", 1.0, 5.0, 4.0, step=0.1)
        review = st.text_area("Write your review here...")
        submit = st.form_submit_button("Submit Review")
        if submit:
            # Declare global before using
            global reviews_data
            st.success("Your review has been submitted successfully!")
            # Append to reviews_data (for POC purposes)
            new_review = {'Rating': rating, 'Review': review}
            reviews_data = pd.concat([reviews_data, pd.DataFrame([new_review])], ignore_index=True)

    st.subheader("Existing Reviews")
    st.dataframe(reviews_data)

# Health Records
def health_records():
    # Declare global before using
    global records_data
    st.header("Health Records Management")
    st.subheader("Your Health Records")
    st.dataframe(records_data)

    st.subheader("Upload New Record")
    with st.form("upload_record_form"):
        record_type = st.selectbox("Record Type", ["Lab Result", "Prescription", "Imaging"])
        details = st.text_area("Details", "Enter record details here...")
        upload = st.file_uploader("Upload File", type=["pdf", "jpg", "png"])
        submit = st.form_submit_button("Upload")
        if submit:
            st.success("Health record uploaded successfully!")
            # Append to records_data (for POC purposes)
            new_record = {
                'Record Type': record_type,
                'Details': details,
                'Access Permissions': 'Patient, Doctor'
            }
            records_data = pd.concat([records_data, pd.DataFrame([new_record])], ignore_index=True)

# Medical Representatives
def medical_representatives():
    st.header("Collaborate with Medical Representatives")
    st.subheader("List of Medical Representatives")
    st.dataframe(med_reps_data)

    st.subheader("Contact a Representative")
    rep_name = st.selectbox("Select Representative", med_reps_data['Rep Name'].tolist())
    rep_info = med_reps_data[med_reps_data['Rep Name'] == rep_name].iloc[0]
    st.write(f"**Products:** {rep_info['Specialty Products']}")
    st.write(f"**Contact:** {rep_info['Contact Information']}")
    if st.button("Contact"):
        st.info(f"Contacting {rep_info['Rep Name']}...")

# Medical Loans
def medical_loans():
    st.header("Medical Loan Providers")
    st.subheader("List of Providers")
    st.dataframe(loan_providers_data)

    st.subheader("Apply for a Loan")
    with st.form("loan_form"):
        provider = st.selectbox("Select Provider", loan_providers_data['Provider Name'].tolist())
        amount = st.number_input("Loan Amount", min_value=1000, max_value=100000, step=1000)
        # Retrieve interest rate and repayment terms based on provider
        selected_provider = loan_providers_data[loan_providers_data['Provider Name'] == provider].iloc[0]
        interest = selected_provider['Interest Rates']
        repayment = selected_provider['Repayment Terms']
        submit = st.form_submit_button("Apply")
        if submit:
            st.success(f"Loan application submitted to {provider} for ${amount} at {interest} with repayment terms of {repayment}.")






# ==========================
# Display Pages Based on Navigation
# ==========================

if st.session_state.page == 'Home':
    show_home()
elif st.session_state.page == "Medical Shops":
    medical_shops()
elif st.session_state.page == "Book Ambulance":
    book_ambulance()
elif st.session_state.page == "List Hospitals":
    list_hospitals()
elif st.session_state.page == "Compare Health Insurance":
    compare_health_insurance()
elif st.session_state.page == "Book Appointments":
    book_appointments()
elif st.session_state.page == "Telemedicine":
    telemedicine()
elif st.session_state.page == "Reviews & Ratings":
    reviews_ratings()
elif st.session_state.page == "Health Records":
    health_records()
elif st.session_state.page == "Medical Representatives":
    medical_representatives()
elif st.session_state.page == "Medical Loans":
    medical_loans()
elif st.session_state.page == "Book Doctor for Death Certificate":
    book_death_certificate()
else:
    show_home()

# ==========================
# Reset Navigation (Optional)
# ==========================
st.sidebar.markdown("---")
if st.sidebar.button("Home"):
    set_page("Home")
