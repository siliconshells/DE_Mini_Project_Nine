from mylib.lib import load_dataset, calculate_summaries
from script import save_bar_chart, save_histogram
import os

# Data
dataset_path = "https://raw.githubusercontent.com/fivethirtyeight/data/master/urbanization-index/urbanization-census-tract.csv"


def test_data_loading():
    """Testing data loading"""
    dataset = load_dataset(dataset_path)
    assert dataset is not None
    assert dataset.shape == (73280, 8)


def test_summaries():
    # Bringing it into the function because pytest doesn't find it when it comes in as a parameter
    dataset = load_dataset(dataset_path)
    my_calculated_summaries = calculate_summaries(
        dataset, "population", "Population", "urbanindex", "Urban Index", True
    )
    pandas_summaries = dataset.describe()
    assert (
        pandas_summaries.loc["mean", "population"]
        == my_calculated_summaries.loc["Mean", "Population"]
    )
    assert (
        pandas_summaries.loc["std", "population"]
        == my_calculated_summaries.loc["Standard Deviation", "Population"]
    )
    assert (
        pandas_summaries.loc["min", "population"]
        == my_calculated_summaries.loc["Min", "Population"]
    )
    assert (
        pandas_summaries.loc["max", "population"]
        == my_calculated_summaries.loc["Max", "Population"]
    )


def test_file_creation(cleanup=True):
    dataset = load_dataset(dataset_path)
    # Remove existing ones
    if os.path.exists("population_bar.png"):
        os.remove("population_bar.png")
    if os.path.exists("population_histogram.png"):
        os.remove("population_histogram.png")

    # Test and create new ones
    assert not os.path.exists("population_bar.png")
    assert not os.path.exists("population_histogram.png")

    # Interestingly calling the bar chart first makes the histogram save a barchart
    save_histogram(dataset)
    save_bar_chart(dataset)

    assert os.path.exists("population_bar.png")
    assert os.path.exists("population_histogram.png")

    # Clean up
    if cleanup:
        if os.path.exists("population_bar.png"):
            os.remove("population_bar.png")
        if os.path.exists("population_histogram.png"):
            os.remove("population_histogram.png")


if __name__ == "__main__":
    dataset = test_data_loading()
    test_summaries()
    test_file_creation(False)
    print("Test completed successfully")
