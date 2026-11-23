"""Week 10 Class 3 Homework — Pandas extension."""

from pathlib import Path
import pandas as pd

INPUT_FILE = Path(__file__).with_name("production_surveillance.csv")


def valid_active_oil_observations(df):
    """Select valid ACTIVE oil observations."""
    mask = (
        (df["status"] == "ACTIVE")
        & (df["oil_bbl"].notna())
        & (df["oil_bbl"] >= 0)
    )

    valid_df = df.loc[mask].copy()

    return valid_df


def top_three_active_oil(df):
    """Return the three largest valid ACTIVE oil observations."""
    valid_df = valid_active_oil_observations(df)

    top_three = valid_df.sort_values(
        by=["oil_bbl", "well_id", "date"],
        ascending=[False, True, True]
    )

    return top_three.head(3).copy()


def add_well_oil_share_pct(df):
    """Calculate each valid observation's share of its well's oil."""
    valid_df = valid_active_oil_observations(df)

    well_oil_total = valid_df.groupby("well_id")["oil_bbl"].transform("sum")

    valid_df["well_oil_share_pct"] = (
        valid_df["oil_bbl"] / well_oil_total * 100
    ).where(well_oil_total != 0)

    return valid_df


def field_well_oil_pivot(df):
    """Create a pivot table of oil totals by field and well."""
    valid_df = valid_active_oil_observations(df)

    pivot_table = valid_df.pivot_table(
        index="field",
        columns="well_id",
        values="oil_bbl",
        aggfunc="sum"
    )

    return pivot_table


def main():
    df = pd.read_csv(INPUT_FILE, parse_dates=["date"])

    print("Top Three ACTIVE Oil Observations:")
    print(top_three_active_oil(df)[
        ["record_id", "date", "well_id", "oil_bbl"]
    ])

    print("\nWell Oil Share Percentages:")
    share_df = add_well_oil_share_pct(df)
    print(share_df[
        ["record_id", "well_id", "oil_bbl", "well_oil_share_pct"]
    ])

    print("\nOil Totals by Field and Well:")
    print(field_well_oil_pivot(df))


if __name__ == "__main__":
    main()