import streamlit as st
import pandas as pd
import joblib

def predict_status(input_data):
    # Load model dan komponen terkait
    model_data = joblib.load("model/best_model.joblib")

    model = model_data["model"]
    encoders = model_data["encoders"]
    scaler = model_data.get("scaler", None)
    numerical_cols = model_data.get("numerical_cols", [])
    categorical_cols = model_data.get("categorical_cols", [])

    print('categorical_cols', model_data["categorical_cols"])

# =========================
# 2. Fungsi Prediksi
# =========================
    df = input_data.copy()

    # Encode kolom kategorikal
    for col in categorical_cols:
        if col in df.columns and col in encoders:
            le = encoders[col]
            df[col] = df[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
            df[col] = le.transform(df[col])

    # Standarisasi kolom numerik
    if scaler and numerical_cols:
        df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Prediksi
    result = model.predict(df)
    print("result1: ", result)

    # Decode hasil prediksi ke label asli (Graduate / Dropout)
    if "Status" in encoders:
        return encoders["Status"].inverse_transform(result)
    else:
        return result

# =========================
# 3. Sidebar Aplikasi
# =========================
st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="wide")

with st.sidebar:
    st.title("🎓 EduPredict App")
    st.markdown("Aplikasi untuk memprediksi apakah mahasiswa akan **Dropout** atau **Graduate** berdasarkan data akademik mereka.")
    st.info("Created by: **Nisa Agni**", icon="💡")
    st.markdown("---")
    st.markdown("📧 agniafifah21@gmail.com")

# =========================
# 4. Judul Aplikasi
# =========================
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Masukkan data akademik mahasiswa untuk melihat prediksinya.")

# =========================
# 5. Form Input Data
# =========================
with st.form("prediction_form"):
    st.header("📝 Form Input Mahasiswa")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # Mapping kode ke nama jurusan
        course_dict = {
            33: "Biofuel Production Technologies",
            171: "Animation and Multimedia Design",
            8014: "Social Service (evening attendance)",
            9003: "Agronomy",
            9070: "Communication Design",
            9085: "Veterinary Nursing",
            9119: "Informatics Engineering",
            9130: "Equinculture",
            9147: "Management",
            9238: "Social Service",
            9254: "Tourism",
            9500: "Nursing",
            9556: "Oral Hygiene",
            9670: "Advertising and Marketing Management",
            9773: "Journalism and Communication",
            9853: "Basic Education",
            9991: "Management (evening attendance)"
        }

        # Balik dictionary untuk lookup
        name_to_code = {v: k for k, v in course_dict.items()}
        course_name = st.selectbox("🎓 Program Studi", list(course_dict.values()))
        Course = name_to_code[course_name]
        attendance = st.selectbox("⏰ Attendance", ['Daytime', 'Evening'])
        gender = st.selectbox("⚧️ Gender", ['Male', 'Female'])
        age = st.number_input("🎂 Age at Enrollment", 15, 100, 20)

        with col2:
            displaced = st.selectbox("🚪 Displaced", ['Yes', 'No'])
            debtor = st.selectbox("💳 Debtor", ['Yes', 'No'])
            tuition_fees_up_to_date = st.selectbox("💰 Tuition Fees Up to Date", ['Yes', 'No'])
            scholarship = st.selectbox("🎓 Scholarship Holder", ['Yes', 'No'])

        # col3, col4 = st.columns(2)
        with col3:
            cu1_credited = st.number_input("📚 CU 1st Sem Credited", 0)
            cu1_enrolled = st.number_input("📝 CU 1st Sem Enrolled", 0)
            cu1_approved = st.number_input("✅ CU 1st Sem Approved", 0)
            cu1_grade = st.number_input("📈 CU 1st Sem Grade", 0.0)

        with col4:
            cu2_credited = st.number_input("📚 CU 2nd Sem Credited", 0)
            cu2_enrolled = st.number_input("📝 CU 2nd Sem Enrolled", 0)
            cu2_approved = st.number_input("✅ CU 2nd Sem Approved", 0)
            cu2_grade = st.number_input("📉 CU 2nd Sem Grade", 0.0)

    submitted = st.form_submit_button("🔍 Prediksi Status")

# =========================
# 6. Prediksi dan Output
# =========================
    if submitted:
        input_data = pd.DataFrame([{
            'Course': Course, 
            'Daytime_evening_attendance': attendance,
            'Displaced': displaced,
            'Debtor': debtor,
            'Tuition_fees_up_to_date': tuition_fees_up_to_date,
            'Gender': gender,
            'Scholarship_holder': scholarship,
            'Age_at_enrollment': age,
            'Curricular_units_1st_sem_credited': cu1_credited,
            'Curricular_units_1st_sem_enrolled': cu1_enrolled,
            'Curricular_units_1st_sem_approved': cu1_approved,
            'Curricular_units_1st_sem_grade': cu1_grade,
            'Curricular_units_2nd_sem_credited': cu2_credited,
            'Curricular_units_2nd_sem_enrolled': cu2_enrolled,
            'Curricular_units_2nd_sem_approved': cu2_approved,
            'Curricular_units_2nd_sem_grade': cu2_grade
        }])

        print('input_data: ', input_data.__len__)

    # Ambil elemen pertama dari hasil prediksi (karena result adalah array)
        result = predict_status(input_data)[0]
        print("result2", result)

        print({
            # Course, 
            attendance, 
            displaced, 
            debtor, 
            tuition_fees_up_to_date, 
            gender, 
            scholarship, 
            age, 
            cu1_credited, 
            cu1_enrolled, 
            cu1_approved, 
            cu1_grade, 
            cu2_credited, 
            cu2_enrolled, 
            cu2_approved, 
            cu2_grade
        })

    # Cek string hasil prediksi secara langsung
        if result == 1:
            st.success("🎉 Prediksi: Mahasiswa akan **Lulus (Graduate)**", icon="✅")
        else:
            st.error("⚠️ Prediksi: Mahasiswa berisiko **Dropout**")
