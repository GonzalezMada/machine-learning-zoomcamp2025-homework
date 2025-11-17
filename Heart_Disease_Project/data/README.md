# Data acquisition

This project uses the "heart disease dataset" from Kaggle:
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

Option A — Using Kaggle CLI (recommended)
1. Install kaggle CLI:
   pip install kaggle
2. Place your Kaggle API token (kaggle.json) at ~/.kaggle/kaggle.json (chmod 600).
3. Run:
   mkdir -p data
   kaggle datasets download -d johnsmith88/heart-disease-dataset -p data --unzip
4. After unzipping you should find a file like `data/heart.csv`. If the filename differs, rename it to `data/heart.csv`.

Option B — Manual download
1. Go to the dataset URL and download the CSV.
2. Place the CSV in `data/heart.csv`.

File expected: data/heart.csv
- The notebook and scripts assume `data/heart.csv` is present.