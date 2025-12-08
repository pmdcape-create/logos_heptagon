# ==============================
# logic/exporters.py
# ==============================

import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

def reading_to_pdf(reading_text: str) -> BytesIO:
    """
    Converts the full LOGOS findings/summary into a beautiful landscape PDF
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4), topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    story = []
    story.append(Paragraph("LOGOS Heptagon – Complete Findings", styles['Title']))
    story.append(Spacer(1, 30))
    story.append(Paragraph(reading_text.replace("\n", "<br/>"), styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer


def grid_to_html(df: pd.DataFrame, topic: str, coherence: float, ratio: float) -> BytesIO:
    """
    Converts the 7×7 grid + metadata into a beautiful standalone HTML file
    """
    buffer = BytesIO()
    
    styled_df = df.to_html(classes="table table-striped", border=0, justify="left")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>LOGOS Heptagon – {topic}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f8fafc; }}
            h1 {{ color: #1e3a8a; }}
            .info {{ background: #e0f2fe; padding: 15px; border-radius: 8px; margin: 20px 0; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 12px; text-align: left; border: 1px solid #94a3b8; }}
            th {{ background: #1e3a8a; color: white; }}
        </style>
    </head>
    <body>
        <h1>LOGOS Heptagon Analysis</h1>
        <div class="info">
            <strong>Question:</strong> {topic}<br/>
            <strong>Coherence Score:</strong> {coherence:.1f}%  │  
            <strong>Coherence Ratio:</strong> {ratio:.3f}/1.000
        </div>
        {styled_df}
    </body>
    </html>
    """
    buffer.write(html_content.encode('utf-8'))
    buffer.seek(0)
    return buffer
