Start-Sleep -Seconds 1

try {
    $outlook   = New-Object -ComObject Outlook.Application
    $mail      = $outlook.CreateItem(0)

    $mail.To      = "[CLIENT_EMAIL]"
    $mail.Subject = "[CLIENT COMPANY] - Tax Computation YA[YEAR] - For Review & Approval"

    $body = @"
Dear [CLIENT CONTACT NAME],

Greetings.

Please find attached the Income Tax Computation for [CLIENT COMPANY] for Year of Assessment [YEAR] (basis period: [START DATE] to [END DATE]) for your review and approval.

TAX COMPUTATION SUMMARY
=======================
Tax Reference    : C [TAX REF NO]
Year of Assess.  : 2021
Basis Period     : 01 Jan 2021 - 31 Dec 2021
Business         : 64923 Licensed Money Lending Activities

Profit / (Loss) before tax   : RM (17,347)
Adjusted income / (loss)     : RM (13,461)
Chargeable Income            : NIL
Income Tax Payable           : NIL
Tax Loss Carried Forward     : RM 13,461

DOCUMENTS INCLUDED IN THIS PDF
===============================
  Cover / Index
  Statement A  -  Income Tax Computation
  Schedule A   -  Analysis of Non-Deductible Expenses
                  (Fine & penalty, Auditors' remuneration,
                   Professional fee, Tax agent fee)
  Statement B  -  Capital Allowance Schedule
                  (All assets fully written off; CA = NIL)
  Deferred Tax -  Computation
                  (Net DTA RM1,001 - not recognised; DTL = NIL)

NOTES
=====
1. This is a LOSS YEAR. No tax is payable for YA2021.
2. The business loss of RM13,461 will be carried forward to YA2022.
3. Deferred tax liability is NIL at 31 December 2021 (all qualifying
   assets fully claimed for capital allowance purposes by YA2020).
4. Non-qualifying assets (Renovation, Electrical Installation,
   Signboard) are excluded from the deferred tax computation.

Kindly review the attached tax computation and revert with your
approval or any comments at your earliest convenience.

Thank you.

Best regards,

[PREPARER NAME]
Tax Department
[FIRM NAME]
Email: [PREPARER EMAIL]
"@

    $mail.Body = $body

    # Update path to match client engagement folder
    $pdfPath = "[CLIENT_FOLDER_PATH]\Tax Computation [YEAR] - [CLIENT COMPANY].pdf"
    $mail.Attachments.Add($pdfPath) | Out-Null

    $mail.Display()

    Write-Host "Email displayed in Outlook. Please review and click Send."
}
catch {
    Write-Host "Error: $_"
    Write-Host "Please ensure Outlook is running and try again."
}
