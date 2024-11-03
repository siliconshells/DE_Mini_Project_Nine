import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(dataset):
    """loads the data"""
    df = pd.read_csv(dataset)
    return df


# Summary Statistics
def calculate_summaries(
    data,
    column_one,
    column_one_heading,
    column_two,
    column_two_heading,
    set_first_column_index=False,
) -> pd.DataFrame:
    """Generates the statistics"""
    stats_list = []
    stats_list.append(["Count", data[column_one].count(), data[column_two].count()])
    stats_list.append(["Mean", data[column_one].mean(), data[column_two].mean()])
    stats_list.append(["Median", data[column_one].median(), data[column_two].median()])
    stats_list.append(["Max", data[column_one].max(), data[column_two].max()])
    stats_list.append(["Min", data[column_one].min(), data[column_two].min()])
    stats_list.append(
        ["Standard Deviation", data[column_one].std(), data[column_two].std()]
    )

    stats_df = pd.DataFrame(stats_list)

    stats_df.rename(
        columns={0: "Statistic", 1: column_one_heading, 2: column_two_heading},
        inplace=True,
    )
    # Necessary if we want to reference a row by the statistic's name
    if set_first_column_index:
        stats_df.set_index("Statistic", inplace=True)

    return stats_df


# Data Visualization
def create_bar_chart(
    data: pd.DataFrame, title, xLabel, yLabel, save_chart: bool, save_path=""
):
    data.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend(title="States")
    if save_chart:
        plt.tight_layout()
        plt.savefig(save_path)
    else:
        plt.show()


def create_histogram(data, column, title, yLabel, save_chart: bool, save_path=""):
    plt.hist(data[column], edgecolor="gray", bins=200)
    plt.title(title)
    plt.xlabel(column.capitalize())
    plt.ylabel(yLabel)
    if save_chart:
        plt.savefig(save_path)
    else:
        plt.show()
