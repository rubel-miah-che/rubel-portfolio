# Success criteria (short)

- **Accuracy (RMSE):** RMSE on spatial holdout ≤ 10% of mean observed nitrate.
- **Parameter recovery:** Relative error ≤ 10% on synthetic inverse tests (≤ 20–30% under realistic noise).
- **Uncertainty (coverage):** 90% predictive interval empirical coverage ~ 85–95%.
- **Exceedance detection:** F1 score ≥ 0.7 for classifying concentration > threshold T (mg/L).
- **Spatial generalization:** Holdout-site RMSE ≤ 1.2 × training RMSE.
- **Data efficiency:** With 25% sensors, RMSE ≤ 2 × RMSE(full sensors).
- **Physical consistency:** No significant negative concentrations; mass-balance error ≤ 5%.
- **Reproducibility:** Main experiment reproducible with `python reproduce_main.py --config PINN/templates/config.yml`.
