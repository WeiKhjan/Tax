---
name: excel-generation
description: Generate professional Excel workbooks for Malaysian tax engagement deliverables using Python and openpyxl. Covers PBC checklists and query lists with styling, color-coded status tracking, and multi-sheet structures.
---

# Excel Generation Skill

## Purpose

Generate professional `.xlsx` workbooks for Malaysian corporate tax engagements, including:
- PBC (Provided By Client) checklists with color-coded status tracking
- Tax query lists with client response columns

## Available Scripts

All scripts are located in the `scripts/` folder.

### `create_excel.py`
Creates a PBC checklist Excel workbook from scratch.

- **Input**: Hardcoded or passed client details (name, company no., YA year)
- **Output**: `PBC_Checklist_[ClientName].xlsx`
- **Features**:
  - Multiple sheets grouped by category (Statutory, Financial, Fixed Assets, etc.)
  - Color-coded status column: green = Received, yellow = Pending, red = Missing
  - Bold headers with background fill
  - Column width auto-fit

### `create_excel_updated.py`
Enhanced version of the PBC checklist builder.

- **Input**: Same as `create_excel.py`
- **Output**: `PBC_Checklist_[ClientName]_v2.xlsx`
- **Improvements over base version**:
  - Improved header font sizing and bold formatting
  - Consistent cell borders across all data rows
  - Better text alignment (center for status, left for descriptions)
  - Remarks column included with placeholder text

### `update_excel.py`
Updates an existing PBC Excel workbook to mark items as received.

- **Input**: Existing `.xlsx` file path, list of row indices or document names to mark
- **Output**: Modified `.xlsx` file (overwrites or saves as new)
- **Features**:
  - Sets status cell to "Received" with green fill
  - Adds RM amount or description in Remarks column
  - Preserves existing formatting on unchanged rows

## Key Capabilities

| Capability | Detail |
|---|---|
| Library | `openpyxl` (read/write .xlsx) |
| Fonts | Bold headers, size control, color |
| Borders | Thin/medium borders on data ranges |
| Fill colors | PatternFill for status coding |
| Alignment | Horizontal/vertical cell alignment |
| Column width | Manual or auto-sized |
| Formulas | Standard Excel formulas as strings |
| Multi-sheet | Workbooks with cross-sheet references |
| Merged cells | For report-style headers |

## When to Use Each Script

| Scenario | Script |
|---|---|
| New engagement, need PBC checklist | `create_excel.py` |
| PBC checklist with cleaner formatting | `create_excel_updated.py` |
| Client returned documents, update status | `update_excel.py` |
| Full tax computation needed | Use `malaysian-tax-computation` skill (HTML viewer) |

## Dependencies

```
openpyxl>=3.1.0
python>=3.8
```

Install with:
```bash
pip install openpyxl
```

## Usage Notes

- Tax computations are produced as markdown working papers and viewed via the HTML viewer — Excel is not used for tax computation output.
- Status colors follow a consistent convention: `00C000` (green) = Received, `FFFF00` (yellow) = Pending, `FF0000` (red) = Missing.
- Always save output to the correct client folder following the standard folder structure: `[CLIENT NAME] YA [YEAR]/`.
- For large workbooks, use `write_only=True` mode in openpyxl to reduce memory usage.
