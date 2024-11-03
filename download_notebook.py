import os.path
import gdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(BASE_DIR, "Downloaded_Notebook.ipynb")


def download_notebook(
    file_id: str,
):
    """ "Download Notebook to a file path"""
    gdown.download(f"https://drive.google.com/uc?id={file_id}", "Downloaded_Notebook.ipynb", quiet=False)
    return "Download Successful"


if __name__ == "__main__":
    fileid="1z7n6Kh3i_gyrFDlgFQk_zKyxmyB82Z7m"
    dataset = download_notebook(fileid)