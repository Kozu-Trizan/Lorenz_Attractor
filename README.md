# Lorenz Attractor

A small Python simulation and Matplotlib animation of the Lorenz attractor (chaotic system).

This repository contains a simple explicit-Euler integrator and an animated 3D plot demonstrating sensitivity to initial conditions.

Contents
- `Lorenz_attractor.py` — main simulation and animation script.

Requirements
- Python 3.8+
- numpy
- matplotlib

Install dependencies (recommended inside a virtual environment):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install numpy matplotlib
```

Run

From the project root run:

```bash
python Lorenz_Attractor/Lorenz_attractor.py
```

Notes & parameters
- The script uses three core parameters at the top of the file: `SIGMA`, `RHO`, `BETA`.
- Time integration is explicit Euler; chaotic systems can grow large or diverge if parameters or timestep are unsuitable. If you see overflow/NaN warnings, reduce `dt`, shorten total simulated time, or revert to standard parameters (SIGMA=10, RHO=28, BETA=8/3).
- Initial conditions are in the `states` list — the attractor illustrates sensitivity to small changes in these values.

Lorenz attractor simulation — visual demo below.

![Lorenz attractor demo](Lorenz_Attractor/lorenz_attractor.gif)

```bash
Lorenz_Attractor/Lorenz_attractor.py
```

License

MIT License
