# Security Code Review

**Date:** 2026-03-10
**Scope:** All scripts in `.claude/skills/` (10 Python, 2 PowerShell, 1 HTML template)
**Severity Levels:** CRITICAL | HIGH | MEDIUM | LOW | INFO

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| HIGH     | 4 |
| MEDIUM   | 4 |
| LOW      | 3 |

---

## CRITICAL Findings

### C1. Hardcoded PII and Sensitive Client Data in Source Code

**Files affected:** All 12 script files

Personally identifiable information and confidential client data are hardcoded directly in version-controlled source files:

- **NRIC numbers:** `720512-08-5788` (create_excel_updated.py:57,68,74,80)
- **Email addresses:** `nurulfarahdayana.mohdnorzian@bossboleh.com` (send_email.ps1:10), `catherinetan22@gmail.com` (email_kilat_ya2021.ps1:7), `weikhjan.chan@yyc.asia` (both .ps1 files)
- **Tax file numbers:** `C 2359253703`, `C 2370777306`, `C 58577123050` (multiple files)
- **Company registration numbers:** `724858-P`, `202401008787`, `1554637-X` (multiple files)
- **Director names, addresses, financial positions** (create_excel.py, create_excel_updated.py)
- **Specific financial amounts:** loan balances, director advances, rental income figures

**Risk:** If this repository is ever shared, forked, or accidentally made public, all client data is immediately exposed. This is a potential breach of client confidentiality and Malaysia's Personal Data Protection Act (PDPA) 2010.

**Recommendation:**
- Move all client-specific data to configuration files (JSON/YAML) stored inside the gitignored `Clients/` folder
- Scripts should accept parameters or read from config files, not embed client data
- Run `git filter-branch` or `BFG Repo-Cleaner` to purge PII from git history if these files were ever committed with real client data

---

### C2. Markdown-to-HTML Conversion Without Sanitization (XSS)

**Files:** `export_to_pdf.py:452-465`, `export_to_print_pdf.py:649-661`

```python
def markdown_to_html(md_content):
    html = markdown(md_content, extensions=['tables', 'fenced_code', ...])
    return html
```

Markdown files from the `Clients/` folder are converted to HTML and rendered without any sanitization. If a markdown file contains injected HTML/JavaScript (e.g., from a compromised or malicious client document), it will execute in the generated HTML output.

The `export_to_print_pdf.py` output is designed to be opened in a browser, making this a direct XSS vector.

**Recommendation:**
- Sanitize HTML output using `bleach` or `nh3` library before embedding
- Example: `import bleach; html = bleach.clean(html, tags=[...], attributes={...})`

---

## HIGH Findings

### H1. Chrome Launched with `--no-sandbox`

**File:** `generate_pdf_direct.py:78`

```python
cmd = [
    browser_path,
    '--headless',
    '--no-sandbox',       # <-- disables Chrome sandbox
    ...
]
```

The `--no-sandbox` flag disables Chrome's security sandbox. If the HTML file being processed contains malicious content, there is no sandbox boundary to prevent system-level exploitation.

**Recommendation:**
- Remove `--no-sandbox` unless running in a container/rootless environment that already provides isolation
- If needed for compatibility, document the reason and limit to known-safe HTML inputs

---

### H2. Hardcoded Windows User Path Exposes Username

**Files:** All Python scripts, both PowerShell scripts

```python
BASE_DIR = Path(r"C:\Users\khjan\Downloads\Demo - YYC - Calude\...")
```

The username `khjan` is embedded in every script. This is an information disclosure that reveals the developer's identity and system structure. Combined with the email `weikhjan.chan@yyc.asia`, this creates a complete identity profile.

**Recommendation:**
- Use relative paths, environment variables (`os.environ['USERPROFILE']`), or command-line arguments
- Example: `BASE_DIR = Path(os.environ.get('TAX_OUTPUT_DIR', './output'))`

---

### H3. CDN Dependencies Without Subresource Integrity (SRI)

**File:** `VIEWER_TEMPLATE.md:18-20`

