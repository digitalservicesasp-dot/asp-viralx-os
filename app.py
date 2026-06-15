import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime

# --- GOOGLE SHEETS SETUP ---
def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    try:
        creds_dict = json.loads(st.secrets["gcloud_service_account"])
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        sheet = client.open("ASP_ViralX_Database").sheet1
        return sheet
    except Exception as e:
        return None

sheet = connect_to_sheets()

# --- APP LAYOUT ---
st.set_page_config(page_title="ASP ViralX Dashboard", layout="wide")
st.title("🚀 ASP ViralX Custom Operating System")
st.write("Welcome, Ashwamegh! Control your Content, Tech, and Sales in one place.")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation Panel")
tab = st.sidebar.radio("Go To:", ["📊 Commerce OS (Leads)", "🤖 AI Script Studio", "🔥 Competitor Leaderboard"])

# --- TAB 1: COMMERCE OS ---
if tab == "📊 Commerce OS (Leads)":
    st.header("🛒 Live Sales & B2B Leads Tracker")
    st.write("This data is synced directly with your Google Sheet `ASP_ViralX_Database`.")
    
    if sheet:
        try:
            data = sheet.get_all_records()
            if data:
                st.dataframe(data, use_container_width=True)
            else:
                st.info("Database sheet is currently empty. Add some test data!")
        except Exception as e:
            st.error("Error fetching data from Google Sheets.")
    else:
        st.warning("Google Sheet setup is pending. Please configure secrets in Streamlit Cloud.")
        
    st.subheader("➕ Add New Lead Manually")
    with st.form("lead_form", clear_on_submit=True):
        c_name = st.text_input("Customer Name")
        c_whatsapp = st.text_input("WhatsApp Number")
        c_email = st.text_input("Email ID")
        c_product = st.selectbox("Product", ["Canva Pro", "WaSender Tool", "Google Map Scraper", "Digital Bundle"])
        c_status = st.selectbox("Payment Status", ["Paid", "Pending"])
        
        submit = st.form_submit_button("Save Lead")
        if submit and sheet:
            today = str(datetime.date.today())
            sheet.append_row([today, c_name, c_whatsapp, c_email, c_product, c_status])
            st.success("Lead added successfully!")
            st.rerun()

# --- TAB 2: AI SCRIPT STUDIO ---
elif tab == "🤖 AI Script Studio":
    st.header("📝 HPPC Viral Script Generator")
    st.write("Generate short-form video scripts instantly based on Nawaz's HPPC Framework.")
    
    product_name = st.text_input("Enter Product Name (e.g., Canva Pro, WaSender):")
    target_audience = st.text_input("Target Audience:", "Freelancers")
    
    if st.button("Generate Script"):
        if product_name:
            st.subheader("🔥 Your 1000x Optimized Script:")
            script = f"""
**[0-3 Sec] HOOK:** "Stop wasting thousands on expensive subscriptions! If you are a {target_audience}, this secret is for you."
    
**[3-7 Sec] PROOF:** *(Show screen recording of your custom dashboard or active premium account)* "See this? Lifetime premium access activated without paying monthly rental prices."
    
**[7-12 Sec] PROCESS:** "I'm using the automated {product_name} framework. All you need to do is plug in your setup, and it works on complete autopilot."
    
**[12-15 Sec] CALL TO ACTION (CTA):** "Want direct access? Don't DM me. Just comment '{product_name.upper().replace(' ', '')}' below, and my automated chatbot will drop the link straight to your DM!"
            """
            st.markdown(script)
        else:
            st.warning("Please enter a product name.")

# --- TAB 3: COMPETITOR LEADERBOARD ---
elif tab == "🔥 Competitor Leaderboard":
    st.header("📈 Organic Competitor Insights")
    st.write("Track trending digital product frameworks without paid keys.")
    st.info("Pro Tip: Add top creator handles to monitor high-performing viral hooks manually using Instagram Saved Folders.")
    st.table([
        {"Keyword": "#digitalproducts", "Avg Views": "1.5M+", "Comment Action": "High (ManyChat)"},
        {"Keyword": "#leadgeneration", "Avg Views": "950K+", "Comment Action": "B2B Focus"},
        {"Keyword": "#canvapro", "Avg Views": "1.2M+", "Comment Action": "Instant Convert"},
        {"Keyword": "#wasender", "Avg Views": "800K+", "Comment Action": "Local B2B Business"}
    ])
