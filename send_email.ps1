# Wait a moment for any previous COM objects to release
Start-Sleep -Seconds 2

# Create Outlook application
try {
    $outlook = New-Object -ComObject Outlook.Application
    $namespace = $outlook.GetNameSpace("MAPI")
    $mail = $outlook.CreateItem(0)

    $mail.To = "[CLIENT_EMAIL]"
    $mail.Subject = "Circular Tech Asia Sdn Bhd - PBC & Query List for Tax Computation YA 2025"

    $body = @"
Dear Farah,

Greetings from YYC.

We are currently preparing the Form C Tax Computation for Circular Tech Asia Sdn Bhd for Year of Assessment 2025 (basis period: 01 March 2024 to 28 February 2025).

Based on our review of the General Ledger provided, we require additional documents and clarifications to complete the tax working papers. Please find attached:

1. PBC Checklist (PBC_Checklist_CircularTech_YA2025.xlsx)
   - List of documents required for tax filing
   - Please mark status and provide the documents listed

2. Query List (Query_List_CircularTech_YA2025.xlsx)
   - 4 queries requiring your response/clarification
   - Please fill in the "Client Response" column (Column F)

SUMMARY OF TAX POSITION (Draft):
================================
Net Loss per Accounts     : RM (1,512.36)
Chargeable Income         : NIL
Tax Payable               : NIL
Loss Carried Forward      : RM 1,412.36

PRIORITY ITEMS REQUIRED:
========================
1. SSM Company Profile (Company Registration Number)
2. Director's particulars - Full name, NRIC, Address (for Query Q001)
3. Shareholders details (for SME status verification)
4. Beneficial ownership information

FORM C FILING DEADLINE: 30 September 2025

Please complete the attached Excel files and return them together with the supporting documents at your earliest convenience.

If you have any questions, please do not hesitate to contact me.

Thank you.

Best regards,

[PREPARER NAME]
Tax Department
YYC Holdings Sdn Bhd

Email: [PREPARER EMAIL]
"@

    $mail.Body = $body
    $mail.Attachments.Add("C:\Users\khjan\Downloads\Demo - YYC - Calude\Circular Tech Asia Sdn Bhd YA 2025\PBC_Checklist_CircularTech_YA2025.xlsx") | Out-Null
    $mail.Attachments.Add("C:\Users\khjan\Downloads\Demo - YYC - Calude\Circular Tech Asia Sdn Bhd YA 2025\Query_List_CircularTech_YA2025.xlsx") | Out-Null

    $mail.Display()

    Write-Host "Email created and displayed in Outlook. Please review and click Send."
}
catch {
    Write-Host "Error: $_"
    Write-Host "Please make sure Outlook is open and try again."
}
