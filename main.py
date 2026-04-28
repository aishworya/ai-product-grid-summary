import pandas as pd
import os
from openai import OpenAI

# =========================
# CONFIGURATION
# =========================
USE_AI = True  # 🔁 Change to True when you want real AI response

# Simulating CRM field (Solution-level complexity)
user_complexity = "Level 2"

# =========================
# LOAD DATA
# =========================
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("❌ data.csv file not found. Please check the file location.")
    exit()

# =========================
# BASIC ANALYSIS
# =========================
total_items = len(df)
total_quantity = df["Quantity"].sum()

category_summary = df.groupby("Category")["Quantity"].sum()

# =========================
# PRINT BASIC SUMMARY
# =========================
print("\n=== PRODUCT GRID SUMMARY ===")
print(f"Total line items: {total_items}")
print(f"Total quantity: {total_quantity}")

print("\nCategory Breakdown:")
for category, qty in category_summary.items():
    print(f"- {category}: {qty}")

print(f"\nUser Selected Complexity: {user_complexity}")

# =========================
# PREPARE DATA FOR AI
# =========================
data_text = df.to_string()

prompt = f"""
You are a network solutions expert reviewing a CRM solution.

Product grid:
{data_text}

User selected complexity: {user_complexity}

Tasks:
1. Summarize the overall solution
2. Generate a justification for the selected complexity
3. Evaluate if the selected complexity is appropriate (Yes/No)
4. If not appropriate, suggest the correct level (0–3)
5. Provide clear reasoning

Keep the response concise and professional for an approval workflow.
"""

# =========================
# AI / DEMO OUTPUT
# =========================
print("\n=== AI ANALYSIS ===\n")

if USE_AI:
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        ai_output = response.choices[0].message.content
        print(ai_output)

    except Exception as e:
        print("❌ Error while calling AI:")
        print(e)
else:
    # 🔹 Demo mode (for GitHub / sharing)
    demo_output = """
Summary:
The solution includes multiple network components such as routers and switches along with service elements.

Justification:
The presence of network infrastructure combined with services indicates moderate implementation effort.

Validation:
Yes, the selected complexity appears appropriate.

Suggested Complexity:
Level 2

Reason:
The scale of hardware and inclusion of services aligns with a medium level of effort and design involvement.
"""
    print(demo_output)