```html
<link rel="stylesheet" href="https://uicdn.toast.com/editor/3.2.2/toastui-editor.min.css" />
<script src="https://uicdn.toast.com/editor/3.2.2/toastui-editor-all.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

External JavaScript is loaded from CDNs without integrity hashes. If these CDNs are compromised or a supply-chain attack occurs, arbitrary JavaScript would execute in the viewer where confidential tax data is displayed.

**Recommendation:**
- Add SRI hashes: `<script src="..." integrity="sha384-..." crossorigin="anonymous"></script>`
- Or bundle dependencies locally instead of loading from CDNs

---

### H4. HTTP Server Without Authentication or HTTPS

**File:** `VIEWER_TEMPLATE.md` (references `START_VIEWER.bat` using `python -m http.server`)

The working papers viewer runs on a local Python HTTP server with:
- No authentication
- No HTTPS/TLS
- Default binding (potentially accessible on the network, not just localhost)

Anyone on the same network could access confidential tax working papers.

**Recommendation:**
- Bind to localhost only: `python -m http.server 8000 --bind 127.0.0.1`
- Consider adding basic authentication or token-based access
- Display a warning to the user about network exposure

---

## MEDIUM Findings

### M1. `os.startfile()` on Constructed Path

**File:** `generate_pdf_direct.py:131`

```python
os.startfile(PDF_OUTPUT)
```

`os.startfile()` invokes the Windows shell handler for a file. While the path is constructed from constants here (not user input), this function can execute arbitrary programs depending on file associations. If `PDF_OUTPUT` were ever influenced by external input, this would be a command execution vulnerability.

**Recommendation:**
- Validate that the file exists and has the expected `.pdf` extension before calling `os.startfile()`
- Consider using `subprocess.Popen(['start', '', path], shell=True)` with explicit validation

---

### M2. File Deletion Without Safeguards

**File:** `create_excel.py:267-273`

```python
csv_pbc = r"C:\Users\khjan\...\PBC_Outstanding_Items.csv"
if os.path.exists(csv_pbc):
    os.remove(csv_pbc)
```

Files are deleted without confirmation. While paths are hardcoded, this pattern is risky if refactored to accept dynamic paths.

**Recommendation:**
- Add logging before deletion
- Move to a trash/backup location instead of permanent deletion
- Validate file type before removing

---

### M3. Excel COM Automation with Alerts Suppressed

**File:** `print_kilat_ya2021.py:49-50`

```python
xl = win32.Dispatch("Excel.Application")
xl.Visible = False
xl.DisplayAlerts = False
```

Disabling `DisplayAlerts` suppresses all Excel security warnings, including macro warnings and protected view alerts. If an opened workbook contains malicious macros, they could execute silently.

**Recommendation:**
- Only suppress alerts during the specific export operation, re-enable immediately after
- Validate file source before opening
- Consider using `openpyxl` (already used elsewhere) instead of COM where possible

---

### M4. Outlook COM Creates Emails with Hardcoded Recipients

**Files:** `send_email.ps1:10`, `email_kilat_ya2021.ps1:7`

Emails are composed with hardcoded recipient addresses. If a script is accidentally run or the recipient field is modified, confidential tax data could be sent to unintended recipients.

**Recommendation:**
- Require confirmation before displaying/sending: currently uses `.Display()` which is good (draft mode)
- Add a validation prompt or parameter for the recipient address
- Log all email creation attempts

---

## LOW Findings

### L1. No Error Handling for PDF Annotation

**Files:** `annotate_gl.py`, `annotate_gl_v2.py`

Both scripts open PDF files and modify them without try/except blocks around the main operations. If the PDF structure changes or pages don't exist, the script will crash and potentially leave corrupted output.

**Recommendation:**
- Wrap file operations in try/except with proper cleanup
- Validate page count before accessing specific page indices (`doc[8]`, `doc[9]`)

---

### L2. `sys.stdout.reconfigure()` May Fail

**Files:** `annotate_gl_v2.py:5`, `export_to_pdf.py:22`, etc.

```python
sys.stdout.reconfigure(encoding='utf-8')
```

This call can fail on non-Windows platforms or in environments where stdout is not a text stream. No error handling is present.

**Recommendation:**
- Wrap in try/except: `try: sys.stdout.reconfigure(encoding='utf-8') except: pass`

---

### L3. `.gitignore` Pattern May Be Incomplete

**File:** `.gitignore`

```
.claude/*
!.claude/skills/
```

The `.claude/skills/` exception re-includes skill files, which means all Python and PowerShell scripts with embedded PII (Finding C1) **are tracked by git and will be pushed**. The `Clients/` folder is correctly excluded, but the scripts themselves contain client data.

**Recommendation:**
- Either remove PII from scripts (preferred) or add scripts with client data to `.gitignore`
- Consider a `.gitsecrets` or pre-commit hook to scan for PII patterns (NRIC format, email addresses)

---

## Recommendations Summary (Priority Order)

1. **Parameterize all scripts** - Remove hardcoded PII; use config files in `Clients/` folder or CLI arguments
2. **Sanitize HTML output** - Add `bleach` or `nh3` to the markdown-to-HTML pipeline
3. **Remove `--no-sandbox`** from Chrome headless invocation
4. **Add SRI hashes** to all CDN-loaded scripts in the viewer template
5. **Bind HTTP server to localhost** in START_VIEWER.bat
6. **Add pre-commit hooks** to scan for PII patterns (NRIC, email, tax file numbers)
7. **Scrub git history** if real client data was ever committed
8. **Use relative/configurable paths** instead of hardcoded Windows paths

---

*Review performed by automated security analysis. Findings should be validated and prioritized by the development team.*
