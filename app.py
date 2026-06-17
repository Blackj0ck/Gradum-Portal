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
    --red:#d98c8c;
    --blue:#8ca6d9;
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
.danger{background:rgba(217,140,140,.12);color:var(--red)}

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

.gantt{min-width:900px;padding:20px}

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
.gantt-project{color:var(--text);font-size:14px}

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

.gantt-bar.review{background:linear-gradient(90deg,#8f8f8a,#d7d0bf)}
.gantt-bar.donebar{background:linear-gradient(90deg,#6eaf7d,#9be0aa)}

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

/* FINANCE DASHBOARD */
.finance-table{
    width:100%;
    border-collapse:collapse;
    overflow:hidden;
    border-radius:16px;
}

.finance-table th,
.finance-table td{
    padding:15px;
    border-bottom:1px solid rgba(255,255,255,.06);
    text-align:left;
    color:var(--muted);
    font-size:14px;
}

.finance-table th{
    color:var(--gold);
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1.2px;
}

.finance-table td strong{
    color:var(--text);
    font-weight:500;
}

.trend-up{color:var(--green)!important}
.trend-down{color:var(--red)!important}

.cashflow{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:12px;
    margin-top:12px;
}

.cash-month{
    background:rgba(255,255,255,.025);
    border:1px solid var(--line);
    border-radius:16px;
    padding:16px;
}

.cash-month h4{
    font-size:13px;
    font-weight:500;
    margin-bottom:12px;
}

.cash-bar{
    height:100px;
    display:flex;
    align-items:flex-end;
    gap:6px;
}

.cash-in,.cash-out{
    width:50%;
    border-radius:8px 8px 0 0;
}

.cash-in{background:linear-gradient(180deg,var(--green),rgba(133,212,154,.35))}
.cash-out{background:linear-gradient(180deg,var(--red),rgba(217,140,140,.30))}

.document-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
}

.doc-card{
    background:rgba(7,9,12,.50);
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
}

.doc-card h3{
    font-size:15px;
    font-weight:500;
    margin-bottom:8px;
}

.doc-card small{color:var(--muted)}

@media(max-width:1000px){
    body{display:block}
    .sidebar{width:100%;height:auto;position:relative}
    .main{margin-left:0;width:100%;padding:22px}
    .grid4,.grid3,.timeline-summary,.cashflow,.document-grid{grid-template-columns:1fr}
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
        <div class="card" onclick="openFinanceDashboard('Cliente Corporativo')">
            <div>
                <div class="eyebrow">Finance Operations</div>
                <h3>Contabilidad</h3>
                <p>Financial Control Center, estados financieros, cash flow, impuestos y documentos contables.</p>
            </div>
            <span class="status progress">Open Finance Dashboard</span>
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

function openFinanceDashboard(clientName){
    const container = document.getElementById("servicesProject");
    container.innerHTML = financeDashboard(clientName);
}

function financeDashboard(clientName){
    return `
    <div class="panel" style="margin-top:22px">
        <div class="eyebrow">Financial Control Center</div>
        <h2>Contabilidad & Finanzas · ${clientName}</h2>
        <p>Dashboard financiero para monitorear ingresos, gastos, utilidad, flujo de caja, cuentas por cobrar, cuentas por pagar, impuestos y documentos contables.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('finance-summary', this)">Resumen Financiero</button>
            <button onclick="showModule('finance-income', this)">Estado de Resultados</button>
            <button onclick="showModule('finance-cashflow', this)">Cash Flow</button>
            <button onclick="showModule('finance-arap', this)">CxC / CxP</button>
            <button onclick="showModule('finance-taxes', this)">Impuestos</button>
            <button onclick="showModule('finance-kpis', this)">KPIs Financieros</button>
            <button onclick="showModule('finance-docs', this)">Documentos</button>
        </div>

        <div id="finance-summary" class="module active">
            <div class="grid3">
                <div class="widget"><h3>Ingresos</h3><strong>RD$2.4M</strong><p>Facturación mensual estimada.</p></div>
                <div class="widget"><h3>Gastos</h3><strong>RD$1.6M</strong><p>Costos y gastos operativos.</p></div>
                <div class="widget"><h3>Utilidad Neta</h3><strong>RD$820K</strong><p>Resultado neto del período.</p></div>
            </div>

            <div class="grid3">
                <div class="widget"><h3>Margen Neto</h3><strong>34%</strong><p>Rentabilidad sobre ingresos.</p></div>
                <div class="widget"><h3>Cash Balance</h3><strong>RD$1.1M</strong><p>Disponible proyectado.</p></div>
                <div class="widget"><h3>Compliance</h3><strong>OK</strong><p>Sin alertas fiscales críticas.</p></div>
            </div>

            <div class="item">
                <h3>Lectura ejecutiva</h3>
                <small>El período muestra una posición saludable, con margen positivo, flujo de caja estable y obligaciones fiscales bajo control. Se recomienda dar seguimiento a facturas vencidas y pagos programados.</small>
            </div>
        </div>

        <div id="finance-income" class="module">
            <table class="finance-table">
                <thead>
                    <tr>
                        <th>Concepto</th>
                        <th>Actual</th>
                        <th>Anterior</th>
                        <th>Variación</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>Ingresos</strong></td><td>RD$2,400,000</td><td>RD$2,050,000</td><td class="trend-up">+17.1%</td></tr>
                    <tr><td><strong>Costos Directos</strong></td><td>RD$920,000</td><td>RD$870,000</td><td class="trend-down">+5.7%</td></tr>
                    <tr><td><strong>Margen Bruto</strong></td><td>RD$1,480,000</td><td>RD$1,180,000</td><td class="trend-up">+25.4%</td></tr>
                    <tr><td><strong>Gastos Operativos</strong></td><td>RD$530,000</td><td>RD$510,000</td><td class="trend-down">+3.9%</td></tr>
                    <tr><td><strong>EBITDA</strong></td><td>RD$950,000</td><td>RD$670,000</td><td class="trend-up">+41.8%</td></tr>
                    <tr><td><strong>Utilidad Neta</strong></td><td>RD$820,000</td><td>RD$590,000</td><td class="trend-up">+39.0%</td></tr>
                </tbody>
            </table>
        </div>

        <div id="finance-cashflow" class="module">
            <div class="item">
                <h3>Cash Flow Projection</h3>
                <small>Entradas y salidas proyectadas por mes. Verde representa entradas; rojo representa salidas.</small>
            </div>

            <div class="cashflow">
                <div class="cash-month"><h4>Enero</h4><div class="cash-bar"><div class="cash-in" style="height:70%"></div><div class="cash-out" style="height:48%"></div></div></div>
                <div class="cash-month"><h4>Febrero</h4><div class="cash-bar"><div class="cash-in" style="height:76%"></div><div class="cash-out" style="height:56%"></div></div></div>
                <div class="cash-month"><h4>Marzo</h4><div class="cash-bar"><div class="cash-in" style="height:82%"></div><div class="cash-out" style="height:50%"></div></div></div>
                <div class="cash-month"><h4>Abril</h4><div class="cash-bar"><div class="cash-in" style="height:64%"></div><div class="cash-out" style="height:58%"></div></div></div>
                <div class="cash-month"><h4>Mayo</h4><div class="cash-bar"><div class="cash-in" style="height:88%"></div><div class="cash-out" style="height:60%"></div></div></div>
                <div class="cash-month"><h4>Junio</h4><div class="cash-bar"><div class="cash-in" style="height:92%"></div><div class="cash-out" style="height:62%"></div></div></div>
            </div>

            <div class="grid3" style="margin-top:22px">
                <div class="widget"><h3>Entradas</h3><strong>RD$2.1M</strong><p>Cobros esperados.</p></div>
                <div class="widget"><h3>Salidas</h3><strong>RD$1.3M</strong><p>Pagos programados.</p></div>
                <div class="widget"><h3>Balance</h3><strong>RD$800K</strong><p>Flujo neto proyectado.</p></div>
            </div>
        </div>

        <div id="finance-arap" class="module">
            <div class="grid2">
                <div class="panel">
                    <h2>Cuentas por Cobrar</h2>
                    <div class="item"><h3>Factura #00124</h3><small>Cliente A · RD$240,000 · Vence en 5 días</small><br><span class="status progress">Pendiente</span></div>
                    <div class="item"><h3>Factura #00125</h3><small>Cliente B · RD$185,000 · Vencida 12 días</small><br><span class="status danger">Vencida</span></div>
                    <div class="item"><h3>Factura #00126</h3><small>Cliente C · RD$310,000 · Vence en 18 días</small><br><span class="status review">En plazo</span></div>
                </div>

                <div class="panel">
                    <h2>Cuentas por Pagar</h2>
                    <div class="item"><h3>Proveedor Materiales</h3><small>RD$360,000 · Pago programado</small><br><span class="status progress">Próximo pago</span></div>
                    <div class="item"><h3>Servicios Profesionales</h3><small>RD$95,000 · Pendiente aprobación</small><br><span class="status review">Revisión</span></div>
                    <div class="item"><h3>Software / Licencias</h3><small>RD$48,000 · Recurrente mensual</small><br><span class="status done">Controlado</span></div>
                </div>
            </div>
        </div>

        <div id="finance-taxes" class="module">
            <div class="grid3">
                <div class="widget"><h3>ITBIS por pagar</h3><strong>RD$186K</strong><p>Estimado del período.</p></div>
                <div class="widget"><h3>Retenciones</h3><strong>RD$42K</strong><p>Retenciones acumuladas.</p></div>
                <div class="widget"><h3>Próxima fecha</h3><strong>20</strong><p>Día límite fiscal.</p></div>
            </div>

            <div class="item"><h3>Estado fiscal</h3><small>Declaraciones en preparación. No se detectan atrasos críticos en el período actual.</small><br><span class="status done">Compliance OK</span></div>
            <div class="item"><h3>Acción recomendada</h3><small>Validar comprobantes fiscales, retenciones y conciliación de ingresos antes de cierre.</small><br><span class="status review">Revisión necesaria</span></div>
        </div>

        <div id="finance-kpis" class="module">
            <div class="grid3">
                <div class="widget"><h3>Margen Bruto</h3><strong>61%</strong><p>Ingresos menos costos directos.</p></div>
                <div class="widget"><h3>Margen Neto</h3><strong>34%</strong><p>Utilidad neta sobre ingresos.</p></div>
                <div class="widget"><h3>Liquidez</h3><strong>1.8x</strong><p>Capacidad de cubrir obligaciones.</p></div>
            </div>

            <div class="grid3">
                <div class="widget"><h3>DSO</h3><strong>28d</strong><p>Días promedio de cobro.</p></div>
                <div class="widget"><h3>Endeudamiento</h3><strong>22%</strong><p>Pasivos sobre activos.</p></div>
                <div class="widget"><h3>Burn Rate</h3><strong>RD$530K</strong><p>Gasto operativo mensual.</p></div>
            </div>
        </div>

        <div id="finance-docs" class="module">
            <div class="document-grid">
                <div class="doc-card"><h3>Estados Financieros</h3><small>Balance general, estado de resultados y flujo de efectivo.</small></div>
                <div class="doc-card"><h3>Facturas</h3><small>Emitidas, recibidas, vencidas y pagadas.</small></div>
                <div class="doc-card"><h3>Recibos</h3><small>Soportes de pagos y cobros.</small></div>
                <div class="doc-card"><h3>Conciliación Bancaria</h3><small>Validación mensual de movimientos.</small></div>
                <div class="doc-card"><h3>Declaraciones Fiscales</h3><small>ITBIS, retenciones y reportes fiscales.</small></div>
                <div class="doc-card"><h3>Comprobantes</h3><small>NCF, proveedores y documentos tributarios.</small></div>
                <div class="doc-card"><h3>Presupuestos</h3><small>Proyección financiera y control presupuestario.</small></div>
                <div class="doc-card"><h3>Reportes Ejecutivos</h3><small>Resumen financiero para gerencia o cliente.</small></div>
            </div>
        </div>
    </div>`;
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
                <div class="widget"><h3>Avance</h3><strong>62%</strong><p>Progreso general del proyecto.</p></div>
                <div class="widget"><h3>Estado</h3><strong>Activo</strong><p>Proyecto en ejecución.</p></div>
                <div class="widget"><h3>Próximo hito</h3><strong>28 Jun</strong><p>Entrega parcial programada.</p></div>
            </div>
            <div class="item"><h3>Executive Summary</h3><small>El proyecto avanza conforme al plan. Existen documentos pendientes de aprobación, un cambio en revisión y próximos hitos programados para cierre de fase.</small></div>
        </div>

        <div id="${id}-timeline" class="module">
            <div class="visual-timeline">
                <div class="timeline-step completed"><div class="circle">1</div><div class="line"></div><h3>Brief / Alcance</h3><small>Definición inicial, objetivos, responsables y entregables.</small><span>01 Jun - 03 Jun</span></div>
                <div class="timeline-step completed"><div class="circle">2</div><div class="line"></div><h3>Planificación</h3><small>Cronograma, presupuesto, recursos y estructura de trabajo.</small><span>04 Jun - 10 Jun</span></div>
                <div class="timeline-step active-step"><div class="circle">3</div><div class="line"></div><h3>Ejecución</h3><small>Desarrollo operativo, construcción, diseño o implementación.</small><span>11 Jun - 25 Jun</span></div>
                <div class="timeline-step pending"><div class="circle">4</div><div class="line"></div><h3>Revisión</h3><small>Validación interna, control de calidad y aprobación del cliente.</small><span>26 Jun - 28 Jun</span></div>
                <div class="timeline-step pending"><div class="circle">5</div><h3>Entrega Final</h3><small>Cierre, documentación final y entrega formal del proyecto.</small><span>29 Jun</span></div>
            </div>
            <div class="timeline-summary">
                <div class="widget"><h3>Fase actual</h3><strong>3/5</strong><p>Ejecución en progreso.</p></div>
                <div class="widget"><h3>Días restantes</h3><strong>12</strong><p>Hasta entrega final.</p></div>
                <div class="widget"><h3>Riesgo</h3><strong>Bajo</strong><p>Sin retrasos críticos registrados.</p></div>
            </div>
        </div>

        <div id="${id}-gantt" class="module">
            <div class="item"><h3>Diagrama de Gantt</h3><small>Vista temporal de proyectos y fases principales dentro del portafolio activo.</small></div>
            <div class="gantt-wrapper">
                <div class="gantt">
                    <div class="gantt-header">
                        <div>Proyecto / Fase</div><div>Semana 1</div><div>Semana 2</div><div>Semana 3</div><div>Semana 4</div><div>Semana 5</div><div>Semana 6</div><div>Semana 7</div><div>Semana 8</div>
                    </div>
                    <div class="gantt-row">
                        <div class="gantt-project">Remodelación Local Comercial</div>
                        <div class="gantt-cell"><div class="gantt-bar donebar" style="width:100%"></div></div><div class="gantt-cell"><div class="gantt-bar donebar" style="width:100%"></div></div><div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div><div class="gantt-cell"><div class="gantt-bar" style="width:85%"></div></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div>
                    </div>
                    <div class="gantt-row">
                        <div class="gantt-project">Obra Residencial Moderna</div>
                        <div class="gantt-cell"></div><div class="gantt-cell"><div class="gantt-bar review" style="width:70%"></div></div><div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div><div class="gantt-cell"><div class="gantt-bar" style="width:100%"></div></div><div class="gantt-cell"><div class="gantt-bar" style="width:60%"></div></div><div class="gantt-cell"></div><div class="gantt-cell"></div><div class="gantt-cell"></div>
                    </div>
                </div>
            </div>
            <div class="gantt-legend">
                <div class="legend-item"><span class="legend-dot done-dot"></span> Completado</div>
                <div class="legend-item"><span class="legend-dot"></span> En ejecución</div>
                <div class="legend-item"><span class="legend-dot review-dot"></span> Revisión / planificación</div>
            </div>
        </div>

        <div id="${id}-weekly" class="module"><div class="item"><h3>Informe Semanal #01</h3><small>Avance, tareas realizadas, fotos, incidencias y próximos pasos.</small><br><button class="btn">Ver informe</button></div></div>
        <div id="${id}-visits" class="module"><div class="item"><h3>Informe de visita / reunión</h3><small>Fecha: 17 Junio 2026 · Observaciones, acuerdos, responsables y próximos pasos.</small></div></div>
        <div id="${id}-changes" class="module"><div class="item"><h3>Cambio solicitado</h3><small>Impacto: +4 días · Costo estimado: US$1,200 · Estado: pendiente aprobación.</small><br><span class="status review">Pendiente</span></div></div>
        <div id="${id}-docs" class="module"><div class="item"><h3>Documento de alcance</h3><small>PDF · Entregado al cliente.</small></div></div>
        <div id="${id}-milestones" class="module"><div class="item"><h3>Aprobación pendiente</h3><small>Cliente debe aprobar el último entregable para avanzar.</small></div></div>
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
