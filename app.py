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
    --bg:#0a1f1a;
    --panel:#0e2620;
    --panel2:#123028;
    --line:#1f3a32;
    --text:#eaf6e6;
    --muted:#88a89a;
    --gold:#7be3a8;
    --gold2:#bef576;
    --green:#7be3a8;
    --red:#ff8a8a;
    --blue:#9bd4c4;
}

*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,Arial,sans-serif}

body{
    background:
        radial-gradient(circle at top right,rgba(190,245,118,.14),transparent 32%),
        radial-gradient(circle at bottom left,rgba(123,227,168,.10),transparent 30%),
        var(--bg);
    color:var(--text);
    display:flex;
}

.sidebar{
    width:292px;
    height:100vh;
    background:rgba(10,31,26,.92);
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
    color:#6b8a7a;
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
    color:#bcd4c6;
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
    border-color:rgba(123,227,168,.45);
    background:linear-gradient(135deg,rgba(123,227,168,.10),rgba(255,255,255,.025));
}

.hamburger-btn{
    margin-top:16px;
    border-color:rgba(123,227,168,.25)!important;
}

.division-menu{
    display:none;
    margin-top:8px;
    padding-left:10px;
    border-left:1px solid rgba(123,227,168,.25);
}

.division-menu.open{display:block}
.division-menu button{font-size:13px;color:#88a89a}

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
    color:#d8ead2;
    background:rgba(255,255,255,.03);
}

.hero{
    background:
        linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.012)),
        linear-gradient(120deg,#123028,#0a1f1a);
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
    background:rgba(123,227,168,.06);
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
    color:#a3c3b3;
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
    border-color:rgba(123,227,168,.48);
    background:linear-gradient(180deg,rgba(123,227,168,.07),rgba(255,255,255,.015));
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
    background:rgba(10,31,26,.55);
    border:1px solid var(--line);
    border-left:3px solid var(--gold);
    padding:17px;
    border-radius:16px;
    margin-bottom:12px;
    transition:.25s;
}

.item:hover{border-color:rgba(123,227,168,.45)}
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

.progress{background:rgba(123,227,168,.12);color:var(--gold2)}
.review{background:rgba(255,255,255,.08);color:#e3f0d8}
.done{background:rgba(123,227,168,.12);color:var(--green)}
.danger{background:rgba(255,138,138,.12);color:var(--red)}

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
    color:#d2e6cf;
    border-radius:999px;
    cursor:pointer;
    transition:.25s;
}

.tabs button:hover,
.tabs button.active{
    border-color:rgba(123,227,168,.7);
    background:rgba(123,227,168,.12);
    color:var(--text);
}

.module{display:none}
.module.active{display:block}

.bar{
    height:8px;
    background:#1a3a30;
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

.btn:hover{background:var(--gold);color:#0a1f1a}

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
    background:#2c4a40;
    z-index:1;
}

.timeline-step h3{font-size:17px;margin-bottom:8px;font-weight:500}
.timeline-step small{display:block;margin-bottom:12px}
.timeline-step span{color:var(--gold);font-size:13px}

.completed .circle,
.active-step .circle{
    background:var(--gold);
    color:#0a1f1a;
}

.active-step{
    border-color:rgba(123,227,168,.7);
    background:rgba(123,227,168,.08);
}

.active-step .circle{box-shadow:0 0 0 7px rgba(123,227,168,.13)}
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
    box-shadow:0 0 18px rgba(123,227,168,.16);
}

