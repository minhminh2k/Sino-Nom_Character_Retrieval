# Sino-Nom_Character_Retrieval

## Contributors

- Dương Quang Minh - 21020219
- Dương Bảo Long - 21021514
- Vũ Thành Long - 21020647

## Goals

This repository finds the five 3D models from a given database with the highest similarity to the 2D query image.

## Description

Mid-Term Project for Image Processing Class INT3404E 20.

This repo was made by UET-VNU students.

Topic: Sino-Nom Character Retrieval with input is a 2D query image, and output is the five 3D models from a given database with the highest similarity.

Some implemented methods: Histogram of oriented gradient (HOG), Scale-invariant feature transform (SIFT), Oriented FAST and Rotated BRIEF (ORB), Structural Similarity, Template matching.

## Download the dataset

```bash
gdown --id 1_9NPC8E-kt4pU6rTi5lkh91eFR_jnFav
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/minhminh2k/Sino-Nom_Character_Retrieval.git
   ```

2. Change the directory:

   ```
   cd Sino-Nom_Character_Retrieval
   ```

3. Create a conda environment and install dependencies:

   ```
   conda create -p ./env python=3.10
   ```

4. Activate the conda environment:

   ```
   conda activate ./env
   ```

5. Install necessary dependencies

   ```
   pip install -r requirements.txt
   ```

## Evaluation: 2D-3D retrieval

```
    python task3.py --gt_csv GT_PATH --pred_csv PRED_PATH
```

where

- GT_PATH: the directory contains test grounth-truth file (\*.csv)
- PRED_PATH: the directory contains your prediction file (\*.csv)

## Structure of repository

The directory structure

```
├── data                   <- Project data
│
├── report                 <- Folder containing the report
│
├── results                <- Results of all methods
│   ├── database                 <- Results of all methods in the database dataset
│   ├── pairs                    <- Results of all methods in the pairs dataset
│
├── 2d-3d-all-method.ipynb       <- The jupyter notebook contains all methods
│
├── 2d-3d-retrieval-final.ipynb  <- The jupyter notebook contains the template matching method for the final evaluation
│
├── task3.py                  <- Run evaluation
│
├── .gitignore                <- List of files ignored by git
├── requirements.txt          <- File for installing python dependencies
└── README.md
```

## Results

Here are our results obtained from experiments:

| Method            | Database   | Pairs      |
| ----------------- | ---------- | ---------- |
| HOG + Cosine      | **0.8935** | 0.7507     |
| Template matching | 0.8900     | **0.7787** |
| SSIM              | 0.8731     | 0.7550     |
| ORB               | 0.7603     | 0.7617     |
| SIFT              | 0.7743     | 0.7145     |

## Report

- [Abstract Report](report/Mid_term_Phase_2_Image_Processing_group11.pdf)
- [Mid-term Phase 2 Report](report/Mid_term_Phase_2_Image_Processing_group11.pdf)
