# Monte Carlo Simulation for Insurance Risk

This Python project simulates aggregate annual losses for a non-life insurance portfolio using a compound distribution:

- **Frequency**: Poisson distribution for the number of claims
- **Severity**: Mixture of Gamma (moderate claims) and Pareto (catastrophic claims)
- **Risk metrics**: Value-at-Risk (VaR), Tail Value-at-Risk (TVaR), histograms

---

## Purpose

To explore the impact of heavy-tailed losses in actuarial modeling and quantify potential extreme risks using stochastic methods.

---

## Key Concepts

- Monte Carlo simulation
- Mixed distributions (Gamma + Pareto)
- Heavy-tailed risk modeling
- Quantile-based risk metrics

---

## Structure

- `MonteCarlo-main.py` – main script for running simulations
- `README.md` – project overview and context
- `plots/` – optional folder for output visualizations

---

## Requirements

- Python 3.9+
- `numpy`, `pandas`, `matplotlib`

```bash
pip install numpy pandas matplotlib