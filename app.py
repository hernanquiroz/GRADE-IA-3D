import os
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from google import genai

# ============================================================
# GRADE IA 3D v4.1
# Plataforma educativa inmersiva multimotor
# ============================================================

APP_VERSION = "4.1"

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
AVISO_FILE = ASSETS_DIR / "aviso_grade_original.jpg"

st.set_page_config(
    page_title="GRADE IA 3D",
    page_icon="🦅",
    layout="wide"
)

# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

.stApp {
    background: radial-gradient(circle at 50% 0%, #263b70 0%, #10192e 45%, #070c17 100%);
    color: #f5f7ff;
}
html, body, [class*="css"] {
    font-family: Montserrat, sans-serif;
}
h1, h2, h3, p, label {
    color: #f4f6ff !important;
}
.hero {
    text-align:center;
    padding:20px 8px 10px 8px;
}
.hero-title {
    font-size: clamp(42px, 6vw, 86px);
    font-weight: 800;
    letter-spacing: 12px;
    background: linear-gradient(90deg,#fff,#83e6ff,#c4c8ff,#fff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.hero-subtitle {
    letter-spacing: 4px;
    color: #c2d8ff;
    font-size: 13px;
}
.panel {
    background: rgba(16,35,64,.82);
    border: 1px solid rgba(127,196,255,.22);
    padding: 20px;
    border-radius: 16px;
}
div[data-testid="stChatMessage"] {
    background: rgba(24,40,70,.65);
    border: 1px solid rgba(130,175,255,.18);
    border-radius: 14px;
}
.stButton button {
    border-radius: 10px;
    border: 1px solid #648dff;
}
div[data-testid="stChatInput"] {
    border-radius: 12px;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# ENCABEZADO
# ============================================================

st.markdown("""
<div class="hero">
<div class="hero-title">GRADE</div>
<div class="hero-subtitle">
INVESTIGACIÓN · EDUCACIÓN · CIENCIA · INTELIGENCIA ARTIFICIAL
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="panel">
<b>GRADE IA 3D — Experiencia inmersiva 4.1</b><br>
Un espacio de exploración del conocimiento, la investigación educativa,
la ciencia, la creatividad y la inteligencia artificial.
</div>
""", unsafe_allow_html=True)

# ============================================================
# ESCENA 3D
# ============================================================

scene_html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
html,body {
 margin:0;
 width:100%;
 height:100%;
 overflow:hidden;
 background:#050b17;
}
#stage {
 width:100%;
 height:600px;
 position:relative;
 overflow:hidden;
}
#hud {
 position:absolute;
 left:0;
 right:0;
 bottom:15px;
 color:#c2eaff;
 text-align:center;
 font:12px Arial;
 letter-spacing:3px;
 pointer-events:none;
}
#sequence {
 position:absolute;
 top:15px;
 right:15px;
 padding:10px 14px;
 background:#243d77;
 color:#fff;
 border:1px solid #90c8ff;
 border-radius:9px;
 cursor:pointer;
 z-index:5;
}
</style>
</head>
<body>
<div id="stage">
<button id="sequence">Iniciar recorrido cinematográfico</button>
<div id="hud">GRADE · UNIVERSO DE CONOCIMIENTO</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
const root = document.getElementById("stage");
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x050b17);
scene.fog = new THREE.Fog(0x050b17, 12, 35);

const camera = new THREE.PerspectiveCamera(
  50, root.clientWidth/root.clientHeight, 0.1, 100
);
camera.position.set(0, 2.3, 11);

const renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setSize(root.clientWidth,root.clientHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
root.appendChild(renderer.domElement);

scene.add(new THREE.AmbientLight(0x99baff,2.2));

const light1 = new THREE.PointLight(0x42d9ff,80,30);
light1.position.set(0,4,4);
scene.add(light1);

const light2 = new THREE.PointLight(0xffb95c,55,25);
light2.position.set(-5,3,0);
scene.add(light2);

const floor = new THREE.Mesh(
 new THREE.CircleGeometry(13,80),
 new THREE.MeshStandardMaterial({color:0x101d39,roughness:.85})
);
floor.rotation.x=-Math.PI/2;
floor.position.y=-2;
scene.add(floor);

// ------------------------------------------------------------
// GRADE 3D
// ------------------------------------------------------------

const grade = new THREE.Group();

const letterMaterial = new THREE.MeshStandardMaterial({
 color:0x77dfff,
 metalness:.7,
 roughness:.2,
 emissive:0x103a67,
 emissiveIntensity:.8
});

const letters = "GRADE";

letters.split("").forEach((letter,index)=>{
 const mesh = new THREE.Mesh(
  new THREE.BoxGeometry(.9,1.3,.28),
  letterMaterial
 );
 mesh.position.x=(index-2)*1.05;
 grade.add(mesh);
});

grade.position.set(0,-.2,0);
scene.add(grade);

// ------------------------------------------------------------
// CEREBRO HOLOGRAFICO
// ------------------------------------------------------------

const brain = new THREE.Group();

const brainMaterial = new THREE.MeshStandardMaterial({
 color:0x25bfff,
 wireframe:true,
 transparent:true,
 opacity:.7,
 emissive:0x0077ff,
 emissiveIntensity:1
});

const hemisphere1 = new THREE.Mesh(
 new THREE.SphereGeometry(.8,24,18),
 brainMaterial
);
hemisphere1.scale.set(.9,1.1,1);
hemisphere1.position.x=-.38;

const hemisphere2 = hemisphere1.clone();
hemisphere2.position.x=.38;

brain.add(hemisphere1,hemisphere2);

const nodeMaterial = new THREE.MeshBasicMaterial({color:0xa8f3ff});

for(let i=0;i<55;i++){
 const node = new THREE.Mesh(
  new THREE.SphereGeometry(.035,8,8),
  nodeMaterial
 );
 const phi=Math.acos(2*Math.random()-1);
 const theta=2*Math.PI*Math.random();
 node.position.set(
  Math.sin(phi)*Math.cos(theta),
  Math.cos(phi),
  Math.sin(phi)*Math.sin(theta)
 );
 brain.add(node);
}

brain.position.set(0,2.5,-.5);
scene.add(brain);

// ------------------------------------------------------------
// CONDOR ESTILIZADO
// ------------------------------------------------------------

const condor = new THREE.Group();

const bodyMat = new THREE.MeshStandardMaterial({
 color:0x172335,
 metalness:.3,
 roughness:.6
});

const body = new THREE.Mesh(
 new THREE.SphereGeometry(.5,18,14),
 bodyMat
);
body.scale.set(.7,1.2,.65);
condor.add(body);

const neck = new THREE.Mesh(
 new THREE.CylinderGeometry(.13,.25,.65,12),
 bodyMat
);
neck.position.y=.62;
condor.add(neck);

const head = new THREE.Mesh(
 new THREE.SphereGeometry(.23,16,12),
 new THREE.MeshStandardMaterial({color:0x9f3547})
);
head.position.y=1.05;
condor.add(head);

const beak = new THREE.Mesh(
 new THREE.ConeGeometry(.11,.28,8),
 new THREE.MeshStandardMaterial({color:0xffc76a})
);
beak.rotation.x=Math.PI/2;
beak.position.set(0,.98,.26);
condor.add(beak);

// Alas
const wings=[];

[-1,1].forEach(side=>{
 const pivot=new THREE.Group();
 pivot.position.set(side*.25,.3,0);
 condor.add(pivot);

 const wing = new THREE.Mesh(
  new THREE.BoxGeometry(2.2,.12,.45),
  bodyMat
 );
 wing.position.x=side*1.1;
 pivot.add(wing);

 // Plumas estilizadas
 for(let i=0;i<8;i++){
  const feather = new THREE.Mesh(
   new THREE.BoxGeometry(.42,.07,.14),
   new THREE.MeshStandardMaterial({color:0x243950})
  );
  feather.position.set(side*(.4+i*.22),-.12,-.12);
  pivot.add(feather);
 }

 wings.push({pivot,side});
});

condor.position.set(-4,1,0);
condor.scale.set(.85,.85,.85);
scene.add(condor);

// Libro
const book = new THREE.Group();

const cover = new THREE.Mesh(
 new THREE.BoxGeometry(.9,.1,.65),
 new THREE.MeshStandardMaterial({color:0x9b6d3b})
);
book.add(cover);

const pages = new THREE.Mesh(
 new THREE.BoxGeometry(.8,.08,.55),
 new THREE.MeshStandardMaterial({color:0xf0e5c8})
);
pages.position.y=.08;
book.add(pages);

book.position.set(-4,-.3,.2);
scene.add(book);

// ------------------------------------------------------------
// ECOSISTEMA
// ------------------------------------------------------------

const ecosystem = new THREE.Group();

for(let i=0;i<8;i++){
 const angle=i*Math.PI/4;
 const orb = new THREE.Mesh(
  new THREE.SphereGeometry(.16,12,10),
  new THREE.MeshStandardMaterial({
   color:[0x5de5ff,0xffd56d,0xb49aff,0x6affc6][i%4],
   emissive:0x16446a
  })
 );
 orb.position.set(
  Math.cos(angle)*2.4,
  Math.sin(angle)*1.2,
  Math.sin(angle)*1.8
 );
 ecosystem.add(orb);
}

ecosystem.position.set(0,-1.2,-1);
scene.add(ecosystem);

// ------------------------------------------------------------
// ANILLOS
// ------------------------------------------------------------

const rings=[];

for(let i=0;i<5;i++){
 const ring = new THREE.Mesh(
  new THREE.TorusGeometry(2.8+i*.35,.018,8,100),
  new THREE.MeshBasicMaterial({
   color:i%2?0x4c8aff:0x67eaff
  })
 );
 ring.rotation.x=Math.PI/2.4;
 ring.position.y=-1.4+i*.1;
 scene.add(ring);
 rings.push(ring);
}

// ------------------------------------------------------------
// PARTICULAS
// ------------------------------------------------------------

const count=850;
const particlePositions=new Float32Array(count*3);

for(let i=0;i<count;i++){
 particlePositions[i*3]=(Math.random()-.5)*24;
 particlePositions[i*3+1]=(Math.random()-.5)*12;
 particlePositions[i*3+2]=(Math.random()-.5)*20;
}

const particleGeometry=new THREE.BufferGeometry();
particleGeometry.setAttribute(
 "position",new THREE.BufferAttribute(particlePositions,3)
);

const particleSystem=new THREE.Points(
 particleGeometry,
 new THREE.PointsMaterial({color:0x62caff,size:.028})
);
scene.add(particleSystem);

// ------------------------------------------------------------
// SECUENCIA
// ------------------------------------------------------------

let cinematic=false;
let cinematicStart=0;
let clock=new THREE.Clock();

document.getElementById("sequence").onclick=()=>{
 cinematic=true;
 cinematicStart=performance.now();
};

function animate(){
 requestAnimationFrame(animate);

 const t=clock.getElapsedTime();

 grade.rotation.y=Math.sin(t*.4)*.12;
 brain.rotation.y=t*.3;
 brain.position.y=2.5+Math.sin(t)*.15;

 condor.position.y=1+Math.sin(t*1.5)*.15;
 condor.rotation.y=Math.sin(t*.6)*.2;

 wings.forEach(w=>{
  w.pivot.rotation.z=w.side*Math.sin(t*3)*.28;
 });

 ecosystem.rotation.y=t*.15;

 rings.forEach((r,i)=>{
  r.rotation.z=t*(.1+i*.03);
 });

 particleSystem.rotation.y=t*.015;

 if(cinematic){
  const elapsed=(performance.now()-cinematicStart)/1000;
  const progress=Math.min(elapsed/90,1);

  camera.position.x=Math.sin(progress*Math.PI*2)*1.4;
  camera.position.z=11-progress*2;
  camera.position.y=2.3+Math.sin(progress*Math.PI)*1.4;
  camera.lookAt(0,.2,0);

  if(progress>=1) cinematic=false;
 }else{
  camera.lookAt(0,.2,0);
 }

 renderer.render(scene,camera);
}

animate();

window.addEventListener("resize",()=>{
 camera.aspect=root.clientWidth/root.clientHeight;
 camera.updateProjectionMatrix();
 renderer.setSize(root.clientWidth,root.clientHeight);
});
</script>
</body>
</html>
"""

components.html(scene_html, height=620, scrolling=False)

# ============================================================
# MÚSICA
# ============================================================

st.markdown("## 🎵 Ambiente sonoro")

music_html = r"""
<div style="background:#172849;padding:15px;border-radius:12px;color:white">
<button id="musicToggle" style="padding:10px 15px;background:#254e87;color:white;border-radius:9px;border:1px solid #85caff">
▶ Activar / Pausar ambiente
</button>
<span style="padding-left:10px">Ambiente electrónico espacial</span>
</div>
<script>
let audioContext;
let oscillators=[];
let master;
let active=false;

document.getElementById("musicToggle").onclick=()=>{
 if(!audioContext){
  audioContext=new (window.AudioContext||window.webkitAudioContext)();
  master=audioContext.createGain();
  master.gain.value=.035;
  master.connect(audioContext.destination);
 }
 audioContext.resume();

 if(!active){
  const frequencies=[110,164.81,220];
  frequencies.forEach((frequency,index)=>{
   const osc=audioContext.createOscillator();
   const gain=audioContext.createGain();
   osc.type=index===1?"triangle":"sine";
   osc.frequency.value=frequency;
   gain.gain.value=index===0?.5:.22;
   osc.connect(gain);
   gain.connect(master);
   osc.start();
   oscillators.push({osc,gain});
  });
  active=true;
  document.getElementById("musicToggle").innerText="Ⅱ Pausar ambiente";
 }else{
  oscillators.forEach(o=>{
   try{o.osc.stop()}catch(e){}
  });
  oscillators=[];
  active=false;
  document.getElementById("musicToggle").innerText="▶ Activar ambiente";
 }
};
</script>
"""

components.html(music_html, height=75)

# ============================================================
# AVISO INSTITUCIONAL ORIGINAL
# ============================================================

st.markdown("---")

with st.expander("📄 Aviso institucional original"):
    if AVISO_FILE.exists():
        st.image(str(AVISO_FILE), use_container_width=True)
        st.caption("Archivo original. No se realizan modificaciones.")
    else:
        st.warning(
            "No se encuentra el aviso original. Coloca la imagen en "
            "assets/aviso_grade_original.jpg"
        )

# ============================================================
# ASISTENTE MULTIMOTOR
# ============================================================

st.markdown("---")
st.markdown("# 🧠 Asistente académico GRADE IA")

st.write(
    "Consulta sobre investigación, educación, ciencia, "
    "inteligencia artificial y transformación pedagógica."
)

# ------------------------------------------------------------
# CONFIGURACIÓN DE PROVEEDOR
# ------------------------------------------------------------

with st.sidebar:
    st.markdown("# ⚙️ Configuración IA")
    provider = st.radio(
        "Motor de inteligencia artificial",
        ["Groq", "Gemini"]
    )

    st.markdown("---")

    if provider == "Groq":
        st.caption("Motor de inferencia Groq")
    else:
        st.caption("Motor Google Gemini")

    if st.button("🗑️ Reiniciar conversación"):
        st.session_state.grade_history = []
        st.rerun()

# ------------------------------------------------------------
# HISTORIAL
# ------------------------------------------------------------

if "grade_history" not in st.session_state:
    st.session_state.grade_history = []

for message in st.session_state.grade_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------------------------------------------------
# PROMPT ACADÉMICO
# ------------------------------------------------------------

SYSTEM_PROMPT = """
Eres GRADE IA, un asistente académico para investigación y educación.

Áreas de conocimiento:
- Educación
- Investigación educativa
- Inteligencia artificial
- Ciencias naturales
- Física
- Pensamiento crítico
- Innovación pedagógica
- Ética y gobernanza de IA
- Tecnología educativa

INSTRUCCIONES:

Responde en español.

Mantén rigor científico y académico.

Explica los conceptos de manera clara y estructurada.

Cuando corresponda:
- Define conceptos.
- Explica mecanismos.
- Propón metodologías.
- Diseña actividades.
- Presenta ejemplos.
- Sugiere evaluación.
- Identifica limitaciones.

No inventes autores, DOI, citas, artículos ni estadísticas.

Diferencia claramente:
- Hechos comprobados.
- Interpretaciones.
- Hipótesis.
- Recomendaciones.

Promueve pensamiento crítico.

Protege la privacidad.

No tomes decisiones automáticas definitivas sobre personas.

No afirmes representar oficialmente a GRADE o a la Universidad de Antioquia.
"""

# ------------------------------------------------------------
# ENTRADA
# ------------------------------------------------------------

prompt = st.chat_input("Escribe tu pregunta académica...")

# ------------------------------------------------------------
# API KEYS
# ------------------------------------------------------------

def read_secret(secret_name):
    try:
        value = st.secrets.get(secret_name, "")
        if value:
            return value
    except Exception:
        pass

    return os.getenv(secret_name, "")

# ------------------------------------------------------------
# PROCESAR CONSULTA
# ------------------------------------------------------------

if prompt:

    st.session_state.grade_history.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        recent_history = st.session_state.grade_history[-12:]

        # ----------------------------------------------------
        # GROQ
        # ----------------------------------------------------

        if provider == "Groq":

            api_key = read_secret("GROQ_API_KEY")

            if not api_key:
                st.error("No está configurada GROQ_API_KEY.")
                st.stop()

            groq_model = read_secret("GROQ_MODEL") or \
                "llama-3.3-70b-versatile"

            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1",
                timeout=90
            )

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + recent_history

            with st.chat_message("assistant"):

                with st.spinner("Groq está procesando..."):

                    response = client.chat.completions.create(
                        model=groq_model,
                        messages=messages,
                        temperature=0.4,
                        max_tokens=2000
                    )

                    answer = response.choices[0].message.content or \
                        "El modelo no devolvió texto."

                    st.markdown(answer)

        # ----------------------------------------------------
        # GEMINI
        # ----------------------------------------------------

        else:

            api_key = read_secret("GEMINI_API_KEY")

            if not api_key:
                st.error("No está configurada GEMINI_API_KEY.")
                st.stop()

            gemini_model = read_secret("GEMINI_MODEL") or \
                "gemini-2.5-flash"

            client = genai.Client(api_key=api_key)

            conversation = SYSTEM_PROMPT + "\n\n"

            for message in recent_history:

                role = (
                    "Usuario"
                    if message["role"] == "user"
                    else "Asistente"
                )

                conversation += (
                    role + ": " + message["content"] + "\n\n"
                )

            with st.chat_message("assistant"):

                with st.spinner("Gemini está procesando..."):

                    response = client.models.generate_content(
                        model=gemini_model,
                        contents=conversation
                    )

                    answer = response.text or \
                        "El modelo no devolvió texto."

                    st.markdown(answer)

        # ----------------------------------------------------
        # GUARDAR RESPUESTA
        # ----------------------------------------------------

        st.session_state.grade_history.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as error:

        st.error("No se pudo completar la consulta.")

        st.code(str(error)[:1000])

# ============================================================
# INFORMACIÓN
# ============================================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#a9c7e9;padding:15px">
GRADE IA 3D · Versión 4.1<br>
Investigación · Educación · Ciencia · Inteligencia Artificial
</div>
""", unsafe_allow_html=True)
