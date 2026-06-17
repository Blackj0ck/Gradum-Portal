from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Gradum OS</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
    --bg:#07090c;
    --panel:#0d1117;
    --panel2:#111821;
    --line:#232832;
    --text:#f4efe3;
    --muted:#9b9b93;
    --gold:#c8ad6a;
    --gold2:#e0c987;
    --green:#85d49a;
}

*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,Arial,sans-serif}

body{
    background:
        radial-gradient(circle at top right,rgba(200,173,106,.10),transparent 30%),
        radial-gradient(circle at bottom left,rgba(70,90,120,.12),transparent 28%),
        var(--bg);
    color:var(--text);
    display:flex;
}

.sidebar{
    width:292px;
    height:100vh;
    background:rgba(7,9,12,.92);
    border-right:1px solid var(--line);
    padding:34px 24px;
    position:fixed;
    backdrop-filter:blur(18px);
}

.logo{font-size:31px;letter-spacing:3px;font-weight:700}

.subtitle{
    color:var(--gold);
    font-size:11px;
    letter-spacing:2px;
    text-transform:uppercase;
    margin:9px 0 42px;
}

.menu-label{
    color:#676b72;
    font-size:11px;
    letter-spacing:1.5px;
    text-transform:uppercase;
    margin-bottom:14px;
}

.menu button{
    display:block;
    width:100%;
    padding:14px 15px;
    margin-bottom:9px;
    background:transparent;
    color:#b8b8b2;
    border:1px solid transparent;
    border-radius:10px;
    text-align:left;
    cursor:pointer;
    transition:.25s;
    font-size:14px;
}

.menu button:hover,
.menu button.active{
    color:var(--text);
    border-color:rgba(200,173,106,.45);
    background:linear-gradient(135deg,rgba(200,173,106,.10),rgba(255,255,255,.025));
}

.hamburger-btn{
    margin-top:16px;
    border-color:rgba(200,173,106,.25)!important;
}

.division-menu{
    display:none;
    margin-top:8px;
    padding-left:10px;
    border-left:1px solid rgba(200,173,106,.25);
}

.division-menu.open{display:block}
.division-menu button{font-size:13px;color:#9b9b93}

.main{
    margin-left:292px;
    width:calc(100% - 292px);
    padding:38px;
}

.topbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:30px;
}

.eyebrow{
    color:var(--gold);
    text-transform:uppercase;
    letter-spacing:2.4px;
    font-size:11px;
    margin-bottom:10px;
}

h1{font-size:42px;font-weight:500;letter-spacing:-1px}

.user{
    border:1px solid var(--line);
    padding:12px 18px;
    border-radius:999px;
    color:#d7d0bf;
    background:rgba(255,255,255,.03);
}

.hero{
    background:
        linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.012)),
        linear-gradient(120deg,#111821,#07090c);
    border:1px solid var(--line);
    border-radius:28px;
    padding:44px;
    margin-bottom:28px;
    position:relative;
    overflow:hidden;
}

.hero:after{
    content:"";
    position:absolute;
    width:240px;
    height:240px;
    border-radius:50%;
    background:rgba(200,173,106,.06);
    right:-90px;
    top:-90px;
    filter:blur(8px);
}

.hero h2{
    font-size:44px;
    font-weight:500;
    letter-spacing:-1px;
    line-height:1.12;
    margin-bottom:16px;
    max-width:850px;
}

.hero p{
    color:#aaa79f;
    line-height:1.8;
    max-width:700px;
    font-size:15px;
}

.section{display:none}
.section.active{display:block}

.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:22px}
.grid2{display:grid;grid-template-columns:2fr 1fr;gap:22px}

.card,.panel,.widget{
    background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.012));
    border:1px solid var(--line);
    border-radius:24px;
    padding:26px;
    box-shadow:0 20px 80px rgba(0,0,0,.16);
}

