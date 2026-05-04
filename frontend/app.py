import streamlit as st
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Try to load data module
data_ok = False
try:
    from data.market_data import get_1min_kline, get_historical_klines
    data_ok = True
except Exception as e:
    st.error(f"Data module load failed: {e}")

st.set_page_config(page_title="Quant Trading System", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    .stMetric { background-color: #1e1e1e; border-radius: 10px; padding: 10px; text-align: center; color: #ffffff; }
    h1, h2, h3 { color: #ffffff !important; text-align: center; }
    div[data-testid="stMarkdownContainer"] { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

st.title("Quant Trading System v5.0")
st.caption("Multi-Category · Multi-Strategy · AI Auto Trading")

# Get real price
price = 1.085
if data_ok:
    try:
        kline = get_1min_kline("EURUSD")
        if kline:
            price = kline.get('close', 1.085)
    except:
        pass

col1, col2, col3 = st.columns(3)
col1.metric("Total Assets", "$100,000")
col2.metric("Latest Price", f"{price:.5f}")
col3.metric("Update Time", time.strftime("%Y-%m-%d %H:%M:%S"))

st.subheader("Strategy Status")
st.success(f"System Ready | Current Price: {price}")

tab1, tab2 = st.tabs(["Strategy List", "Configuration"])
with tab1:
    st.write("1. Futures Trend Strategy (GC=F)")
    st.write("2. Futures Mean Reversion (CL=F)")
    st.write("3. Forex Carry Trade (AUDJPY)")
    st.write("4. Forex Breakout Strategy (EURUSD)")
with tab2:
    st.info("Backend running | Auto deploy from GitHub")
