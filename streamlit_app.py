import streamlit as st

st.title("Streamlit Header Probe")

st.write("### IP detectado")
st.code(str(st.context.ip_address))

st.write("### Headers recebidos")
headers = dict(st.context.headers)

for key, value in sorted(headers.items()):
    if key.lower() in {"cookie", "authorization"}:
        value = "[REDACTED]"

    st.write(f"**{key}**")
    st.code(str(value))
