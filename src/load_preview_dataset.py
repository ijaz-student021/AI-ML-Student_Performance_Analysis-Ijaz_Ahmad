import pandas as pd


def load_and_preview_dataset():
    file_path = "data/StudentsPerformance.csv"

    df = pd.read_csv(file_path)

    print("=" * 60)
    print("FIRST 10 ROWS OF THE DATASET")
    print("=" * 60)
    print(df.head(10))

    print("=" * 60)
    print("LAST 5 ROWS OF THE DATASET")
    print("=" * 60)
    print(df.tail(5))

    print("=" * 60)
    print("RANDOM SAMPLE OF 8 ROWS")
    print("=" * 60)
    print(df.sample(8, random_state=42))

    # Save outputs
    df.head(10).to_csv("output/head_10.csv", index=False)
    df.tail(5).to_csv("output/tail_5.csv", index=False)
    df.sample(8, random_state=42).to_csv("output/sample_8.csv", index=False)

    print("\nPreview files saved in output folder successfully ")


if __name__ == "__main__":
    load_and_preview_dataset()