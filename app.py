from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Gradum OS SaaS</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,Arial,sans-serif}
body{background:#0b0f14;color:#f5f1e8;display:flex}
.sidebar{width:285px;height:100vh;background:#080b0f;border-right:1px solid #252525;padding:30px 22px;position:fixed}
.logo{font-size:30px;letter-spacing:2px;font-weight:700}
.subtitle{color:#b8a77a;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;margin:8px 0 35px}
.menu button{display:block;width:100%;padding:14px;margin-bottom:9px;background:transparent;color:#b8b8b8;border:1px solid transparent;border-radius:8px;text-align:left;cursor:pointer}
.menu button:hover,.menu button.active{color:#f5f1e8;border-color:#b8a77a;background:rgba(184,167,122,.08)}
.main{margin-left:285px;width:calc(100% - 285px);padding:36px}
.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px}
.eyebrow{color:#b8a77a;text-transform:uppercase;letter-spacing:2px;font-size:12px;margin-bottom:8px}
h1{font-size:38px;font-weight:600}
.user{border:1px solid #333;padding:12px 18px;border-radius:999px;color:#d6d1c4}
.hero{background:linear-gradient(135deg,#111820,#080b0f);border:1px solid #252525;border-radius:22px;padding:30px;margin-bottom:24px}
.hero h2{font-size:30px;font-weight:500;margin-bottom:12px}
.hero p{color:#b8b8b8;line-height:1.7;max-width:950px}
.section{display:none}.section.active{display:block}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:22px}
.grid2{display:grid;grid-template-columns:2fr 1fr;gap:22px}
.card,.panel,.widget{background:#10151b;border:1px solid #242a31;border-radius:20px;padding:24px}
.card{cursor:pointer;transition:.25s;border-left:4px solid #b8a77a}
.card:hover{transform:translateY(-5px);border-color:#b8a77a}
.card h3,.widget h3,.panel h2{font-weight:500;margin-bottom:10px}
.card p,.widget p,.panel p, small{color:#a8a8a8;line-height:1.6}
.widget strong{font-size:34px;color:#b8a77a}
.item{background:#080b0f;border:1px solid #242a31;border-left:4px solid #b8a77a;padding:16px;border-radius:14px;margin-bottom:12px}
.item h3{font-size:17px;margin-bottom:6px}
.status{display:inline-block;margin-top:12px;padding:6px 12px;border-radius:999px;font-size:12px;text-transform:uppercase}
.progress{background:rgba(184,167,122,.15);color:#d6c48f}
.review{background:rgba(255,255,255,.1);color:#f5f1e8}
.done{background:rgba(74,222,128,.12);color:#86efac}
.tabs{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:22px}
.tabs button{padding:11px 14px;border:1px solid #242a31;background:#10151b;color:#d6d1c4;border-radius:999px;cursor:pointer}
.tabs button:hover,.tabs button.active{border-color:#b8a77a;background:rgba(184,167,122,.1);color:#f5f1e8}
.module{display:none}.module.active{display:block}
.bar{height:9px;background:#222b35;border-radius:999px;margin-top:12px;overflow:hidden}
.fill{height:100%;background:#b8a77a}
.btn{padding:12px 16px;border:1px solid #b8a77a;background:transparent;color:#f5f1e8;border-radius:8px;cursor:pointer;margin-top:14px}
.btn:hover{background:#b8a77a;color:#080b0f}

.visual-timeline{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:0;
    margin-top:20px;
}

.timeline-step{
    position:relative;
    background:#10151b;
    border:1px solid #242a31;
    padding:24px 18px;
    min-height:190px;
}

.timeline-step:first-child{
    border-radius:18px 0 0 18px;
}

.timeline-step:last-child{
    border-radius:0 18px 18px 0;
}

.circle{
    width:40px;
    height:40px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:18px;
    font-weight:bold;
    border:1px solid #b8a77a;
    position:relative;
    z-index:2;
}

.line{
    position:absolute;
    top:43px;
    left:58px;
    right:-22px;
    height:2px;
    background:#334155;
    z-index:1;
}

.timeline-step h3{
    font-size:17px;
    margin-bottom:8px;
}

.timeline-step small{
    display:block;
    color:#a8a8a8;
    margin-bottom:12px;
}

.timeline-step span{
    color:#b8a77a;
    font-size:13px;
}

.completed .circle{
    background:#b8a77a;
    color:#080b0f;
}

.active-step{
    border-color:#b8a77a;
    background:rgba(184,167,122,.08);
}

.active-step .circle{
    background:#b8a77a;
    color:#080b0f;
    box-shadow:0 0 0 6px rgba(184,167,122,.12);
}

.pending .circle{
    color:#b8a77a;
}

.timeline-summary{
    margin-top:22px;
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
}

@media(max-width:1000px){
body{display:block}
.sidebar{width:100%;height:auto;position:relative}
.main{margin-left:0;width:100%;padding:22px}
.grid4,.grid3,.timeline-summary{grid-template-columns:1fr}
.grid2{grid-template-columns:1fr}
.visual-timeline{grid-template-columns:1fr;gap:14px}
.timeline-step{border-radius:18px !important}
.line{display:none}
}
</style>
</head>

<body>

<div class="sidebar">
    <div class="logo">GRADUM</div>
    <div class="subtitle">Client & Project OS</div>

    <div class="menu">
        <button class="active" onclick="showSection('home', this)">Home</button>
        <button onclick="showSection('services', this)">Services</button>
        <button onclick="showSection('construction', this)">Construction</button>
        <button onclick="showSection('consulting', this)">Consulting</button>
        <button onclick="showSection('ventures', this)">Ventures</button>
    </div>
</div>

<div class="main">

<div class="topbar">
    <div>
        <div class="eyebrow">Structured Advisory · Engineered Execution</div>
        <h1>Gradum OS</h1>
    </div>
    <div class="user">Elvin González</div>
</div>

<div id="home" class="section active">
    <div class="hero">
        <div class="eyebrow">Corporate Home</div>
        <h2>Portal SaaS para gestión, visualización y entrega de proyectos.</h2>
        <p>
            Gradum OS centraliza Services, Construction, Consulting y Ventures.
            Cada división contiene proyectos con dashboard ejecutivo, cronograma visual,
            informes, visitas, cambios, documentos, hitos y comunicación con cliente.
        </p>
    </div>

    <div class="grid4">
        <div class="card" onclick="goTo('services')">
            <h3>Services</h3>
            <p>Contabilidad, diseño gráfico, web design y servicios profesionales.</p>
            <span class="status progress">Servicios activos</span>
        </div>

        <div class="card" onclick="goTo('construction')">
            <h3>Construction</h3>
            <p>Gestión integral de construcción, arquitectura, ingeniería y obra.</p>
            <span class="status progress">Obras activas</span>
        </div>

        <div class="card" onclick="goTo('consulting')">
            <h3>Consulting</h3>
            <p>Diagnóstico, estrategia, procesos y acompañamiento empresarial.</p>
            <span class="status review">Advisory</span>
        </div>

        <div class="card" onclick="goTo('ventures')">
            <h3>Ventures</h3>
            <p>Impulsadora de startups, MVPs, validación e innovación.</p>
            <span class="status done">Startups</span>
        </div>
    </div>
</div>

<div id="services" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Services</div>
        <h2>Servicios profesionales organizados por cliente y proyecto.</h2>
        <p>Contabilidad, diseño gráfico y web design con entregables, reportes, hitos y aprobación del cliente.</p>
    </div>

    <div class="grid3">
        <div class="card" onclick="openProject('services','Contabilidad para Cliente Corporativo')">
            <h3>Contabilidad</h3>
            <p>Reportes financieros, impuestos, conciliaciones y documentos contables.</p>
        </div>

        <div class="card" onclick="openProject('services','Identidad Visual Marca Premium')">
            <h3>Diseño Gráfico</h3>
            <p>Branding, piezas visuales, campañas, contenido y aprobaciones.</p>
        </div>

        <div class="card" onclick="openProject('services','Web Design Portal Comercial')">
            <h3>Web Design</h3>
            <p>Sitios web, landing pages, UI, contenido y publicación.</p>
        </div>
    </div>

    <div id="servicesProject"></div>
</div>

<div id="construction" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Construction</div>
        <h2>Gestión integral de proyectos constructivos.</h2>
        <p>Arquitectura e ingeniería funcionan como componentes del flujo constructivo: diseño, planos, presupuesto, ejecución, supervisión y entrega.</p>
    </div>

    <div class="grid3">
        <div class="widget"><h3>Obras activas</h3><strong>12</strong><p>Proyectos en ejecución o planificación.</p></div>
        <div class="widget"><h3>Avance promedio</h3><strong>62%</strong><p>Avance físico general.</p></div>
        <div class="widget"><h3>Reportes emitidos</h3><strong>8</strong><p>Informes semanales y visitas.</p></div>
    </div>

    <div class="grid2">
        <div class="panel">
            <h2>Proyectos Construction</h2>

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
</div>

<div id="consulting" class="section">
    <div class="hero">
        <div class="eyebrow">Gradum Consulting</div>
        <h2>Advisory, estrategia y acompañamiento.</h2>
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
        <h2>Impulsadora de startups, MVPs y nuevas unidades de negocio.</h2>
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
function showSection(sectionId, button){
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
    document.getElementById(sectionId).classList.add("active");

    document.querySelectorAll(".menu button").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
}

function goTo(sectionId){
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
        <p>Espacio SaaS del proyecto con visibilidad para equipo interno y cliente.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('${id}-dashboard', this)">Dashboard Ejecutivo</button>
            <button onclick="showModule('${id}-timeline', this)">Cronograma General</button>
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
                <h3>Resumen ejecutivo</h3>
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
                <div class="widget">
                    <h3>Fase actual</h3>
                    <strong>3/5</strong>
                    <p>Ejecución en progreso.</p>
                </div>

                <div class="widget">
                    <h3>Días restantes</h3>
                    <strong>12</strong>
                    <p>Hasta entrega final.</p>
                </div>

                <div class="widget">
                    <h3>Riesgo</h3>
                    <strong>Bajo</strong>
                    <p>Sin retrasos críticos registrados.</p>
                </div>
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
            <div class="item">
                <h3>Documento de alcance</h3>
                <small>PDF · Entregado al cliente.</small>
            </div>

            <div class="item">
                <h3>Presupuesto / propuesta</h3>
                <small>Documento comercial pendiente de firma.</small>
            </div>

            <div class="item">
                <h3>Entregables técnicos</h3>
                <small>Archivos finales, planos, artes, reportes o prototipos según división.</small>
            </div>
        </div>

        <div id="${id}-milestones" class="module">
            <div class="item">
                <h3>Aprobación pendiente</h3>
                <small>Cliente debe aprobar el último entregable para avanzar.</small>
            </div>

            <div class="item">
                <h3>Entrega parcial</h3>
                <small>Programada para el próximo ciclo de trabajo.</small>
            </div>

            <div class="item">
                <h3>Cierre de fase</h3>
                <small>Revisión ejecutiva y documentación final.</small>
            </div>
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
