---
name: capital-allowance
description: Malaysian Capital Allowance computation skill under Schedule 3 ITA 1967. Covers IA/AA rates, motor vehicle cost caps, small value assets, balancing adjustments, and working paper preparation for Form C Schedule B.
---

# Capital Allowance (Schedule 3 ITA 1967)

## Initial Allowance (IA) Rates

| Asset Category | IA Rate |
|---|---|
| Industrial Buildings | 10% |
| Plant & Machinery | 20% |
| Heavy Machinery | 20% |
| Motor Vehicles | 20% |
| Office Equipment | 20% |
| ICT Equipment | 20% |

IA is claimable in the **year of acquisition and first use**. No IA if asset is not brought into use in the basis period.

## Annual Allowance (AA) Rates

| Asset Category | AA Rate |
|---|---|
| Industrial Buildings | 3% |
| Heavy Machinery / General Plant & Machinery | 14% |
| Motor Vehicles | 20% |
| Office Equipment / Furniture & Fittings | 10% |
| ICT Equipment (normal) | 20% |
| ICT Equipment (accelerated) | 40% |
| Small Value Assets (cost < RM2,000 each) | 100% |

AA is claimable each year on the **Tax Written Down Value (TWDV)** until fully absorbed.

## Motor Vehicle Cost Cap Rules

| Vehicle Type | Cost Cap |
|---|---|
| New vehicle (on-the-road price) | RM200,000 |
| Used / second-hand vehicle | RM100,000 |
| Commercial vehicle (e.g., lorry, van, bus) | No cap |
| Vehicle used for hire (e.g., taxi, rental) | No cap |

The cap applies to the **qualifying cost** for IA and AA computation. If actual cost exceeds the cap, use the capped amount as the cost base. Prior-year TWDV must also be restricted proportionally if cap was applied.

## Small Value Assets (SVA)

- Individual asset cost must be **less than RM2,000** (excluding GST/SST)
- 100% write-off in the **year of acquisition**
- **Annual aggregate cap: RM20,000** total SVA claim per year of assessment
- Excess SVA above RM20,000 reverts to normal IA + AA treatment at applicable rates
- SVA pool is tracked separately; no TWDV carried forward if fully written off

## CA Computation Template Structure

### Schedule B Layout

```
SCHEDULE B - CAPITAL ALLOWANCE
YA [YEAR] | Basis Period: [DD/MM/YY] to [DD/MM/YY]

SECTION A: Plant & Machinery
  Cost / TWDV b/f | Additions | Disposals | TWDV | IA (20%) | AA (14%) | Total CA

SECTION B: Motor Vehicles (Cost Capped)
  Cost (capped) / TWDV b/f | Additions | Disposals | TWDV | IA (20%) | AA (20%) | Total CA

SECTION C: Industrial Building Allowance
  Cost / TWDV b/f | Additions | Disposals | TWDV | IA (10%) | AA (3%) | Total CA

SECTION D: Accelerated CA / ICT Equipment
  Cost / TWDV b/f | Additions | Disposals | TWDV | IA (20%) | AA (40%) | Total CA

SECTION E: Small Value Assets
  Total additions < RM2,000 each | SVA claim (100%, capped at RM20,000)

SECTION F: Summary
  Total CA (A + B + C + D + E)
  Less: Restriction to 70% of Statutory Income (if applicable)
  CA Absorbed in Current Year
  CA Carried Forward (unabsorbed)
```

### Restriction to 70% Statutory Income

Under Section 44(2) ITA 1967, CA may be restricted so that CA does not reduce SI below 30% (i.e., maximum CA absorbed = 70% of SI). Unabsorbed CA is carried forward indefinitely.

## Balancing Adjustments (on Disposal)

| Scenario | Outcome | Formula |
|---|---|---|
| Disposal proceeds < TWDV | Balancing Allowance (BA) | BA = TWDV - Proceeds |
| Disposal proceeds > TWDV | Balancing Charge (BC) | BC = Proceeds - TWDV |
| Disposal proceeds > Original Cost | BC capped at cost | BC max = Original Cost - TWDV |

- BA increases total CA deduction (additional relief)
- BC is added back to Adjusted Income (taxable)
- BC cannot exceed the total allowances previously granted (i.e., capped at original cost less TWDV)
- Balancing adjustment arises when the asset **pool is fully disposed** or when a single asset pool is used

## Working Paper File Structure - Schedule B Folder

```
03_CAPITAL_ALLOWANCE/
├── CA_01_CA_Summary.md          <- Total CA, restriction, absorbed, c/f
├── CA_02_Plant_Machinery.md     <- Section A workings (IA 20%, AA 14%)
├── CA_03_Motor_Vehicles.md      <- Section B workings (cost cap applied)
├── CA_04_Office_Equipment.md    <- IA 20%, AA 10%
├── CA_05_Computer_Equipment.md  <- IA 20%, AA 20%/40% accelerated
├── CA_06_Small_Value_Assets.md  <- SVA pool, 100% write-off, RM20k cap
├── CA_07_Balancing_Adjustment.md <- BA/BC on disposals
└── CA_08_CA_Brought_Forward.md  <- Unabsorbed CA b/f reconciliation
```

Each file must include: asset description, date of acquisition, cost (pre/post cap), TWDV b/f, IA, AA, TWDV c/f, and supporting invoice/grant references.
