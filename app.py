import streamlit as st
import streamlit.components.v1 as components
import json

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Curato | Professional Gifting, Without Guesswork",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. CORE INVENTORY (SOURCE OF TRUTH)
# =========================================================
# NOTE:
# - Intentionally limited
# - Opinionated
# - Tiered (safe / bold)
# - Human judgment embedded
# - Amazon links should be ASIN / Idea List ready

INVENTORY = [
    {
        "id": "parker_vector",
        "name": "Parker Vector Stainless Steel Pen",
        "category": "desk",
        "tier": "safe",
        "price": 450,
        "budget_bucket": 500,
        "certainty_score": 9.5,
        "human_reason": "Matte steel body feels substantial in hand and never looks cheap in meetings.",
        "avoid_if": ["very casual teams"],
        "amazon_url": "https://www.amazon.in/dp/B00LMRZ4PE"
    },
    {
        "id": "laptop_stand",
        "name": "Aluminium Laptop Stand (Foldable)",
        "category": "tech",
        "tier": "safe",
        "price": 699,
        "budget_bucket": 1500,
        "certainty_score": 9.2,
        "human_reason": "Solves neck strain instantly and works for anyone using a laptop daily.",
        "avoid_if": ["desktop-only roles"],
        "amazon_url": "https://www.amazon.in/dp/B08F2L1G1C"
    },
    {
        "id": "milton_thermosteel",
        "name": "Milton Thermosteel Bottle (500ml)",
        "category": "universal",
        "tier": "safe",
        "price": 750,
        "budget_bucket": 1500,
        "certainty_score": 9.0,
        "human_reason": "Zero leakage, no branding embarrassment, and genuinely used every day.",
        "avoid_if": ["people who already carry glass bottles"],
        "amazon_url": "https://www.amazon.in/dp/B01M1YIY8U"
    },
    {
        "id": "tech_organiser",
        "name": "Structured Tech Organiser Pouch",
        "category": "tech",
        "tier": "safe",
        "price": 1299,
        "budget_bucket": 3000,
        "certainty_score": 8.8,
        "human_reason": "Immediately reduces cable clutter for hybrid workers.",
        "avoid_if": ["non-tech roles"],
        "amazon_url": "https://www.amazon.in/dp/B09GFPQ8MJ"
    },
    {
        "id": "moleskine_notebook",
        "name": "Moleskine Classic Notebook",
        "category": "desk",
        "tier": "bold",
        "price": 1900,
        "budget_bucket": 3000,
        "certainty_score": 7.8,
        "human_reason": "Premium feel that creatives appreciate, but overkill for some roles.",
        "avoid_if": ["strict cost-sensitive environments"],
        "amazon_url": "https://www.amazon.in/dp/B07M5L7LXY"
    },
    {
        "id": "samsonite_backpack",
        "name": "Samsonite Professional Laptop Backpack",
        "category": "travel",
        "tier": "bold",
        "price": 3800,
        "budget_bucket": 10000,
        "certainty_score": 7.5,
        "human_reason": "Corporate-safe premium that signals seriousness without being flashy.",
        "avoid_if": ["junior interns", "very casual startups"],
        "amazon_url": "https://www.amazon.in/dp/B084JH8L8P"
    }
]

# =========================================================
# 3. AVOID LIST (TRUST BUILDER)
# =========================================================
AVOID_LIST = [
    "Clothing or apparel (size risk)",
    "Mugs with text or jokes",
    "Religious or political symbols",
    "Cheap plastic desk decor",
    "Anything that sits unused"
]

# =========================================================
# 4. RECOMMENDATION ENGINE (CERTAINTY-FIRST)
# =========================================================
def recommend_items(
    context: str,
    budget: int,
    tier: str = "safe",
    limit: int = 3
):
    """
    Core decision engine.
    Reduces choice instead of expanding it.
    """

    # Budget handling
    if budget == 10000:
        budget_cap = 100000
        min_price = 3000
    else:
        budget_cap = budget
        min_price = 0

    filtered = []

    for item in INVENTORY:
        if item["price"] < min_price:
            continue
        if item["price"] > budget_cap:
            continue
        if tier == "safe" and item["tier"] != "safe":
            continue
        if context != "any" and item["category"] != context:
            continue
        filtered.append(item)

    # Rank by certainty score
    filtered.sort(key=lambda x: x["certainty_score"], reverse=True)

    return filtered[:limit]

# =========================================================
# 5. EXPOSE DATA TO FRONTEND (SESSION BRIDGE)
# =========================================================
if "api_response" not in st.session_state:
    st.session_state.api_response = {}

query_params = st.experimental_get_query_params()

if "fetch" in query_params:
    context = query_params.get("context", ["any"])[0]
    budget = int(query_params.get("budget", [1500])[0])
    tier = query_params.get("tier", ["safe"])[0]

    results = recommend_items(context, budget, tier)

    st.session_state.api_response = {
        "results": results,
        "avoid_list": AVOID_LIST,
        "mode": "b2c",
        "tier": tier
    }

# =========================================================
# 6. LOAD FRONTEND
# =========================================================
with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Inject backend data safely
html_with_data = html_template.replace(
    "__CURATO_DATA__",
    json.dumps(st.session_state.api_response)
)

components.html(
    html_with_data,
    height=2000,
    scrolling=True
)
