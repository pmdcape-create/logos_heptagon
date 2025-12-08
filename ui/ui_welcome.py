# ==============================
# UI_WELCOME
# ==============================

import streamlit as st
import streamlit.components.v1 as components

# These are the correct 7 planes (exactly as in your original beautiful gem)
PLANES = [
    "Purpose",
    "Information/Truth",
    "Design",
    "Creation",
    "Refinement",
    "Revelation",
    "Continuity"
]

def show_welcome():
    st.title("LOGOS Heptagon Revealer")
    st.markdown("""
    **A 7×7 Metaphysical Diagnostic for Real-Life Questions**  
    Powered exclusively by Grok AI
    """)

    st.markdown("### The Heptagon Gem – 7 Planes of Resonance")

    # ──────────────────────────────────────────────
    # THE FIXED, BEAUTIFUL, FULLY WORKING HEPTAGON
    # ──────────────────────────────────────────────
    heptagon_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LOGOS Heptagon</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body{font-family:'Inter',sans-serif;background:transparent;margin:0;padding:20px 0;overflow:hidden}
            .heptagon-container{position:relative;width:360px;height:360px;margin:0 auto}
            .center-dot{position:absolute;top:50%;left:50%;width:34px;height:34px;background:#fca5a5;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 18px rgba(252,165,165,.9);z-index:5}
            .point{position:absolute;width:80px;height:80px;background:white;border-radius:16px;box-shadow:0 5px 15px rgba(0,0,0,.18);display:flex;flex-direction:column;justify-content:center;align-items:center;padding:6px;cursor:pointer;transition:all .3s;z-index:10}
            .point:hover,.point.active{transform:scale(1.1) translateY(-6px);box-shadow:0 0 15px 30px rgba(0,0,0,.3);z-index:30}
            .layer-number{font-weight:700;font-size:1.4rem;color:#1e293b}
            .pane-name{font-weight:600;font-size:0.72rem;color:#475569;margin-top:3px}
            #popup{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:300px;background:white;border:2px solid #1e3a8a;border-radius:14px;padding:16px;box-shadow:0 12px 40px rgba(30,58,138,.45);z-index:100;pointer-events:none;opacity:0;transition:opacity .3s;text-align:left}
            #popup.visible{opacity:1}
            #popup h4{margin:0 0 10px;font-size:16px;color:#1e3a8a}
            #popup p{margin:0;font-size:12px;line-height:1.45;color:#475569}
        </style>
    </head>
    <body>
        <div class="heptagon-container" id="heptagon">
            <div class="center-dot"></div>
            <div id="popup"></div>
        </div>
        <script>
            const data = [
                {l:1,p:"Purpose",c:"bg-indigo-200",i:"L1: Receives 'raw potential' and initializes unique entities or events."},
                {l:2,p:"Information/Truth",c:"bg-blue-200",i:"L2: Maintains continuity and identity; subject to feedback from higher layers."},
                {l:3,p:"Design",c:"bg-teal-200",i:"L3: How instances affect the environment; creates observable outcomes."},
                {l:4,p:"Creation",c:"bg-green-200",i:"L4: Mediates interactions among 1–3; the 'arena' of experience and evolution."},
                {l:5,p:"Refinement",c:"bg-yellow-200",i:"L5: Introduces choice, adaptation, and probabilistic collapse."},
                {l:6,p:"Revelation",c:"bg-orange-200",i:"L6: Maintains coherence, imposes laws and principles; system governance."},
                {l:7,p:"Continuity",c:"bg-red-200",i:"L7: Provides ultimate direction, purpose, and overarching alignment."}
            ];
            const CX=180,CY=180,R=150;
            const container=document.getElementById('heptagon'), popup=document.getElementById('popup');
            let active=null;
            function pos(i){const a=Math.PI*2*i/7-Math.PI/2;return{x:CX+R*Math.cos(a),y:CY+R*Math.sin(a)};}
            function build(){
                [...container.children].filter(c=>!c.classList?.contains('center-dot')&&c.id!=='popup').forEach(c=>c.remove());
                let pts="",coords=[];
                data.forEach((d,i)=>{let p=pos(i);coords.push({x:p.x,y:p.y,d});pts+=`${p.x},${p.y} `;});
                const svg=document.createElementNS("http://www.w3.org/2000/svg","svg");
                svg.style.position="absolute";svg.style.inset=0;svg.style.zIndex=2;
                const line=document.createElementNS("http://www.w3.org/2000/svg","polyline");
                line.setAttribute("points",pts.trim());line.setAttribute("fill","none");line.setAttribute("stroke","#64748b");line.setAttribute("stroke-width","3");
                svg.appendChild(line);container.appendChild(svg);
                coords.forEach(o=>{
                    const el=document.createElement("div");
                    el.className=`point ${o.d.c}`;
                    el.style.left=`${o.x-40}px`;el.style.top=`${o.y-40}px`;
                    el.innerHTML=`<div class="layer-number">${o.d.l}</div><div class="pane-name">${o.d.p}</div>`;
                    el.onmouseenter=_=>{
                        popup.innerHTML=`<h4>Layer ${o.d.l}: ${o.d.p}</h4><p>${o.d.i}</p>`;
                        popup.classList.add("visible");
                        if(active)active.classList.remove("active");el.classList.add("active");active=el;
                    };
                    el.onmouseleave=_=>{if(active===el){el.classList.remove("active");popup.classList.remove("visible");active=null;}};
                    container.appendChild(el);
                });
            }
            build();
            window.addEventListener("resize",build);
        </script>
    </body>
    </html>
    """

    components.html(heptagon_html, height=420, scrolling=False)

    st.caption("Hover over any plane to see its metaphysical role")

    # ──────────────────────────────────────────────
    # Big beautiful button to start the analysis
    # ──────────────────────────────────────────────
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("I'm ready → Begin LOGOS Analysis", type="primary", use_container_width=True):
            st.session_state.first_run = False
            st.rerun()

    st.stop()
