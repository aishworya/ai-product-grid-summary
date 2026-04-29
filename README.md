# AI-Assisted Complexity Validation for Pricing Approvals in CRM

## Overview

This project demonstrates how AI can assist in **pricing approval workflows** within a CRM system by validating and justifying the **Level of Complexity (LoC)** assigned to a solution.

In this context, the Level of Complexity is used to determine **implementation effort**, which directly influences **pricing adjustments**. When pricing exceeds predefined thresholds, the solution must go through an **approval process**.

This project introduces an AI layer that helps approvers make faster and more informed decisions.

---

## Business Context

In the current CRM workflow:

* A user creates a solution and selects a **Level of Complexity**
* Complexity influences **pricing of the overall solution**
* If pricing crosses a threshold, it requires **approval**
* Approvers must manually review:

  * Product grid
  * Solution components
  * Implementation effort

### Challenges:

* Manual review of large product grids is time-consuming
* No standardized justification for complexity selection
* Inconsistent decision-making across approvers
* Slower approval turnaround time

---

## Solution

This project introduces an **AI-powered assistant layer** that:

* Analyzes the product grid
* Generates a concise **solution summary**
* Provides a **justification for the selected complexity**
* Validates whether the complexity aligns with the solution
* Suggests corrections if required

👉 The goal is **not to replace the approver**, but to:

* Reduce manual effort
* Improve consistency
* Speed up approvals

---

## How It Helps Approvers

Instead of manually analyzing the entire product grid, approvers receive:

* A **structured summary**
* A **clear justification**
* A **validation signal (correct / needs review)**

This enables:

* Faster decision-making
* Reduced cognitive load
* Better focus on exceptions

---

## How It Works

1. Load product grid data (`data.csv`)
2. Read user-selected Level of Complexity
3. Perform basic aggregation (category, quantity)
4. Send structured input to AI model
5. Generate:

   * Solution summary
   * Justification
   * Validation
   * Suggested complexity (if needed)

---
## Architecture Flow

```text
User (Sales / Solutioning)
        ↓
Selects Level of Complexity (CRM)
        ↓
Product Grid (data.csv)
        ↓
Python Processing Layer (Pandas)
        ↓
AI Layer (OpenAI)
        ↓
-----------------------------------
|  Summary                        |
|  Justification                 |
|  Validation                    |
-----------------------------------
        ↓
Approver Decision
(Faster, Informed Approval)
```


## Example Output

```
Summary:
The solution includes multiple network components and service elements.

Justification:
The combination of infrastructure and services indicates moderate implementation effort.

Validation:
Yes, the selected complexity is appropriate.

Suggested Complexity:
Level 2
```

---

## Tech Stack

* Python
* Pandas (data processing)
* OpenAI API (AI reasoning layer)

---

## How to Run

### 1. Install dependencies

```
pip install pandas openai
```

### 2. Set API Key (recommended)

```
setx OPENAI_API_KEY "your-api-key"
```

### 3. Run the project

```
python main.py
```

---

## Demo Mode

To run without API usage:

```
USE_AI = False
```

---

## Key Design Principles

* **Human-in-the-loop**: AI assists, does not replace decision-making
* **Explainability**: Focus on justification, not just output
* **Business-aligned**: Designed around pricing and approval workflows
* **Practical AI usage**: Applied where manual effort is high

---

## Future Enhancements

* AI-generated approval email (end-to-end workflow)
* Confidence scoring for AI recommendations
* Integration with CRM platforms (e.g., Dynamics, Salesforce)
* Feedback loop to improve model accuracy over time

---

## Author

Business Analyst with experience in CRM systems, transitioning into AI-driven workflow design and decision-support systems.
