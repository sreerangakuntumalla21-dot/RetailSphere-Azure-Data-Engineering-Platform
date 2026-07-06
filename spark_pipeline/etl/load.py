import os
import pandas as pd


def export_csv(df, filename):

    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    path = os.path.join(output_folder, filename)

    if isinstance(df, pd.DataFrame):
        df.to_csv(path, index=False)
    else:
        df.toPandas().to_csv(path, index=False)

    print(f"✅ {filename} exported successfully!")