from mylib.lib import (
    load_dataset,
    calculate_summaries,
    create_bar_chart,
    create_histogram,
)

# Data
dataset_path = "https://raw.githubusercontent.com/fivethirtyeight/data/master/urbanization-index/urbanization-census-tract.csv"


# saving markdown
def save_to_markdown(data) -> str:
    with open("population_summary.md", "w") as file:
        file.write("# Population Summaries\n")
        file.write(
            calculate_summaries(
                data, "population", "Population", "urbanindex", "Urban Index"
            ).to_markdown()
        )
        file.write("\n\n")
        file.write("# Population Histogram")
        file.write("\n\n")
        file.write("![population_histogram](population_histogram.png)")
        file.write("\n\n")
        file.write("# Population Bar Chart")
        file.write("\n\n")
        file.write("![population_bar](population_bar.png)")
    return "Markdown written successfully"


def save_histogram(df):
    """Create histogram to file"""
    create_histogram(
        df,
        "population",
        "Population across areas in the U.S.",
        "Frequency",
        True,
        "population_histogram.png",
    )


def save_bar_chart(df):
    """Create bar chart to file"""
    population_sums = df.groupby(["state"])["population"].sum()
    create_bar_chart(
        population_sums,
        "Populations for U.S. states",
        "States",
        "Populations",
        True,
        "population_bar.png",
    )


if __name__ == "__main__":
    df = load_dataset(dataset_path)
    save_histogram(df)
    save_bar_chart(df)
    """Save markdown"""
    save_to_markdown(df)
