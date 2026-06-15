import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime

# Page Configuration & Title
st.set_page_config(page_title="ASP ViralX OS", page_icon="🚀", layout="wide")

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

# --- Session State Data Initialization ---
if 'liked_reels' not in st.session_state:
    st.session_state.liked_reels = [
        {"Title": "Automation Secret", "Link": "https://instagram.com/reel/1", "Views": "2.5M"},
        {"Title": "Canva Pro Free Hack", "Link": "https://instagram.com/reel/2", "Views": "1.8M"}
    ]

if 'calendar_events' not in st.session_state:
    st.session_state.calendar_events = [
        {"Date": "2026-06-16", "Platform": "Instagram", "Topic": "WaSender Software Launch", "Status": "Scheduled"},
        {"Date": "2026-06-18", "Platform": "YouTube Shorts", "Topic": "Canva Pro Mastery", "Status": "Draft"}
    ]

# --- SIDEBAR NAVIGATION PANEL (NAWAZ STYLE) ---
st.sidebar.title("🚀 ASP VIRALX OS")
st.sidebar.markdown("---")

# Main System Selector (Nawaz Style Parent Menu)
main_system = st.sidebar.selectbox("SELECT SYSTEM:", ["🟢 VIRALITY OS (Content)", "🛒 COMMERCE OS (Sales & Leads)"])

st.sidebar.markdown("---")

# Sub-Tabs routing based on Parent selection
if main_system == "🟢 VIRALITY OS (Content)":
    st.sidebar.subheader("🎥 Content Modules")
    nav_selection = st.sidebar.radio(
        "Go To:",
        ["🏠 Home Dashboard", "📄 Script Studio", "❤️ Liked Reels Vault", "👥 Competitors Board", "📊 Content Analytics", "📅 Posting Calendar", "✍️ AI Hooks Studio", "🎬 AI Editor Helper", "👤 Profile Panel"]
    )
else:
    st.sidebar.subheader("💼 Commerce Modules")
    nav_selection = st.sidebar.radio(
        "Go To:",
        ["📊 Sales Dashboard & Live Leads", "➕ Add New Lead Entry", "📈 Revenue Analytics"]
    )

# --- MAIN PANEL ROUTING ---

# === VIRALITY OS TABS ===
if nav_selection == "🏠 Home Dashboard":
    st.title("🏠 Virality Dashboard - Home")
    st.write("Welcome back, Ashwamegh! System is active and running.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Viral Views", "24.8M", "+12% This Week")
    col2.metric("Saved Video Templates", len(st.session_state.liked_reels), "+2 New")
    col3.metric("Scheduled Content", "5 Videos", "Next: Tomorrow")
    col4.metric("Active Competitors", "5 Accounts", "Tracking Live")

    st.markdown("### 🔥 Trending Organic Keywords")
    keywords_df = pd.DataFrame({
        "Hashtag/Keyword": ["#digitalproducts", "#wasender", "#canvapro", "#automation", "#marketingtips"],
        "Avg Views": ["12.4M", "5.2M", "8.1M", "4.3M", "2.9M"],
        "Funnel Action": ["ManyChat Link", "Direct DM", "Bio Link", "WhatsApp Automation", "ManyChat Link"]
    })
    st.table(keywords_df)

elif nav_selection == "📄 Script Studio":
    st.title("📄 15-Second Viral Script Engine")
    st.write("Generate high-converting scripts based on Nawaz's HPPC Framework (Hook, Proof, Process, CTA).")
    
    prod_name = st.text_input("Enter Product/Software Name:", placeholder="e.g., Canva Pro, WaSender")
    target_aud = st.text_input("Target Audience:", placeholder="e.g., Students, Freelancers, Business Owners")
    
    if st.button("Generate HPPC Script"):
        if prod_name and target_aud:
            st.markdown(f"### 🎬 Generated Script for {prod_name} ({target_aud})")
            st.write(f"**🪝 HOOK (0-3 Sec):** Stop scrolling agar aap ek {target_aud} hain! Main aapko dikhane wala hoon kaise aap roz ka 2 ghanta bacha sakte hain.")
            st.write(f"**🔥 PROOF (3-7 Sec):** Screen par dekhiye, yeh tool automatic saara kaam kar raha hai bina kisi dikkat ke. Meri pichli video par isse 10k+ leads aayi hain!")
            st.write(f"**⚙️ PROCESS (7-12 Sec):** Bas is {prod_name} tool ko active kijiye, apni target list upload kijiye aur aapka complete automation ready.")
            st.write(f"**📢 CALL TO ACTION (12-15 Sec):** Agar aapko bhi iska access chahiye, toh abhi niche comment me \"READY\" likhiye, aur link aapke DM me instantly pohoch jayega!")
        else:
            st.error("Please fill out both fields first!")

elif nav_selection == "❤️ Liked Reels Vault":
    st.title("❤️ Saved Viral Reels Vault")
    st.write("Save and monitor viral reels links in one workspace.")
    
    new_title = st.text_input("Video/Reel Title:")
    new_link = st.text_input("Instagram Reel Link:")
    if st.button("Save Reel Link"):
        if new_title and new_link:
            st.session_state.liked_reels.append({"Title": new_title, "Link": new_link, "Views": "Tracking"})
            st.success("Reel successfully added to vault!")
            
    st.markdown("### 📋 Saved Vault Content")
    st.dataframe(pd.DataFrame(st.session_state.liked_reels), use_container_width=True)

