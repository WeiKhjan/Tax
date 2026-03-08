---
name: working-papers-viewer
description: Generates tax_viewer.html and START_VIEWER.bat for Malaysian Form C tax working papers. Mandatory step after completing or updating any tax working papers. Creates an interactive HTML viewer with dark nav panel, markdown preview, search, and Download All feature, plus a Python HTTP server launcher batch file.
---

# Working Papers Viewer Generator

## Purpose

MANDATORY generation of `tax_viewer.html` and `START_VIEWER.bat` after completing any tax working papers. This is Step 4 and Step 5 in the tax engagement workflow.

## Trigger

Generate or update these files every time:
- A new schedule is created
- A schedule is deleted
- A new section/folder is added
- Final submission to LHDN is prepared
- Client review is requested

Note: When only schedule *content* is updated (not structure), HTML regeneration is not required as content auto-loads from `.md` files.

---

## Folder Structure

All working papers reside under `[CLIENT NAME] YA [YEAR]/`:

```
master_data.json             Master data variables (shared across all .md files)
01_TAX_COMPUTATION/          TC_  prefix  (Main Tax Computation)
02_ANALYSIS_OF_ACCOUNTS/     AA_  prefix  (Schedule A)
03_CAPITAL_ALLOWANCE/        CA_  prefix  (Schedule B)
04_DIRECTORS_DETAILS/        DD_  prefix  (Schedule C)
05_SHAREHOLDERS_DETAILS/     SH_  prefix  (Schedule D)
06_BENEFICIAL_OWNERSHIP/     BO_  prefix  (Schedule E)
07_PBC_QUERY/                PBC_ / QRY_ prefix
08_SUPPORTING_WORKINGS/      SW_  prefix
09_PRIOR_YEAR_REFERENCE/     PY_  prefix
tax_viewer.html
server.py
START_VIEWER.bat
```

---

## HTML Viewer Requirements

### Structure
- **Left nav panel**: 320px wide, dark theme (`#1e293b` background)
  - Header with logo (`YYC_Logo_white.webp`), client name, YA year
  - Search input (Ctrl+F shortcut)
  - Download All Working Papers button (MANDATORY - see below)
  - Collapsible sections with file items
  - Stats bar showing document count
- **Resizer**: 4px draggable divider between panels
- **Right preview panel**: White background, renders markdown via marked.js CDN
- Active item highlight: `#1e40af` background, `#60a5fa` left border

### Dependencies
- Toast UI Editor CSS: `https://uicdn.toast.com/editor/3.2.2/toastui-editor.min.css`
- Toast UI Editor JS: `https://uicdn.toast.com/editor/3.2.2/toastui-editor-all.min.js`
- marked.js: `https://cdn.jsdelivr.net/npm/marked/marked.min.js`

### Master Data Variable System
The viewer includes a variable substitution system:
- Loads `master_data.json` on startup via `GET /api/master`
- Replaces `{{variable_name}}` and `{{variable_name|modifier}}` in markdown before rendering
- Includes a Master Data Editor panel (purple button in nav) for editing variables
- Includes an "Insert Variable" button in the WYSIWYG editor toolbar
- Server endpoints: `GET /api/master` and `PUT /api/master` in `server.py`

### WYSIWYG Editor
The viewer uses Toast UI Editor for rich text editing of .md files:
- Edit button switches to WYSIWYG mode (not raw markdown textarea)
- Tables render as actual tables, bold text appears bold while editing
- `tuiEditor.getMarkdown()` extracts clean markdown on save
- `{{variable}}` placeholders are preserved in .md files (not substituted)

### Sections Array
The `sections` JavaScript array maps folders to files. Each entry:
```javascript
{id: "01_TAX_COMPUTATION", icon: "TC", title: "01 - Tax Computation (MAIN)", files: [
    {name: "TC_01_Cover_Page.md", display: "TC 01 - Cover Page"},
    ...
]}
```
Update this array whenever files are added or removed.

### Placeholders to Replace
- `[CLIENT NAME]` - Company name
- `[COMPANY NO.]` - SSM registration number
- `[YEAR]` - Year of Assessment
- `[START DATE]` / `[END DATE]` - Basis period dates
- `[CLIENT_NAME]` - Used in download filename (no spaces)

---

## Download All Feature (MANDATORY)

Every `tax_viewer.html` MUST include a Download All button that generates a standalone offline HTML file.

