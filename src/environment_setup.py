#Task 1: Environment Setup Verification

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


def check_environment():
    data = {
        "Library Name": ["NumPy", "Pandas", "Matplotlib", "Seaborn"],
        "Version": [
            np.__version__,
            pd.__version__,
            plt.matplotlib.__version__,
            sns.__version__
        ]
    }

    df = pd.DataFrame(data)

    print("=" * 60)
    print("ENVIRONMENT SETUP VERIFICATION")
    print("=" * 60)
    print(df)

    df.to_csv("output/library_versions.csv", index=False)

    print("\nStatus: Environment verified successfully ")


if __name__ == "__main__":
    check_environment()