# Malaysian Tax Agent - Skills & Deliverables Configuration

## General Office Skills

### PDF Operations
- Read and extract data from PDF financial statements
- Analyze scanned documents (invoices, receipts, contracts)
- Extract trial balance and ledger information
- Review supporting documents for tax deductions
- Parse LHDN notices and correspondence

### Microsoft Excel Skills
- Create and maintain tax computation workbooks
- Build capital allowance schedules with formulas
- Develop analysis templates with pivot tables
- Perform data validation and reconciliation
- Generate summary reports and dashboards
- Use VLOOKUP, SUMIF, INDEX-MATCH for data analysis
- Create linked worksheets for integrated computations

### Microsoft Word Skills
- Draft tax computation reports
- Prepare cover letters for LHDN submissions
- Create engagement letters and fee quotations
- Document tax positions and technical memos
- Generate professional client correspondence

### Microsoft PowerPoint Skills
- Prepare tax planning presentation decks
- Create visual summaries for client meetings
- Develop training materials on tax compliance
- Present tax savings opportunities to management

---

## Tax Analysis Skills

### Analysis of Accounts (Profit & Loss Statement)

#### Revenue Analysis
| Account Category | Tax Treatment | Reference |
|------------------|---------------|-----------|
| Sales Revenue | Taxable | Section 4(a) |
| Service Income | Taxable | Section 4(a) |
| Interest Income | Taxable (or exempt) | Section 4(c) / Sch 6 |
| Dividend Income | Single-tier exempt | Section 12(1B) |
| Rental Income | Taxable | Section 4(d) |
| Royalty Income | Taxable | Section 4(d) |
| Foreign Exchange Gain | Revenue vs Capital | Case law |
| Insurance Claims | Depends on nature | Section 22 |
| Government Grants | Taxable / Exempt | Specific orders |

#### Expenditure Analysis
| Account Category | Tax Treatment | Reference |
|------------------|---------------|-----------|
| Salaries & Wages | Deductible | Section 33(1) |
| EPF Contribution | Deductible (19% limit) | Section 34(4) |
| SOCSO/EIS | Deductible | Section 33(1) |
| Directors' Fees | Deductible | Section 33(1) |
| Rental Expense | Deductible | Section 33(1) |
| Repairs & Maintenance | Revenue vs Capital | Section 33(1) |
| Professional Fees | Deductible | Section 33(1) |
| Bad Debts | Specific write-off only | Section 34(2) |
| General Provisions | Not deductible | - |
| Depreciation | Add back (claim CA) | - |
| Entertainment | 50% or 100% | Section 33(1), PR 3/2008 |
| Donations | Approved only | Section 44(6) |
| Interest Expense | Deductible (thin cap rules) | Section 33(1) |
| Penalties & Fines | Not deductible | - |
| Private Expenses | Not deductible | Section 39(1)(a) |

#### Common Add-Backs
- Depreciation (all forms)
- General provisions (doubtful debts, stock obsolescence)
- Private motor vehicle expenses (above threshold)
- Non-business entertainment
- Penalties, fines, compounds
- Donations to non-approved bodies
- Capital expenditure wrongly expensed
- Leave passage (above RM3,000 local / RM3,000 overseas)
- Medical benefits (above RM2,000 unless exempted)

#### Common Deductions
- Unutilized capital allowances brought forward
- Approved donations (Section 44(6))
- Double deductions (training, R&D, promotions)
- Reinvestment allowance
- Investment tax allowance

---

## Capital Allowance Computation Skills

### Schedule 3 ITA 1967 - Capital Allowances

#### Initial Allowance (IA) Rates
| Asset Category | IA Rate |
|----------------|---------|
| Industrial Buildings | 10% |
| Plant & Machinery | 20% |
| Heavy Machinery | 20% |
| Motor Vehicles | 20% |
| Office Equipment | 20% |
| ICT Equipment | 20% |

#### Annual Allowance (AA) Rates
| Asset Category | AA Rate |
|----------------|---------|
| Industrial Buildings | 3% |
| Heavy Machinery/General Plant | 14% |
| Motor Vehicles | 20% |
| Office Equipment/Furniture | 10% |
| ICT Equipment (Computer) | 20% (or 40% accelerated) |
| Small Value Assets (<RM2,000) | 100% |

