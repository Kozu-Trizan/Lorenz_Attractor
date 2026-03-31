# Lorenz Attractor

A small Python simulation and Matplotlib animation of the Lorenz attractor (chaotic system).

This repository contains a simple explicit-Euler integrator and an animated 3D plot demonstrating sensitivity to initial conditions.

Contents
- `Lorenz_attractor.py` — main simulation and animation script.
- `Lorenz_attractor_rk4.py` — RK4 integrator version (higher-order solver) for improved stability.

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

From the project root, you can run the Euler version:

```bash
python Lorenz_Attractor/Lorenz_attractor.py
```

Or for significantly better numerical stability, run the Runge-Kutta 4 (RK4) version:

```bash
python Lorenz_Attractor/Lorenz_attractor_rk4.py
```

Notes & parameters
- The scripts use three core parameters at the top of the file: `SIGMA`, `RHO`, `BETA`.
- The `Lorenz_attractor.py` script uses explicit Euler integration. The `Lorenz_attractor_rk4.py` script uses a proper 4th-order Runge-Kutta method, which improves accuracy and remains stable over much longer runtimes (`DUR = 100`) without causing exponential blowup to `NaN` and `Inf` limits.
- Initial conditions are in the `states` list — the attractor illustrates sensitivity to small changes in these values.


[Script — Euler](Lorenz_Attractor/Lorenz_attractor.py#L1)
[Script — RK4](Lorenz_Attractor/Lorenz_attractor_rk4.py#L1)

License

MIT License
