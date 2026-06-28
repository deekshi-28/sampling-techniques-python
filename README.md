# Sampling Techniques using Python

## Project Overview

This project demonstrates various **sampling techniques** used in data analytics and statistics using **Python**, **Pandas**, **NumPy**, and **Scikit-learn**. It illustrates how to extract representative samples from a dataset using different sampling methods and compare their characteristics.

The project covers four commonly used sampling techniques:

* Simple Random Sampling
* Systematic Sampling
* Cluster Sampling
* Stratified Random Sampling

---

## Objectives

* Load and explore a dataset using Pandas.
* Perform Simple Random Sampling.
* Perform Systematic Sampling.
* Perform Cluster Sampling.
* Perform Stratified Random Sampling.
* Calculate and compare the mean Sale Price of different samples.

---

## Technologies Used

* Python 3.x
* Pandas
* NumPy
* Scikit-learn
* VS Code

---

## Project Structure

```text
Sampling/
│
├── Dataset.csv
├── sampling.py
└── README.md
```

---

## Dataset

The dataset contains information about house sales.

Required columns:

| Column    | Description         |
| --------- | ------------------- |
| Id        | Unique House ID     |
| SalePrice | House Selling Price |

---

## Sampling Techniques

### 1. Simple Random Sampling

Simple Random Sampling randomly selects records from the entire dataset, ensuring each record has an equal probability of being chosen.

```python
simpleRandomSample = dataset.sample(n=5)
```

---

### 2. Systematic Sampling

Systematic Sampling selects every **k-th** record from the dataset.

Example:

```python
index = np.arange(0, len(dataset), step=3)
```

This selects every third record.

---

### 3. Cluster Sampling

Cluster Sampling divides the dataset into equal-sized clusters and selects entire clusters instead of individual records.

Example:

```python
dataset["cluster_id"]
```

The project selects all even-numbered clusters.

---

### 4. Stratified Random Sampling

Stratified Sampling divides the population into homogeneous groups (strata) and randomly selects records from each group.

This project uses:

```python
StratifiedShuffleSplit()
```

to generate balanced samples from each stratum.

---

## Features

* Dataset exploration and statistical summary.
* Random selection of samples.
* Systematic interval-based sampling.
* Cluster-based sampling.
* Stratified random sampling using Scikit-learn.
* Mean calculation for sampled datasets.

---

## Sample Output

```text
===== Dataset Shape =====
(20, 2)

===== Statistical Summary =====
...

===== Simple Random Sampling =====
Mean of Simple Random Sample: 182450.25

===== Systematic Sampling =====
Mean of Systematic Sample: 179325.60

===== Cluster Sampling =====
Mean of Cluster Sample: 185710.80

===== Stratified Sampling =====
...
```

---

## Installation

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

---

## How to Run

### Clone the Repository

```bash
git clone https://github.com/<your-username>/sampling-techniques-python.git
```

### Navigate to the Project Folder

```bash
cd sampling-techniques-python
```

### Run the Program

```bash
python sampling.py
```

or

```bash
py sampling.py
```

---

## Learning Outcomes

After completing this project, you will understand:

* Population vs Sample
* Importance of Sampling
* Random Sampling Techniques
* Systematic Sampling
* Cluster Sampling
* Stratified Sampling
* Data analysis using Pandas and NumPy
* Practical use of Scikit-learn for sampling

---

## Future Enhancements

* Add user input for sample size.
* Visualize sampled data using Matplotlib.
* Compare sampling methods using graphs.
* Export sampled datasets to CSV files.
* Support larger real-world datasets.

---

## Author

**Name:** Deekshitha U

**Course:** B.Tech – Artificial Intelligence and Data Science

**Project:** Sampling Techniques using Python
