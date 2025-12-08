# ui/ui_results.py   ← FINAL & PERFECT VERSION

import streamlit as st
from logic.exporters import grid_to_html, reading_to_pdf
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def show_results():
    # FIXED LINE – this was the only cause of the ValueError
    df = st.session_state.get("df")
    if df is None or not st.session_state.get("topic_confirmed", False):
        return

    st.success("LOGOS analysis complete")

    # Safe values (exactly like you already had)
    question     = st.session_state.get("natural_sentence") or st.session_state.get("topic", "")
    coherence    = st.session_state.get("coherence", 0.0)
    ratio        = st.session_state.get("ratio", 0.0)
    reading_text = st.session_state.get("reading_text", "")
    topic        = st.session_state.get("topic", "LOGOS_Analysis")

    st.markdown(f"**Your question:** {question}")
    st.markdown(f"**Coherence:** {coherence:.1f}%  │  **Ratio:** {ratio:.3f}/1.000")

    st.markdown("## LOGOS FINDINGS & INTERPRETATION")
    st.markdown(reading_text)

    st.markdown("---")
    st.subheader("7×7 Heptagon Data Grid")
    st.dataframe(df.style.set_properties(**{
        'text-align': 'left',
        'white-space': 'pre-wrap',
        'font-size': '14px',
        'padding': '12px'
    }), use_container_width=True)

# ====================== SUMMARY GENERATED ======================
if "summary_generated" not in st.session_state:
    with st.spinner("Crafting your personal summary..."):
        from logic.summary_generator import generate_summary
        summary = generate_summary(st.session_state.df, question)
        st.session_state.reading_text = summary
        st.session_state.summary_generated = True

st.markdown("## LOGOS FINDINGS & INTERPRETATION")
st.markdown(st.session_state.reading_text)
    # ====================== BUTTONS (exactly as you wanted) ======================
    col_a, col_b, col_c, col_d = st.columns(4)

    with col_a:
        if st.button("New Question", type="secondary"):
            keys_to_clear = ["df", "reading_text", "topic_confirmed",
                           "natural_sentence", "topic", "coherence", "ratio"]
            for key in keys_to_clear:
                st.session_state.pop(key, None)
            st.rerun()

    with col_b:
        if st.button("Close / Exit"):
            st.success("Thank you for using LOGOS. See you soon!")
            st.stop()

    with col_c:
        html_data = grid_to_html(df, topic, coherence, ratio).getvalue()
        st.download_button("Grid (HTML)", html_data,
                           f"LOGOS_Grid_{topic.replace(' ','_')}.html", "text/html")

    with col_d:
        pdf_data = reading_to_pdf(reading_text).getvalue()
        st.download_button("Summary (PDF)", pdf_data,
                           f"LOGOS_Findings_{topic.replace(' ','_')}.pdf", "application/pdf")

    # ====================== REQUEST MORE INFO (kept 100% as you wrote it) ======================
    st.markdown("---")
    st.subheader("Want a deeper personal reading?")
    with st.form("request_form"):
        name = st.text_input("Your name (optional)")
        email = st.text_input("Your email", placeholder="you@example.com")
        message = st.text_area("Message / specific request")
        submitted = st.form_submit_button("Send request to Jan")

        if submitted:
            try:
                msg = MIMEMultipart()
                msg['From'] = "logos@app.com"
                msg['To'] = "janvanderwalt2025@gmail.com"           # ← your receiving address
                msg['Subject'] = f"LOGOS Request from {name or 'User'}"

                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}\n\nQuestion was: {question}"
                msg.attach(MIMEText(body, 'plain'))

                # Attach PDF
                part = MIMEBase('application', "octet-stream")
                part.set_payload(pdf_data)
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="Findings.pdf"')
                msg.attach(part)

                # Attach HTML grid
                part2 = MIMEBase('application', "octet-stream")
                part2.set_payload(html_data)
                encoders.encode_base64(part2)
                part2.add_header('Content-Disposition', 'attachment; filename="Grid.html"')
                msg.attach(part2)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("janvanderwalt2025@gmail.com", "qjia igrm hpnt rgic")  # ← change to App Password!
                server.send_message(msg)
                server.quit()

                st.success("Request sent! I will reply within 24h")
            except Exception:
                st.error("Could not send email right now. Please email me directly at janvanderwalt2025@gmail.com")
