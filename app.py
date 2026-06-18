from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Gradum OS · Client Portal</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
    --bg:#071713;
    --panel:#0b211b;
    --panel2:#0f2a23;
    --line:#1c3a31;
    --text:#edf8ea;
    --muted:#8eaa9c;
    --accent:#7be3a8;
    --accent2:#c8f57b;
    --danger:#ff8a8a;
    --soft:rgba(255,255,255,.035);
}

*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,Arial,sans-serif}

body{
    min-height:100vh;
    background:
        radial-gradient(circle at top right,rgba(200,245,123,.12),transparent 32%),
        radial-gradient(circle at bottom left,rgba(123,227,168,.10),transparent 30%),
        var(--bg);
    color:var(--text);
    display:flex;
}

.sidebar{
    width:280px;
    height:100vh;
    position:fixed;
    padding:30px 22px;
    border-right:1px solid var(--line);
    background:rgba(7,23,19,.92);
    backdrop-filter:blur(16px);
}

.logo{
    font-size:30px;
    letter-spacing:3px;
    font-weight:700;
}

.subtitle{
    margin:8px 0 36px;
    color:var(--accent);
    font-size:11px;
    letter-spacing:2px;
    text-transform:uppercase;
}

.menu-label{
    margin-bottom:12px;
    color:#668475;
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1.4px;
}

.menu button{
    width:100%;
    margin-bottom:8px;
    padding:13px 14px;
    border:1px solid transparent;
    border-radius:12px;
    background:transparent;
    color:#c5dccf;
    text-align:left;
    cursor:pointer;
    transition:.2s;
}

.menu button:hover,
.menu button.active{
    color:var(--text);
    border-color:rgba(123,227,168,.42);
    background:rgba(123,227,168,.08);
}

.menu-group{
    margin-top:12px;
}

.division-menu{
    display:none;
    padding-left:10px;
    margin-top:8px;
    border-left:1px solid rgba(123,227,168,.22);
}

.division-menu.open{display:block}
.division-menu button{font-size:13px;color:var(--muted)}

.main{
    margin-left:280px;
    width:calc(100% - 280px);
    padding:34px;
}

.topbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:28px;
}

.eyebrow{
    color:var(--accent);
    text-transform:uppercase;
    letter-spacing:2.3px;
    font-size:11px;
    margin-bottom:9px;
}

h1{
    font-size:40px;
    font-weight:500;
    letter-spacing:-1px;
}

.user{
    border:1px solid var(--line);
    border-radius:999px;
    padding:11px 16px;
    color:#d9eadb;
    background:var(--soft);
}

.hero{
    border:1px solid var(--line);
    border-radius:28px;
    padding:42px;
    margin-bottom:24px;
    background:
        linear-gradient(135deg,rgba(255,255,255,.04),rgba(255,255,255,.01)),
        linear-gradient(120deg,#102b24,#071713);
    overflow:hidden;
    position:relative;
}

.hero:after{
    content:"";
    position:absolute;
    width:220px;
    height:220px;
    border-radius:50%;
    background:rgba(123,227,168,.055);
    right:-80px;
    top:-80px;
}

.hero h2{
    max-width:800px;
    font-size:43px;
    line-height:1.12;
    font-weight:500;
    letter-spacing:-1px;
    margin-bottom:14px;
}

.hero p{
    max-width:720px;
    color:#a8c4b5;
    line-height:1.75;
    font-size:15px;
}

.section,.module{display:none}
.section.active,.module.active{display:block}

.grid4{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:16px;
}

.grid3{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
    margin-bottom:18px;
}

.grid2{
    display:grid;
    grid-template-columns:1.4fr .9fr;
    gap:18px;
}

.card,.panel,.widget,.item{
    border:1px solid var(--line);
    border-radius:22px;
    background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.012));
    box-shadow:0 20px 70px rgba(0,0,0,.14);
}

