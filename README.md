# Malaysian Tax Agent - Claude Code Skills

A professional Malaysian tax agent system built as [Claude Code](https://claude.com/claude-code) skills. Automates the preparation of Form C tax working papers, PBC checklists, query lists, capital allowance schedules, and supporting deliverables.

## Prerequisites

### Required

| Software | Version | Purpose |
|----------|---------|---------|
| [Claude Code](https://claude.com/claude-code) | Latest | CLI agent that runs the skills |
| [Python](https://www.python.org/downloads/) | 3.9+ | Script execution for Excel, PDF generation |
| [Git](https://git-scm.com/downloads) | Any | Version control |

### Python Packages

Install all required packages in one command:

```bash
pip install openpyxl PyMuPDF markdown
```

| Package | PyPI Name | Used By |
|---------|-----------|---------|
| openpyxl | `openpyxl` | Excel workbook generation (PBC checklists, query lists) |
| PyMuPDF | `PyMuPDF` | PDF annotation and GL document markup (imported as `fitz`) |
| markdown | `markdown` | Markdown-to-HTML conversion for PDF export |

### Optional (for specific features)

| Software / Package | Install | Used By |
|--------------------|---------|---------|
| weasyprint | `pip install weasyprint` | HTML-to-PDF conversion (requires GTK3 on Windows) |
| pywin32 | `pip install pywin32` | Outlook email automation (Windows only) |
| Microsoft Outlook | Desktop app | Email automation via COM (Windows only) |
| Chrome or Edge | Desktop browser | Headless PDF generation, viewing tax_viewer.html |

### Windows-Specific Notes

- **pywin32** is only needed for Outlook email automation
- **Outlook** must be installed and configured for the email automation skill to work
- **weasyprint** on Windows requires GTK3 runtime — see [weasyprint docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/WeiKhjan/Tax.git
   cd Tax
   ```

2. **Install Python dependencies**
   ```bash
   pip install openpyxl PyMuPDF markdown
   ```

3. **Open with Claude Code**
   ```bash
   claude
   ```
   Claude Code will automatically load the skills from `.claude/skills/` and the project configuration from `CLAUDE.md`.

4. **Start a tax engagement**

   Tell Claude the client details and provide financial documents. Claude will:
   - Assess information completeness
   - Generate PBC lists and query lists if needed
   - Prepare full Form C tax working papers
   - Generate an interactive HTML viewer (`tax_viewer.html`)

## Project Structure

```
.
├── CLAUDE.md                          # Project configuration and instructions
├── .gitignore
├── Clients/                           # Client work output (gitignored, confidential)
│   └── [CLIENT NAME] YA [YEAR]/       # Per-engagement folders
│       ├── 01_TAX_COMPUTATION/
│       ├── 02_ANALYSIS_OF_ACCOUNTS/
│       ├── ...
│       ├── tax_viewer.html
│       └── START_VIEWER.bat
└── .claude/
    └── skills/                        # Claude Code agent skills
        ├── capital-allowance/
        ├── email-automation/
        ├── excel-generation/
        ├── malaysian-tax-computation/
        ├── pbc-query-management/
        ├── pdf-operations/
        └── working-papers-viewer/
```

## Skills Overview

| Skill | Description |
|-------|-------------|
| `malaysian-tax-computation` | Core Form C tax computation, legislation references, all schedules |
| `capital-allowance` | Schedule 3 ITA 1967 — IA/AA rates, motor vehicle caps, SVA, balancing adjustments |
| `pbc-query-management` | PBC document checklists and tax query lists for client engagements |
| `excel-generation` | Excel workbooks for PBC checklists and query lists |
| `pdf-operations` | PDF export, GL annotation with tickmarks, print-ready reports |
| `email-automation` | Outlook COM automation for client communications |
| `working-papers-viewer` | Interactive HTML viewer with markdown preview, search, and download |

## Confidentiality

- The `Clients/` folder is **gitignored** — client data never enters version control
- All script templates use `[PLACEHOLDER]` values — replace with actual client data at runtime
- Maintain professional confidentiality standards per MIA/CTIM requirements
