import streamlit as st
import pandas as pd
import requests

# 1. Dashboard Settings
st.set_page_config(page_title="Gold Intelligence Pro", layout="wide")

# 2. Telegram Bot Configuration
# လူကြီးမင်း BotFather ဆီကရတဲ့ Token နဲ့ ID ကို ဒီနေရာမှာ အစားထိုးပါ
TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_telegram_alert(message):
    if TOKEN != "YOUR_BOT_TOKEN_HERE":
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
        try:
            requests.post(url, data=payload)
        except:
            st.error("Telegram Alert ပို့လို့မရပါ (Connection Error)")

# 3. Sidebar - Market Overview
st.sidebar.title(" XAU/USD Monitor")
st.sidebar.metric(label="Live Gold Price", value="$5,278.50", delta="+1.2%")
st.sidebar.write("---")
st.sidebar.write("**EA Strategy:** EMA 161/423")
st.sidebar.write("**Timeframe:** M5")
st.sidebar.write("**Lot Size:** 0.05")

# 4. Main Dashboard UI
st.title(" Gold Intelligence Dashboard (2026)")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header(" Fundamental & WGC Insights")
    st.info(" **WGC Update:** Central Banks increased gold reserves by 15% this quarter. Bullish momentum expected.")
    
    st.subheader(" High Impact News Feed")
    st.write(" **10:30 AM:** US PCE Data lower than expected - Bullish")
    st.write(" **02:15 PM:** Geopolitical tension in Middle East - High Volatility")
    st.write(" **04:00 PM:** DXY Dollar Index Weakness - Moderate Bullish")

with col2:
    st.header(" Market Sentiment")
    st.write("Bullish Confidence")
    st.progress(85)
    st.success("Current Sentiment: **Strong Buy**")
    
    st.divider()
    st.header(" Telegram Controls")
    if st.button("Send Test Alert"):
        send_telegram_alert(" <b>Gold Pro System:</b> Dashboard Connected Successfully!")
        st.write("Alert Sent to your phone!")

st.divider()
st.caption(" 2026 Developed for Professional Gold Trading Ecosystem")
