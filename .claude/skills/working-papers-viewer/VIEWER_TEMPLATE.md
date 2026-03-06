# Working Papers Viewer - Template Resources

This file contains the complete templates for generating HTML viewers and batch files for Form C tax computation working papers.

---

## Section 1: tax_viewer.html Template

The complete HTML template for the tax working papers viewer. This file should be saved as `tax_viewer.html` in the root of each tax computation folder.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[CLIENT NAME] - Tax Working Papers Viewer</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; height: 100vh; overflow: hidden; background: #f5f5f5; }
        #nav-panel { width: 320px; background: #1e293b; color: #e2e8f0; overflow-y: auto; display: flex; flex-direction: column; }
        #nav-header { background: #0f172a; padding: 16px 20px; border-bottom: 1px solid #334155; display: flex; align-items: center; gap: 14px; }
        #nav-header img { width: 50px; height: 50px; object-fit: contain; }
        #nav-header .header-text { flex: 1; }
        #nav-header h1 { font-size: 14px; font-weight: 600; color: #60a5fa; margin-bottom: 4px; }
        #nav-header h2 { font-size: 11px; font-weight: 400; color: #94a3b8; }
        #search-box { padding: 12px 16px; background: #0f172a; }
        #search-input { width: 100%; padding: 8px 12px; background: #1e293b; border: 1px solid #334155; border-radius: 6px; color: #e2e8f0; font-size: 13px; }
        #search-input:focus { outline: none; border-color: #60a5fa; }
        #download-all-btn { margin: 12px 16px; padding: 10px 16px; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s; }
        #download-all-btn:hover { background: linear-gradient(135deg, #059669 0%, #047857 100%); transform: translateY(-1px); }
        #download-all-btn:disabled { background: #6b7280; cursor: not-allowed; transform: none; }
        #nav-content { flex: 1; overflow-y: auto; }
        .nav-section { border-bottom: 1px solid #334155; }
        .nav-section-header { display: flex; align-items: center; padding: 12px 16px; cursor: pointer; background: #1e293b; transition: background 0.2s; }
        .nav-section-header:hover { background: #334155; }
        .nav-section-header .icon { width: 24px; height: 24px; margin-right: 10px; display: flex; align-items: center; justify-content: center; background: #374151; border-radius: 4px; color: #60a5fa; font-weight: 600; font-size: 11px; }
        .nav-section-header .title { flex: 1; font-size: 13px; font-weight: 500; }
        .nav-section-header .arrow { font-size: 10px; transition: transform 0.2s; color: #64748b; }
        .nav-section.expanded .arrow { transform: rotate(90deg); }
        .nav-section-items { display: none; background: #0f172a; }
        .nav-section.expanded .nav-section-items { display: block; }
        .nav-item { padding: 8px 16px 8px 50px; cursor: pointer; font-size: 12px; color: #94a3b8; transition: all 0.2s; border-left: 3px solid transparent; }
        .nav-item:hover { background: #1e293b; color: #e2e8f0; }
        .nav-item.active { background: #1e40af; color: #fff; border-left-color: #60a5fa; }
        #stats-bar { padding: 8px 16px; background: #0f172a; border-top: 1px solid #334155; font-size: 11px; color: #64748b; }
        #resizer { width: 4px; background: #334155; cursor: col-resize; }
        #resizer:hover { background: #60a5fa; }
        #preview-panel { flex: 1; display: flex; flex-direction: column; background: #fff; overflow: hidden; }
        #preview-header { padding: 16px 24px; background: #fff; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; gap: 12px; }
        #preview-header .breadcrumb { font-size: 12px; color: #64748b; }
        #preview-header .filename { font-size: 16px; font-weight: 600; color: #1e293b; }
        #preview-content { flex: 1; overflow-y: auto; padding: 24px 40px; }
        #preview-content h1 { font-size: 28px; font-weight: 700; color: #1e293b; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 2px solid #e2e8f0; }
        #preview-content h2 { font-size: 22px; font-weight: 600; color: #334155; margin: 28px 0 12px; }
        #preview-content h3 { font-size: 18px; font-weight: 600; color: #475569; margin: 24px 0 10px; }
        #preview-content p { font-size: 14px; line-height: 1.7; color: #475569; margin-bottom: 12px; }
        #preview-content ul, #preview-content ol { margin: 12px 0 12px 24px; color: #475569; }
        #preview-content li { font-size: 14px; line-height: 1.7; margin-bottom: 4px; }
        #preview-content table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; }
        #preview-content th { background: #f1f5f9; padding: 10px 12px; text-align: left; font-weight: 600; color: #334155; border: 1px solid #e2e8f0; }
        #preview-content td { padding: 10px 12px; border: 1px solid #e2e8f0; color: #475569; }
        #preview-content tr:hover td { background: #f8fafc; }
        #preview-content code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-family: Consolas, Monaco, monospace; font-size: 13px; color: #e11d48; }
        #preview-content pre { background: #1e293b; padding: 16px; border-radius: 8px; overflow-x: auto; margin: 16px 0; }
        #preview-content pre code { background: none; color: #e2e8f0; padding: 0; }
        #preview-content hr { border: none; border-top: 1px solid #e2e8f0; margin: 24px 0; }
        #preview-content strong { font-weight: 600; color: #1e293b; }
        .welcome { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; color: #64748b; text-align: center; }
        .welcome h2 { font-size: 24px; color: #334155; margin-bottom: 12px; }
        @media print { #nav-panel, #resizer { display: none; } #preview-panel { width: 100%; } }
    </style>
</head>
<body>
    <div id="nav-panel">
        <div id="nav-header">
            <img src="YYC_Logo_white.webp" alt="YYC Logo">
            <div class="header-text">
                <h1>[CLIENT NAME]</h1>
                <h2>YA [YEAR] - Tax Working Papers</h2>
            </div>
        </div>
        <div id="search-box">
            <input type="text" id="search-input" placeholder="Search files... (Ctrl+F)">
        </div>
        <button id="download-all-btn" onclick="downloadAllDocuments()">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/>
            </svg>
            Download All Working Papers
        </button>
        <div id="nav-content"></div>
        <div id="stats-bar">Loading...</div>
    </div>
    <div id="resizer"></div>
    <div id="preview-panel">
        <div id="preview-header">
            <span class="breadcrumb">Select a file from the navigation</span>
            <span class="filename"></span>
        </div>
        <div id="preview-content">
            <div class="welcome">
                <h2>Form C Tax Computation Viewer</h2>
                <p>Select a document from the navigation panel to preview.</p>
            </div>
        </div>
    </div>
<script>
// UPDATE sections array based on actual files created
var sections = [
    {id: "01_TAX_COMPUTATION", icon: "TC", title: "01 - Tax Computation (MAIN)", files: [
        {name: "TC_01_Cover_Page.md", display: "TC 01 - Cover Page"},
        {name: "TC_02_Main_Tax_Computation.md", display: "TC 02 - Main Tax Computation"},
        {name: "TC_03_Tax_Summary.md", display: "TC 03 - Tax Summary"},
        {name: "TC_04_CP204_Comparison.md", display: "TC 04 - CP204 Comparison"}
    ]},
    {id: "02_ANALYSIS_OF_ACCOUNTS", icon: "A", title: "02 - Analysis of Accounts (Sch A)", files: [
        {name: "AA_01_Analysis_Summary.md", display: "AA 01 - Analysis Summary"},
        {name: "AA_02_Revenue_Analysis.md", display: "AA 02 - Revenue Analysis"},
        {name: "AA_03_Expenditure_Analysis.md", display: "AA 03 - Expenditure Analysis"},
        {name: "AA_04_Add_Back_Schedule.md", display: "AA 04 - Add Back Schedule"},
        {name: "AA_05_Non_Taxable_Income.md", display: "AA 05 - Non-Taxable Income"},
        {name: "AA_06_Reconciliation.md", display: "AA 06 - Reconciliation"}
    ]},
    {id: "03_CAPITAL_ALLOWANCE", icon: "B", title: "03 - Capital Allowance (Sch B)", files: [
        {name: "CA_01_CA_Summary.md", display: "CA 01 - CA Summary"},
        {name: "CA_02_Plant_Machinery.md", display: "CA 02 - Plant & Machinery"},
        {name: "CA_03_Motor_Vehicles.md", display: "CA 03 - Motor Vehicles"},
        {name: "CA_04_Office_Equipment.md", display: "CA 04 - Office Equipment"},
        {name: "CA_05_Computer_Equipment.md", display: "CA 05 - Computer Equipment"},
        {name: "CA_06_Small_Value_Assets.md", display: "CA 06 - Small Value Assets"},
        {name: "CA_07_Balancing_Adjustment.md", display: "CA 07 - Balancing Adjustment"},
        {name: "CA_08_CA_Brought_Forward.md", display: "CA 08 - CA Brought Forward"}
    ]},
    {id: "04_DIRECTORS_DETAILS", icon: "C", title: "04 - Directors Details (Sch C)", files: [
        {name: "DD_01_Directors_Particulars.md", display: "DD 01 - Directors Particulars"},
        {name: "DD_02_Directors_Remuneration.md", display: "DD 02 - Directors Remuneration"},
        {name: "DD_03_Directors_Interest.md", display: "DD 03 - Directors Interest in Shares"}
    ]},
    {id: "05_SHAREHOLDERS_DETAILS", icon: "D", title: "05 - Shareholders Details (Sch D)", files: [
        {name: "SH_01_Share_Capital_Info.md", display: "SH 01 - Share Capital Information"},
        {name: "SH_02_Shareholders_List.md", display: "SH 02 - Shareholders List"},
        {name: "SH_03_Corporate_Shareholders.md", display: "SH 03 - Corporate Shareholders"},
        {name: "SH_04_SME_Status_Verification.md", display: "SH 04 - SME Status Verification"}
    ]},
    {id: "06_BENEFICIAL_OWNERSHIP", icon: "E", title: "06 - Beneficial Ownership (Sch E)", files: [
        {name: "BO_01_Beneficial_Owners_List.md", display: "BO 01 - Beneficial Owners List"},
        {name: "BO_02_Ownership_Structure.md", display: "BO 02 - Ownership Structure Chart"},
        {name: "BO_03_Declaration.md", display: "BO 03 - Declaration"}
    ]},
    {id: "07_PBC_QUERY", icon: "P", title: "07 - PBC & Query", files: [
        {name: "PBC_01_Document_Checklist.md", display: "PBC 01 - Document Checklist"},
        {name: "PBC_02_Outstanding_Items.md", display: "PBC 02 - Outstanding Items"},
        {name: "QRY_01_Query_List.md", display: "QRY 01 - Query List"},
        {name: "QRY_02_Query_Response.md", display: "QRY 02 - Query Response"}
    ]},
    {id: "08_SUPPORTING_WORKINGS", icon: "S", title: "08 - Supporting Workings", files: [
        {name: "SW_01_Depreciation_vs_CA.md", display: "SW 01 - Depreciation vs CA"},
        {name: "SW_02_Entertainment_50_Percent.md", display: "SW 02 - Entertainment 50%"},
        {name: "SW_03_Motor_Vehicle_Restriction.md", display: "SW 03 - Motor Vehicle Restriction"},
        {name: "SW_04_Bad_Debts_Analysis.md", display: "SW 04 - Bad Debts Analysis"},
        {name: "SW_05_Donations_Approved.md", display: "SW 05 - Approved Donations"},
        {name: "SW_06_Related_Party_Trans.md", display: "SW 06 - Related Party Trans"},
        {name: "SW_07_Losses_BF_Utilization.md", display: "SW 07 - Losses B/F Utilization"},
        {name: "SW_08_WHT_Summary.md", display: "SW 08 - Withholding Tax Summary"}
    ]},
    {id: "09_PRIOR_YEAR_REFERENCE", icon: "PY", title: "09 - Prior Year Reference", files: [
        {name: "PY_01_Prior_Year_Tax_Comp.md", display: "PY 01 - Prior Year Tax Computation"},
        {name: "PY_02_Prior_Year_CA.md", display: "PY 02 - Prior Year CA Schedule"}
    ]}
];
var allFiles = [];
var navContent = document.getElementById('nav-content');
var totalFiles = 0;
sections.forEach(function(sec) {
    var section = document.createElement('div');
    section.className = 'nav-section';
    section.setAttribute('data-folder', sec.id);
    var header = document.createElement('div');
    header.className = 'nav-section-header';
    header.innerHTML = '<span class="icon">' + sec.icon + '</span><span class="title">' + sec.title + '</span><span class="arrow">&#9658;</span>';
    header.onclick = function() { section.classList.toggle('expanded'); };
    var items = document.createElement('div');
    items.className = 'nav-section-items';
    sec.files.forEach(function(file) {
        var item = document.createElement('div');
        item.className = 'nav-item';
        item.textContent = file.display;
        item.setAttribute('data-folder', sec.id);
        item.setAttribute('data-file', file.name);
        item.onclick = function() { loadFile(sec.id, file.name, file.display); };
        items.appendChild(item);
        allFiles.push({folder: sec.id, name: file.name, display: file.display, element: item});
        totalFiles++;
    });
    section.appendChild(header);
    section.appendChild(items);
    navContent.appendChild(section);
});
document.getElementById('stats-bar').textContent = totalFiles + ' documents in ' + sections.length + ' sections';
document.querySelector('.nav-section').classList.add('expanded');
function loadFile(folder, filename, displayName) {
    document.querySelectorAll('.nav-item').forEach(function(item) { item.classList.remove('active'); });
    var activeItem = document.querySelector('.nav-item[data-folder="' + folder + '"][data-file="' + filename + '"]');
    if (activeItem) activeItem.classList.add('active');
    var section = document.querySelector('.nav-section[data-folder="' + folder + '"]');
    if (section) section.classList.add('expanded');
    document.getElementById('preview-header').innerHTML = '<span class="breadcrumb">' + folder + ' /</span><span class="filename">' + displayName + '</span>';
    document.getElementById('preview-content').innerHTML = '<div class="welcome"><p>Loading...</p></div>';
    fetch(folder + '/' + filename)
        .then(function(response) { if (!response.ok) throw new Error('File not found'); return response.text(); })
        .then(function(markdown) { document.getElementById('preview-content').innerHTML = marked.parse(markdown); })
        .catch(function(error) { document.getElementById('preview-content').innerHTML = '<div class="welcome"><h2>Cannot Load File</h2><p>Run START_VIEWER.bat to view files.</p></div>'; });
}
document.getElementById('search-input').addEventListener('input', function(e) {
    var query = e.target.value.toLowerCase();
    allFiles.forEach(function(file) {
        var matches = file.display.toLowerCase().includes(query) || file.name.toLowerCase().includes(query);
        file.element.style.display = matches ? '' : 'none';
    });
    if (query) { document.querySelectorAll('.nav-section').forEach(function(section) { var hasVisible = section.querySelectorAll('.nav-item:not([style*="display: none"])').length > 0; if (hasVisible) section.classList.add('expanded'); }); }
});
var resizer = document.getElementById('resizer');
var navPanel = document.getElementById('nav-panel');
var isResizing = false;
resizer.onmousedown = function() { isResizing = true; document.body.style.cursor = 'col-resize'; };
document.onmousemove = function(e) { if (isResizing && e.clientX > 200 && e.clientX < 500) navPanel.style.width = e.clientX + 'px'; };
document.onmouseup = function() { isResizing = false; document.body.style.cursor = ''; };
document.onkeydown = function(e) { if (e.key === 'f' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); document.getElementById('search-input').focus(); } };
async function downloadAllDocuments() {
    var btn = document.getElementById('download-all-btn');
    var originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = 'Fetching files...';
    var loadedFiles = [];
    var totalFiles = 0;
    var loadedCount = 0;
    sections.forEach(function(sec) { totalFiles += sec.files.length; });
    for (var i = 0; i < sections.length; i++) {
        var sec = sections[i];
        for (var j = 0; j < sec.files.length; j++) {
            var file = sec.files[j];
            try {
                var response = await fetch(sec.id + '/' + file.name);
                if (response.ok) {
                    var content = await response.text();
                    loadedFiles.push({ section: sec.title, sectionId: sec.id, sectionIcon: sec.icon, name: file.name, display: file.display, content: content, html: marked.parse(content) });
                }
            } catch (e) { console.log('Could not load: ' + sec.id + '/' + file.name); }
            loadedCount++;
            btn.innerHTML = 'Fetching... ' + loadedCount + '/' + totalFiles;
        }
    }
    btn.innerHTML = 'Generating HTML...';
    var filesBySection = {};
    loadedFiles.forEach(function(item) {
        if (!filesBySection[item.sectionId]) { filesBySection[item.sectionId] = { title: item.section, icon: item.sectionIcon, files: [] }; }
        filesBySection[item.sectionId].files.push(item);
    });
    var html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>[CLIENT NAME] - Tax Working Papers (Offline)</title>';
    html += '<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;display:flex;height:100vh;overflow:hidden;background:#f5f5f5}#nav-panel{width:320px;background:#1e293b;color:#e2e8f0;overflow-y:auto;display:flex;flex-direction:column}#nav-header{background:#0f172a;padding:16px 20px;border-bottom:1px solid #334155}#nav-header h1{font-size:14px;font-weight:600;color:#60a5fa;margin-bottom:4px}#nav-header h2{font-size:11px;color:#94a3b8}#nav-content{flex:1;overflow-y:auto}.nav-section{border-bottom:1px solid #334155}.nav-section-header{display:flex;align-items:center;padding:12px 16px;cursor:pointer;background:#1e293b}.nav-section-header:hover{background:#334155}.nav-section-header .icon{width:24px;height:24px;margin-right:10px;display:flex;align-items:center;justify-content:center;background:#374151;border-radius:4px;color:#60a5fa;font-weight:600;font-size:11px}.nav-section-header .title{flex:1;font-size:13px;font-weight:500}.nav-section-header .arrow{font-size:10px;color:#64748b;transition:transform .2s}.nav-section.expanded .arrow{transform:rotate(90deg)}.nav-section-items{display:none;background:#0f172a}.nav-section.expanded .nav-section-items{display:block}.nav-item{padding:8px 16px 8px 50px;cursor:pointer;font-size:12px;color:#94a3b8;border-left:3px solid transparent}.nav-item:hover{background:#1e293b;color:#e2e8f0}.nav-item.active{background:#1e40af;color:#fff;border-left-color:#60a5fa}#preview-panel{flex:1;display:flex;flex-direction:column;background:#fff;overflow:hidden}#preview-header{padding:16px 24px;background:#fff;border-bottom:1px solid #e2e8f0}#preview-header .breadcrumb{font-size:12px;color:#64748b;margin-right:8px}#preview-header .filename{font-size:16px;font-weight:600;color:#1e293b}#preview-content{flex:1;overflow-y:auto;padding:24px 40px}#preview-content h1{font-size:28px;font-weight:700;color:#1e293b;margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e2e8f0}#preview-content h2{font-size:22px;font-weight:600;color:#334155;margin:28px 0 12px}#preview-content h3{font-size:18px;font-weight:600;color:#475569;margin:24px 0 10px}#preview-content p{font-size:14px;line-height:1.7;color:#475569;margin-bottom:12px}#preview-content ul,#preview-content ol{margin:12px 0 12px 24px;color:#475569}#preview-content li{font-size:14px;line-height:1.7;margin-bottom:4px}#preview-content table{width:100%;border-collapse:collapse;margin:16px 0;font-size:12px}#preview-content th{background:#f1f5f9;padding:10px 12px;text-align:left;font-weight:600;color:#334155;border:1px solid #e2e8f0}#preview-content td{padding:10px 12px;border:1px solid #e2e8f0;color:#475569}#preview-content tr:hover td{background:#f8fafc}#preview-content code{background:#f1f5f9;padding:2px 6px;border-radius:4px;font-family:Consolas,Monaco,monospace;font-size:13px;color:#e11d48}#preview-content pre{background:#1e293b;padding:16px;border-radius:8px;overflow-x:auto;margin:16px 0}#preview-content pre code{background:none;color:#e2e8f0;padding:0}#preview-content strong{font-weight:600;color:#1e293b}.welcome{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#64748b;text-align:center}.welcome h2{font-size:24px;color:#334155;margin-bottom:12px}</style></head><body>';
    html += '<div id="nav-panel"><div id="nav-header"><h1>[CLIENT NAME]</h1><h2>Tax Working Papers (Offline)</h2></div><div id="nav-content">';
    Object.keys(filesBySection).forEach(function(secId) {
        var sec = filesBySection[secId];
        html += '<div class="nav-section" data-section="' + secId + '"><div class="nav-section-header" onclick="this.parentElement.classList.toggle(\'expanded\')"><span class="icon">' + sec.icon + '</span><span class="title">' + sec.title + '</span><span class="arrow">&#9658;</span></div><div class="nav-section-items">';
        sec.files.forEach(function(f) { html += '<div class="nav-item" data-idx="' + loadedFiles.indexOf(f) + '" onclick="showFile(' + loadedFiles.indexOf(f) + ')">' + f.display + '</div>'; });
        html += '</div></div>';
    });
    html += '</div></div><div id="preview-panel"><div id="preview-header"><span class="breadcrumb">Select a file</span><span class="filename"></span></div><div id="preview-content"><div class="welcome"><h2>Tax Working Papers</h2><p>Select a document from the navigation panel.</p></div></div></div>';
    // CRITICAL: String concatenation for script tags to avoid HTML parser issues
    html += '<scr' + 'ipt>\n';
    html += 'var filesData = ' + JSON.stringify(loadedFiles.map(function(f) {
        var safeHtml = f.html.split('</' + 'script>').join('&lt;/script&gt;').split('<' + 'script').join('&lt;script');
        return { sectionId: f.sectionId, section: f.section, name: f.name, display: f.display, html: safeHtml };
    })) + ';\n';
    html += 'function showFile(idx){var f=filesData[idx];document.querySelectorAll(".nav-item").forEach(function(el){el.classList.remove("active")});document.querySelector(".nav-item[data-idx=\\""+idx+"\\"]").classList.add("active");var sec=document.querySelector(".nav-section[data-section=\\""+f.sectionId+"\\"]");if(sec)sec.classList.add("expanded");document.getElementById("preview-header").innerHTML=\'<span class="breadcrumb">\'+f.section+\' /</span><span class="filename">\'+f.display+\'</span>\';document.getElementById("preview-content").innerHTML=f.html;}\n';
    html += 'document.querySelector(".nav-section").classList.add("expanded");\n';
    html += '</' + 'script>\n</body></html>';
    var blob = new Blob([html], {type: 'text/html'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = '[CLIENT_NAME]_Tax_Working_Papers.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    btn.disabled = false;
    btn.innerHTML = originalText;
}
</script>
</body>
</html>
```

---

## Section 2: START_VIEWER.bat Template

Batch file to launch the HTML viewer with Python HTTP server. Save as `START_VIEWER.bat` in the root of each tax computation folder.

```batch
@echo off
title Form C Tax Computation - [CLIENT NAME]
echo ============================================================
echo.
echo   [CLIENT NAME]
echo   [COMPANY NO.]
echo.
echo   FORM C TAX COMPUTATION
echo   Year of Assessment [YEAR]
echo   Basis Period: [START DATE] to [END DATE]
echo.
echo ============================================================
echo.
echo   DELIVERABLES:
echo   -------------
echo   [TC]  Main Tax Computation
echo   [A]   Analysis of Accounts
echo   [B]   Capital Allowance Schedule
echo   [C]   Directors Details
echo   [D]   Shareholders Details
echo   [E]   Beneficial Ownership
echo.
echo ============================================================
echo.
echo Starting local server...
echo.

cd /d "%~dp0"

:: Try to open browser after 2 seconds
start "" cmd /c "timeout /t 2 >nul && start http://localhost:8000/tax_viewer.html"

:: Start Python server
echo Server running at: http://localhost:8000/tax_viewer.html
echo.
echo Press Ctrl+C to stop the server when done.
echo ============================================================
echo.

python -m http.server 8000

:: If Python fails, try python3
if %errorlevel% neq 0 (
    echo.
    echo Python not found. Trying python3...
    python3 -m http.server 8000
)

:: If still fails, show error
if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo ERROR: Python is not installed.
    echo.
    echo Please install Python from:
    echo https://www.python.org/downloads/
    echo ============================================================
    pause
)
```

---

## Section 3: Placeholders to Replace

When generating templates for a specific tax engagement, replace the following placeholders throughout both files:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[CLIENT NAME]` | Full company name | ABC Manufacturing Sdn Bhd |
| `[COMPANY NO.]` | SSM company registration number | 123456-U |
| `[YEAR]` | Year of Assessment | 2025 |
| `[START DATE]` | Basis period start date | 01 Jan 2024 |
| `[END DATE]` | Basis period end date | 31 Dec 2024 |
| `[CLIENT_NAME]` | Company name with underscores (for file names) | ABC_Manufacturing_Sdn_Bhd |

### Replacement Guide

1. **In tax_viewer.html:**
   - Replace `[CLIENT NAME]` in the title tag
   - Replace `[CLIENT NAME]` in the nav-header h1 tag
   - Replace `[YEAR]` in the nav-header h2 tag
   - Replace `[CLIENT_NAME]` in the download button filename

2. **In START_VIEWER.bat:**
   - Replace all placeholders in the header section
   - Replace `[CLIENT NAME]` in the window title
   - Replace `[CLIENT_NAME]` if used in filename references

---

## Usage Instructions

1. Copy the complete HTML code and save as `tax_viewer.html` in the root of the tax computation folder
2. Copy the batch file code and save as `START_VIEWER.bat` in the root of the tax computation folder
3. Replace all placeholders with actual client and engagement details
4. Ensure all markdown files are in their respective subdirectories (01_TAX_COMPUTATION, 02_ANALYSIS_OF_ACCOUNTS, etc.)
5. Optional: Include company logo as `YYC_Logo_white.webp` in the root directory
6. Double-click `START_VIEWER.bat` to launch the viewer
7. The viewer will open at `http://localhost:8000/tax_viewer.html`

---

## Key Features

- Split-panel interface with navigation on left and content on right
- Full-text search across all documents (Ctrl+F)
- Expandable/collapsible section navigation
- Resizable navigation panel (drag the divider)
- Markdown parsing using marked.js library
- Professional styling for tax working papers
- Download All button to generate offline-compatible HTML
- Auto-opens browser on startup
- Python HTTP server for local viewing

---

*Last Updated: 2026-03-06*
