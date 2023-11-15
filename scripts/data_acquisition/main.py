import os
import zipfile
import gdown

def download_file():
        
    try: 
        dataset_url = "https://drive.google.com/file/d/1Dv8-CCtxS-W-x5JygLgd0UIZlvlhcQBf/view?usp=sharing"
        zip_download_dir = "kidney_tumor_dataset.zip"
        os.makedirs("data/data_ingestion", exist_ok=True)

        file_id = dataset_url.split("/")[-2]
        prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(prefix+file_id,zip_download_dir)

    except Exception as e:
        raise e
        
    
def extract_zip_file():
    
    unzip_path = "data/data_ingestion"
    os.makedirs(unzip_path, exist_ok=True)
    with zipfile.ZipFile(zip_download_dir, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)