.gantt-bar.review{background:linear-gradient(90deg,#7aa091,#d8ead2)}
.gantt-bar.donebar{background:linear-gradient(90deg,#65c89a,#b6f0cc)}

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

.legend-dot.review-dot{background:#d8ead2}
.legend-dot.done-dot{background:#b6f0cc}

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

.cash-in{background:linear-gradient(180deg,var(--green),rgba(123,227,168,.35))}
.cash-out{background:linear-gradient(180deg,var(--red),rgba(255,138,138,.30))}

.document-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
}

.doc-card{
    background:rgba(10,31,26,.50);
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

.planning-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
    margin-top:14px;
}

.plan-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
}

.plan-card h3{
    font-size:15px;
    font-weight:500;
    margin-bottom:8px;
}

.plan-value{
    font-size:26px;
    color:var(--gold2);
    margin:8px 0;
}

.variance-good{color:var(--green)!important}
.variance-risk{color:var(--red)!important}

.forecast-line{
    height:180px;
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
    background:
        linear-gradient(to top,rgba(255,255,255,.04) 1px,transparent 1px),
        rgba(255,255,255,.018);
    background-size:100% 36px;
    display:flex;
    align-items:flex-end;
    gap:12px;
    margin-top:14px;
}

.forecast-bar{
    flex:1;
    border-radius:10px 10px 0 0;
    background:linear-gradient(180deg,var(--gold2),rgba(123,227,168,.35));
    position:relative;
}

.forecast-bar span{
    position:absolute;
    bottom:-24px;
    left:50%;
    transform:translateX(-50%);
    color:var(--muted);
    font-size:11px;
}

.scenario-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
}

.scenario-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:20px;
    padding:20px;
}

.scenario-card h3{
    font-size:18px;
    font-weight:500;
    margin-bottom:12px;
}

.scenario-card strong{
    color:var(--gold2);
    font-size:30px;
    font-weight:500;
}

.close-list{
    display:grid;
    gap:12px;
}

.close-row{
    display:grid;
    grid-template-columns:1.5fr .8fr .8fr;
    gap:12px;
    align-items:center;
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:16px;
    padding:16px;
}

.alert-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:14px;
}

.alert-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-left:3px solid var(--red);
    border-radius:18px;
    padding:18px;
}

.alert-card.medium{border-left-color:var(--gold)}
.alert-card.low{border-left-color:var(--green)}

.report-box{
    background:rgba(10,31,26,.55);
    border:1px solid var(--line);
    border-radius:20px;
    padding:24px;
    line-height:1.8;
    color:var(--muted);
}

.report-box strong{
    color:var(--text);
    font-weight:500;
}


/* CONSTRUCTION LIVE DASHBOARD */
.live-grid{
    display:grid;
    grid-template-columns:1.4fr .9fr;
    gap:18px;
    margin-bottom:22px;
}

.activity-feed{
    display:grid;
    gap:12px;
}

.activity-row{
    display:grid;
    grid-template-columns:86px 1fr;
    gap:14px;
    align-items:flex-start;
    background:rgba(10,31,26,.55);
    border:1px solid var(--line);
    border-left:3px solid var(--gold);
    border-radius:16px;
    padding:16px;
}

.activity-time{
    color:var(--gold);
    font-size:12px;
    letter-spacing:.8px;
    text-transform:uppercase;
}

.stage-list{
    display:grid;
    gap:14px;
}

.stage-row{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:16px;
    padding:16px;
}

.stage-head{
    display:flex;
    justify-content:space-between;
    gap:12px;
    margin-bottom:10px;
}

.stage-head span{
    color:var(--muted);
    font-size:13px;
}

.evidence-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:14px;
}

.evidence-card{
    background:rgba(10,31,26,.55);
    border:1px solid var(--line);
    border-radius:18px;
    overflow:hidden;
}

.evidence-thumb{
    height:130px;
    background:
        linear-gradient(135deg,rgba(123,227,168,.25),rgba(255,255,255,.04)),
        radial-gradient(circle at center,rgba(255,255,255,.08),transparent 40%);
    display:flex;
    align-items:center;
    justify-content:center;
    color:var(--gold2);
    font-size:34px;
}

.evidence-body{
    padding:16px;
}

.next-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
}

.next-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
}

.next-card h3{
    font-size:15px;
    font-weight:500;
    margin-bottom:8px;
}

.compare-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.compare-box{
    border:1px solid var(--line);
    border-radius:20px;
    overflow:hidden;
    background:rgba(10,31,26,.50);
}

.compare-image{
    height:220px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:
        linear-gradient(135deg,rgba(123,227,168,.20),rgba(255,255,255,.035)),
        repeating-linear-gradient(45deg,rgba(255,255,255,.03) 0 8px,transparent 8px 16px);
    font-size:42px;
    color:var(--gold2);
}

.compare-box h3{
    padding:16px 16px 4px;
    font-size:18px;
    font-weight:500;
}

.compare-box small{
    display:block;
    padding:0 16px 16px;
}

.weather-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.weather-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:20px;
    padding:22px;
}

.weather-temp{
    font-size:46px;
    color:var(--gold2);
    margin:10px 0;
}

.traffic-grid{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:14px;
}

.traffic-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
}

.traffic-dot{
    width:14px;
    height:14px;
    border-radius:50%;
    display:inline-block;
    margin-right:8px;
    background:var(--green);
}

.traffic-dot.yellow{background:var(--gold)}
.traffic-dot.red{background:var(--red)}

