import { defineConfig } from "vite";
export default defineConfig({
  // IMPORTANT: relative asset paths so Streamlit can serve from its mount point
  base: "",
  build: { outDir: "dist" },
});