.card{
    min-height:250px;
    padding:26px;
    cursor:pointer;
    transition:.22s;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.card:hover{
    transform:translateY(-4px);
    border-color:rgba(123,227,168,.50);
    background:rgba(123,227,168,.055);
}

.card h3{
    font-size:28px;
    font-weight:500;
    margin-bottom:12px;
}

.card p,.panel p,.widget p,.item small,small{
    color:var(--muted);
    line-height:1.6;
}

.panel,.widget,.item{
    padding:22px;
}

.panel h2,.widget h3,.item h3{
    font-weight:500;
    margin-bottom:8px;
}

.widget strong{
    display:block;
    color:var(--accent2);
    font-size:32px;
    font-weight:500;
    margin-bottom:4px;
}

.item{
    margin-bottom:12px;
    background:rgba(10,31,26,.55);
}

.status{
    display:inline-block;
    margin-top:12px;
    padding:6px 11px;
    border-radius:999px;
    font-size:11px;
    letter-spacing:.65px;
    text-transform:uppercase;
}

.progress{background:rgba(123,227,168,.12);color:var(--accent2)}
.review{background:rgba(255,255,255,.08);color:#e3f0d8}
.done{background:rgba(123,227,168,.12);color:var(--accent)}
.danger{background:rgba(255,138,138,.13);color:var(--danger)}

.tabs{
    display:flex;
    gap:9px;
    flex-wrap:wrap;
    margin:20px 0;
}

.tabs button{
    padding:10px 13px;
    border:1px solid var(--line);
    border-radius:999px;
    background:rgba(255,255,255,.025);
    color:#d7ead3;
    cursor:pointer;
    transition:.2s;
}

.tabs button:hover,
.tabs button.active{
    border-color:rgba(123,227,168,.65);
    background:rgba(123,227,168,.10);
}

.btn,.btn-soft{
    padding:11px 14px;
    border-radius:11px;
    cursor:pointer;
    transition:.2s;
}

.btn{
    border:1px solid var(--accent);
    background:transparent;
    color:var(--text);
}

.btn:hover{background:var(--accent);color:#071713}

.btn-soft{
    border:1px solid var(--line);
    background:rgba(255,255,255,.035);
    color:var(--text);
}

.btn-soft:hover{
    border-color:rgba(123,227,168,.55);
    background:rgba(123,227,168,.10);
}

.bar{
    height:8px;
    background:#18382e;
    border-radius:999px;
    margin-top:12px;
    overflow:hidden;
}

.fill{
    height:100%;
    border-radius:999px;
    background:linear-gradient(90deg,var(--accent),var(--accent2));
}

/* Construction essentials */
.live-row{
    display:grid;
    grid-template-columns:86px 1fr;
    gap:14px;
    padding:15px;
    border:1px solid var(--line);
    border-left:3px solid var(--accent);
    border-radius:16px;
    background:rgba(10,31,26,.55);
    margin-bottom:10px;
}

.live-time{
    color:var(--accent);
    font-size:12px;
    text-transform:uppercase;
    letter-spacing:.7px;
}

.stage-row{
    padding:15px;
    border:1px solid var(--line);
    border-radius:16px;
    background:rgba(10,31,26,.50);
    margin-bottom:12px;
}

.stage-head{
    display:flex;
    justify-content:space-between;
    margin-bottom:8px;
}

.evidence-grid,.next-grid,.traffic-grid,.document-grid{
    display:grid;
    gap:14px;
}

.evidence-grid{grid-template-columns:repeat(3,1fr)}
.next-grid{grid-template-columns:repeat(4,1fr)}
.traffic-grid{grid-template-columns:repeat(5,1fr)}
.document-grid{grid-template-columns:repeat(4,1fr)}

.evidence-card,.next-card,.traffic-card,.doc-card{
    border:1px solid var(--line);
    border-radius:18px;
    background:rgba(10,31,26,.50);
    overflow:hidden;
}

.evidence-thumb{
    height:126px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:34px;
    color:var(--accent2);
    background:
        linear-gradient(135deg,rgba(123,227,168,.20),rgba(255,255,255,.035)),
        radial-gradient(circle at center,rgba(255,255,255,.08),transparent 42%);
}

.evidence-body,.next-card,.traffic-card,.doc-card{padding:17px}

.traffic-dot{
    width:13px;
    height:13px;
    border-radius:50%;
    display:inline-block;
    margin-right:7px;
    background:var(--accent);
}

.traffic-dot.yellow{background:var(--accent2)}
.traffic-dot.red{background:var(--danger)}

.visual-timeline{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    margin-top:16px;
}

.timeline-step{
    min-height:176px;
    padding:20px 16px;
    border:1px solid var(--line);
    background:rgba(255,255,255,.024);
    position:relative;
}

.timeline-step:first-child{border-radius:18px 0 0 18px}
.timeline-step:last-child{border-radius:0 18px 18px 0}

.circle{
    width:38px;
    height:38px;
    border-radius:50%;
    border:1px solid var(--accent);
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:14px;
    position:relative;
    z-index:2;
}

.line{
    position:absolute;
    top:39px;
    left:54px;
    right:-18px;
    height:2px;
    background:#2d4c40;
}

.completed .circle,.active-step .circle{
    background:var(--accent);
    color:#071713;
}

.active-step{
    border-color:rgba(123,227,168,.60);
    background:rgba(123,227,168,.07);
}

.timeline-step span{
    display:block;
    margin-top:10px;
    color:var(--accent);
    font-size:12px;
}

.gantt-wrapper{
    overflow-x:auto;
    border:1px solid var(--line);
    border-radius:20px;
    background:rgba(255,255,255,.018);
}

.gantt{min-width:860px;padding:18px}

.gantt-header,.gantt-row{
    display:grid;
    grid-template-columns:210px repeat(8,1fr);
    gap:10px;
    align-items:center;
}

.gantt-header{
    color:var(--accent);
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1px;
    padding-bottom:12px;
    border-bottom:1px solid var(--line);
}

.gantt-row{
    min-height:52px;
    border-bottom:1px solid rgba(255,255,255,.04);
}

.gantt-cell{
    height:18px;
    border-radius:999px;
    background:rgba(255,255,255,.035);
}

.gantt-bar{
    height:18px;
    border-radius:999px;
    background:linear-gradient(90deg,var(--accent),var(--accent2));
}

.gantt-bar.donebar{background:linear-gradient(90deg,#65c89a,#b6f0cc)}
.gantt-bar.review{background:linear-gradient(90deg,#7aa091,#d8ead2)}

/* Approval center */
.approval-grid{
    display:grid;
    grid-template-columns:1.15fr .85fr;
    gap:18px;
}

.approval-card{
    border:1px solid var(--line);
    border-left:3px solid var(--accent);
    border-radius:18px;
    padding:18px;
    background:rgba(10,31,26,.55);
    margin-bottom:14px;
}

.approval-meta{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:9px;
    margin:14px 0;
}

.approval-meta div{
    padding:11px;
    border:1px solid var(--line);
    border-radius:14px;
    background:rgba(255,255,255,.025);
}

.approval-meta span{
    display:block;
    color:var(--accent);
    font-size:10px;
    text-transform:uppercase;
    letter-spacing:1px;
    margin-bottom:4px;
}

.comment-box textarea{
    width:100%;
    min-height:70px;
    margin-top:10px;
    resize:vertical;
    background:rgba(10,31,26,.72);
    border:1px solid var(--line);
    border-radius:14px;
    color:var(--text);
    padding:12px;
    outline:none;
}

.comment-box textarea:focus{border-color:rgba(123,227,168,.65)}

.approval-actions{
    display:flex;
    gap:9px;
    flex-wrap:wrap;
    margin-top:12px;
}

.history-event,.history-row,.approval-note{
    border:1px solid var(--line);
    border-radius:16px;
    background:rgba(10,31,26,.50);
    padding:14px;
    margin-bottom:10px;
}

.approval-note{
    color:var(--muted);
    line-height:1.6;
}

.toast{
    position:fixed;
    right:24px;
    bottom:24px;
    display:none;
    z-index:1000;
    padding:13px 15px;
    border:1px solid rgba(123,227,168,.45);
    border-radius:16px;
    background:rgba(7,23,19,.96);
    box-shadow:0 20px 60px rgba(0,0,0,.35);
}

.toast.show{display:block}

/* Finance essentials */
.finance-table{
    width:100%;
    border-collapse:collapse;
}

.finance-table th,.finance-table td{
    padding:14px;
    border-bottom:1px solid rgba(255,255,255,.06);
    text-align:left;
    color:var(--muted);
    font-size:14px;
}

.finance-table th{
    color:var(--accent);
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1px;
}

.finance-table td strong{color:var(--text);font-weight:500}

@media(max-width:1000px){
    body{display:block}
    .sidebar{width:100%;height:auto;position:relative}
    .main{margin-left:0;width:100%;padding:20px}
    .grid4,.grid3,.grid2,.evidence-grid,.next-grid,.traffic-grid,.document-grid,.approval-grid,.approval-meta{grid-template-columns:1fr}
    .visual-timeline{grid-template-columns:1fr;gap:12px}
    .timeline-step{border-radius:18px!important}
    .line{display:none}
    .topbar{align-items:flex-start;gap:12px;flex-direction:column}
    .hero h2{font-size:34px}
}
</style>
</head>

<body>

<div class="sidebar">
    <div class="logo">GRADUM</div>
    <div class="subtitle">Client Portal</div>

    <div class="menu">
        <div class="menu-label">Navigation</div>
        <button class="active" onclick="showSection('home', this)">Home</button>

        <div class="menu-group">
            <button onclick="toggleDivisions()">☰ Servicios</button>
            <div id="divisionMenu" class="division-menu">
                <button onclick="showSection('services', this)">Services</button>
                <button onclick="showSection('construction', this)">Construction</button>
                <button onclick="showSection('consulting', this)">Consulting</button>
                <button onclick="showSection('ventures', this)">Ventures</button>
            </div>
        </div>
    </div>
</div>

<div class="main">
    <div class="topbar">
        <div>
            <div class="eyebrow">Private Client Workspace</div>
            <h1>Gradum OS</h1>
        </div>
        <div class="user">Elvin González</div>
    </div>

    <div id="home" class="section active">
        <div class="hero">
            <div class="eyebrow">Operating Intelligence</div>
            <h2>Un portal claro para ver, aprobar y dar seguimiento.</h2>
            <p>Una experiencia sencilla para que cada cliente visualice su servicio, sus entregables, avances, documentos y decisiones importantes.</p>
        </div>

        <div class="grid4">
            <div class="card" onclick="goTo('services')"><div><div class="eyebrow">Professional Services</div><h3>Services</h3><p>Contabilidad, diseño y web.</p></div></div>
            <div class="card" onclick="goTo('construction')"><div><div class="eyebrow">Built Environment</div><h3>Construction</h3><p>Obra, avance y entregables.</p></div></div>
            <div class="card" onclick="goTo('consulting')"><div><div class="eyebrow">Strategic Advisory</div><h3>Consulting</h3><p>Diagnóstico y roadmap.</p></div></div>
            <div class="card" onclick="goTo('ventures')"><div><div class="eyebrow">Venture Studio</div><h3>Ventures</h3><p>MVPs y validación.</p></div></div>
        </div>
    </div>

    <div id="services" class="section">
        <div class="hero">
            <div class="eyebrow">Gradum Services</div>
            <h2>Servicios profesionales por cliente y entregable.</h2>
            <p>Cada servicio tiene su propio espacio, documentos, aprobaciones y reportes.</p>
        </div>

        <div class="grid3">
            <div class="card" onclick="openFinanceDashboard('Cliente Corporativo')">
                <div><div class="eyebrow">Finance Operations</div><h3>Contabilidad</h3><p>Dashboard financiero, impuestos y documentos.</p></div>
            </div>
            <div class="card" onclick="openProject('services','Identidad Visual Marca Premium')">
                <div><div class="eyebrow">Brand Systems</div><h3>Diseño Gráfico</h3><p>Diseños, revisiones y aprobaciones.</p></div>
            </div>
            <div class="card" onclick="openProject('services','Web Design Portal Comercial')">
                <div><div class="eyebrow">Digital Experience</div><h3>Web Design</h3><p>Desarrollo, QA y entrega.</p></div>
            </div>
        </div>

        <div id="servicesProject"></div>
    </div>

    <div id="construction" class="section">
        <div class="hero">
            <div class="eyebrow">Gradum Construction</div>
            <h2>Proyecto de obra con visibilidad simple y en vivo.</h2>
            <p>Avance, aprobaciones, evidencias, cronograma, documentos y próximos pasos.</p>
        </div>

        <div class="grid3">
            <div class="widget"><h3>Avance</h3><strong>62%</strong><p>Progreso general.</p></div>
            <div class="widget"><h3>Próximo hito</h3><strong>28 Jun</strong><p>Entrega parcial.</p></div>
            <div class="widget"><h3>Estado</h3><strong>Activo</strong><p>Sin alertas críticas.</p></div>
        </div>

        <div class="panel">
            <h2>Proyectos</h2>
            <div class="item" onclick="openProject('construction','Remodelación Local Comercial')">
                <h3>Remodelación Local Comercial</h3>
                <small>Cliente corporativo · Avance 62%</small>
                <div class="bar"><div class="fill" style="width:62%"></div></div>
                <span class="status progress">Abrir proyecto</span>
            </div>
            <div class="item" onclick="openProject('construction','Obra Residencial Moderna')">
                <h3>Obra Residencial Moderna</h3>
                <small>Diseño, presupuesto y planificación inicial.</small>
                <div class="bar"><div class="fill" style="width:35%"></div></div>
                <span class="status review">Abrir proyecto</span>
            </div>
        </div>

        <div id="constructionProject"></div>
    </div>

    <div id="consulting" class="section">
        <div class="hero">
            <div class="eyebrow">Gradum Consulting</div>
            <h2>Consultoría organizada por diagnóstico, roadmap y entregables.</h2>
            <p>Seguimiento simple para decisiones, reuniones y documentos clave.</p>
        </div>
        <div class="panel">
            <div class="item" onclick="openProject('consulting','Diagnóstico Operativo Empresarial')"><h3>Diagnóstico Operativo Empresarial</h3><small>Mapa de procesos y recomendaciones.</small></div>
            <div class="item" onclick="openProject('consulting','Plan Estratégico Comercial')"><h3>Plan Estratégico Comercial</h3><small>Roadmap de crecimiento.</small></div>
        </div>
        <div id="consultingProject"></div>
    </div>

    <div id="ventures" class="section">
        <div class="hero">
            <div class="eyebrow">Gradum Ventures</div>
            <h2>Startups, MVPs y nuevas unidades de negocio.</h2>
            <p>Validación, roadmap, métricas, inversión y escalabilidad.</p>
        </div>
        <div class="panel">
            <div class="item" onclick="openProject('ventures','Gradum OS SaaS')"><h3>Gradum OS SaaS</h3><small>Portal del cliente y gestión de proyectos.</small></div>
            <div class="item" onclick="openProject('ventures','Motor de Recomendaciones Locales')"><h3>Motor de Recomendaciones Locales</h3><small>Google Places y tendencias.</small></div>
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
    if(button){button.classList.add("active");}
}

function goTo(sectionId){
    document.getElementById("divisionMenu").classList.add("open");
    document.querySelectorAll(".menu button").forEach(b => {
        if(b.textContent.toLowerCase().includes(sectionId)){
            b.click();
        }
    });
}

function openProject(division, projectName){
    const container = document.getElementById(division + "Project");
    container.innerHTML = projectWorkspace(projectName, division);
}

function openFinanceDashboard(clientName){
    document.getElementById("servicesProject").innerHTML = `
    <div class="panel" style="margin-top:20px">
        <div class="eyebrow">Financial Workspace</div>
        <h2>Contabilidad & Finanzas · ${clientName}</h2>
        <p>Vista simplificada para revisar estado financiero, impuestos, documentos y decisiones.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('finance-summary', this)">Resumen</button>
            <button onclick="showModule('finance-budget', this)">Budget vs Actual</button>
            <button onclick="showModule('finance-taxes', this)">Impuestos</button>
            <button onclick="showModule('finance-docs', this)">Documentos</button>
        </div>

        <div id="finance-summary" class="module active">
            <div class="grid3">
                <div class="widget"><h3>Ingresos</h3><strong>RD$2.4M</strong><p>Período actual.</p></div>
                <div class="widget"><h3>Utilidad</h3><strong>RD$820K</strong><p>Resultado neto.</p></div>
                <div class="widget"><h3>Cash</h3><strong>RD$1.1M</strong><p>Disponible proyectado.</p></div>
            </div>
            <div class="item"><h3>Lectura ejecutiva</h3><small>El período se mantiene saludable. Se recomienda dar seguimiento a facturas vencidas y cierre fiscal.</small></div>
        </div>

        <div id="finance-budget" class="module">
            <table class="finance-table">
                <thead><tr><th>Partida</th><th>Presupuesto</th><th>Actual</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td><strong>Ingresos</strong></td><td>RD$2.22M</td><td>RD$2.4M</td><td><span class="status done">Favorable</span></td></tr>
                    <tr><td><strong>Costos</strong></td><td>RD$855K</td><td>RD$920K</td><td><span class="status review">Atención</span></td></tr>
                    <tr><td><strong>Utilidad</strong></td><td>RD$725K</td><td>RD$820K</td><td><span class="status done">Favorable</span></td></tr>
                </tbody>
            </table>
        </div>

        <div id="finance-taxes" class="module">
            <div class="grid3">
                <div class="widget"><h3>ITBIS</h3><strong>RD$186K</strong><p>Estimado por pagar.</p></div>
                <div class="widget"><h3>Retenciones</h3><strong>RD$42K</strong><p>Acumulado.</p></div>
                <div class="widget"><h3>Fecha límite</h3><strong>20</strong><p>Día fiscal.</p></div>
            </div>
        </div>

        <div id="finance-docs" class="module">
            <div class="document-grid">
                <div class="doc-card"><h3>Estados Financieros</h3><small>Balance y resultados.</small></div>
                <div class="doc-card"><h3>Facturas</h3><small>Emitidas y recibidas.</small></div>
                <div class="doc-card"><h3>Conciliación</h3><small>Movimientos bancarios.</small></div>
                <div class="doc-card"><h3>Declaraciones</h3><small>ITBIS y retenciones.</small></div>
            </div>
        </div>
    </div>`;
}

function projectWorkspace(name, division){
    const id = division + "Module";

    return `
    <div class="panel" style="margin-top:20px">
        <div class="eyebrow">Project Workspace</div>
        <h2>${name}</h2>
        <p>Un espacio simple para ver estado, aprobar entregables, revisar avances y consultar documentos.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('${id}-overview', this)">Resumen</button>
            <button onclick="showModule('${id}-approvals', this)">Aprobaciones</button>
            ${division === 'construction' ? `
                <button onclick="showModule('${id}-live', this)">Obra en Vivo</button>
                <button onclick="showModule('${id}-evidence', this)">Evidencias</button>
                <button onclick="showModule('${id}-timeline', this)">Cronograma</button>
                <button onclick="showModule('${id}-gantt', this)">Gantt</button>
            ` : `
                <button onclick="showModule('${id}-timeline', this)">Cronograma</button>
            `}
            <button onclick="showModule('${id}-docs', this)">Documentos</button>
        </div>

        <div id="${id}-overview" class="module active">
            <div class="grid3">
                <div class="widget"><h3>Avance</h3><strong>${division === 'construction' ? '62%' : '48%'}</strong><p>Progreso general.</p></div>
                <div class="widget"><h3>Estado</h3><strong>Activo</strong><p>Sin alertas críticas.</p></div>
                <div class="widget"><h3>Próximo hito</h3><strong>28 Jun</strong><p>Entrega parcial.</p></div>
            </div>
            <div class="item"><h3>Resumen ejecutivo</h3><small>El proyecto avanza conforme al plan. Hay entregables pendientes de aprobación y próximos hitos programados.</small></div>
        </div>

        <div id="${id}-approvals" class="module">
            <div class="approval-grid">
                <div class="panel">
                    <div class="eyebrow">Pendientes</div>
                    <h2>Aprobaciones</h2>
                    <p>Aprueba o solicita cambios. Las decisiones se guardan en el navegador.</p>
                    ${approvalCard(id, "approval-1", "Entregable Principal V03", "Documento pendiente de revisión del cliente.", "V03", "18 Jun 2026", "Gradum")}
                    ${approvalCard(id, "approval-2", "Presupuesto Ajustado V02", "Actualización por cambio de alcance.", "V02", "19 Jun 2026", "Dirección Técnica")}
                </div>

                <div class="panel">
                    <div class="eyebrow">Historial</div>
                    <h2>Decisiones</h2>
                    <div id="${id}-approval-events"></div>
                    <div class="approval-note">
                        Las aprobaciones son una simulación funcional. En producción se conectan con usuario, PDF, firma digital y base de datos.
                    </div>
                    <button class="btn-soft" style="margin-top:10px" onclick="resetApprovalCenter('${id}')">Reiniciar demo</button>
                </div>
            </div>
        </div>

        ${division === 'construction' ? `
        <div id="${id}-live" class="module">
            <div class="grid2">
                <div class="panel">
                    <div class="eyebrow">Live Feed</div>
                    <h2>Actividad reciente</h2>
                    <div class="live-row"><div class="live-time">Hoy · 9:15</div><div><h3>Armado de acero completado</h3><small>Zona de columnas principales.</small></div></div>
                    <div class="live-row"><div class="live-time">Hoy · 11:40</div><div><h3>Llegada de materiales</h3><small>Cemento, acero y agregados.</small></div></div>
                    <div class="live-row"><div class="live-time">Hoy · 3:20</div><div><h3>Supervisión técnica</h3><small>Revisión de seguridad y avance.</small></div></div>
                </div>
                <div class="panel">
                    <div class="eyebrow">Semáforo</div>
                    <h2>Estado general</h2>
                    <div class="traffic-card"><h3><span class="traffic-dot"></span>Cronograma</h3><small>Dentro del plan.</small></div>
                    <div class="traffic-card"><h3><span class="traffic-dot"></span>Presupuesto</h3><small>Sin desviaciones críticas.</small></div>
                    <div class="traffic-card"><h3><span class="traffic-dot yellow"></span>Riesgos</h3><small>Materiales en seguimiento.</small></div>
                </div>
            </div>
        </div>

        <div id="${id}-evidence" class="module">
            <div class="evidence-grid">
                <div class="evidence-card"><div class="evidence-thumb">📷</div><div class="evidence-body"><h3>Semana 1</h3><small>24 fotos · Excavación.</small></div></div>
                <div class="evidence-card"><div class="evidence-thumb">🎥</div><div class="evidence-body"><h3>Semana 2</h3><small>31 fotos · Cimentación.</small></div></div>
                <div class="evidence-card"><div class="evidence-thumb">📸</div><div class="evidence-body"><h3>Semana 3</h3><small>18 fotos · Muros.</small></div></div>
            </div>
        </div>
        ` : ``}

        <div id="${id}-timeline" class="module">
            <div class="visual-timeline">
                <div class="timeline-step completed"><div class="circle">1</div><div class="line"></div><h3>Alcance</h3><small>Objetivos y entregables.</small><span>01-03 Jun</span></div>
                <div class="timeline-step completed"><div class="circle">2</div><div class="line"></div><h3>Planificación</h3><small>Cronograma y recursos.</small><span>04-10 Jun</span></div>
                <div class="timeline-step active-step"><div class="circle">3</div><div class="line"></div><h3>Ejecución</h3><small>Trabajo principal.</small><span>11-25 Jun</span></div>
                <div class="timeline-step"><div class="circle">4</div><div class="line"></div><h3>Revisión</h3><small>Calidad y aprobación.</small><span>26-28 Jun</span></div>
                <div class="timeline-step"><div class="circle">5</div><h3>Entrega</h3><small>Cierre formal.</small><span>29 Jun</span></div>
            </div>
        </div>

        ${division === 'construction' ? `
        <div id="${id}-gantt" class="module">
            <div class="gantt-wrapper">
                <div class="gantt">
                    <div class="gantt-header"><div>Fase</div><div>S1</div><div>S2</div><div>S3</div><div>S4</div><div>S5</div><div>S6</div><div>S7</div><div>S8</div></div>
                    <div class="gantt-row"><div>Estructura</div><div class="gantt-cell"><div class="gantt-bar donebar"></div></div><div class="gantt-cell"><div class="gantt-bar donebar"></div></div><div class="gantt-cell"><div class="gantt-bar"></div></div><div class="gantt-cell"><div class="gantt-bar"></div></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div></div>
                    <div class="gantt-row"><div>Mampostería</div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"><div class="gantt-bar review"></div></div><div class="gantt-cell"><div class="gantt-bar"></div></div><div class="gantt-cell"><div class="gantt-bar"></div></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div></div>
                </div>
            </div>
        </div>
        ` : ``}

        <div id="${id}-docs" class="module">
            <div class="document-grid">
                <div class="doc-card"><h3>Contrato</h3><small>Documento base.</small></div>
                <div class="doc-card"><h3>Planos</h3><small>Versiones aprobadas.</small></div>
                <div class="doc-card"><h3>Informes</h3><small>Reportes semanales.</small></div>
                <div class="doc-card"><h3>Entregables</h3><small>Archivos finales.</small></div>
            </div>
        </div>
    </div>`;
}

function approvalCard(id, localId, title, description, version, date, owner){
    const fullId = id + "-" + localId;
    return `
    <div class="approval-card" id="${fullId}">
        <h3>${title}</h3>
        <small>${description}</small>
        <div class="approval-meta">
            <div><span>Versión</span><small>${version}</small></div>
            <div><span>Fecha</span><small>${date}</small></div>
            <div><span>Responsable</span><small>${owner}</small></div>
            <div><span>Estado</span><small id="${fullId}-status">Pendiente</small></div>
        </div>
        <span class="status review" id="${fullId}-badge">Pendiente</span>
        <div class="comment-box">
            <textarea id="${fullId}-comment" placeholder="Comentario opcional..."></textarea>
        </div>
        <div class="approval-actions">
            <button class="btn-soft" onclick="viewDocument('${title}')">Ver</button>
            <button class="btn-soft" onclick="approvalAction('${id}','${fullId}','${title}','Aprobado')">Aprobar</button>
            <button class="btn-soft" onclick="approvalAction('${id}','${fullId}','${title}','Cambios solicitados')">Solicitar cambios</button>
        </div>
    </div>`;
}

function showModule(moduleId, button){
    const parent = button.closest(".panel");
    parent.querySelectorAll(".module").forEach(m => m.classList.remove("active"));
    document.getElementById(moduleId).classList.add("active");
    parent.querySelectorAll(".tabs button").forEach(b => b.classList.remove("active"));
    button.classList.add("active");

    if(moduleId.endsWith("-approvals")){
        loadApprovalCenter(moduleId.replace("-approvals",""));
    }
}

function getStore(id){
    try{return JSON.parse(localStorage.getItem("gradum_approvals_"+id)) || {documents:{},events:[]};}
    catch(e){return {documents:{},events:[]};}
}

function saveStore(id, store){
    localStorage.setItem("gradum_approvals_"+id, JSON.stringify(store));
}

function approvalAction(id, fullId, title, statusText){
    const commentEl = document.getElementById(fullId+"-comment");
    const comment = commentEl ? commentEl.value.trim() : "";
    const date = new Date().toLocaleString("es-DO",{day:"2-digit",month:"short",hour:"2-digit",minute:"2-digit"});
    const store = getStore(id);

    store.documents[fullId] = {status:statusText, comment, date};
    store.events.unshift({title, status:statusText, comment, date});
    saveStore(id, store);

    updateApprovalUI(fullId, store.documents[fullId]);
    renderEvents(id);
    toast(`${title}: ${statusText}`);
}

function updateApprovalUI(fullId, state){
    const status = document.getElementById(fullId+"-status");
    const badge = document.getElementById(fullId+"-badge");
    const comment = document.getElementById(fullId+"-comment");

    if(status){status.textContent = state.status;}
    if(badge){
        badge.textContent = state.status;
        badge.className = state.status === "Aprobado" ? "status done" :
                          state.status === "Cambios solicitados" ? "status danger" : "status review";
    }
    if(comment && state.comment){comment.value = state.comment;}
}

function loadApprovalCenter(id){
    const store = getStore(id);
    Object.keys(store.documents).forEach(fullId => updateApprovalUI(fullId, store.documents[fullId]));
    renderEvents(id);
}

function renderEvents(id){
    const box = document.getElementById(id+"-approval-events");
    if(!box){return;}
    const store = getStore(id);
    if(!store.events.length){
        box.innerHTML = `<div class="approval-note">Sin decisiones nuevas todavía.</div>`;
        return;
    }
    box.innerHTML = store.events.map(e => `
        <div class="history-event">
            <strong>${e.status}</strong>
            <small style="display:block;margin-top:4px">${e.title} · ${e.date}</small>
            <p>${e.comment || "Sin comentario adicional."}</p>
        </div>`).join("");
}

function resetApprovalCenter(id){
    localStorage.removeItem("gradum_approvals_"+id);
    ["approval-1","approval-2"].forEach(localId => {
        const fullId = id+"-"+localId;
        updateApprovalUI(fullId,{status:"Pendiente",comment:""});
        const txt = document.getElementById(fullId+"-comment");
        if(txt){txt.value = "";}
    });
    renderEvents(id);
    toast("Demo reiniciada");
}

function viewDocument(title){
    toast("Vista previa: " + title);
}

function toast(message){
    let t = document.getElementById("toast");
    if(!t){
        t = document.createElement("div");
        t.id = "toast";
        t.className = "toast";
        document.body.appendChild(t);
    }
    t.textContent = message;
    t.classList.add("show");
    setTimeout(()=>t.classList.remove("show"),2200);
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
