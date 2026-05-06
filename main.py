import pandas as pd
from openai import OpenAI

# =========================
# CONFIG
# =========================

USE_AI = True  # Set False if you want demo mode

# If using environment variable (recommended), keep this:
client = OpenAI()

# OR if you want to hardcode (not recommended):
# client = OpenAI(api_key="your-api-key-here")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data.csv")

# Convert dataframe to text
data_text = df.to_string(index=False)

# Simulated user input (you can change this)
user_complexity = 2

# =========================
# AI CALL / DEMO OUTPUT
# =========================

if USE_AI:
    prompt = f"""
You are a network solutions expert reviewing a CRM solution.

Product grid:
{data_text}

User selected complexity: {user_complexity}

Tasks:
1. Summarize the solution
2. Justify the selected complexity
3. Validate if the complexity is appropriate (Yes/No)
4. Suggest correct complexity (0–3 if needed)
5. Provide a confidence score (0 to 100)

Output format:

Summary:
...

Justification:
...

Validation:
...

Suggested Complexity:
...

Confidence:
...
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        ai_output = response.choices[0].message.content

    except Exception as e:
        print("Error while calling AI:", e)
        ai_output = "AI failed. Switching to demo output."
        USE_AI = False

# Demo output if AI is off or fails
demo_output = """
Summary:
Basic network setup with limited integrations.

Justification:
The number of components and integrations is moderate.

Validation:
Yes

Suggested Complexity:
2

Confidence:
85
"""

# =========================
# PRINT AI OUTPUT
# =========================

print("\n=== AI ANALYSIS ===\n")

if USE_AI:
    print(ai_output)
else:
    print(demo_output)

# =========================
# CONFIDENCE FUNCTIONS
# =========================

def extract_confidence(ai_text):
    try:
        for line in ai_text.split("\n"):
            if "confidence" in line.lower():
                return line.split(":")[-1].strip()
    except:
        return "Unknown"
    return "Unknown"


def decision_from_confidence(conf):
    try:
        score = int(conf.replace("%", "").strip())
        if score >= 75:
            return "APPROVE"
        elif score >= 50:
            return "REVIEW REQUIRED"
        else:
            return "HIGH RISK – RECHECK"
    except:
        return "REVIEW REQUIRED"

# =========================
# APPLY CONFIDENCE LOGIC
# =========================

confidence = extract_confidence(ai_output if USE_AI else demo_output)

print("\n=== CONFIDENCE SCORE ===")
print(confidence)

decision = decision_from_confidence(confidence)

print("\n=== FINAL DECISION ===")
print(decision)

# =========================
# EMAIL GENERATION
# =========================

def generate_email(ai_text, user_complexity, confidence, decision):
    email = f"""
Subject: Complexity Review – Approval Required

Dear Approver,

A solution has been submitted with Level of Complexity:
{user_complexity}

AI Assessment:
{ai_text}

Confidence: {confidence}
Recommendation: {decision}

Please review and confirm.

Regards,
AI Assistant
"""
    return email


email_output = generate_email(
    ai_output if USE_AI else demo_output,
    user_complexity,
    confidence,
    decision
)

print("\n=== APPROVAL EMAIL ===")
print(email_output)