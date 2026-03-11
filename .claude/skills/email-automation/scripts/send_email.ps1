# Wait a moment for any previous COM objects to release
Start-Sleep -Seconds 2

# Create Outlook application
try {
    $outlook = New-Object -ComObject Outlook.Application
    $namespace = $outlook.GetNameSpace("MAPI")
    $mail = $outlook.CreateItem(0)

    $mail.To = "[CLIENT_EMAIL]"
    $mail.Subject = "[CLIENT COMPANY] - PBC & Query List for Tax Computation YA [YEAR]"

    $body = @"
Dear [CLIENT CONTACT NAME],

Greetings from [FIRM NAME].

We are currently preparing the Form C Tax Computation for [CLIENT COMPANY] for Year of Assessment [YEAR] (basis period: [START DATE] to [END DATE]).

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
[FIRM NAME]

Email: [PREPARER EMAIL]
"@

    $mail.Body = $body
    # Update paths to match client engagement folder
    # $mail.Attachments.Add("[CLIENT_FOLDER_PATH]\PBC_Checklist.xlsx") | Out-Null
    # $mail.Attachments.Add("[CLIENT_FOLDER_PATH]\Query_List.xlsx") | Out-Null

    $mail.Display()

    Write-Host "Email created and displayed in Outlook. Please review and click Send."
}
catch {
    Write-Host "Error: $_"
    Write-Host "Please make sure Outlook is open and try again."
}
