from script import save_to_markdown
from mylib.lib import load_dataset

# Data
dataset_path = "https://raw.githubusercontent.com/fivethirtyeight/data/master/urbanization-index/urbanization-census-tract.csv"


def test_writing_markdown():
    """Testing writing markdown file"""
    df = load_dataset(dataset_path)
    result = save_to_markdown(df)
    assert result == "Markdown written successfully"


if __name__ == "__main__":
    test_writing_markdown()
    print("Test completed successfully")
