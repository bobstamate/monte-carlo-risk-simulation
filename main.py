import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulation Parameters
num_simulations = 10000
portfolio_size = 1000
lambda_poisson = 2  # Expected number of claims per year

# Severity Distribution Parameters
gamma_shape = 2.0
gamma_scale = 3000.0  # Mean = shape * scale = 6000

pareto_scale = 10000.0  # xm
pareto_alpha = 1.5      # Heavy tail: E[X] = (α * xm)/(α - 1) = 30,000

#Mixed severity function (95% Gamma, 5% Pareto)
def mixed_severity(n):
    severities = []
    for _ in range(n):
        p = np.random.uniform()
        if p <= 0.95:
            severity = np.random.gamma(shape=gamma_shape, scale=gamma_scale)
        else:
            # Inverse transform sampling for Pareto
            u = np.random.uniform()
            severity = pareto_scale / (u ** (1 / pareto_alpha))
        severities.append(severity)
    return severities

# Simulate number of claims per year
claim_counts = np.random.poisson(lam=lambda_poisson, size=num_simulations)

#Simulate total annual losses
total_losses = []
for count in claim_counts:
    if count > 0:
        losses = mixed_severity(count)
        total_losses.append(np.sum(losses))
    else:
        total_losses.append(0)

# Store results in DataFrame
results_df = pd.DataFrame({
    'simulation': range(num_simulations),
    'num_claims': claim_counts,
    'total_loss': total_losses
})

#  Risk metrics
mean_loss = results_df['total_loss'].mean()
var_95 = np.percentile(results_df['total_loss'], 95)
var_99 = np.percentile(results_df['total_loss'], 99)
tvar_99 = results_df[results_df['total_loss'] > var_99]['total_loss'].mean()

# Print summary
print(f"Mean annual loss: €{mean_loss:,.2f}")
print(f"Value at Risk (95%): €{var_95:,.2f}")
print(f"Value at Risk (99%): €{var_99:,.2f}")
print(f"Tail Value at Risk (99%): €{tvar_99:,.2f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(results_df['total_loss'], bins=60, color='skyblue', edgecolor='black')
plt.axvline(var_95, color='orange', linestyle='dashed', linewidth=2, label=f'VaR 95% ≈ €{var_95:,.0f}')
plt.axvline(var_99, color='red', linestyle='dashed', linewidth=2, label=f'VaR 99% ≈ €{var_99:,.0f}')
plt.title('Simulated Annual Aggregate Loss Distribution\nwith 5% Catastrophic Loss Component')
plt.xlabel('Total Loss (€)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()