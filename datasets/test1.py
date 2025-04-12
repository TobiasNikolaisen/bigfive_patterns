import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("/Users/tobiasnikolaisen/Documents/Github/HEL8048/bigfive_patterns/datasets/merged_output.csv")

# Traits to plot
traits = ["extraversion", "openness", "conscientiousness", "neuroticism", "agreeableness"]

# Compare two individuals
id1 = "1"  # Replace with desired ID
id2 = "2"  # Replace with desired ID

person1 = df[df["id"] == id1].iloc[0]
person2 = df[df["id"] == id2].iloc[0]

name1 = person1["name"] if "name" in person1 and pd.notnull(person1["name"]) else f"ID {person1['id']}"
name2 = person2["name"] if "name" in person2 and pd.notnull(person2["name"]) else f"ID {person2['id']}"

scores1 = person1[traits].values
scores2 = person2[traits].values

import numpy as np
x = np.arange(len(traits))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, scores1, width, label=name1)
plt.bar(x + width/2, scores2, width, label=name2)
plt.xticks(ticks=x, labels=[t.capitalize() for t in traits], rotation=30)
plt.xlabel("Trait")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.title(f"Big Five Comparison: {name1} vs {name2}")
plt.legend()
plt.tight_layout()
plt.show()

# Folder to save plots
output_dir = "/Users/tobiasnikolaisen/Documents/Github/HEL8048/bigfive_patterns/results/individual_personality_profiles"

# Loop through each individual
for idx, row in df.iterrows():
    name = row["name"] if "name" in row and pd.notnull(row["name"]) else f"ID {row['id']}"
    
    # Build filename: e.g. Albert_Einstein_profile.png
    safe_base = "_".join(str(name).split())  # Replace spaces with underscores
    safe_base = "".join(c if c.isalnum() or c in "_-" else "_" for c in safe_base)  # Clean filename
    filename = f"{output_dir}/{safe_base}_profile.png"

    # Get trait values
    values = row[traits].values
    
    # Create bar plot
    plt.figure(figsize=(6, 4))
    plt.bar(traits, values)
    plt.ylim(0, 1)
    plt.title(f"Personality Profile: {name}")
    plt.ylabel("Score")
    plt.xlabel("Trait")
    plt.xticks(ticks=range(len(traits)), labels=[t.capitalize() for t in traits], rotation=30)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("merged_output.csv")

# === STEP 1: Define traits and their actual facets from your dataset ===

traits = {
    "extraversion": [
        "active", "assertive", "cheerful",
        "excitement_seeking", "outgoing", "gregariousness"
    ],
    "openness": [
        "adventurous", "artistic", "emotionally_aware",
        "imaginative", "intellectual", "authority_challenging"
    ],
    "conscientiousness": [
        "cautious", "disciplined", "dutiful",
        "achievement_striving", "orderliness", "self_efficacy"
    ],
    "neuroticism": [
        "melancholy", "self_conscious", "stress_prone",
        "fiery", "prone_to_worry", "immoderation"
    ],
    "agreeableness": [
        "cooperative", "trusting", "altruism",
        "modesty", "uncompromising", "sympathy"
    ]
}
# === STEP 2: Correlation matrix of the main traits ===

main_traits = list(traits.keys())
main_trait_corr = df[main_traits].corr()

print("Correlation matrix for main Big Five traits:")
print(main_trait_corr)

plt.figure(figsize=(6, 5))
sns.heatmap(main_trait_corr, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar=True,
            vmin=-1, vmax=1)
plt.title("Correlation between Big Five traits")
plt.tight_layout()
plt.show()
# === STEP 3: Correlation matrix within each trait's facets ===

for trait, facets in traits.items():
    facets_present = [f for f in facets if f in df.columns]
    if len(facets_present) <= 1:
        continue

    facet_data = df[facets_present]

    # Compute correlation matrix; NaNs occur for constant columns
    corr = facet_data.corr(numeric_only=True, method="pearson", min_periods=1)
    corr_display = corr.fillna(0)

    print(f"\nCorrelation matrix for {trait.title()} facets:")
    print(corr)

    plt.figure(figsize=(7, 6))
    sns.heatmap(corr_display, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar=True,
                vmin=-1, vmax=1)
    plt.title(f"Facet correlations for {trait.title()}")
    plt.tight_layout()
    plt.show()
