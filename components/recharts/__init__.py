import os
import streamlit.components.v1 as components
from typing import List, Dict, Any, Optional

# We serve built assets from frontend_dist
_BUILD_DIR = os.path.join(os.path.dirname(__file__), "frontend_dist")
_recharts = components.declare_component("recharts_component", path=_BUILD_DIR)

def recharts(
    data: List[Dict[str, Any]],
    xKey: str,
    series: List[Dict[str, Any]],
    kind: str = "line",
    height: int = 320,
    key: Optional[str] = None,
):
    """
    Render a Recharts chart.

    Args:
      data: list of dict records
      xKey: field name for X axis
      series: list of dicts, e.g. [{"type":"line","dataKey":"AR","name":"AR","yAxisId":"left","stroke":"#2563eb"}, ...]
      kind: default chart type ("line" | "bar" | "area")
      height: pixels
    """
    return _recharts(data=data, xKey=xKey, series=series, kind=kind, height=height, key=key, default=None)
