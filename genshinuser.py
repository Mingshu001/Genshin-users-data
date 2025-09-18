import matplotlib.pyplot as plt

# Simulated RPD (Revenue Per Download) data for Genshin Impact (2021-2024)
years = [2021, 2022, 2023, 2024]
RPD = [35, 45, 62, 58]  # USD, based on article trend

plt.figure(figsize=(8, 5))
plt.plot(years, RPD, marker='o', color='purple', linewidth=2)
plt.title('Genshin Impact 90-day RPD Trend (2021-2024)')
plt.xlabel('Year')
plt.ylabel('90-day RPD (USD)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()