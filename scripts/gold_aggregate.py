import pandas as pd
from pathlib import Path

def run_gold_aggregate(**context):
    silver_file = context["ti"].xcom_pull(
        key="silver_file", task_ids="silver_transform"
    )

    if not silver_file:
        raise ValueError("Silver file not found in xcom")

    df = pd.read_csv(silver_file, on_bad_lines='skip')  # ← skip bad rows

    agg = (
        df.groupby("origin_country")
        .agg(
            total_flights=("icao24", "count"),
            avg_velocity=("velocity", "mean"),
            on_ground=("on_ground", "sum")
        )
        .reset_index()
    )

    gold_path = Path(silver_file.replace("silver", "gold"))
    gold_path.parent.mkdir(parents=True, exist_ok=True)  # ← make sure folder exists

    agg.to_csv(gold_path, index=False)
    context["ti"].xcom_push(key="gold_file", value=str(gold_path))