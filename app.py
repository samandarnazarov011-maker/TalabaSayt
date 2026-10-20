import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TDIU HEMIS AI - Student Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Glassmorphism & Neon Dark Theme
st.markdown("""
<style>
    .stApp {
        background: #090d16;
        color: #f8fafc;
    }
    
    /* Neon Glassmorphism Card */
    .glass-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }

    /* Glowing Interactive Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: 700;
        border-radius: 14px;
        border: none;
        padding: 12px 24px;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.6);
    }

    /* Student ID Card Badge */
    .id-card {
        background: linear-gradient(135deg, #1e1b4b 0%, #311b92 100%);
        border: 2px solid #6366f1;
        border-radius: 16px;
        padding: 20px;
        color: white;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown("<h1 style='text-align: center; color: #818cf8;'>🚀 TDIU HEMIS NextGen — AI Talaba Ekosistemasi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Toshkent Davlat Iqtisodiyot Universiteti | Smart Talaba Portali</p>", unsafe_allow_html=True)
st.markdown("---")

file_path = "talabalar (5).xlsx"

try:
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower()

    # Sidebar Navigation
    st.sidebar.markdown("### 🎛 Navigation Control")
    menu = st.sidebar.radio("Bo'limni tanlang:", [
        "🆔 Talaba ID Profil & Dashboard",
        "📅 Dars Jadvali (II-52/24)",
        "💰 Moliya: Ijara & Stipendiya Portali",
        "📚 Fanlar, Ballar & NB Kalkulyatori",
        "👨‍🏫 Professor-O'qituvchilar Portali",
        "📄 Avto-Spravka & Grant Arizalari",
        "🤖 AI Akademik Yordamchi & Predictor"
    ])

    search_query = st.sidebar.text_input("🔍 Qidiruv (Ism/Familiya):")

    filtered_df = df.copy()
    if search_query and 'ism' in df.columns:
        filtered_df = filtered_df[filtered_df['ism'].str.contains(search_query, case=False, na=False)]

    # 1. ID Profil va Dashboard
    if menu == "🆔 Talaba ID Profil & Dashboard":
        st.subheader("💳 Virtual Talaba ID Kartasi va Statistika")
        
        col_id, col_stats = st.columns([1, 2])
        
        with col_id:
            st.markdown("""
            <div class='id-card'>
                <h3>🎓 TDIU / HEMIS STUDENT</h3>
                <p><b>F.I.Sh:</b> Nazarov Samandar</p>
                <p><b>ID Kodu:</b> 324241109702</p>
                <p><b>Yo'nalish:</b> Sun'iy intellekt</p>
                <p><b>Guruh:</b> II-52/24</p>
                <p><b>Telefon:</b> +998 91 951 73 05</p>
                <p><b>Bosqich:</b> 3-kurs (Kunduzgi)</p>
                <p><b>Status:</b> Aktiv / Grant 🟢</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col_stats:
            c1, c2, c3 = st.columns(3)
            c1.metric("GPA Ko'rsatkich", "4.40", "+0.20")
            c2.metric("Umumiy Kreditlar", "180 / 240", "75%")
            c3.metric("Semestr Reytingi", "1-o'rin", "Top 1%")
            
            st.markdown("### 📊 Akademik Baza Holati")
            st.dataframe(filtered_df.head(8), use_container_width=True)

    # 2. Dars Jadvali (Yangi bo'lim)
    elif menu == "📅 Dars Jadvali (II-52/24)":
        st.subheader("📅 Guruh Dars Jadvali: II-52/24")
        st.caption("Tashkent State University of Economics — 2026-Akademik yil")
        
        schedule_data = pd.DataFrame({
            "Kun / Vaqt": ["Dushanba (Mn)", "Seshanba (Tu)", "Chorshanba (Wed)", "Payshanba (Thu)", "Juma (Fri)"],
            "1-para (8:00 - 9:20)": [
                "Mashinali o'qitishga kirish (Ma) - Absalamova G (5/305-54)",
                "Buyumlar interneti (Ma) - Nasimov R (5/305-54)",
                "Kompyuterli ko'rish (Ma) - Xo'jamqulov A (5/305-54)",
                "Mashinali o'qitishga kirish (Ma) - Absalamova G (5/305-54)",
                "Buyumlar interneti (Sem) - Jumanazarov J (5/413-36)"
            ],
            "2-para (9:30 - 10:50)": [
                "Buyumlar interneti (Ma) - Nasimov R (5/305-54)",
                "Buyumlar interneti (Sem) - Jumanazarov J (5/417-30)",
                "Kompyuterli ko'rish (Ma) - Xo'jamqulov A (5/305-54)",
                "Mashinali o'qitishga kirish (Ma) - Absalamova G (5/305-54)",
                "Mashinali o'qitishga kirish (Sem) - Absalamova G (5/413-36)"
            ],
            "3-para (11:00 - 12:20)": [
                "Kompyuterli ko'rish (Ma) - Xo'jamqulov A (5/305-54)",
                "Kompyuterli ko'rish (Sem) - Xo'jamqulov A (5/417-30)",
                "Kompyuterli ko'rish (Sem) - Xo'jamqulov A (5/411-30)",
                "Buyumlar interneti (Ma) - Nasimov R (5/305-54)",
                "Mashinali o'qitishga kirish (Sem) - Absalamova G (5/413-36)"
            ],
            "4-para (13:00 - 14:20)": [
                "Kelajak soati (Ma'naviyat) - Sayfullayev S.N. (1/321L)",
                "-",
                "-",
                "-",
                "-"
            ]
        })
        st.dataframe(schedule_data, use_container_width=True)

    # 3. Moliya: Ijara va Stipendiya
    elif menu == "💰 Moliya: Ijara & Stipendiya Portali":
        st.subheader("💳 Moliyaviy Ko'rsatkichlar va Oylik Tushumlar Monitoringi")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Oylik Stipendiya Summasi", "610 000 so'm", "Tushdi ✅")
        m2.metric("Ijara To'lovi Kompensatsiyasi", "440 000 so'm", "O'tkazildi ✅")
        m3.metric("Jami Oylik Tushum", "1 050 000 so'm", "Oktyabr 2026")

        st.markdown("---")
        
        tab_stip, tab_ijara = st.tabs(["📊 Oylik Stipendiyalar Ro'yxati", "🏠 Ijara To'lovi Ariza & Status"])
        
        with tab_stip:
            st.markdown("### 📅 2026-Akademik Yil Oylik Stipendiya Tushumlari (610,000 so'm)")
            stip_data = pd.DataFrame({
                "Oylar": ["Sentabr 2026", "Oktyabr 2026", "Noyabr 2026", "Dekabr 2026"],
                "Stipendiya Turi": ["A'lo (Grant)", "A'lo (Grant)", "A'lo (Grant)", "Rejalashtirilgan"],
                "Summa (So'm)": ["610 000", "610 000", "610 000", "610 000"],
                "Karta/Hisob": ["8600 **** **** 4412", "8600 **** **** 4412", "8600 **** **** 4412", "8600 **** **** 4412"],
                "Holati": ["To'landi ✅", "To'landi ✅", "Jarayonda ⏳", "Kutilmoqda 💤"]
            })
            st.dataframe(stip_data, use_container_width=True)
            
        with tab_ijara:
            st.markdown("### 🏠 Talaba Ijarasi Kompensatsiya Tizimi (440,000 so'm)")
            st.info("💡 **Ma'lumot:** Davlat tomonidan ijara shartnomasi bor talabalarga har oy 440,000 so'm kompensatsiya to'lanadi.")
            
            ijara_data = pd.DataFrame({
                "Hujjat / Shartnoma ID": ["IJ-2026-9912", "IJ-2026-9913"],
                "Ijara Manzili": ["Toshkent sh., Chilonzor t., 12-mavze", "Toshkent sh., Chilonzor t., 12-mavze"],
                "Oylik Kompensatsiya": ["440 000 so'm", "440 000 so'm"],
                "Taqdim etilgan Oy": ["Sentabr 2026", "Oktyabr 2026"],
                "Dekanat Tasdiqlashi": ["Tasdiqlangan ✅", "Tasdiqlangan ✅"]
            })
            st.dataframe(ijara_data, use_container_width=True)

    # 4. Fanlar, Ballar & NB Kalkulyator
    elif menu == "📚 Fanlar, Ballar & NB Kalkulyatori":
        st.subheader("📚 Semestr Fanlari, Nazorat Ballari va NB Analiz")
        
        grades_df = pd.DataFrame({
            "Fan nomi": [
                "Buyumlar interneti (Ma'ruza)", 
                "Buyumlar interneti (Seminar)", 
                "Mashinali o'qitishga kirish (Seminar)", 
                "Mashinali o'qitishga kirish (Ma'ruza)", 
                "Kompyuterli ko'rish (Seminar)", 
                "Kompyuterli ko'rish (Ma'ruza)"
            ],
            "O'qituvchi": ["Nasimov R.", "Jumanazarov J.", "Absalamova G.", "Absalamova G.", "Xo'jamqulov A.", "Xo'jamqulov A."],
            "Joriy Nazorat (30)": [30, 29, 30, 28, 29, 30],
            "Oraliq Nazorat (30)": [29, 28, 29, 27, 28, 29],
            "Yakuniy Nazorat (40)": [40, 39, 40, 37, 38, 39],
            "Jami Ball": [99, 96, 99, 92, 95, 98],
            "Qoldirilgan Dars (NB)": ["0 soat", "0 soat", "2 soat", "4 soat", "0 soat", "2 soat"]
        })
        
        st.dataframe(grades_df, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 🧮 NB (Dars Qoldirish) Limit Kalkulyatori")
        col_nb1, col_nb2 = st.columns(2)
        with col_nb1:
            nb_hours = st.slider("Jami qoldirilgan dars soatingizni kiriting:", 0, 100, 8)
            max_allowed = 36
            
            if nb_hours > max_allowed:
                st.error(f"⚠️ Diqqat! Siz ruxsat berilgan limitdan ({max_allowed} soat) {nb_hours - max_allowed} soat ko'p dars qoldirgansiz!")
            else:
                st.success(f"✅ Ko'rsatkich a'lo! Sizda yana {max_allowed - nb_hours} soat dars qoldirish limiti bor.")

    # 5. O'qituvchilar Portali
    elif menu == "👨‍🏫 Professor-O'qituvchilar Portali":
        st.subheader("👨‍🏫 Fan O'qituvchilari Ro'yxati va Mashg'ulotlar Turi")
        
        teachers = pd.DataFrame({
            "№": [1, 2, 3, 4, 5, 6],
            "O'qituvchi F.I.Sh.": ["Nasimov R.", "Jumanazarov J.", "Absalamova G.", "Absalamova G.", "Xo'jamqulov A.", "Xo'jamqulov A."],
            "Fan Nomi": ["Buyumlar interneti", "Buyumlar interneti", "Mashinali o'qitishga kirish", "Mashinali o'qitishga kirish", "Kompyuterli ko'rish", "Kompyuterli ko'rish"],
            "Dars Turi": ["Ma'ruza", "Seminar", "Seminar", "Ma'ruza", "Seminar", "Ma'ruza"],
            "Xona": ["5/305-54", "5/417-30", "5/413-36", "5/305-54", "5/411-30", "5/305-54"]
        })
        st.dataframe(teachers, use_container_width=True)

    # 6. Avto-Spravka va Grant
    elif menu == "📄 Avto-Spravka & Grant Arizalari":
        st.subheader("📄 QR-Kodli Avto-Spravka va Onlayn Arizalar")
        
        t1, t2 = st.tabs(["📄 QR Ma'lumotnoma Olish", "📝 Grant va Chegirma Ariza"])
        
        with t1:
            st.markdown("### 🖨 O'qish joyidan ma'lumotnoma (Spravka) generatsiya qilish")
            spravka_type = st.selectbox("Ma'lumotnoma kimga/qayerga taqdim etiladi?", ["Tuman Mudofaa Ishlari Bo'limiga", "Bankka (Kredit uchun)", "Ish joyiga taqdim etish uchun", "Umumiy ma'lumotnoma"])
            
            if st.button("⚡ QR-Kodli Spravkani Avtomatik Yaratish"):
                st.success("✅ Ma'lumotnoma tayyor bo'ldi!")
                st.info(f"📄 **Talaba:** Nazarov Samandar (Guruh: II-52/24)\n🔑 **QR-Kod Tekshiruv Kodi:** `TDIU-HEMIS-2026-X324241109702`")
                st.download_button("📥 PDF Formatda Yuklab Olish", data="TDIU Official Document PDF", file_name="TDIU_HEMIS_Spravka.pdf")

        with t2:
            st.markdown("### 📝 Onlayn Arizalar Yuborish")
            st.selectbox("Ariza Turi:", ["Prezident Stipendiyasiga Ariza", "Rektor Stipendiyasi", "Moddiy Yordam So'rovi", "Ijara Kompensatsiya Arizasi"])
            st.text_area("Ariza Mazmuni:")
            if st.button("📤 Arizani Dekanatga Yuborish"):
                st.success("🎉 Arizangiz TDIU HEMIS tizimi orqali dekanatga yuborildi!")

    # 7. AI Akademik Yordamchi
    elif menu == "🤖 AI Akademik Yordamchi & Predictor":
        st.subheader("🤖 Sun'iy Intellekt Neyrotarmog'i Tahlili")
        
        col_ai1, col_ai2 = st.columns(2)
        with col_ai1:
            st.markdown("### 🎛 Ko'rsatkichlarni kiriting:")
            cur_gpa = st.slider("Hozirgi GPA:", 1.0, 5.0, 4.4, 0.1)
            cur_nb = st.number_input("Qoldirilgan soat (NB):", 0, 100, 8)
            cur_debts = st.slider("Qarzdorliklar soni:", 0, 5, 0)
            
            run_ai = st.button("🧠 AI Prognozni Hisoblash")
            
        with col_ai2:
            if run_ai:
                st.markdown("### 🎯 AI Natijasi va Tavsiyalar:")
                risk_factor = (5.0 - cur_gpa) * 15 + cur_nb * 0.8 + cur_debts * 20
                risk_factor = min(100, int(risk_factor))
                
                st.write(f"**Akademik Xavf Indeksi:** {risk_factor}%")
                st.progress(risk_factor / 100)
                
                if risk_factor < 25:
                    st.success("🟢 Muvaffaqiyat ko'rsatkichi: **A'LO (98%)!** Samandar, ko'rsatkichlaringiz oliy darajada, Prezident stipendiyasi va Qizil diplom ehtimoli juda yuqori!")
                elif risk_factor < 55:
                    st.warning("🟡 Muvaffaqiyat ko'rsatkichi: **O'RTA.** GPA balni oshirish tavsiya etiladi.")
                else:
                    st.error("🔴 Muvaffaqiyat ko'rsatkichi: **XAVFLI!**")

except Exception as e:
    st.error(f"Xatolik: {e}")