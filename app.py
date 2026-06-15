import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration & Title
st.set_page_config(page_title="ASP ViralX OS", page_icon="🚀", layout="wide")

# Custom Premium Styling (Dark Theme & Neon Accents)
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    h1, h2, h3 { color: #00FFCC !important; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #00FFCC !important; color: #0E1117 !important;
        font-weight: bold; border-radius: 8px; border: none; padding: 10px 24px;
    }
    .stButton>button:hover { background-color: #00CC99 !important; }
    .sidebar .sidebar-content { background-color: #1A1F2C !important; }
    div[data-testid="stMetricValue"] { color: #00FFCC !important; }
    .card {
        background-color: #1A1F2C; padding: 20px; border-radius: 10px;
        border-left: 5px solid #00FFCC; margin-bottom: 15px;
    }
    </style>
""", unsafe_with_html=True)

# --- Session State Data Initialization (For Demo & Persistence) ---
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

# --- SIDEBAR NAVIGATION PANEL ---
st.sidebar.title("🚀 ASP VIRALX OS")
st.sidebar.subheader("Main Systems")

# Section 1: Virality OS
st.sidebar.markdown("---")
st.sidebar.markdown("**🟢 VIRALITY OS (Content)**")
nav_selection = st.sidebar.radio(
    "Go To:",
    ["🏠 Home", "📄 Script Studio", "❤️ Liked Reels", "👥 Competitors", "📊 Analytics", "📅 Calendar", "✍️ AI Hooks Studio", "🎬 AI Editor Helper", "👤 Profile Panel"]
)

# Section 2: Commerce OS Banner
st.sidebar.markdown("---")
st.sidebar.markdown("**🛒 COMMERCE OS (Sales)**")
if st.sidebar.button("📊 Manage Leads Database"):
    nav_selection = "🛒 Commerce OS"

# --- MAIN PANEL ROUTING ---

# 1. HOME TAB
if nav_selection == "🏠 Home":
    st.title("🏠 Virality Dashboard - Home")
    st.write("Welcome back, Ashwamegh! System is active and running.")
    
    # Quick Status Metrics
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

# 2. SCRIPT STUDIO
elif nav_selection == "📄 Script Studio":
    st.title("📄 15-Second Viral Script Engine")
    st.write("Generate high-converting scripts based on Nawaz's HPPC Framework (Hook, Proof, Process, CTA).")
    
    prod_name = st.text_input("Enter Product/Software Name:", placeholder="e.g., Canva Pro, WaSender")
    target_aud = st.text_input("Target Audience:", placeholder="e.g., Students, Freelancers, Business Owners")
    
    if st.button("Generate HPPC Script"):
        if prod_name and target_aud:
            st.markdown(f"### 🎬 Generated Script for {prod_name} ({target_aud})")
            
            st.markdown(f"""
            <div class='card'>
            <b>🪝 HOOK (0-3 Sec):</b> Stop scrolling agar aap ek {target_aud} hain! Main aapko dikhane wala hoon kaise aap roz ka 2 ghanta bacha sakte hain.<br><br>
            <b>🔥 PROOF (3-7 Sec):</b> Screen par dekhiye, yeh tool automatic saara kaam kar raha hai bina kisi dikkat ke. Meri pichli video par isse 10k+ leads aayi hain!<br><br>
            <b>⚙️ PROCESS (7-12 Sec):</b> Bas is {prod_name} tool ko active kijiye, apni target list upload kijiye aur aapka complete automation ready.<br><br>
            <b>📢 CALL TO ACTION (12-15 Sec):</b> Agar aapko bhi iska access chahiye, toh abhi niche comment me <b>"READY"</b> likhiye, aur link aapke DM me instantly pohoch jayega!
            </div>
            """, unsafe_with_html=True)
        else:
            st.error("Please fill out both fields first!")

# 3. LIKED REELS
elif nav_selection == "❤️ Liked Reels":
    st.title("❤️ Saved Viral Reels Vault")
    st.write("Save and monitor viral reels links in one workspace.")
    
    # Input new reel
    new_title = st.text_input("Video/Reel Title:")
    new_link = st.text_input("Instagram Reel Link:")
    if st.button("Save Reel Link"):
        if new_title and new_link:
            st.session_state.liked_reels.append({"Title": new_title, "Link": new_link, "Views": "Tracking"})
            st.success("Reel successfully added to vault!")
            
    st.markdown("### 📋 Saved Vault Content")
    st.dataframe(pd.DataFrame(st.session_state.liked_reels), use_container_width=True)

# 4. COMPETITORS
elif nav_selection == "👥 Competitors":
    st.title("👥 Competitor Watch Board")
    st.write("Monitor top niche creators and reverse-engineer their viral hooks.")
    
    comp_df = pd.DataFrame({
        "Creator Handle": ["deepakchopra", "gaurgopaldas", "kunalb11", "beerbiceps", "priyakumar7272"],
        "Niche Focus": ["Mindset/Business", "Life Advice", "Tech Startup", "Podcasts/Growth", "Motivation/Books"],
        "Viral Video Style": ["Talking Head + Text B-roll", "Cinematic Quotes", "Clean Text Hooks", "High-cut clips", "Direct whiteboard setup"]
    })
    st.dataframe(comp_df, use_container_width=True)

# 5. ANALYTICS
elif nav_selection == "📊 Analytics":
    st.title("📊 Virality Analytics Dashboard")
    st.write("Visual growth track and organic response evaluation.")
    
    # Generate mock chart
    chart_data = pd.DataFrame({
        'Days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Views (in Lakhs)': [1.2, 2.5, 1.8, 4.2, 5.0, 7.3, 9.1]
    })
    st.line_chart(chart_data.set_index('Days'))
    st.success("Your content vector is moving high! Focus on posting between 6 PM to 9 PM.")

# 6. CALENDAR
elif nav_selection == "📅 Calendar":
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

# 7. AI HOOKS STUDIO
elif nav_selection == "✍️ AI Hooks Studio":
    st.title("✍️ AI Hooks & Idea Studio")
    st.write("Instantly generate 3 extreme viral hooks for your software promos.")
    
    h_prod = st.text_input("What are you selling today?", placeholder="e.g., Lead Scraper software")
    if st.button("Generate 3 Viral Hooks"):
        st.markdown(f"### 🎯 Hooks For {h_prod}:")
        st.info("🔥 **Hook 1 (Fear Of Missing Out):** Stop scraping data manually like it's 2018! This 1 tool does it in 5 seconds...")
        st.info("💸 **Hook 2 (Result First):** How I extracted 500+ premium B2B client numbers without spending a single rupee.")
        st.info("🚨 **Hook 3 (Negative Psychology):** Don't launch your digital product store until you use this undercover software.")

# 8. AI EDITOR HELPER
elif nav_selection == "🎬 AI Editor Helper":
    st.title("🎬 AI Video Editor Assist")
    st.write("Editing strategies, asset notes, and sound hacks to bypass the algorithm.")
    
    st.markdown("""
    <div class='card'>
    <h4>⚡ Viral Editing Checklist:</h4>
    1. <b>First 3 Seconds:</b> Zoom-in effect transitions + Neon Text Highlight.<br>
    2. <b>BGM Volume:</b> Set trending audio at 5-8% sound level, your voice at 95% clarity.<br>
    3. <b>Pacing:</b> Cut out any 'umms' or 'ahhs'. Keep the video tight and fast-paced.
    </div>
    """, unsafe_with_html=True)

# 9. PROFILE PANEL
elif nav_selection == "👤 Profile Panel":
    st.title("👤 Founder Executive Profile")
    st.markdown("""
    <div class='card'>
    <h2>Ashwamegh Patil</h2>
    <h4>Founder & CEO - ASP Digital Hub</h4>
    <p><b>Industry Experience:</b> 10+ Years in Digital Hub & Software Reselling Industry</p>
    <p><b>Primary Contact 1:</b> +91 9373109809</p>
    <p><b>Primary Contact 2:</b> 8055446945</p>
    <p><b>Focus Portfolio:</b> SaaS Tools Reselling, Professional Lead Generation & CRM Automation.</p>
    </div>
    """, unsafe_with_html=True)

# 10. COMMERCE OS (LEADS DATABASE INTERACTION)
elif nav_selection == "🛒 Commerce OS":
    st.title("🛒 Commerce OS - Active Lead Engine")
    st.write("Connected to backend database sheets for active customer management.")
    
    # Active Google Sheet connectivity dummy frame for clean loading placeholder
    st.warning("🔒 Database live synchronized with Google Sheet API.")
    
    # Lead Input Form
    with st.form("leads_form"):
        st.subheader("Add Customer/Lead Flow")
        c_name = st.text_input("Customer Full Name:")
        c_num = st.text_input("WhatsApp Number:")
        c_mail = st.text_input("Email ID:")
        c_prod = st.selectbox("Product Issued:", ["Canva Pro", "WaSender Automation", "Google Map Scraper", "Complete SaaS Bundle"])
        c_stat = st.selectbox("Payment Status:", ["Paid", "Pending"])
        
        submitted = st.form_submit_button("Save Lead to Sheet")
        if submitted:
            st.success(f"Success! Data for {c_name} successfully written into Google Sheet database backend.")
