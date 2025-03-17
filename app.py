import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Task Web App", page_icon="🪙", layout="wide")

# Theme Colors
st.markdown(
    """
    <style>
    body {
        background-color: #001f3f;
        color: white;
    }
    .stButton>button {
        background-color: #6A0DAD;
        color: white;
        font-size: 18px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User Data
if "coins" not in st.session_state:
    st.session_state["coins"] = 0
if "tasks_completed" not in st.session_state:
    st.session_state["tasks_completed"] = 0
if "referrals" not in st.session_state:
    st.session_state["referrals"] = 0
if "clicks" not in st.session_state:
    st.session_state["clicks"] = 0

# Header
st.title("🎯 Task Web App - Earn Coins")
st.subheader("Complete Tasks & Earn Rewards")

# Tasks Section
st.markdown("### ✅ Complete Tasks")
if st.session_state["tasks_completed"] < 10:
    if st.button("Watch Ad (5 Coins)"):
        st.session_state["coins"] += 5
        st.session_state["tasks_completed"] += 1
        st.success("You earned 5 coins!")
    if st.button("Complete Survey (5 Coins)"):
        st.session_state["coins"] += 5
        st.session_state["tasks_completed"] += 1
        st.success("Survey completed! +5 coins")
    if st.button("Install App (5 Coins)"):
        st.session_state["coins"] += 5
        st.session_state["tasks_completed"] += 1
        st.success("App installed! +5 coins")
else:
    st.warning("🚫 Daily task limit reached (10 tasks)")

# Referral Section
st.markdown("### 👥 Referral System")
if st.session_state["referrals"] < 10:
    if st.button("Refer a Friend (5 Coins)"):
        st.session_state["coins"] += 5
        st.session_state["referrals"] += 1
        st.success("Referral added! +5 coins")
else:
    st.warning("🚫 Max referrals reached (10)")

# Ad Click Section
st.markdown("### 🎯 Click Ads")
if st.session_state["clicks"] < 5:
    if st.button("Click Ad (5 Coins)"):
        st.session_state["coins"] += 5
        st.session_state["clicks"] += 1
        st.success("Ad clicked! +5 coins")
else:
    st.warning("🚫 Max ad clicks reached (5)")

# Coin Balance
st.markdown("## 🏆 Your Balance")
st.info(f"💰 Total Coins: {st.session_state['coins']}")

# Withdrawal Section
if st.session_state["coins"] >= 15000:
    st.markdown("### 💸 Request Withdrawal")
    method = st.selectbox("Choose Payment Method:", ["JazzCash", "EasyPaisa", "Payoneer", "PayPal"])
    account = st.text_input("Enter Your Account Number")
    if st.button("Withdraw"):
        st.success(f"Withdrawal requested via {method} to {account}")
        st.session_state["coins"] = 0
else:
    st.warning("⚠️ Minimum 15000 coins required for withdrawal")
