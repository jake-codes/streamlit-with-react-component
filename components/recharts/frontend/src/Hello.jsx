import React from "react";
import { Streamlit, withStreamlitConnection, StreamlitComponentBase } from "streamlit-component-lib";

class Hello extends StreamlitComponentBase {
  componentDidMount() { Streamlit.setFrameHeight(); }
  componentDidUpdate() { Streamlit.setFrameHeight(); }

  render() {
    const message = this.props.args?.message ?? "Hello from React 👋";
    const accent = this.props.args?.accent ?? "#0ea5e9"; // sky-500
    const size = this.props.args?.size ?? 18;

    return (
      <div style={{
        fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif",
        border: `1px solid ${accent}33`,
        background: `${accent}0d`,
        color: "#0f172a",
        borderRadius: 12, padding: 12, fontSize: size
      }}>
        <strong style={{ color: accent }}>HelloReact:</strong> {message}
      </div>
    );
  }
}

export default withStreamlitConnection(Hello);
