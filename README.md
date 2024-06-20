# Digit Predictor Application

## Overview

This is a digit predictor application built with PyQt5 and a pre-trained Support Vector Machine (SVM) model. Users can draw digits on a canvas, and the application will predict the digit based on the drawing.

## Features
- **Interactive Canvas:** Draw digits using the mouse.

- **Prediction Display:** Shows the predicted digit in real-time.

- **Clear Button:** Clear the canvas to draw a new digit.

- **Auto-Prediction:** Predicts the drawn digit every second.
## Requirements
- **Python 3.6+**

- **PyQt5**

- **NumPy**

- **Pillow (PIL)**

- **scikit-learn (for the SVM model)**
## Installation

1. **Clone the repository:**

    ```python
    git clone https://github.com/AsrinTopal/Digit-Predictor.git
    cd Digit-Predictor
    ```

2. **Install the required dependencies:**

    Make sure you have install the requirements.txt file:

    ```python
    pip install -r requirements.txt

    ```
3. **Ensure you have the SVM model file (svm_model.pkl) in the project directory.**
## Usage

1. **Run the application:**

```python
python main.py
```

2. **Draw a digit on the canvas.**

3. **View the prediction displayed below the canvas.**

4. **Clear the canvas using the "CLEAR" button to draw a new digit.**
## Files
**main.py:** Main application file containing the PyQt5 interface and logic.

**svm_model.pkl:** Pre-trained SVM model for digit prediction.

**requirements.txt:** List of required Python packages.

**mnist_loader.py:** Script to load and preprocess MNIST data and train the SVM model.

**mnist.pkl:** Preprocessed MNIST data saved as a pickle file.

**mnist:** Folder for data.

**README.md:** Readme file.
## Project Structure
```graphql
Digit-Predictor/
│
├── mnist                  # Data files
├── main.py                # Main application script
├── mnist.pkl              # Preprocessed MNIST data file
├── mnistExtractor.py      # Extracting MNIST data 
├── mnistTrainer.py        # training script
├── requirements.txt       # Required Python packages
├── svm_model.pkl          # Pre-trained SVM model file
└── README.md              # Readme file
```

## Model Training (Optional)
1. **Prepare the MNIST dataset:** Ensure you have the MNIST data files (train-images.idx3-ubyte, train-labels.idx1-ubyte, t10k-images.idx3-ubyte, t10k-labels.idx1-ubyte) in the project directory.

2. **Run the mnistExtractor.py**

3. **Run the mnistTrainer.py**
## Acknowledgements

- **PyQt5:** Used for building the graphical user interface.
- **scikit-learn:** Used for training and saving the SVM model.
- **Pillow:** Used for image processing.

# Classification Metrics Report

This report provides the classification metrics including precision, recall, F1-score, and support for each class in a multi-class classification task. Additionally, overall accuracy, macro average, and weighted average metrics are included.

## Metrics Table

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.98      | 0.99   | 0.99     | 980     |
| 1     | 0.99      | 0.99   | 0.99     | 1135    |
| 2     | 0.98      | 0.97   | 0.98     | 1032    |
| 3     | 0.97      | 0.99   | 0.98     | 1010    |
| 4     | 0.98      | 0.98   | 0.98     | 982     |
| 5     | 0.99      | 0.98   | 0.98     | 892     |
| 6     | 0.99      | 0.99   | 0.99     | 958     |
| 7     | 0.98      | 0.97   | 0.97     | 1028    |
| 8     | 0.97      | 0.98   | 0.97     | 974     |
| 9     | 0.97      | 0.96   | 0.97     | 1009    |
| **Accuracy**    |       |        | **0.98** | **10000** |
| **Macro Avg**   | **0.98**  | **0.98** | **0.98**  | **10000** |
| **Weighted Avg**| **0.98**  | **0.98** | **0.98**  | **10000** |

## Definitions

- **Precision**: The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall**: The ratio of correctly predicted positive observations to the all observations in actual class.
- **F1-Score**: The weighted average of Precision and Recall. It ranges from 0 to 1, with 1 being the best possible score.
- **Support**: The number of actual occurrences of the class in the dataset.
- **Accuracy**: The ratio of correctly predicted observations to the total observations.
- **Macro Average**: The average of Precision, Recall, and F1-Score calculated independently for each class and then averaged.
- **Weighted Average**: The average of Precision, Recall, and F1-Score calculated for each class but weighted by the number of instances of each class.

## Summary

The model shows high precision, recall, and F1-score across all classes with an overall accuracy of 0.98. Both macro and weighted averages also indicate consistent performance across different classes.

## Usage

This report can be used to evaluate the performance of the classification model, understand its strengths and weaknesses, and identify areas for improvement.

## Demo


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