#### Capital Allowance Computation Template
```
SCHEDULE OF CAPITAL ALLOWANCES
Year of Assessment: ____

A. PLANT & MACHINERY
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ Asset    │ Date    │ Cost   │ IA   │ AA   │ Total │ TWDV   │ Disposal │ BC  │
   │ Desc     │ Acquired│ (RM)   │ (RM) │ (RM) │ CA    │ C/F    │ Proceeds │     │
   ├──────────┼─────────┼────────┼──────┼──────┼───────┼────────┼──────────┼─────┤
   │          │         │        │      │      │       │        │          │     │
   └─────────────────────────────────────────────────────────────────────────────┘

B. MOTOR VEHICLES (Cost Cap: RM100,000 / RM200,000 for new on-the-road)

C. INDUSTRIAL BUILDING ALLOWANCE (IBA)

D. ACCELERATED CAPITAL ALLOWANCE (if applicable)

E. SUMMARY
   Total CA Current Year:          RM ________
   Less: Restricted to 70% of SI:  RM ________  (if applicable)
   CA Absorbed:                    RM ________
   CA Carried Forward:             RM ________
```

#### Motor Vehicle Cost Cap Rules
| Vehicle Type | Cost Cap |
|--------------|----------|
| New vehicle (on-the-road) | RM200,000 |
| Used vehicle | RM100,000 |
| Commercial vehicles | No cap |
| Vehicles for hire | No cap |

#### Small Value Assets (SVA)
- Individual cost < RM2,000 per item
- 100% write-off in year of acquisition
- Annual cap: RM20,000 per YA (excess at normal rates)

---

## Form C Deliverables Structure

### 1. MAIN TAX COMPUTATION

```
                    [COMPANY NAME]
                    [COMPANY NO.]
            TAX COMPUTATION FOR YEAR OF ASSESSMENT ____
            (Basis Period: DD/MM/YYYY to DD/MM/YYYY)

                                                    RM              RM
BUSINESS INCOME
Net Profit/(Loss) per Accounts                                  XXX,XXX

ADD: NON-ALLOWABLE EXPENSES
     Depreciation                              XX,XXX
     General Provision for Bad Debts           XX,XXX
     Entertainment (50%)                       XX,XXX
     Donations - Non Approved                  XX,XXX
     Motor Vehicle Expenses (Private)          XX,XXX
     Penalties and Fines                       XX,XXX
                                                              ─────────
                                                                XX,XXX
                                                              ─────────
                                                               XXX,XXX

LESS: NON-TAXABLE INCOME
      Single-tier Dividend                     XX,XXX
      Interest Income (Exempt)                 XX,XXX
                                                              ─────────
                                                               (XX,XXX)
                                                              ─────────
ADJUSTED INCOME/(LOSS)                                         XXX,XXX

LESS: CAPITAL ALLOWANCES
      Current Year                             XX,XXX
      Brought Forward                          XX,XXX
                                                              ─────────
                                                               (XX,XXX)
                                                              ─────────
STATUTORY INCOME FROM BUSINESS                                 XXX,XXX

ADD:  OTHER SOURCES OF INCOME
      Interest Income (Taxable)                XX,XXX
      Rental Income                            XX,XXX
                                                              ─────────
AGGREGATE INCOME                                               XXX,XXX

LESS: APPROVED DONATIONS (Section 44(6))                       (XX,XXX)
                                                              ─────────
TOTAL INCOME                                                   XXX,XXX

LESS: LOSSES B/F (Section 44(5B) - 10 year limit)             (XX,XXX)
                                                              ─────────
CHARGEABLE INCOME                                              XXX,XXX
                                                              =========

TAX COMPUTATION:
SME Rate:
  First RM150,000 @ 15%                                         22,500
  Next RM450,000 @ 17%                                          76,500
  Balance @ 24%                                                 XX,XXX
                                                              ─────────
TAX CHARGED                                                     XX,XXX

LESS: TAX REBATE (Section 6A)                                       -
LESS: SET-OFF (Section 110)                                    (X,XXX)
LESS: TAX INSTALMENTS PAID (CP204)                           (XX,XXX)
                                                              ─────────
TAX PAYABLE/(REFUNDABLE)                                        X,XXX
                                                              =========
```

---

### 2. ANALYSIS OF ACCOUNTS (Supporting Schedule)

