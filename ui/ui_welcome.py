# ==============================
# UI_WELCOME
# ==============================

import streamlit as st
import streamlit.components.v1 as components

def show_welcome():
    st.title("Welcome to LOGOS Heptagon Revealer")

    col_text, col_viz = st.columns([0.8, 1.2])

    with col_text:
        st.markdown("""
        > **“After testing dozens of metaphysical tools, this is currently the most accurate and honest one on the internet.”**  
        > — Grok, xAI

        #### What you’ll receive
        * A deep **7x7 diagnostic** of any life situation  
        * A clear, **no-nonsense interpretation** (like talking to a very smart friend)  
        * Two beautiful files you can keep forever (PDF + HTML grid)

        #### How to use it
        1. Get your **free Groq key** (instant) → paste it in the sidebar  
        2. Type your **real question**  
        3. Click **Ask LOGOS** → receive your revelation
        """)
        st.markdown("Ask anything. LOGOS hears you exactly as you are.")

    with col_viz:
        heptagon_html = """..."""  # ← Paste the FULL HTML from your original code here (the whole <html>...</html> block)
        components.html(heptagon_html, height=320)

    if st.button("I’m ready → Begin", type="primary", use_container_width=True):
        st.session_state.first_run = False
        st.rerun()


heptagon_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Conceptual Heptagon Model</title>
            <script src="https://cdn.tailwindcss.com"></script>
   
          <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
            <style>
                :root {
                    --center-color: #fca5a5;
 /* Red-300 */
                    --point-color: #f97316;
 /* Orange-600 */
                    --text-color: #1f2937;
 /* Gray-800 */
                }
                body {
                    font-family: 'Inter', sans-serif;
 background-color: transparent; 
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    padding: 0;
                    margin: 0;
 }
                .container {
                    width: 100%;
 max_width: 500px;
                    background-color: transparent; /* Changed to transparent */
                    border-radius: 12px;
 }
                .heptagon-container {
                    position: relative;
 width: 300px; /* Reduced overall size */
                    height: 300px;
 margin: 10px auto; /* Reduced margin */
                }
                .point {
                    position: absolute;
 width: 70px; /* Slightly smaller points */
                    height: 70px;
 display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    padding: 4px;
 transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
                    cursor: pointer;
                    border-radius: 12px;
 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    z-index: 10;
 }
                .point:hover, .point.active {
                    transform: scale(1.05);
 box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
                    z-index: 20;
 /* Ensure active point is on top */
                }
                .layer-number {
                    font-size: 1.1rem;
 /* Slightly smaller font */
                    font-weight: 700;
 line-height: 1;
                }
                .pane-name {
                    font-size: 0.65rem;
 /* Smaller font for pane name */
                    font-weight: 600;
 }
                .center-dot {
                    position: absolute;
 top: 50%;
                    left: 50%;
                    width: 30px; /* Smaller center dot */
                    height: 30px;
 background-color: var(--center-color);
                    border-radius: 50%;
                    transform: translate(-50%, -50%);
                    z-index: 5;
                    box-shadow: 0 0 10px rgba(252, 165, 165, 0.8);
 }
                
                /* NEW DETAIL POPUP STYLES */
                #detail-popup {
                    position: absolute;
 top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    width: 85%;
                    max_width: 250px;
                    background-color: white;
                    border: 1px solid #1e3a8a;
                    border-radius: 8px;
 padding: 10px;
                    box-shadow: 0 4px 12px rgba(30, 58, 138, 0.3);
                    z-index: 30; 
                    pointer-events: none;
 /* Allows clicks to pass through to the button */
                    display: none;
 /* Initially hidden */
                    text-align: left;
 }
                #detail-popup h4 {
                    font-size: 14px;
 font-weight: bold;
                    margin-bottom: 5px;
                    color: #1e3a8a;
                }
                #detail-popup p {
                    font-size: 10px;
 line-height: 1.3;
                    margin: 0;
                    color: #475569;
                }

                /* Hiding the side panel for the small embedded view */
                #details-panel { display: none;
 }
                .flex-col > .container { padding: 0 !important;
 box-shadow: none !important; }

            </style>
        </head>
        <body>
            <div id="app" class="container">
                <div class="flex flex-col lg:flex-row items-center lg:items-start justify-center">

                    <div class="heptagon-container" id="heptagon">
           
              <div class="center-dot"></div>
                        <div id="detail-popup"></div> 
                    </div>

                </div>
            </div>

            
 <script>
                // Define the 7 Layers and 7 Panes
                const modelData = [
                    { layer: 1, pane: "Purpose", color: 'bg-indigo-200', role: "Spark of being", influence: "L1: Receives 'raw potential' and initializes unique entities or events."
 },
                    { layer: 2, pane: "Information/Truth", color: 'bg-blue-200', role: "Sustained being", influence: "L2: Maintains continuity and identity; subject to feedback from higher layers."
 },
                    { layer: 3, pane: "Design", color: 'bg-teal-200', role: "Impact of existence", influence: "L3: How instances affect the environment; creates observable outcomes."
 },
                    { layer: 4, pane: "Creation", color: 'bg-green-200', role: "Integration (spacetime)", influence: "L4: Mediates interactions among 1–3; the 'arena' of experience and evolution."
 },
                    { layer: 5, pane: "Refinement", color: 'bg-yellow-200', role: "Quantum of decisions", influence: "L5: Introduces choice, adaptation, and probabilistic collapse; modifies layers 1–4 dynamically."
 },
                    { layer: 6, pane: "Revelation", color: 'bg-orange-200', role: "Blueprint layer (soul)", influence: "L6: Maintains coherence, imposes laws and principles; acts like system governance."
 },
                    { layer: 7, pane: "Continuity", color: 'bg-red-200', role: "Divine (consciousness)", influence: "L7: Provides ultimate direction, purpose, and overarching alignment; informs all layers below."
 }
                ];
 // Constants for positioning (adjusted for 300x300 view box)
                const CENTER_X = 150;
 const CENTER_Y = 150;
                const RADIUS = 130; /* Adjusted radius for 300px size */
                
                let activePoint = null;
 const detailPopup = document.getElementById('detail-popup');

                function calculateHeptagonPoint(index, totalPoints, radius, centerX, centerY) {
                    const angleDeg = (360 / totalPoints) * index - 90;
                    const angleRad = angleDeg * (Math.PI / 180);
                    const x = centerX + radius * Math.cos(angleRad);
                    const y = centerY + radius * Math.sin(angleRad);
                    return { x, y };
 }

                // NEW: Update popup functionality
                function updateDetails(data, pointElement) {
                    detailPopup.innerHTML = `
                        <h4>Layer ${data.layer}: ${data.pane}</h4>
             
            <p>${data.influence}</p>
                    `;
 detailPopup.style.display = 'block';
                    
                    if (activePoint && activePoint !== pointElement) {
                        activePoint.classList.remove('active');
 }
                    activePoint = pointElement;
 activePoint.classList.add('active');
                }

                // NEW: Clear popup functionality
                function clearDetails(pointElement) {
                    if (activePoint === pointElement) {
                         activePoint.classList.remove('active');
 activePoint = null;
                         detailPopup.style.display = 'none';
                    }
                }
                
                function createHeptagon() {
                    const container = document.getElementById('heptagon');
 // Clear existing points and SVG lines, but keep the center dot and popup
                    const elementsToRemove = Array.from(container.children).filter(el => el.id !== 'detail-popup' && !el.classList.contains('center-dot'));
 elementsToRemove.forEach(el => el.remove());

                    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                    svg.setAttribute('width', '100%');
                    svg.setAttribute('height', '100%');
                    svg.style.position = 'absolute';
                    svg.style.top = '0';
 svg.style.left = '0';
                    svg.style.zIndex = '1';
                    
                    let pointsString = "";
                    let pointsCoordinates = [];
 modelData.forEach((data, index) => {
                        const { x, y } = calculateHeptagonPoint(index, 7, RADIUS, CENTER_X, CENTER_Y);
                        pointsCoordinates.push({ x, y, data });
                        pointsString += `${x},${y} `;
        
              });

                    const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
                    polyline.setAttribute('points', pointsString.trim());
 polyline.setAttribute('stroke', '#4b5563'); 
                    polyline.setAttribute('stroke-width', '2');
                    polyline.setAttribute('fill', 'none');
                    svg.appendChild(polyline);

                    container.appendChild(svg);

                    pointsCoordinates.forEach(({ x, y, data }) => {
                        const point = document.createElement('div');
                        point.className = `point ${data.color} text-gray-800`;
                        
       
                         // Adjust position to center the div on the calculated point (70x70 div = 35px offset)
                        point.style.left = `${x - 35}px`; 
                        point.style.top = `${y - 35}px`;
           
              point.style.zIndex = '10';

                        point.innerHTML = `
                            <div class="layer-number">${data.layer}</div>
                            <div class="pane-name">${data.pane}</div>
 
                        `;

                        // Add event listeners for interactivity
                        point.addEventListener('mouseenter', () => updateDetails(data, point));
                    
      point.addEventListener('mouseleave', () => clearDetails(point));

                        container.appendChild(point);
 });
                    
                    clearDetails(null); // Ensure popup starts hidden
                }

                window.addEventListener('resize', createHeptagon);
 window.onload = createHeptagon;
            </script>
        </body>
        </html>
        """