.milestone-hero{
    background:
        linear-gradient(135deg,rgba(123,227,168,.14),rgba(255,255,255,.02)),
        rgba(10,31,26,.50);
    border:1px solid rgba(123,227,168,.30);
    border-radius:24px;
    padding:28px;
}

.milestone-hero h3{
    font-size:26px;
    font-weight:500;
    margin-bottom:10px;
}

/* BIM / API VIEWER MOCKUP */
.viewer-grid{
    display:grid;
    grid-template-columns:1.5fr .8fr;
    gap:18px;
}
.viewer-shell{
    background:#05110e;
    border:1px solid var(--line);
    border-radius:24px;
    overflow:hidden;
    min-height:520px;
    position:relative;
}
.viewer-toolbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:12px;
    padding:14px 16px;
    border-bottom:1px solid var(--line);
    background:rgba(255,255,255,.025);
}
.viewer-actions{
    display:flex;
    gap:8px;
    flex-wrap:wrap;
}
.viewer-actions button,
.api-pill{
    border:1px solid rgba(123,227,168,.32);
    background:rgba(123,227,168,.06);
    color:#d9f5de;
    border-radius:999px;
    padding:8px 11px;
    font-size:12px;
    cursor:pointer;
}
.viewer-actions button:hover{background:rgba(123,227,168,.15)}
.viewer-canvas{
    height:440px;
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
    background:
        radial-gradient(circle at 55% 45%,rgba(123,227,168,.22),transparent 24%),
        linear-gradient(135deg,rgba(140,166,217,.10),rgba(255,255,255,.015)),
        repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 1px,transparent 1px 44px),
        repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 1px,transparent 1px 44px);
}
.model-box{
    width:300px;
    height:230px;
    border:1px solid rgba(224,201,135,.7);
    transform:rotateX(58deg) rotateZ(-36deg);
    transform-style:preserve-3d;
    position:relative;
    box-shadow:0 0 45px rgba(123,227,168,.16);
    background:rgba(123,227,168,.035);
}
.model-box:before,
.model-box:after{
    content:"";
    position:absolute;
    inset:34px;
    border:1px solid rgba(224,201,135,.38);
}
.model-box:after{
    inset:75px;
    border-color:rgba(140,166,217,.45);
}
.model-label{
    position:absolute;
    bottom:22px;
    left:22px;
    color:var(--muted);
    font-size:12px;
    background:rgba(10,31,26,.75);
    border:1px solid var(--line);
    border-radius:12px;
    padding:10px 12px;
}
.viewer-side{
    display:grid;
    gap:14px;
}
.integration-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:20px;
    padding:18px;
}
.integration-card h3{
    font-size:17px;
    font-weight:500;
    margin-bottom:8px;
}
.api-log{
    background:rgba(10,31,26,.70);
    border:1px solid var(--line);
    border-radius:16px;
    padding:16px;
    color:#b9d7c9;
    font-family:Consolas,monospace;
    font-size:12px;
    line-height:1.7;
    white-space:pre-wrap;
}
.connector-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:14px;
    margin-top:16px;
}
.connector-card{
    background:rgba(10,31,26,.50);
    border:1px solid var(--line);
    border-radius:18px;
    padding:18px;
}
.connector-card strong{
    display:block;
    color:var(--gold2);
    margin-bottom:8px;
    font-weight:500;
}