```
                    [COMPANY NAME]
         ANALYSIS OF ACCOUNTS - YEAR OF ASSESSMENT ____
                                                              Schedule A

A. REVENUE ANALYSIS
   ┌──────────────────────────────────────────────────────────────────┐
   │ Per Accounts │ Description        │ Taxable │ Non-Taxable │ Ref │
   │     (RM)     │                    │   (RM)  │    (RM)     │     │
   ├──────────────┼────────────────────┼─────────┼─────────────┼─────┤
   │              │ Sales              │         │             │     │
   │              │ Service Income     │         │             │     │
   │              │ Interest Income    │         │             │     │
   │              │ Dividend Income    │         │      ✓      │Sch 6│
   │              │ Other Income       │         │             │     │
   ├──────────────┼────────────────────┼─────────┼─────────────┼─────┤
   │ TOTAL        │                    │         │             │     │
   └──────────────────────────────────────────────────────────────────┘

B. EXPENDITURE ANALYSIS
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ Per Accounts │ Description          │Deductible│Add Back│ Remarks  │ Ref │
   │     (RM)     │                      │   (RM)   │  (RM)  │          │     │
   ├──────────────┼──────────────────────┼──────────┼────────┼──────────┼─────┤
   │              │ Salaries & Wages     │    ✓     │        │          │s33  │
   │              │ EPF                  │    ✓     │        │≤19%      │s34(4)│
   │              │ Directors' Fees      │    ✓     │        │          │s33  │
   │              │ Depreciation         │          │   ✓    │Claim CA  │     │
   │              │ Bad Debts - Specific │    ✓     │        │Written off│s34(2)│
   │              │ Bad Debts - General  │          │   ✓    │Provision │     │
   │              │ Entertainment        │   50%    │  50%   │Business  │PR3/08│
   │              │ Motor Vehicle Exp    │  Partial │Partial │Private   │     │
   │              │ Donations            │          │   ✓    │Non-apprvd│     │
   │              │ Professional Fees    │    ✓     │        │          │s33  │
   │              │ Penalties & Fines    │          │   ✓    │          │s39  │
   ├──────────────┼──────────────────────┼──────────┼────────┼──────────┼─────┤
   │ TOTAL        │                      │          │        │          │     │
   └──────────────────────────────────────────────────────────────────────────┘

C. RECONCILIATION
   Net Profit per Accounts                              XXX,XXX
   Add: Total Add-backs                                  XX,XXX
   Less: Non-taxable Income                            (XX,XXX)
                                                       ─────────
   Adjusted Income                                      XXX,XXX
                                                       =========
```

---

### 3. CAPITAL ALLOWANCE SCHEDULE (Supporting Schedule)

```
                    [COMPANY NAME]
         CAPITAL ALLOWANCE COMPUTATION - YA ____
                                                              Schedule B

A. BROUGHT FORWARD FROM PREVIOUS YEAR
   TWDV Brought Forward:                               RM XX,XXX
   Unabsorbed CA Brought Forward:                      RM XX,XXX

B. ADDITIONS DURING THE YEAR
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Date     │ Asset Description    │  Cost  │ IA (20%)│ AA    │ TWDV C/F │
   │ Acquired │                      │  (RM)  │   (RM)  │ (RM)  │   (RM)   │
   ├──────────┼──────────────────────┼────────┼─────────┼───────┼──────────┤
   │          │ Computer Equipment   │        │         │ 40%   │          │
   │          │ Office Furniture     │        │         │ 10%   │          │
   │          │ Plant & Machinery    │        │         │ 14%   │          │
   │          │ Motor Vehicle        │        │         │ 20%   │          │
   │          │ Small Value Assets   │        │  100%   │   -   │    -     │
   ├──────────┼──────────────────────┼────────┼─────────┼───────┼──────────┤
   │ TOTAL ADDITIONS                 │        │         │       │          │
   └────────────────────────────────────────────────────────────────────────┘

C. ASSETS BROUGHT FORWARD
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Asset Description    │ TWDV B/F │ AA Rate │ AA (RM) │ TWDV C/F │ Note │
   ├──────────────────────┼──────────┼─────────┼─────────┼──────────┼──────┤
   │                      │          │         │         │          │      │
   └────────────────────────────────────────────────────────────────────────┘

D. DISPOSALS DURING THE YEAR
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Asset Description │ TWDV  │ Disposal │ Balancing  │ Balancing │ Note │
   │                   │ (RM)  │ Proceeds │ Allowance  │ Charge    │      │
   │                   │       │   (RM)   │    (RM)    │   (RM)    │      │
   ├───────────────────┼───────┼──────────┼────────────┼───────────┼──────┤
   │                   │       │          │            │           │      │
   └────────────────────────────────────────────────────────────────────────┘

E. SUMMARY OF CAPITAL ALLOWANCES
   ┌────────────────────────────────────────────────────────┐
   │ Description                              │     RM      │
   ├──────────────────────────────────────────┼─────────────┤
   │ Initial Allowance - Current Year         │             │
   │ Annual Allowance - Current Year          │             │
   │ Balancing Allowance                      │             │
   │ Less: Balancing Charge                   │      (    ) │
   ├──────────────────────────────────────────┼─────────────┤
   │ Total CA Available - Current Year        │             │
   │ Add: Unabsorbed CA B/F                   │             │
   ├──────────────────────────────────────────┼─────────────┤
   │ Total CA Available for Absorption        │             │
   │ Less: CA Absorbed (limited to SI)        │      (    ) │
   ├──────────────────────────────────────────┼─────────────┤
   │ Unabsorbed CA Carried Forward            │             │
   │ TWDV Carried Forward                     │             │
   └────────────────────────────────────────────────────────┘
```

