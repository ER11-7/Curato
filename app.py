import streamlit as st
import streamlit.components.v1 as components
import json

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Curato | Professional Gifting",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------
# INVENTORY (SOURCE OF TRUTH)
# ----------------------------------
INVENTORY = [
    {
        "name": "Parker Vector Pen",
        "price": 450,
        "context": ["desk"],
        "tier": "safe",
        "human_reason": "Universally accepted. Signals professionalism without trying too hard.",
        "certainty_score": 9,
        "amazon_url": "https://www.amazon.in/s?k=Parker+Vector+Pen"
    },
    {
        "name": "Alloy Laptop Stand",
        "price": 699,
        "context": ["desk", "tech"],
        "tier": "safe",
        "human_reason": "Improves posture instantly. Almost everyone needs one.",
        "certainty_score": 9,
        "amazon_url": "https://www.amazon.in/s?k=Aluminium+Laptop+Stand"
    },
    {
        "name": "Milton Thermosteel Bottle",
        "price": 750,
        "context": ["travel", "desk"],
        "tier": "safe",
        "human_reason": "Daily-use item with no taste or size risk.",
        "certainty_score": 8,
        "amazon_url": "https://www.amazon.in/s?k=Milton+Thermosteel"
    },
    {
        "name": "Logitech Pebble Mouse",
        "price": 1400,
        "context": ["tech"],
        "tier": "bold",
        "human_reason": "Silent, minimal, and surprisingly delightful to use.",
        "certainty_score": 7,
        "amazon_url": "https://www.amazon.in/s?k=Logitech+Pebble+Mouse"
    },
    {
        "name": "Samsonite Laptop Backpack",
        "price": 3800,
        "context": ["travel"],
        "tier": "safe",
        "human_reason": "Corporate standard. Reliable and neutral.",
        "certainty_score": 8,
        "amazon_url": "https://www.amazon.in/s?k=Samsonite+Laptop+Backpack"
    }
]

# ----------------------------------
# AVOID LIST (STATIC FOR NOW)
# ----------------------------------
AVOID_LIST = [
    "Mugs with slogans or jokes",
    "Strong perfumes or personal care items",
    "Cheap plastic desk toys",
    "Food items with dietary assumptions",
    "Oversized branding or novelty gifts"
]

# ----------------------------------
# FILTER ENGINE
# ----------------------------------
def generate_results(context, budget, tier):
    budget = int(budget)

    results = []
    for item in INVENTORY:
        if item["price"] > budget and budget != 10000:
            continue

        if context != "any" and context not in item["context"]:
            continue

        if tier == "safe" and item["tier"] != "safe":
            continue

        results.append(item)

    # If bold tier requested, allow ONE bold item
    if tier == "bold":
        bolds = [i for i in INVENTORY if i["tier"] == "bold" and i not in results]
        if bolds:
            results.append(bolds[0])

    # Sort by certainty
    results.sort(key=lambda x: x["certainty_score"], reverse=True)

    return results[:3]

# ----------------------------------
# HANDLE QUERY PARAMS
# ----------------------------------
query_params = st.query_params

curato_data = {}

if "fetch" in query_params:
    context = query_params.get("context", "any")
    budget = query_params.get("budget", "1500")
    tier = query_params.get("tier", "safe")

    results = generate_results(context, budget, tier)

    curato_data = {
        "results": results,
        "avoid_list": AVOID_LIST
    }

# ----------------------------------
# LOAD HTML TEMPLATE
# ----------------------------------
with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Inject data safely
data_script = f"""
<script>
    const __CURATO_DATA__ = {json.dumps(curato_data)};
</script>
"""

html_template = html_template.replace(
    '<script>\n    const CURATO_DATA = __CURATO_DATA__ || {};\n</script>',
    data_script
)

# ----------------------------------
# RENDER
# ----------------------------------
components.html(
    html_template,
    height=1400,
    scrolling=False
)