.card{
    cursor:pointer;
    transition:.25s;
    min-height:280px;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.card:hover{
    transform:translateY(-6px);
    border-color:rgba(200,173,106,.48);
    background:linear-gradient(180deg,rgba(200,173,106,.07),rgba(255,255,255,.015));
}

.card h3,.widget h3,.panel h2{font-weight:500;margin-bottom:10px}

.card h3{
    font-size:30px;
    margin-bottom:18px;
    font-weight:500;
}

.card p,.widget p,.panel p,small{
    color:var(--muted);
    line-height:1.65;
}

.widget strong{
    font-size:34px;
    color:var(--gold2);
    font-weight:500;
}

.item{
    background:rgba(7,9,12,.55);
    border:1px solid var(--line);
    border-left:3px solid var(--gold);
    padding:17px;
    border-radius:16px;
    margin-bottom:12px;
    transition:.25s;
}

.item:hover{border-color:rgba(200,173,106,.45)}
.item h3{font-size:17px;margin-bottom:6px;font-weight:500}

.status{
    display:inline-block;
    margin-top:18px;
    padding:6px 12px;
    border-radius:999px;
    font-size:11px;
    letter-spacing:.7px;
    text-transform:uppercase;
}

.progress{background:rgba(200,173,106,.12);color:var(--gold2)}
.review{background:rgba(255,255,255,.08);color:#e5ded0}
.done{background:rgba(133,212,154,.12);color:var(--green)}

.tabs{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin:22px 0;
}

.tabs button{
    padding:11px 14px;
    border:1px solid var(--line);
    background:rgba(255,255,255,.025);
    color:#d6d1c4;
    border-radius:999px;
    cursor:pointer;
    transition:.25s;
}

.tabs button:hover,
.tabs button.active{
    border-color:rgba(200,173,106,.7);
    background:rgba(200,173,106,.12);
    color:var(--text);
}

.module{display:none}
.module.active{display:block}

.bar{
    height:8px;
    background:#202833;
    border-radius:999px;
    margin-top:14px;
    overflow:hidden;
}

.fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--gold2))}

.btn{
    padding:12px 16px;
    border:1px solid var(--gold);
    background:transparent;
    color:var(--text);
    border-radius:10px;
    cursor:pointer;
    margin-top:14px;
    transition:.25s;
}