---

### 4. DIRECTORS' DETAILS (Supporting Schedule)

```
                    [COMPANY NAME]
              DIRECTORS' DETAILS - YA ____
                                                              Schedule C

A. PARTICULARS OF DIRECTORS

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │ No │ Name           │ NRIC/Passport │ Nationality │ Date of   │ Residential │
   │    │                │               │             │Appointment│ Address     │
   ├────┼────────────────┼───────────────┼─────────────┼───────────┼─────────────┤
   │ 1  │                │               │             │           │             │
   │ 2  │                │               │             │           │             │
   │ 3  │                │               │             │           │             │
   └──────────────────────────────────────────────────────────────────────────────┘

B. DIRECTORS' REMUNERATION

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │ No │ Name           │ Directors'│ Salary  │ Bonus  │ Benefits │ Total    │EPF │
   │    │                │ Fees (RM) │  (RM)   │  (RM)  │ (RM)     │ (RM)     │(RM)│
   ├────┼────────────────┼───────────┼─────────┼────────┼──────────┼──────────┼────┤
   │ 1  │                │           │         │        │          │          │    │
   │ 2  │                │           │         │        │          │          │    │
   │ 3  │                │           │         │        │          │          │    │
   ├────┼────────────────┼───────────┼─────────┼────────┼──────────┼──────────┼────┤
   │    │ TOTAL          │           │         │        │          │          │    │
   └───────────────────────────────────────────────────────────────────────────────┘

C. DIRECTORS' INTEREST IN SHARES

   ┌────────────────────────────────────────────────────────────────────────┐
   │ No │ Name           │ Direct Interest      │ Indirect Interest      │
   │    │                │ No. of Shares │  %   │ No. of Shares │   %    │
   ├────┼────────────────┼───────────────┼──────┼───────────────┼────────┤
   │ 1  │                │               │      │               │        │
   │ 2  │                │               │      │               │        │
   │ 3  │                │               │      │               │        │
   └────────────────────────────────────────────────────────────────────────┘
```

---

### 5. SHAREHOLDERS' DETAILS (Supporting Schedule)

```
                    [COMPANY NAME]
             SHAREHOLDERS' DETAILS - YA ____
                                                              Schedule D

A. SHARE CAPITAL INFORMATION

   Authorized Share Capital:                   RM ____________
   Issued & Paid-up Share Capital:             RM ____________
   Par Value per Share:                        RM ____________
   Total Number of Shares Issued:              ____________

B. PARTICULARS OF SHAREHOLDERS

   ┌────────────────────────────────────────────────────────────────────────────────┐
   │ No │ Shareholder Name    │ NRIC/Passport/ │ Nationality/ │ No. of  │    %     │
   │    │                     │ Co. Reg. No.   │ Country      │ Shares  │ Holding  │
   ├────┼─────────────────────┼────────────────┼──────────────┼─────────┼──────────┤
   │ 1  │                     │                │              │         │          │
   │ 2  │                     │                │              │         │          │
   │ 3  │                     │                │              │         │          │
   │ 4  │                     │                │              │         │          │
   │ 5  │                     │                │              │         │          │
   ├────┼─────────────────────┼────────────────┼──────────────┼─────────┼──────────┤
   │    │ TOTAL               │                │              │         │   100%   │
   └────────────────────────────────────────────────────────────────────────────────┘

C. CORPORATE SHAREHOLDERS (if applicable)

   For each corporate shareholder, provide:
   - Company Registration Number
   - Country of Incorporation
   - Principal Business Activity
   - Ultimate Holding Company (if applicable)

D. SME STATUS VERIFICATION

   ☐ Paid-up capital ≤ RM2,500,000
   ☐ Gross income ≤ RM50,000,000
   ☐ No shareholder being a company with paid-up > RM2.5M

   SME Status: ☐ Qualified  ☐ Not Qualified
```

