# Nextflow Metabolomics Analysis Pipeline

A lightweight, reproducible **Nextflow pipeline** for metabolomics data analysis using publicly available data from the MTBLS1 study.

This project demonstrates how to design and execute a modular data pipeline for biological data using **Nextflow + Conda**, including data cleaning, normalisation, statistical analysis, and visualisation.

---

## 🚀 Overview

This pipeline processes metabolomics data through the following steps:

1. **Data Cleaning**
2. **Normalisation**
3. **PCA (Principal Component Analysis)**
4. **Differential Analysis (t-test)**

The workflow is fully reproducible and designed to reflect real-world bioinformatics pipelines.

---

## 🧬 Dataset

- Source: [MetaboLights MTBLS1](https://www.ebi.ac.uk/metabolights/MTBLS1)
- Type: Processed LC-MS metabolomics data (TSV format)

---

## ⚙️ Pipeline Architecture

The pipeline is built using Nextflow DSL2 and follows a modular structure:

📊 See workflow diagram:

<img width="496" height="251" alt="flowchart" src="https://github.com/user-attachments/assets/ad5aa36e-fb54-4f13-a10f-5662d06e2833" />


## 🛠️ Technologies Used

- **Nextflow (DSL2)** – workflow orchestration  
- **Python** – data processing & analysis  
- **Pandas / NumPy** – data manipulation  
- **Scikit-learn** – PCA  
- **SciPy** – statistical testing  
- **Matplotlib** – visualisation  
- **Conda** – reproducible environments  

---

## ▶️ Running the Pipeline

### 1. Install Nextflow

```bash
curl -s https://get.nextflow.io | bash
```

### 2. Run the pipeline

```bash
nextflow run main.nf
```

### 3. Optional: Generate reports

```bash
nextflow run main.nf -with-report report.html -with-timeline timeline.html
```

---
## 📊 Outputs

The pipeline produces:

clean.csv – cleaned metabolomics data

normalized.csv – scaled intensity values

pca.png – PCA plot of samples

differential_metabolites.csv – statistical results

---

## 📈 Example Results
PCA Plot
