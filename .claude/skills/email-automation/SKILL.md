---
name: email-automation
description: Send professional Malaysian tax engagement emails via Outlook COM automation. Handles PBC document requests, query lists, tax computation approvals, and final submission notifications with HTML-formatted bodies and attachment support.
---

# Email Automation - Malaysian Tax Engagement

## Purpose

Automate sending of professional tax engagement emails through Microsoft Outlook COM. Covers the full tax workflow: PBC document requests, query list distributions, tax computation review/approval, and LHDN submission notifications.

## Available Scripts

### `scripts/send_email.ps1`
Send PBC list or Query List emails to clients.

**Features:**
- HTML email body with professional letterhead
- Embedded tax engagement summary table
- Attachment handling for PBC checklists and query lists
- Dynamic recipient and CC addresses
- Subject line with client name and YA year

**Usage:**
```powershell
.\send_email.ps1 `
  -To "client@example.com" `
  -CC "manager@yyc.com.my" `
  -ClientName "JATI KIRANA SDN BHD" `
  -CompanyNo "1234567-A" `
  -YA "2025" `
  -EmailType "PBC" `
  -AttachmentPath "C:\...\PBC_01_Document_Checklist.pdf"
```

### `scripts/email_kilat_ya2021.ps1`
Send tax computation approval notification to client.

**Features:**
- Client notification with tax position summary
- Chargeable income and tax payable figures
- Document listing of attached working papers
- Approval request with response deadline
- Professional sign-off block

**Usage:**
```powershell
.\email_kilat_ya2021.ps1 `
  -To "client@example.com" `
  -ClientName "KILAT SDN BHD" `
  -YA "2021" `
  -ChargeableIncome 850000 `
  -TaxPayable 120000 `
  -WorkingPapersPath "C:\...\tax_viewer.html"
```

## Key Capabilities

| Capability | Details |
|---|---|
| Outlook COM | Windows-only, requires Outlook installed and logged in |
| HTML body | Styled tables, letterhead, tax summary section |
| Attachments | PBC checklists, query lists, working papers PDF/HTML |
| Recipients | Dynamic To/CC/BCC from parameters |
| Email types | PBC, Query, Approval, Submission notification |

## Common Email Types

### 1. PBC Document Request
Sent when client information is insufficient. Lists required documents with checklist.

### 2. Query List
Sent when clarifications are needed on accounts. Includes query reference numbers and response deadline.

### 3. Tax Computation for Review/Approval
Sent with attached working papers. Shows chargeable income, tax payable, and CP204 comparison. Requests client sign-off.

### 4. Final Submission Notification
Sent after Form C is filed with LHDN. Confirms submission details and tax position.

## Requirements

- Windows OS
- Microsoft Outlook installed and configured
- PowerShell 5.1 or later
- Outlook profile signed in before running scripts

## Notes

- Scripts use `New-Object -ComObject Outlook.Application` for COM automation
- HTML bodies use inline CSS for email client compatibility
- All monetary values formatted as `RM #,##0.00`
- Emails are created as drafts first; use `-Send $true` to send immediately