---

### 6. BENEFICIAL OWNERSHIP DETAILS (Supporting Schedule)

```
                    [COMPANY NAME]
          BENEFICIAL OWNERSHIP DETAILS - YA ____
                                                              Schedule E

(As required under Section 56 of the Companies Act 2016 and
Anti-Money Laundering requirements)

A. DEFINITION OF BENEFICIAL OWNER
   A natural person who:
   (a) Has interest (directly/indirectly) ≥ 20% of shares; or
   (b) Exercises ultimate effective control over the company

B. PARTICULARS OF BENEFICIAL OWNERS

   ┌─────────────────────────────────────────────────────────────────────────────────┐
   │ No │ Full Name      │ NRIC/Passport │ Nationality │ Date of  │ Residential    │
   │    │ (as per ID)    │ Number        │             │ Birth    │ Address        │
   ├────┼────────────────┼───────────────┼─────────────┼──────────┼────────────────┤
   │ 1  │                │               │             │          │                │
   │ 2  │                │               │             │          │                │
   │ 3  │                │               │             │          │                │
   └─────────────────────────────────────────────────────────────────────────────────┘

C. NATURE OF BENEFICIAL INTEREST

   ┌────────────────────────────────────────────────────────────────────────────────┐
   │ No │ Name           │ Direct    │ Indirect  │ Total     │ Nature of         │
   │    │                │ Interest %│ Interest %│ Interest %│ Control/Interest  │
   ├────┼────────────────┼───────────┼───────────┼───────────┼───────────────────┤
   │ 1  │                │           │           │           │ ☐ Shareholding    │
   │    │                │           │           │           │ ☐ Voting Rights   │
   │    │                │           │           │           │ ☐ Right to Appoint│
   │    │                │           │           │           │ ☐ Other Control   │
   ├────┼────────────────┼───────────┼───────────┼───────────┼───────────────────┤
   │ 2  │                │           │           │           │                   │
   └────────────────────────────────────────────────────────────────────────────────┘

D. CHAIN OF OWNERSHIP (for indirect holdings)

   Ultimate Beneficial Owner
            │
            ▼
   ┌─────────────────┐      ┌─────────────────┐
   │ Holding Co. 1   │──────│ Holding Co. 2   │
   │ (Country, %)    │      │ (Country, %)    │
   └─────────────────┘      └─────────────────┘
            │                        │
            └────────────┬───────────┘
                         ▼
                ┌─────────────────┐
                │ [COMPANY NAME]  │
                │ (Subject Co.)   │
                └─────────────────┘

E. DECLARATION

   We hereby declare that the information provided above is true and
   accurate to the best of our knowledge.

   _______________________          _______________________
   Director's Signature             Director's Signature
   Name:                            Name:
   Date:                            Date:
```

---

## Deliverables Checklist

### Complete Form C Package

| No | Document | Status | Notes |
|----|----------|--------|-------|
| 1 | Main Tax Computation | ☐ | Primary computation |
| 2 | Analysis of Accounts (Schedule A) | ☐ | Revenue & expenditure analysis |
| 3 | Capital Allowance Schedule (Schedule B) | ☐ | IA, AA, BA/BC computations |
| 4 | Directors' Details (Schedule C) | ☐ | Particulars & remuneration |
| 5 | Shareholders' Details (Schedule D) | ☐ | Shareholding structure |
| 6 | Beneficial Ownership (Schedule E) | ☐ | Ultimate beneficial owners |
| 7 | Fixed Asset Register | ☐ | Supporting CA schedule |
| 8 | Tax Reconciliation | ☐ | Accounts vs Tax |
| 9 | Withholding Tax Summary | ☐ | If applicable |
| 10 | Related Party Transactions | ☐ | Transfer pricing |

---

## Quality Control Checklist

- [ ] All figures tie to audited/management accounts
- [ ] Mathematical accuracy verified
- [ ] Correct tax rates applied
- [ ] Capital allowance rates correct per Schedule 3
- [ ] Directors' details match SSM records
- [ ] Shareholders' details match latest Annual Return
- [ ] Beneficial ownership properly traced
- [ ] Prior year figures correctly brought forward
- [ ] All add-backs properly supported
- [ ] Tax incentives eligibility verified
- [ ] Statutory deadlines noted

---

*This skills configuration enables comprehensive Form C tax computation services with all required supporting schedules and documentation.*
