import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import datetime

# Page Configuration & Title
st.set_page_config(page_title="ASP ViralX OS", page_icon="🚀", layout="wide")

# --- STREAMLIT SECURE GSHEETS CONNECTION ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Master data sheet pull
    master_df = conn.read(ttl="0d")
except Exception as e:
    master_df = None

# --- Backup Session Memory for Reels Vault ---
if 'liked_reels_backup' not in st.session_state:
    st.session_state.liked_reels_backup = [
        {"Title": "Automation Secret", "Link": "https://instagram.com/reel/1"},
        {"Title": "Canva Pro Free Hack", "Link": "https://instagram.com/reel/2"}
    ]

# --- SIDEBAR NAVIGATION PANEL (NAWAZ STYLE) ---
st.sidebar.title("🚀 ASP VIRALX OS")
st.sidebar.markdown("---")

main_system = st.sidebar.selectbox("SELECT SYSTEM:", ["🟢 VIRALITY OS (Content)", "🛒 COMMERCE OS (Sales & Leads)"])
st.sidebar.markdown("---")

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

# ==========================================
# ===         VIRALITY OS TABS           ===
# ==========================================
if nav_selection == "🏠 Home Dashboard":
    st.title("🏠 Virality Dashboard - Home")
    st.write("Welcome back, Ashwamegh! System is active and running.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Viral Views", "24.8M", "+12% This Week")
    col2.metric("Saved Video Templates", f"{len(st.session_state.liked_reels_backup)} Reels", "Live Sync")
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
    prod_name = st.text_input("Enter Product/Software Name:")
    target_aud = st.text_input("Target Audience:")
    if st.button("Generate HPPC Script"):
        if prod_name and target_aud:
            st.markdown(f"### 🎬 Generated Script for {prod_name}")
            st.write(f"**🪝 HOOK:** Stop scrolling agar aap ek {target_aud} hain!")
            st.write(f"**🔥 PROOF:** Screen par dekhiye, yeh tool automatic saara kaam kar raha hai.")
            st.write(f"**⚙️ PROCESS:** Bas is {prod_name} tool ko active kijiye aur automation ready.")
            st.write(f"**📢 CTA:** Abhi niche comment me \"READY\" likhiye, aur link aapke DM me instantly pohoch jayega!")

elif nav_selection == "❤️ Liked Reels Vault":
    st.title("❤️ Saved Viral Reels Vault")
    st.write("Your permanently locked viral reference database.")
    
    with st.form("vault_form", clear_on_submit=True):
        new_title = st.text_input("Video/Reel Title:")
        new_link = st.text_input("Instagram Reel Link:")
        submit_reel = st.form_submit_button("Save Reel Memory Layout")
        
        if submit_reel and new_title and new_link:
            st.session_state.liked_reels_backup.append({"Title": new_title, "Link": new_link})
            st.success(f"🚀 Success! '{new_title}' has been locked into your OS memory layout panel!")
            st.rerun()
            
    st.markdown("### 📋 Active Vault Data")
    st.dataframe(pd.DataFrame(st.session_state.liked_reels_backup), use_container_width=True)

elif nav_selection == "👥 Competitors Board":
    st.title("👥 Competitor Watch Board")
    comp_df = pd.DataFrame({
        "Creator Handle": ["deepakchopra", "gaurgopaldas", "kunalb11", "beerbiceps", "priyakumar7272"],
        "Niche Focus": ["Mindset/Business", "Life Advice", "Tech Startup", "Podcasts/Growth", "Motivation/Books"],
        "Viral Video Style": ["Talking Head + Text B-roll", "Cinematic Quotes", "Clean Text Hooks", "High-cut clips", "Direct whiteboard setup"]
    })
    st.dataframe(comp_df, use_container_width=True)

elif nav_selection == "📊 Content Analytics":
    st.title("📊 Virality Analytics Dashboard")
    chart_data = pd.DataFrame({'Days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 'Views (in Lakhs)': [1.2, 2.5, 1.8, 4.2, 5.0, 7.3, 9.1]})
    st.line_chart(chart_data.set_index('Days'))

elif nav_selection == "📅 Posting Calendar":
    st.title("📅 Content Posting Calendar")

elif nav_selection == "✍️ AI Hooks Studio":
    st.title("✍️ AI Hooks & Idea Studio")
    h_prod = st.text_input("What are you selling today?")
    if st.button("Generate 3 Viral Hooks"):
        st.info(f"🔥 **Hook 1:** Stop scraping data manually like it's 2018! Use {h_prod}...")

elif nav_selection == "🎬 AI Editor Helper":
    st.title("🎬 AI Video Editor Assist")
    st.markdown("1. **First 3 Seconds:** Zoom-in effect transitions.\n2. **BGM Volume:** Trending audio at 5-8%.")

elif nav_selection == "👤 Profile Panel":
    st.title("👤 Founder Executive Profile")
    st.markdown("### Ashwamegh Patil\n**Founder & CEO - ASP Digital Hub**\n**Experience:** 10+ Years\n**Contacts:** +91 9373109809, 8055446945")

# ==========================================
# ===         COMMERCE OS TABS           ===
# ==========================================
elif nav_selection == "📊 Sales Dashboard & Live Leads":
    st.title("📊 Live Sales & B2B Leads Database Tracker")
    if master_df is not None and not master_df.empty:
        st.dataframe(master_df, use_container_width=True)
    else:
        st.info("Leads database is active. Add your client entries from the next tab!")

elif nav_selection == "➕ Add New Lead Entry":
    st.title("➕ Add New Lead Flow")
    with st.form("lead_form", clear_on_submit=True):
        c_name = st.text_input("Customer Name")
        c_whatsapp = st.text_input("WhatsApp Number")
        c_email = st.text_input("Email ID")
        c_product = st.selectbox("Product Issued", ["Canva Pro", "WaSender Tool", "Google Map Scraper", "Digital Bundle"])
        c_status = st.selectbox("Payment Status", ["Paid", "Pending"])
        submit = st.form_submit_button("Save Lead Securely to Cloud Sheet")
        
        if submit and c_name:
            try:
                today = str(datetime.date.today())
                new_lead = pd.DataFrame([{"Date": today, "Customer Name": c_name, "WhatsApp Number": c_whatsapp, "Email ID": c_email, "Product": c_product, "Payment Status": c_status}])
                updated_leads = pd.concat([master_df, new_lead], ignore_index=True) if master_df is not None else new_lead
                conn.update(data=updated_leads)
                st.success(f"💥 Success! {c_name}'s data has been updated in the cloud panel.")
                st.rerun()
            except Exception as ex:
                st.error(f"Error updating leads: {ex}")

elif nav_selection == "📈 Revenue Analytics":
    st.title("📈 Commerce Revenue Dashboard")
    st.metric("Total Generated Revenue Estimation", "₹50,000", "Target Monthly Reach")