elif nav_selection == "👥 Competitors Board":
    st.title("👥 Competitor Watch Board")
    st.write("Monitor top niche creators and reverse-engineer their viral hooks.")
    
    comp_df = pd.DataFrame({
        "Creator Handle": ["deepakchopra", "gaurgopaldas", "kunalb11", "beerbiceps", "priyakumar7272"],
        "Niche Focus": ["Mindset/Business", "Life Advice", "Tech Startup", "Podcasts/Growth", "Motivation/Books"],
        "Viral Video Style": ["Talking Head + Text B-roll", "Cinematic Quotes", "Clean Text Hooks", "High-cut clips", "Direct whiteboard setup"]
    })
    st.dataframe(comp_df, use_container_width=True)

elif nav_selection == "📊 Content Analytics":
    st.title("📊 Virality Analytics Dashboard")
    st.write("Visual growth track and organic response evaluation.")
    
    chart_data = pd.DataFrame({
        'Days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Views (in Lakhs)': [1.2, 2.5, 1.8, 4.2, 5.0, 7.3, 9.1]
    })
    st.line_chart(chart_data.set_index('Days'))

elif nav_selection == "📅 Posting Calendar":
    st.title("📅 Content Posting Calendar")
    st.write("Plan your digital marketing campaigns & reselling videos schedule.")
    
    col1, col2, col3 = st.columns(3)
    c_date = col1.date_input("Select Date:")
    c_plat = col2.selectbox("Platform:", ["Instagram", "YouTube Shorts", "Facebook Ads", "WhatsApp Status"])
    c_topic = col3.text_input("Video Topic:")
    
    if st.button("Schedule Video"):
        if c_topic:
            st.session_state.calendar_events.append({"Date": str(c_date), "Platform": c_plat, "Topic": c_topic, "Status": "Scheduled"})
            st.success("Content slot locked successfully!")
            
    st.markdown("### 🗓️ Upcoming Schedule")
    st.table(pd.DataFrame(st.session_state.calendar_events))

elif nav_selection == "✍️ AI Hooks Studio":
    st.title("✍️ AI Hooks & Idea Studio")
    st.write("Instantly generate 3 extreme viral hooks for your software promos.")
    
    h_prod = st.text_input("What are you selling today?", placeholder="e.g., Lead Scraper software")
    if st.button("Generate 3 Viral Hooks"):
        st.markdown(f"### 🎯 Hooks For {h_prod}:")
        st.info("🔥 **Hook 1 (FOMO):** Stop scraping data manually like it's 2018! This 1 tool does it in 5 seconds...")
        st.info("💸 **Hook 2 (Result First):** How I extracted 500+ premium B2B client numbers without spending a single rupee.")
        st.info("🚨 **Hook 3 (Negative Psychology):** Don't launch your digital product store until you use this undercover software.")

elif nav_selection == "🎬 AI Editor Helper":
    st.title("🎬 AI Video Editor Assist")
    st.write("Editing strategies, asset notes, and sound hacks to bypass the algorithm.")
    st.markdown("""
    **⚡ Viral Editing Checklist:**
    1. **First 3 Seconds:** Zoom-in effect transitions + Bold Text Hook.
    2. **BGM Volume:** Set trending audio at 5-8% sound level, your voice at 95% clarity.
    3. **Pacing:** Cut out any gaps. Keep the video tight and fast-paced.
    """)

elif nav_selection == "👤 Profile Panel":
    st.title("👤 Founder Executive Profile")
    st.markdown("### Ashwamegh Patil")
    st.write("**Founder & CEO - ASP Digital Hub**")
    st.write("**Industry Experience:** 10+ Years in Digital Hub & Software Reselling Industry")
    st.write("**Primary Contact 1:** +91 9373109809")
    st.write("**Primary Contact 2:** 8055446945")
    st.write("**Focus Portfolio:** SaaS Tools Reselling, Professional Lead Generation & CRM Automation.")


# === COMMERCE OS TABS ===
elif nav_selection == "📊 Sales Dashboard & Live Leads":
    st.title("📊 Live Sales & B2B Leads Database Tracker")
    st.write("This data is synced directly with your Google Sheet `ASP_ViralX_Database`.")
    
    if sheet:
        try:
            data = sheet.get_all_records()
            if data:
                st.dataframe(data, use_container_width=True)
            else:
                st.info("Database sheet is currently empty. Add some leads from the next tab!")
        except Exception as e:
            st.error("Error fetching data from Google Sheets.")
    else:
        st.warning("Google Sheet setup is pending. Please configure secrets in Streamlit Cloud.")

elif nav_selection == "➕ Add New Lead Entry":
    st.title("➕ Add New Lead Flow")
    st.write("Fill details to instantly append data into Google Sheets backend database.")
    
    if not sheet:
        st.warning("Google Sheet not connected.")
    
    with st.form("lead_form", clear_on_submit=True):
        c_name = st.text_input("Customer Name")
        c_whatsapp = st.text_input("WhatsApp Number")
        c_email = st.text_input("Email ID")
        c_product = st.selectbox("Product Issued", ["Canva Pro", "WaSender Tool", "Google Map Scraper", "Digital Bundle"])
        c_status = st.selectbox("Payment Status", ["Paid", "Pending"])
        
        submit = st.form_submit_button("Save Lead to Sheet")
        if submit and sheet:
            today = str(datetime.date.today())
            sheet.append_row([today, c_name, c_whatsapp, c_email, c_product, c_status])
            st.success(f"Success! {c_name}'s data written into Google Sheet.")

elif nav_selection == "📈 Revenue Analytics":
    st.title("📈 Commerce Revenue Dashboard")
    st.write("Track sales conversion graphs and B2B growth metrics.")
    st.metric("Total Generated Revenue Estimation", "₹50,000", "Target Monthly Reach")
    st.info("Keep driving traffic from AI Hooks Studio to grow this metric!")
