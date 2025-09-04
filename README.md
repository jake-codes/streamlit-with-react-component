# Streamlit + React (Recharts) Demo

This repo is a **minimal example of embedding a React component inside a Streamlit app**.  
It uses [Recharts](https://recharts.org/) (a React charting library) to render charts inside Streamlit via the [Streamlit Components API](https://docs.streamlit.io/library/components).

---

## 🚀 What this shows
- A **Streamlit app (`app.py`)** written in Python.
- A **React frontend (Vite + React + Recharts)** living under `components/recharts/frontend/`.
- A **Python wrapper** (`components/recharts/__init__.py`) that declares the custom component and passes props/data.
- Data created in Python (`pandas`) → rendered as charts in React → displayed in Streamlit.

---

## 🗂 Project structure
├── app.py # Minimal Streamlit app embedding React
├── components/
│ └── recharts/
│ ├── init.py # Python bridge (declares component)
│ ├── frontend/ # React (Vite + Recharts) source
│ │ ├── package.json
│ │ ├── vite.config.js
│ │ ├── index.html
│ │ └── src/
│ │ ├── RechartsHost.jsx
│ │ └── main.jsx
│ └── frontend_dist/ # Build output (copied by Dockerfile)
├── requirements.txt # Python deps
├── Dockerfile # Multi-stage build (Node + Python)
├── docker-compose.yml
└── README.md


---
## ✅ Requirements

Before using the Makefile commands, ensure you have:

- [Docker](https://docs.docker.com/get-docker/) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) (v2 or newer, bundled with recent Docker Desktop)  
- [GNU Make](https://www.gnu.org/software/make/) installed  
  - macOS: `brew install make`  
  - Ubuntu/Debian: `sudo apt-get install make`  
  - Windows: use [WSL](https://learn.microsoft.com/en-us/windows/wsl/) or Git Bash  

---

## Commands

- **Build the image**
  ```bash
  make build

```
- **Start the app**
  ```bash
  make up

```
- **Stop the app**
  ```bash
  make build

```