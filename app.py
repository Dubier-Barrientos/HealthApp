import streamlit as st

with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Visual", "Auditiva", "Haptica")
  )
