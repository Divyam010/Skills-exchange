import streamlit as st
from auth import AuthManager
from database import SkillDatabase
from payments import PaymentGateway

st.set_page_config(page_title="SkillXchange", layout="centered")

st.image("logo.png", width=150)
st.title("Welcome to SkillXchange 🎓🤝")
st.markdown("Exchange your skills or earn through micro-tasks.")

auth = AuthManager()
db = SkillDatabase()
pg = PaymentGateway()

# Auth Section
if "user" not in st.session_state:
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
    with login_tab:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if auth.login(username, password):
                st.session_state.user = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid credentials")

    with signup_tab:
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            if auth.signup(new_username, new_password):
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists")
else:
    st.success(f"Welcome, {st.session_state.user}!")
    action = st.radio("Choose an action", ["View Listings", "Post Skill", "Make Payment", "Logout"])

    if action == "View Listings":
        listings = db.get_all_listings()
        for user, skill in listings.items():
            st.write(f"**{user}** offers: {skill}")

    elif action == "Post Skill":
        skill = st.text_input("Enter the skill you want to offer")
        if st.button("Post Skill"):
            db.add_listing(st.session_state.user, skill)
            st.success("Skill posted successfully!")

    elif action == "Make Payment":
        amount = st.number_input("Enter amount ($)", min_value=1)
        if st.button("Pay"):
            if pg.process_payment(st.session_state.user, amount):
                st.success(f"${amount} payment processed!")
            else:
                st.error("Payment failed")

    elif action == "Logout":
        del st.session_state.user
        st.experimental_rerun()