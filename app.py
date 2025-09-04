# app.py
# Minimal demo: Embed a React (Recharts) component inside Streamlit
# -----------------------------------------------------------------------------
# Prereqs in this repo:
# - components/recharts/frontend/... (Vite + React + Recharts) built to dist/
# - components/recharts/__init__.py declares the component and serves frontend_dist
#
# Build & run (Docker):
#   docker compose build
#   docker compose up -d
#   open http://localhost:8501
#
# Local:
#   pip install -r requirements.txt
#   streamlit run app.py
# -----------------------------------------------------------------------------

import streamlit as st
import pandas as pd
from components.recharts import recharts  # <-- our custom component wrapper

st.set_page_config(page_title="Streamlit + React (Recharts) Demo", layout="centered")

st.title("Streamlit ↔️ React (Recharts) — Minimal Embed")

st.markdown(
    """
This example shows how to pass **Python data** into a **React Recharts** component and render it inside a Streamlit app.

- The React app (built with **Vite**) lives under `components/recharts/frontend/`.
- Build outputs are copied into `components/recharts/frontend_dist/`.
- The Python wrapper (`components/recharts/__init__.py`) exposes a `recharts(...)` function.
"""
)

# --- Sample data (Python side) ------------------------------------------------
df = pd.DataFrame(
    [
        {"month": "Jan", "sales": 120_000, "target": 100_000},
        {"month": "Feb", "sales": 95_000,  "target": 110_000},
        {"month": "Mar", "sales": 135_000, "target": 120_000},
        {"month": "Apr", "sales": 160_000, "target": 130_000},
        {"month": "May", "sales": 150_000, "target": 140_000},
    ]
)

# --- Simple controls to show prop → React behavior ---------------------------
left, right = st.columns(2)
with left:
    kind = st.selectbox("Chart type", ["line", "bar", "area"], index=0)
with right:
    show_target = st.checkbox("Show target (right axis)", value=True)

st.markdown("### Data preview")
st.dataframe(df, use_container_width=True)

# --- Build series prop for the React component -------------------------------
series = [
    {"type": kind, "dataKey": "sales",  "name": "Sales",  "stroke": "#2563eb", "fill": "#93c5fd", "yAxisId": "left"},
]
if show_target:
    # draw target on the right axis as bars (to demonstrate dual-axis support)
    series.append({"type": "bar", "dataKey": "target", "name": "Target", "fill": "#fde68a", "yAxisId": "right"})

st.markdown("### Recharts (rendered by React)")
recharts(
    data=df.to_dict("records"),   # JSON-serializable records
    xKey="month",
    series=series,                # see above
    kind=kind,                    # default series type
    height=320,
    key="demo_chart",
)

st.caption(
    "Tip: The chart above is a React component running inside Streamlit. "
    "Update the controls to see props passed from Python → React."
)
