# PINN: Nitrate-Leaching Research Skeleton

This folder contains a starter skeleton for a Physics-Informed Neural Network (PINN)
project to predict high-resolution nitrate leaching in agricultural fields.

Contents:
- `SUCCESS_CRITERIA.md` — concise success criteria for the MSc project.
- `SKILLS.md` — list of skills to learn (math, coding, ML, domain, GIS).
- `12_week_plan.md` — a compact 12-week plan to build the prototype.
- `environment.yml` — conda environment to reproduce experiments.
- `templates/` — small templates (config.yml, notebook stub).
- `reproduce_main.py` — minimal runner stub to satisfy reproducibility.

How to use:
1. Create/activate env: `conda env create -f PINN/environment.yml`
2. Edit `PINN/config.yml` to set paths, then run:
   `python PINN/reproduce_main.py --config PINN/templates/config.yml`
3. Use this skeleton as a starting point for your MSc work.
