import React, { useEffect } from "react";
import { withStreamlitConnection, StreamlitComponentBase, Streamlit } from "streamlit-component-lib";
import {
  ResponsiveContainer, LineChart, Line, BarChart, Bar, AreaChart, Area,
  CartesianGrid, XAxis, YAxis, Tooltip, Legend
} from "recharts";

class RechartsHost extends StreamlitComponentBase {
  componentDidMount() { Streamlit.setFrameHeight(); }
  componentDidUpdate() { Streamlit.setFrameHeight(); }

  render() {
    const args = this.props.args || {};
    const data = args.data || [];               // list of records
    const xKey = args.xKey || "x";              // field for X axis
    const series = args.series || [];           // [{ type: "line"|"bar"|"area", dataKey, name?, yAxisId?, stroke?, fill? }]
    const kind = args.kind || "line";           // default chart type
    const height = args.height || 320;
    const yRight = series.some(s => s.yAxisId === "right");

    const Chart = kind === "bar" ? BarChart : kind === "area" ? AreaChart : LineChart;

    return (
      <div style={{ width: "100%", height }}>
        <ResponsiveContainer>
          <Chart data={data} margin={{ top: 10, right: 20, left: 0, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={xKey} />
            <YAxis yAxisId="left" />
            {yRight && <YAxis yAxisId="right" orientation="right" />}
            <Tooltip />
            <Legend />
            {series.map((s, i) => {
              const common = {
                key: i, dataKey: s.dataKey, name: s.name || s.dataKey,
                stroke: s.stroke, fill: s.fill, yAxisId: s.yAxisId || "left",
                type: "monotone"
              };
              if (s.type === "bar" || (kind === "bar" && !s.type)) return <Bar {...common} />;
              if (s.type === "area" || (kind === "area" && !s.type)) return <Area {...common} dot={false} />;
              return <Line {...common} dot={false} />;
            })}
          </Chart>
        </ResponsiveContainer>
      </div>
    );
  }
}

export default withStreamlitConnection(RechartsHost);
