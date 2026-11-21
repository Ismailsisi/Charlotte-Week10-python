"""Week 10 Class 2 — student practical."""

from pathlib import Path
import pandas as pd

INPUT_FILE = Path(__file__).with_name("daily_production.csv")
OUTPUT_FILE = Path(__file__).parent / "outputs" / "production_enriched.csv"


def load_production(path: Path = INPUT_FILE) -> pd.DataFrame:
    """Read input CSV and parse the date column."""
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def enrich_production(df: pd.DataFrame) -> pd.DataFrame:
    """Add total liquid and pressure in kPa."""
    enriched_df = df.copy()

    enriched_df["total_liquid_bpd"] = (
        enriched_df["oil_bpd"] + enriched_df["water_bpd"]
    )

    enriched_df["pressure_kpa"] = (
        enriched_df["pressure_psi"] * 6.8947572932
    )

    return enriched_df


def select_producing(df: pd.DataFrame) -> pd.DataFrame:
    """Select producing observations."""
    producing_df = df[df["status"] == "PRODUCING"].copy()
    return producing_df


def data_quality_counts(df: pd.DataFrame) -> dict:
    """Count missing readings and unique wells."""
    quality_counts = {
        "missing_oil_readings": df["oil_bpd"].isna().sum(),
        "missing_pressure_readings": df["pressure_psi"].isna().sum(),
        "unique_wells": df["well_id"].nunique()
    }

    return quality_counts


def main() -> None:
    """Load, inspect and export production data."""
    df = load_production()

    print("Data Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Quality Counts:")
    print(data_quality_counts(df))

    producing_df = select_producing(df)

    print("\nProducing Observations:")
    print(len(producing_df))

    enriched_df = enrich_production(df)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    enriched_df.to_csv(OUTPUT_FILE, index=False)

    print("\nEnriched CSV saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()