.btn:hover{background:var(--gold);color:#07090c}

.visual-timeline{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:0;
    margin-top:20px;
}

.timeline-step{
    position:relative;
    background:rgba(255,255,255,.025);
    border:1px solid var(--line);
    padding:24px 18px;
    min-height:200px;
}

.timeline-step:first-child{border-radius:20px 0 0 20px}
.timeline-step:last-child{border-radius:0 20px 20px 0}

.circle{
    width:42px;
    height:42px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:18px;
    font-weight:bold;
    border:1px solid var(--gold);
    position:relative;
    z-index:2;
}

.line{
    position:absolute;
    top:44px;
    left:58px;
    right:-22px;
    height:2px;
    background:#343b47;
    z-index:1;
}

.timeline-step h3{font-size:17px;margin-bottom:8px;font-weight:500}
.timeline-step small{display:block;margin-bottom:12px}
.timeline-step span{color:var(--gold);font-size:13px}

.completed .circle,
.active-step .circle{
    background:var(--gold);
    color:#07090c;
}

.active-step{
    border-color:rgba(200,173,106,.7);
    background:rgba(200,173,106,.08);
}

.active-step .circle{box-shadow:0 0 0 7px rgba(200,173,106,.13)}
.pending .circle{color:var(--gold)}

.timeline-summary{
    margin-top:22px;
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
}

/* GANTT */
.gantt-wrapper{
    margin-top:18px;
    overflow-x:auto;
    border:1px solid var(--line);
    border-radius:20px;
    background:rgba(255,255,255,.018);
}

.gantt{
    min-width:900px;
    padding:20px;
}

.gantt-header,
.gantt-row{
    display:grid;
    grid-template-columns:220px repeat(8,1fr);
    gap:10px;
    align-items:center;
}

.gantt-header{
    color:var(--gold);
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1.2px;
    margin-bottom:16px;
    padding-bottom:12px;
    border-bottom:1px solid var(--line);
}

.gantt-row{
    min-height:54px;
    border-bottom:1px solid rgba(255,255,255,.04);
}

.gantt-row:last-child{border-bottom:none}

.gantt-project{
    color:var(--text);
    font-size:14px;
}

.gantt-cell{
    height:18px;
    background:rgba(255,255,255,.035);
    border-radius:999px;
    position:relative;
}

.gantt-bar{
    height:18px;
    border-radius:999px;
    background:linear-gradient(90deg,var(--gold),var(--gold2));
    box-shadow:0 0 18px rgba(200,173,106,.16);
}

.gantt-bar.review{
    background:linear-gradient(90deg,#8f8f8a,#d7d0bf);
}

.gantt-bar.donebar{
    background:linear-gradient(90deg,#6eaf7d,#9be0aa);
}

.gantt-legend{
    display:flex;
    gap:12px;
    flex-wrap:wrap;
    margin-top:18px;
}

.legend-item{
    color:var(--muted);
    font-size:12px;
    display:flex;
    align-items:center;
    gap:8px;
}

.legend-dot{
    width:12px;
    height:12px;
    border-radius:50%;
    background:var(--gold);
}

.legend-dot.review-dot{background:#d7d0bf}
.legend-dot.done-dot{background:#9be0aa}

@media(max-width:1000px){
    body{display:block}
    .sidebar{width:100%;height:auto;position:relative}
    .main{margin-left:0;width:100%;padding:22px}
    .grid4,.grid3,.timeline-summary{grid-template-columns:1fr}
    .grid2{grid-template-columns:1fr}
    .visual-timeline{grid-template-columns:1fr;gap:14px}
    .timeline-step{border-radius:20px!important}
    .line{display:none}
}
</style>
</head>

<body>

<div class="sidebar">
    <div class="logo">GRADUM</div>
    <div class="subtitle">Operating Intelligence</div>

    <div class="menu">
        <div class="menu-label">Command Center</div>

        <button class="active" onclick="showSection('home', this)">
            Home
        </button>

        <button class="hamburger-btn" onclick="toggleDivisions()">
            ☰ Divisions
        </button>

        <div id="divisionMenu" class="division-menu">
            <button onclick="showSection('services', this)">Services</button>
            <button onclick="showSection('construction', this)">Construction</button>
            <button onclick="showSection('consulting', this)">Consulting</button>
            <button onclick="showSection('ventures', this)">Ventures</button>
        </div>
    </div>
</div>

<div class="main">

<div class="topbar">
    <div>
        <div class="eyebrow">Strategic Advisory · Execution · Infrastructure</div>
        <h1>Gradum OS</h1>
    </div>
    <div class="user">Elvin González</div>
</div>

<div id="home" class="section active">
    <div class="hero">
        <div class="eyebrow">Operating Intelligence</div>
        <h2>
            Projects, Advisory<br>
            & Execution
        </h2>
        <p>
            A unified environment for planning, delivery,
            collaboration and client visibility across the
            Gradum ecosystem.
        </p>
    </div>

    <div class="grid4">
        <div class="card" onclick="goTo('services')">
            <div>
                <div class="eyebrow">Professional Services</div>
                <h3>Services</h3>
                <p>Professional Services</p>
            </div>
        </div>

        <div class="card" onclick="goTo('construction')">
            <div>
                <div class="eyebrow">Built Environment</div>
                <h3>Construction</h3>
                <p>Built Environment</p>
            </div>
        </div>

        <div class="card" onclick="goTo('consulting')">
            <div>
                <div class="eyebrow">Strategic Advisory</div>
                <h3>Consulting</h3>
                <p>Strategic Advisory</p>
            </div>
        </div>

        <div class="card" onclick="goTo('ventures')">
            <div>
                <div class="eyebrow">Venture Studio</div>
                <h3>Ventures</h3>
                <p>Venture Building</p>
            </div>
        </div>
    </div>
</div>

<div id="services" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Services</div>
        <h2>Professional services organized by client, scope and delivery.</h2>
        <p>Contabilidad, diseño gráfico y web design con entregables, reportes, hitos y aprobación del cliente.</p>
    </div>

    <div class="grid3">
        <div class="card" onclick="openProject('services','Contabilidad para Cliente Corporativo')">
            <div><div class="eyebrow">Finance Operations</div><h3>Contabilidad</h3><p>Reportes financieros, impuestos, conciliaciones y documentos contables.</p></div>
            <span class="status progress">Open Workspace</span>
        </div>

        <div class="card" onclick="openProject('services','Identidad Visual Marca Premium')">
            <div><div class="eyebrow">Brand Systems</div><h3>Diseño Gráfico</h3><p>Branding, piezas visuales, campañas, contenido y aprobaciones.</p></div>
            <span class="status progress">Open Workspace</span>
        </div>

        <div class="card" onclick="openProject('services','Web Design Portal Comercial')">
            <div><div class="eyebrow">Digital Experience</div><h3>Web Design</h3><p>Sitios web, landing pages, UI, contenido y publicación.</p></div>
            <span class="status progress">Open Workspace</span>
        </div>
    </div>

    <div id="servicesProject"></div>
</div>

<div id="construction" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Construction</div>
        <h2>Built environment delivery with executive visibility.</h2>
        <p>Arquitectura e ingeniería funcionan como componentes del flujo constructivo: diseño, planos, presupuesto, ejecución, supervisión y entrega.</p>
    </div>

    <div class="grid3">
        <div class="widget"><h3>Obras activas</h3><strong>12</strong><p>Proyectos en ejecución o planificación.</p></div>
        <div class="widget"><h3>Avance promedio</h3><strong>62%</strong><p>Avance físico general.</p></div>
        <div class="widget"><h3>Reportes emitidos</h3><strong>8</strong><p>Informes semanales y visitas.</p></div>
    </div>

    <div class="grid2">
        <div class="panel">
            <h2>Construction Portfolio</h2>

            <div class="item" onclick="openProject('construction','Remodelación Local Comercial')">
                <h3>Remodelación Local Comercial</h3>
                <small>Cliente corporativo · Avance 62%</small>
                <div class="bar"><div class="fill" style="width:62%"></div></div>
                <span class="status progress">Open Project</span>
            </div>

            <div class="item" onclick="openProject('construction','Obra Residencial Moderna')">
                <h3>Obra Residencial Moderna</h3>
                <small>Diseño, presupuesto y planificación inicial.</small>
                <div class="bar"><div class="fill" style="width:35%"></div></div>
                <span class="status review">Open Project</span>
            </div>
        </div>

        <div id="constructionProject"></div>
    </div>
</div>

<div id="consulting" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Consulting</div>
        <h2>Advisory, strategy and operational transformation.</h2>
        <p>Proyectos de consultoría con diagnóstico, roadmap, entregables, reuniones, aprobaciones y seguimiento.</p>
    </div>

    <div class="grid3">
        <div class="widget"><h3>Clientes activos</h3><strong>5</strong><p>Procesos consultivos abiertos.</p></div>
        <div class="widget"><h3>Entregables</h3><strong>14</strong><p>Reportes y planes de acción.</p></div>
        <div class="widget"><h3>Sesiones</h3><strong>9</strong><p>Reuniones programadas.</p></div>
    </div>

    <div class="panel">
        <div class="item" onclick="openProject('consulting','Diagnóstico Operativo Empresarial')">
            <h3>Diagnóstico Operativo Empresarial</h3>
            <small>Mapa de procesos, hallazgos y recomendaciones.</small>
        </div>

        <div class="item" onclick="openProject('consulting','Plan Estratégico Comercial')">
            <h3>Plan Estratégico Comercial</h3>
            <small>Roadmap de crecimiento y posicionamiento.</small>
        </div>
    </div>

    <div id="consultingProject"></div>
</div>

<div id="ventures" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Ventures</div>
        <h2>Venture studio for startups, MVPs and new business engines.</h2>
        <p>Desde idea hasta validación: hipótesis, mercado, prototipo, métricas, inversión y escalabilidad.</p>
    </div>

    <div class="grid3">
        <div class="widget"><h3>Ideas activas</h3><strong>11</strong><p>Oportunidades en evaluación.</p></div>
        <div class="widget"><h3>MVPs</h3><strong>3</strong><p>Prototipos en desarrollo.</p></div>
        <div class="widget"><h3>Startups</h3><strong>2</strong><p>Proyectos con potencial de spin-off.</p></div>
    </div>

    <div class="panel">
        <div class="item" onclick="openProject('ventures','Gradum OS SaaS')">
            <h3>Gradum OS SaaS</h3>
            <small>Plataforma de gestión y portal del cliente.</small>
        </div>

        <div class="item" onclick="openProject('ventures','Motor de Recomendaciones Locales')">
            <h3>Motor de Recomendaciones Locales</h3>
            <small>Google Places, tendencias y recomendaciones.</small>
        </div>
    </div>

    <div id="venturesProject"></div>
</div>

</div>

<script>
function toggleDivisions(){
    document.getElementById("divisionMenu").classList.toggle("open");
}

function showSection(sectionId, button){
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
    document.getElementById(sectionId).classList.add("active");

    document.querySelectorAll(".menu button").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
}

function goTo(sectionId){
    document.getElementById("divisionMenu").classList.add("open");

    const buttons = document.querySelectorAll(".menu button");
    buttons.forEach(b => {
        if(b.textContent.toLowerCase().includes(sectionId)){
            b.click();
        }
    });
}

function openProject(division, projectName){
    const container = document.getElementById(division + "Project");
    container.innerHTML = projectWorkspace(projectName, division);
}

function projectWorkspace(name, division){
    const id = division + "Module";

    return `
    <div class="panel" style="margin-top:22px">
        <div class="eyebrow">Project Workspace</div>
        <h2>${name}</h2>
        <p>Espacio SaaS del proyecto con visibilidad ejecutiva, trazabilidad y experiencia de cliente.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('${id}-dashboard', this)">Dashboard Ejecutivo</button>
            <button onclick="showModule('${id}-timeline', this)">Cronograma por Fases</button>
            <button onclick="showModule('${id}-gantt', this)">Gantt de Proyectos</button>
            <button onclick="showModule('${id}-weekly', this)">Informes Semanales</button>
            <button onclick="showModule('${id}-visits', this)">Visitas / Reuniones</button>
            <button onclick="showModule('${id}-changes', this)">Registro de Cambios</button>
            <button onclick="showModule('${id}-docs', this)">Documentos</button>
            <button onclick="showModule('${id}-milestones', this)">Próximos Hitos</button>
        </div>

        <div id="${id}-dashboard" class="module active">
            <div class="grid3">
                <div class="widget">
                    <h3>Avance</h3>
                    <strong>62%</strong>
                    <p>Progreso general del proyecto.</p>
                </div>

                <div class="widget">
                    <h3>Estado</h3>
                    <strong>Activo</strong>
                    <p>Proyecto en ejecución.</p>
                </div>

                <div class="widget">
                    <h3>Próximo hito</h3>
                    <strong>28 Jun</strong>
                    <p>Entrega parcial programada.</p>
                </div>
            </div>

            <div class="item">
                <h3>Executive Summary</h3>
                <small>
                    El proyecto avanza conforme al plan. Existen documentos pendientes de aprobación,
                    un cambio en revisión y próximos hitos programados para cierre de fase.
                </small>
            </div>
        </div>

        <div id="${id}-timeline" class="module">
            <div class="visual-timeline">

                <div class="timeline-step completed">
                    <div class="circle">1</div>
                    <div class="line"></div>
                    <h3>Brief / Alcance</h3>
                    <small>Definición inicial, objetivos, responsables y entregables.</small>
                    <span>01 Jun - 03 Jun</span>
                </div>

                <div class="timeline-step completed">
                    <div class="circle">2</div>
                    <div class="line"></div>
                    <h3>Planificación</h3>
                    <small>Cronograma, presupuesto, recursos y estructura de trabajo.</small>
                    <span>04 Jun - 10 Jun</span>
                </div>

                <div class="timeline-step active-step">
                    <div class="circle">3</div>
                    <div class="line"></div>
                    <h3>Ejecución</h3>
                    <small>Desarrollo operativo, construcción, diseño o implementación.</small>
                    <span>11 Jun - 25 Jun</span>
                </div>

                <div class="timeline-step pending">
                    <div class="circle">4</div>
                    <div class="line"></div>
                    <h3>Revisión</h3>
                    <small>Validación interna, control de calidad y aprobación del cliente.</small>
                    <span>26 Jun - 28 Jun</span>
                </div>

                <div class="timeline-step pending">
                    <div class="circle">5</div>
                    <h3>Entrega Final</h3>
                    <small>Cierre, documentación final y entrega formal del proyecto.</small>
                    <span>29 Jun</span>
                </div>

            </div>

            <div class="timeline-summary">
                <div class="widget"><h3>Fase actual</h3><strong>3/5</strong><p>Ejecución en progreso.</p></div>
                <div class="widget"><h3>Días restantes</h3><strong>12</strong><p>Hasta entrega final.</p></div>
                <div class="widget"><h3>Riesgo</h3><strong>Bajo</strong><p>Sin retrasos críticos registrados.</p></div>
            </div>
        </div>

        <div id="${id}-gantt" class="module">
            <div class="item">
                <h3>Diagrama de Gantt</h3>
                <small>Vista temporal de proyectos y fases principales dentro del portafolio activo.</small>
            </div>

            <div class="gantt-wrapper">
                <div class="gantt">
                    <div class="gantt-header">
                        <div>Proyecto / Fase</div>
                        <div>Semana 1</div>
                        <div>Semana 2</div>
                        <div>Semana 3</div>
                        <div>Semana 4</div>
                        <div>Semana 5</div>
                        <div>Semana 6</div>
                        <div>Semana 7</div>
                        <div>Semana 8</div>
                    </div>

                    <div class="gantt-row">
                        <div class="gantt-project">Remodelación Local Comercial</div>
                        <div class="gantt-cell"><div class="gantt-bar donebar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar donebar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:85%"></div></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                    </div>

                    <div class="gantt-row">
                        <div class="gantt-project">Obra Residencial Moderna</div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"><div class="gantt-bar review" style="width:70%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:60%"></div></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                    </div>

                    <div class="gantt-row">
                        <div class="gantt-project">Documentación Técnica</div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"><div class="gantt-bar review" style="width:60%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar review" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar review" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar review" style="width:40%"></div></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                    </div>

                    <div class="gantt-row">
                        <div class="gantt-project">Entrega / Cierre</div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:50%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div>
                        <div class="gantt-cell"><div class="gantt-bar" style="width:80%"></div></div>
                        <div class="gantt-cell"></div>
                    </div>
                </div>
            </div>

            <div class="gantt-legend">
                <div class="legend-item"><span class="legend-dot done-dot"></span> Completado</div>
                <div class="legend-item"><span class="legend-dot"></span> En ejecución</div>
                <div class="legend-item"><span class="legend-dot review-dot"></span> Revisión / planificación</div>
            </div>
        </div>

        <div id="${id}-weekly" class="module">
            <div class="item">
                <h3>Informe Semanal #01</h3>
                <small>Avance, tareas realizadas, fotos, incidencias y próximos pasos.</small><br>
                <button class="btn">Ver informe</button>
            </div>

            <div class="item">
                <h3>Informe Semanal #02</h3>
                <small>Estado actualizado, puntos críticos, decisiones pendientes y evidencias.</small><br>
                <button class="btn">Ver informe</button>
            </div>
        </div>

        <div id="${id}-visits" class="module">
            <div class="item">
                <h3>Informe de visita / reunión</h3>
                <small>Fecha: 17 Junio 2026 · Observaciones, acuerdos, responsables y próximos pasos.</small>
            </div>

            <div class="item">
                <h3>Próxima visita</h3>
                <small>Programada para revisión de avances y validación de entregables.</small>
            </div>
        </div>

        <div id="${id}-changes" class="module">
            <div class="item">
                <h3>Cambio solicitado</h3>
                <small>Impacto: +4 días · Costo estimado: US$1,200 · Estado: pendiente aprobación.</small><br>
                <span class="status review">Pendiente</span>
            </div>

            <div class="item">
                <h3>Ajuste aprobado</h3>
                <small>Modificación menor documentada, aprobada y cerrada.</small><br>
                <span class="status done">Aprobado</span>
            </div>
        </div>

        <div id="${id}-docs" class="module">
            <div class="item"><h3>Documento de alcance</h3><small>PDF · Entregado al cliente.</small></div>
            <div class="item"><h3>Presupuesto / propuesta</h3><small>Documento comercial pendiente de firma.</small></div>
            <div class="item"><h3>Entregables técnicos</h3><small>Archivos finales, planos, artes, reportes o prototipos según división.</small></div>
        </div>

        <div id="${id}-milestones" class="module">
            <div class="item"><h3>Aprobación pendiente</h3><small>Cliente debe aprobar el último entregable para avanzar.</small></div>
            <div class="item"><h3>Entrega parcial</h3><small>Programada para el próximo ciclo de trabajo.</small></div>
            <div class="item"><h3>Cierre de fase</h3><small>Revisión ejecutiva y documentación final.</small></div>
        </div>
    </div>`;
}

function showModule(moduleId, button){
    const parent = button.closest(".panel");
    parent.querySelectorAll(".module").forEach(m => m.classList.remove("active"));
    document.getElementById(moduleId).classList.add("active");

    parent.querySelectorAll(".tabs button").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=False)