@media(max-width:1000px){
    body{display:block}
    .sidebar{width:100%;height:auto;position:relative}
    .main{margin-left:0;width:100%;padding:22px}
    .grid4,.grid3,.timeline-summary,.cashflow,.document-grid,.planning-grid,.scenario-grid,.alert-grid,.live-grid,.viewer-grid,.connector-grid,.evidence-grid,.next-grid,.compare-grid,.weather-grid,.traffic-grid{grid-template-columns:1fr}
    .grid2{grid-template-columns:1fr}
    .close-row{grid-template-columns:1fr}
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
                <p>Financial Control Center, FP&A, budget vs actual, forecast, escenarios, impuestos y cierre mensual.</p>
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
        <h2>Built environment delivery with live project visibility.</h2>
        <p>Portal de obra para visualizar avance, evidencias, bitácora, cronograma, hitos, visitas, cambios y documentación del proyecto.</p>
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
        <p>Financial Control Center inspirado en flujos FP&A/EPM: dashboard financiero, budget vs actual, forecast, escenarios, cash flow, impuestos, cierre mensual, consolidación y reporte ejecutivo.</p>

        <div class="tabs">
            <button class="active" onclick="showModule('finance-summary', this)">Resumen Financiero</button>
            <button onclick="showModule('finance-budget', this)">Budget vs Actual</button>
            <button onclick="showModule('finance-forecast', this)">Forecast</button>
            <button onclick="showModule('finance-scenarios', this)">Escenarios</button>
            <button onclick="showModule('finance-income', this)">Estado de Resultados</button>
            <button onclick="showModule('finance-cashflow', this)">Cash Flow</button>
            <button onclick="showModule('finance-arap', this)">CxC / CxP</button>
            <button onclick="showModule('finance-taxes', this)">Impuestos</button>
            <button onclick="showModule('finance-kpis', this)">KPIs Financieros</button>
            <button onclick="showModule('finance-close', this)">Cierre Mensual</button>
            <button onclick="showModule('finance-consolidation', this)">Consolidación</button>
            <button onclick="showModule('finance-alerts', this)">Alertas</button>
            <button onclick="showModule('finance-report', this)">Reporte Ejecutivo</button>
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


        <div id="finance-budget" class="module">
            <div class="item">
                <h3>Budget vs Actual</h3>
                <small>Comparación entre presupuesto aprobado, ejecución real y variación para detectar desviaciones.</small>
            </div>

            <div class="planning-grid">
                <div class="plan-card"><h3>Ingresos</h3><div class="plan-value">+RD$180K</div><small>Real sobre presupuesto</small><p class="variance-good">+8.1%</p></div>
                <div class="plan-card"><h3>Costos Directos</h3><div class="plan-value">+RD$65K</div><small>Sobre presupuesto</small><p class="variance-risk">+7.6%</p></div>
                <div class="plan-card"><h3>Gastos Operativos</h3><div class="plan-value">-RD$22K</div><small>Debajo del presupuesto</small><p class="variance-good">-4.0%</p></div>
                <div class="plan-card"><h3>Utilidad Neta</h3><div class="plan-value">+RD$95K</div><small>Mejor que plan</small><p class="variance-good">+13.1%</p></div>
            </div>

            <table class="finance-table" style="margin-top:22px">
                <thead><tr><th>Partida</th><th>Presupuesto</th><th>Actual</th><th>Variación</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td><strong>Ingresos</strong></td><td>RD$2,220,000</td><td>RD$2,400,000</td><td class="trend-up">+RD$180,000</td><td><span class="status done">Favorable</span></td></tr>
                    <tr><td><strong>Costos Directos</strong></td><td>RD$855,000</td><td>RD$920,000</td><td class="trend-down">+RD$65,000</td><td><span class="status review">Atención</span></td></tr>
                    <tr><td><strong>Gastos Operativos</strong></td><td>RD$552,000</td><td>RD$530,000</td><td class="trend-up">-RD$22,000</td><td><span class="status done">Controlado</span></td></tr>
                    <tr><td><strong>Utilidad Neta</strong></td><td>RD$725,000</td><td>RD$820,000</td><td class="trend-up">+RD$95,000</td><td><span class="status done">Favorable</span></td></tr>
                </tbody>
            </table>
        </div>

        <div id="finance-forecast" class="module">
            <div class="item">
                <h3>Forecast Financiero</h3>
                <small>Proyección de ingresos, gastos, utilidad neta y caja para los próximos meses.</small>
            </div>

            <div class="grid3">
                <div class="widget"><h3>Revenue Forecast</h3><strong>RD$15.8M</strong><p>Proyección próximos 6 meses.</p></div>
                <div class="widget"><h3>Cash Forecast</h3><strong>RD$4.2M</strong><p>Caja estimada al cierre.</p></div>
                <div class="widget"><h3>Net Profit Forecast</h3><strong>RD$5.1M</strong><p>Utilidad neta proyectada.</p></div>
            </div>

            <div class="forecast-line">
                <div class="forecast-bar" style="height:55%"><span>Jul</span></div>
                <div class="forecast-bar" style="height:62%"><span>Ago</span></div>
                <div class="forecast-bar" style="height:68%"><span>Sep</span></div>
                <div class="forecast-bar" style="height:74%"><span>Oct</span></div>
                <div class="forecast-bar" style="height:82%"><span>Nov</span></div>
                <div class="forecast-bar" style="height:88%"><span>Dic</span></div>
            </div>
        </div>

        <div id="finance-scenarios" class="module">
            <div class="item">
                <h3>Scenario Planning</h3>
                <small>Comparación de escenarios conservador, base y optimista para anticipar impactos en utilidad y caja.</small>
            </div>

            <div class="scenario-grid">
                <div class="scenario-card">
                    <h3>Conservador</h3>
                    <strong>RD$620K</strong>
                    <p>Utilidad neta esperada con menor crecimiento y cobros más lentos.</p>
                    <span class="status review">Riesgo medio</span>
                </div>

                <div class="scenario-card">
                    <h3>Base</h3>
                    <strong>RD$820K</strong>
                    <p>Escenario actual con ejecución estable y margen positivo.</p>
                    <span class="status progress">Escenario activo</span>
                </div>

                <div class="scenario-card">
                    <h3>Optimista</h3>
                    <strong>RD$1.05M</strong>
                    <p>Mayor facturación, mejor cobranza y control operativo.</p>
                    <span class="status done">Alto potencial</span>
                </div>
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


        <div id="finance-close" class="module">
            <div class="item">
                <h3>Cierre Mensual</h3>
                <small>Checklist operativo para controlar el cierre contable, fiscal y financiero.</small>
            </div>

            <div class="close-list">
                <div class="close-row"><div><strong>Conciliación bancaria</strong><br><small>Validación de movimientos y balances.</small></div><span class="status done">Completado</span><small>18 Jun</small></div>
                <div class="close-row"><div><strong>Facturas emitidas y recibidas</strong><br><small>Revisión de NCF, soportes y registros.</small></div><span class="status progress">En proceso</span><small>20 Jun</small></div>
                <div class="close-row"><div><strong>ITBIS y retenciones</strong><br><small>Preparación de obligaciones fiscales.</small></div><span class="status review">Pendiente</span><small>20 Jun</small></div>
                <div class="close-row"><div><strong>Estados financieros</strong><br><small>Generación de reportes para dirección.</small></div><span class="status review">Pendiente</span><small>25 Jun</small></div>
            </div>
        </div>

        <div id="finance-consolidation" class="module">
            <div class="item">
                <h3>Consolidación Financiera</h3>
                <small>Vista resumida por división para entender desempeño financiero del ecosistema Gradum.</small>
            </div>

            <table class="finance-table">
                <thead><tr><th>División</th><th>Ingresos</th><th>Gastos</th><th>Utilidad</th><th>Margen</th></tr></thead>
                <tbody>
                    <tr><td><strong>Services</strong></td><td>RD$2.4M</td><td>RD$1.6M</td><td>RD$820K</td><td class="trend-up">34%</td></tr>
                    <tr><td><strong>Construction</strong></td><td>RD$8.9M</td><td>RD$7.1M</td><td>RD$1.8M</td><td class="trend-up">20%</td></tr>
                    <tr><td><strong>Consulting</strong></td><td>RD$1.7M</td><td>RD$820K</td><td>RD$880K</td><td class="trend-up">52%</td></tr>
                    <tr><td><strong>Ventures</strong></td><td>RD$450K</td><td>RD$620K</td><td>-RD$170K</td><td class="trend-down">Inversión</td></tr>
                </tbody>
            </table>
        </div>

        <div id="finance-alerts" class="module">
            <div class="alert-grid">
                <div class="alert-card">
                    <h3>Factura vencida</h3>
                    <small>Cliente B tiene RD$185,000 vencidos desde hace 12 días.</small><br>
                    <span class="status danger">Alta prioridad</span>
                </div>
                <div class="alert-card medium">
                    <h3>ITBIS próximo</h3>
                    <small>Fecha límite fiscal cercana. Validar comprobantes y retenciones.</small><br>
                    <span class="status review">Media</span>
                </div>
                <div class="alert-card low">
                    <h3>Margen saludable</h3>
                    <small>Margen neto actual por encima del escenario base.</small><br>
                    <span class="status done">Positivo</span>
                </div>
            </div>
        </div>

        <div id="finance-report" class="module">
            <div class="report-box">
                <h3 style="color:var(--text);margin-bottom:12px">Reporte Ejecutivo Automático</h3>
                <p>
                    Durante el período actual, <strong>los ingresos alcanzaron RD$2.4M</strong>, representando un crecimiento de <strong>17.1%</strong> frente al período anterior.
                    La utilidad neta se ubicó en <strong>RD$820K</strong>, con un margen neto aproximado de <strong>34%</strong>.
                    El flujo de caja se mantiene positivo, con una proyección neta de <strong>RD$800K</strong>.
                    Se recomienda priorizar la gestión de cobro de facturas vencidas, validar el cierre fiscal antes del día 20 y mantener seguimiento al presupuesto de costos directos.
                </p>
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
            ${division === 'construction' ? `
                <button onclick="showModule('${id}-live', this)">Obra en Vivo</button>
                <button onclick="showModule('${id}-viewer', this)">Visualizador 3D / API</button>
                <button onclick="showModule('${id}-evidence', this)">Evidencias</button>
                <button onclick="showModule('${id}-progressmap', this)">Mapa de Avance</button>
                <button onclick="showModule('${id}-next7', this)">Próximos 7 Días</button>
                <button onclick="showModule('${id}-compare', this)">Diseño vs Actual</button>
                <button onclick="showModule('${id}-weather', this)">Clima</button>
                <button onclick="showModule('${id}-health', this)">Semáforo</button>
            ` : ``}
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


        ${division === 'construction' ? `
        <div id="${id}-live" class="module">
            <div class="live-grid">
                <div class="panel">
                    <div class="eyebrow">Live Activity Feed</div>
                    <h2>Actividad reciente de obra</h2>
                    <p>Bitácora ejecutiva para que el cliente vea movimientos recientes del proyecto.</p>

                    <div class="activity-feed" style="margin-top:18px">
                        <div class="activity-row"><div class="activity-time">Hoy · 9:15</div><div><h3>Armado de acero completado</h3><small>Equipo estructural completó armado en zona de columnas principales.</small></div></div>
                        <div class="activity-row"><div class="activity-time">Hoy · 11:40</div><div><h3>Llegada de materiales</h3><small>Recepción de cemento, acero y agregados para próxima actividad.</small></div></div>
                        <div class="activity-row"><div class="activity-time">Hoy · 3:20</div><div><h3>Supervisión técnica realizada</h3><small>Revisión de alineación, seguridad y avance físico del frente activo.</small></div></div>
                        <div class="activity-row"><div class="activity-time">Ayer · 4:10</div><div><h3>Área liberada para próxima fase</h3><small>Zona preparada para inicio de mampostería y trabajos complementarios.</small></div></div>
                    </div>
                </div>

                <div class="panel">
                    <div class="eyebrow">Milestone</div>
                    <div class="milestone-hero">
                        <h3>🏆 Hito alcanzado</h3>
                        <p>Cimentación completada y validada por supervisión técnica.</p>
                        <span class="status done">Completado · 12 Jun</span>
                    </div>

                    <div class="item" style="margin-top:16px">
                        <h3>Próximo hito</h3>
                        <small>Inicio de mampostería y cierre de fase estructural parcial.</small><br>
                        <span class="status progress">Programado</span>
                    </div>
                </div>
            </div>
        </div>


        <div id="${id}-viewer" class="module">
            <div class="item">
                <h3>Visualizador 3D integrado por API</h3>
                <small>Ejemplo de cómo Gradum Portal puede mostrar un modelo BIM/3D sin construir un motor propio. En producción este espacio puede usar Autodesk Platform Services Viewer, That Open / IFC.js o Speckle Viewer.</small>
            </div>

            <div class="viewer-grid">
                <div class="viewer-shell">
                    <div class="viewer-toolbar">
                        <div>
                            <span class="api-pill" id="${id}-viewerSource">Autodesk APS Viewer</span>
                        </div>
                        <div class="viewer-actions">
                            <button onclick="setViewerSource('${id}','Autodesk APS Viewer')">Autodesk</button>
                            <button onclick="setViewerSource('${id}','IFC.js / That Open')">IFC</button>
                            <button onclick="setViewerSource('${id}','Speckle Viewer')">Speckle</button>
                            <button onclick="setViewerMode('${id}','Sección')">Sección</button>
                            <button onclick="setViewerMode('${id}','Medición')">Medición</button>
                            <button onclick="setViewerMode('${id}','Markup')">Markup</button>
                        </div>
                    </div>
                    <div class="viewer-canvas">
                        <div class="model-box"></div>
                        <div class="model-label" id="${id}-viewerMode">
                            Modelo: Casa / Local Comercial · Nivel 01<br>
                            Modo activo: Navegación 3D<br>
                            Estado: sincronizado con documentos y avance.
                        </div>
                    </div>
                </div>

                <div class="viewer-side">
                    <div class="integration-card">
                        <div class="eyebrow">Modelo conectado</div>
                        <h3>Modelo BIM / IFC</h3>
                        <p>Archivo fuente: <strong style="font-size:16px">Proyecto_Gradum.ifc</strong></p>
                        <small>Última revisión: V03 · Coordinación arquitectónica y estructural.</small>
                        <br><span class="status done">Modelo actualizado</span>
                    </div>

                    <div class="integration-card">
                        <div class="eyebrow">Documentos vinculados</div>
                        <h3>Planos relacionados</h3>
                        <small>ARQ-MIVED-V03.pdf · Estructural-V02.pdf · Constructivo-Interno-V04.pdf</small>
                        <br><span class="status progress">3 documentos enlazados</span>
                    </div>

                    <div class="integration-card">
                        <div class="eyebrow">Datos del proyecto</div>
                        <h3>Planificado vs ejecutado</h3>
                        <p>El modelo se puede combinar con fotos, reportes, hitos y avance por zona.</p>
                        <div class="bar"><div class="fill" style="width:62%"></div></div>
                        <small>Avance físico vinculado: 62%</small>
                    </div>
                </div>
            </div>

            <div class="connector-grid">
                <div class="connector-card">
                    <strong>Autodesk APS</strong>
                    <small>Para Revit, DWG, Navisworks, modelos 2D/3D, mediciones, secciones y markups embebidos en el portal.</small>
                </div>
                <div class="connector-card">
                    <strong>That Open / IFC.js</strong>
                    <small>Para un visor propio basado en IFC, útil para MVP y menor dependencia de licencias externas.</small>
                </div>
                <div class="connector-card">
                    <strong>Speckle</strong>
                    <small>Para colaboración BIM, versiones, datos del modelo, automatizaciones y conexión con flujos AEC.</small>
                </div>
            </div>

            <div class="panel" style="margin-top:18px">
                <div class="eyebrow">Ejemplo técnico</div>
                <h2>Flujo API recomendado</h2>
                <div class="api-log" id="${id}-apiLog">1. Gradum Portal solicita token seguro al backend.
2. Backend conecta con Autodesk APS / Speckle / almacenamiento IFC.
3. Se carga el modelo en el viewer embebido.
4. El portal cruza modelo + documentos + fotos + avance + incidencias.
5. El cliente ve una experiencia simple, aunque el motor técnico esté por detrás.</div>
            </div>
        </div>

        <div id="${id}-evidence" class="module">
            <div class="item">
                <h3>Centro de Evidencias</h3>
                <small>Fotos, videos y registros visuales organizados por semana para documentar el avance real.</small>
            </div>

            <div class="evidence-grid">
                <div class="evidence-card"><div class="evidence-thumb">📷</div><div class="evidence-body"><h3>Semana 1</h3><small>24 fotos · 2 videos · Excavación e inicio de obra.</small><br><span class="status done">Ver evidencias</span></div></div>
                <div class="evidence-card"><div class="evidence-thumb">🎥</div><div class="evidence-body"><h3>Semana 2</h3><small>31 fotos · 1 video · Cimentación y acero.</small><br><span class="status done">Ver evidencias</span></div></div>
                <div class="evidence-card"><div class="evidence-thumb">📸</div><div class="evidence-body"><h3>Semana 3</h3><small>18 fotos · 4 videos · Muros y preparación.</small><br><span class="status progress">Actualizado hoy</span></div></div>
            </div>
        </div>

        <div id="${id}-progressmap" class="module">
            <div class="item">
                <h3>Mapa de Avance por Etapas</h3>
                <small>Visualización clara del avance físico por componente de obra.</small>
            </div>

            <div class="stage-list">
                <div class="stage-row"><div class="stage-head"><h3>Cimentación</h3><span>100%</span></div><div class="bar"><div class="fill" style="width:100%"></div></div><span class="status done">Completado</span></div>
                <div class="stage-row"><div class="stage-head"><h3>Estructura</h3><span>80%</span></div><div class="bar"><div class="fill" style="width:80%"></div></div><span class="status progress">En progreso</span></div>
                <div class="stage-row"><div class="stage-head"><h3>Mampostería</h3><span>50%</span></div><div class="bar"><div class="fill" style="width:50%"></div></div><span class="status progress">Activo</span></div>
                <div class="stage-row"><div class="stage-head"><h3>Instalaciones</h3><span>20%</span></div><div class="bar"><div class="fill" style="width:20%"></div></div><span class="status review">Inicial</span></div>
                <div class="stage-row"><div class="stage-head"><h3>Terminaciones</h3><span>0%</span></div><div class="bar"><div class="fill" style="width:0%"></div></div><span class="status review">Pendiente</span></div>
            </div>
        </div>

        <div id="${id}-next7" class="module">
            <div class="item">
                <h3>Próximos 7 días</h3>
                <small>Plan inmediato de obra para dar visibilidad al cliente sobre lo que ocurrirá en el corto plazo.</small>
            </div>

            <div class="next-grid">
                <div class="next-card"><div class="eyebrow">17 Jun</div><h3>Colado de columnas</h3><small>Actividad estructural programada.</small><br><span class="status progress">Programado</span></div>
                <div class="next-card"><div class="eyebrow">19 Jun</div><h3>Inicio de mampostería</h3><small>Primer frente de muros interiores.</small><br><span class="status review">Por iniciar</span></div>
                <div class="next-card"><div class="eyebrow">21 Jun</div><h3>Inspección técnica</h3><small>Revisión de calidad y seguridad.</small><br><span class="status progress">Confirmado</span></div>
                <div class="next-card"><div class="eyebrow">24 Jun</div><h3>Entrega de materiales</h3><small>Recepción de blocks y agregados.</small><br><span class="status review">Pendiente</span></div>
            </div>
        </div>

        <div id="${id}-compare" class="module">
            <div class="item">
                <h3>Diseño Original vs Estado Actual</h3>
                <small>Comparación visual para que el cliente entienda la relación entre lo planificado y lo ejecutado.</small>
            </div>

            <div class="compare-grid">
                <div class="compare-box"><div class="compare-image">🏗️</div><h3>Diseño / Render</h3><small>Referencia visual aprobada para ejecución.</small></div>
                <div class="compare-box"><div class="compare-image">📷</div><h3>Estado Actual</h3><small>Registro fotográfico más reciente de la obra.</small></div>
            </div>
        </div>

        <div id="${id}-weather" class="module">
            <div class="weather-grid">
                <div class="weather-card">
                    <div class="eyebrow">Condiciones de obra</div>
                    <h3>Clima actual</h3>
                    <div class="weather-temp">30°C</div>
                    <p>Soleado · Viento 8 km/h · Probabilidad de lluvia baja.</p>
                    <span class="status done">Impacto normal</span>
                </div>

                <div class="weather-card">
                    <div class="eyebrow">Impacto operativo</div>
                    <h3>Evaluación del día</h3>
                    <p>Las condiciones permiten continuar actividades exteriores y trabajos de estructura sin impacto relevante en cronograma.</p>
                    <div class="bar"><div class="fill" style="width:88%"></div></div>
                    <span class="status done">Operación estable</span>
                </div>
            </div>
        </div>

        <div id="${id}-health" class="module">
            <div class="item">
                <h3>Semáforo del Proyecto</h3>
                <small>Lectura ejecutiva rápida sobre el estado general de obra.</small>
            </div>

            <div class="traffic-grid">
                <div class="traffic-card"><h3><span class="traffic-dot"></span>Cronograma</h3><small>Dentro del plan.</small></div>
                <div class="traffic-card"><h3><span class="traffic-dot"></span>Presupuesto</h3><small>Sin desviaciones críticas.</small></div>
                <div class="traffic-card"><h3><span class="traffic-dot"></span>Calidad</h3><small>Validaciones conformes.</small></div>
                <div class="traffic-card"><h3><span class="traffic-dot yellow"></span>Riesgos</h3><small>Materiales en seguimiento.</small></div>
                <div class="traffic-card"><h3><span class="traffic-dot"></span>Seguridad</h3><small>Sin incidentes reportados.</small></div>
            </div>
        </div>
        ` : ``}

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


function setViewerSource(id, source){
    const sourceEl = document.getElementById(id + "-viewerSource");
    const logEl = document.getElementById(id + "-apiLog");

    if(sourceEl){ sourceEl.textContent = source; }

    if(logEl){
        logEl.textContent =
`Conector activo: ${source}

Ejemplo de integración:
- Gradum Portal mantiene la experiencia del cliente.
- El viewer externo renderiza el modelo 3D/BIM.
- El backend protege tokens, permisos y credenciales.
- La base de datos Gradum relaciona modelo, planos, fotos, incidencias y reportes.

Nota MVP:
Esto es una simulación visual. En producción aquí se monta el SDK/API real del proveedor.`;
    }
}

function setViewerMode(id, mode){
    const modeEl = document.getElementById(id + "-viewerMode");

    if(modeEl){
        modeEl.innerHTML =
`Modelo: Casa / Local Comercial · Nivel 01<br>
Modo activo: ${mode}<br>
Estado: herramienta simulada lista para integrarse vía API.`;
    }
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