### Button CSS
```css
#download-all-btn {
    margin: 12px 16px;
    padding: 10px 16px;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white; border: none; border-radius: 6px; cursor: pointer;
    font-size: 13px; font-weight: 500;
    display: flex; align-items: center; justify-content: center; gap: 8px;
    transition: all 0.2s;
}
#download-all-btn:hover { background: linear-gradient(135deg, #059669 0%, #047857 100%); transform: translateY(-1px); }
#download-all-btn:disabled { background: #6b7280; cursor: not-allowed; transform: none; }
```

### Button HTML (place after search box)
```html
<button id="download-all-btn" onclick="downloadAllDocuments()">
    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/>
    </svg>
    Download All Working Papers
</button>
```

### CRITICAL: Script Tag Escaping

When generating the offline HTML inside JavaScript strings, you MUST use string concatenation for script tags to prevent the HTML parser from terminating the script block early:

```javascript
// WRONG - breaks HTML parser:
html += '<script>...</script>';

// CORRECT - use string concatenation:
html += '<scr' + 'ipt>...</' + 'script>';
```

When embedding markdown-rendered HTML content in the offline file, escape any script tags using split/join:

```javascript
var safeHtml = f.html
    .split('</' + 'script>').join('&lt;/script&gt;')
    .split('<' + 'script').join('&lt;script');
```

### Download Function Behavior
1. Disables button, shows "Fetching files..." with progress counter
2. Fetches all `.md` files via `fetch()` using relative paths
3. Parses markdown to HTML using `marked.parse()`
4. Groups files by section
5. Generates complete standalone HTML with embedded content and navigation
6. Shows "Generating HTML..." during assembly
7. Creates Blob, triggers download as `[CLIENT_NAME]_Tax_Working_Papers_YA[YEAR].html`
8. Re-enables button

---

## START_VIEWER.bat Requirements

```batch
@echo off
title Form C Tax Computation - [CLIENT NAME]
echo ============================================================
echo   [CLIENT NAME]
echo   [COMPANY NO.]
echo   FORM C TAX COMPUTATION
echo   Year of Assessment [YEAR]
echo   Basis Period: [START DATE] to [END DATE]
echo ============================================================
echo   DELIVERABLES:
echo   [TC]  Main Tax Computation
echo   [A]   Analysis of Accounts
echo   [B]   Capital Allowance Schedule
echo   [C]   Directors Details
echo   [D]   Shareholders Details
echo   [E]   Beneficial Ownership
echo ============================================================
cd /d "%~dp0"
start "" cmd /c "timeout /t 2 >nul && start http://localhost:8000/tax_viewer.html"
python -m http.server 8000
if %errorlevel% neq 0 (
    python3 -m http.server 8000
)
if %errorlevel% neq 0 (
    echo ERROR: Python not installed. Get it from https://www.python.org/downloads/
    pause
)
```

---

## File Naming Conventions

| Prefix | Schedule | Description |
|--------|----------|-------------|
| `TC_`  | Main | Tax Computation |
| `AA_`  | Sch A | Analysis of Accounts |
| `CA_`  | Sch B | Capital Allowance |
| `DD_`  | Sch C | Directors Details |
| `SH_`  | Sch D | Shareholders Details |
| `BO_`  | Sch E | Beneficial Ownership |
| `PBC_` | - | PBC Document Checklist |
| `QRY_` | - | Query List |
| `SW_`  | - | Supporting Workings |
| `PY_`  | - | Prior Year Reference |

---

## Full HTML Template

See **VIEWER_TEMPLATE.md** for the complete HTML template with all CSS, JavaScript, and the full `downloadAllDocuments()` function implementation.

---

## Checklist Before Delivering

- [ ] All markdown files saved in correct subfolders
- [ ] `sections` array in `tax_viewer.html` matches actual files created
- [ ] All `[CLIENT NAME]`, `[COMPANY NO.]`, `[YEAR]`, `[START DATE]`, `[END DATE]` placeholders replaced
- [ ] Download All button present and functional
- [ ] Script tag string concatenation used in downloadAllDocuments()
- [ ] `START_VIEWER.bat` updated with correct client details
- [ ] 6 main deliverables accessible: TC, Sch A, Sch B, Sch C, Sch D, Sch E
- [ ] Search function works
- [ ] All figures are mathematically accurate
- [ ] `master_data.json` present with all engagement variables
- [ ] .md files use `{{variable}}` placeholders for repeated data
- [ ] Master Data Editor button visible in nav panel
- [ ] Toast UI WYSIWYG editor CDN links included
- [ ] `server.py` includes GET/PUT `/api/master` endpoints
