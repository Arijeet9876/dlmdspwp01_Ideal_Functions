# DLMDSPWP01 Programming with Python Project

## Author

Arijeet Paramanik
DLMDSPWP01 – Programming with Python

## Overview

This project was developed as part of the DLMDSPWP01 Programming with Python module. The objective is to identify the most suitable ideal functions for four training datasets, map test observations to the selected ideal functions according to a predefined deviation criterion, store results in a SQLite database, and generate visualizations for analysis.

The project demonstrates object-oriented programming principles, inheritance, exception handling, database integration using SQLAlchemy, automated testing, and data visualization using Bokeh.

---

## Project Structure

```text
DLMDSPWP01_PROJECT
│
├── data
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
│
├── output
│   ├── plots
│   │   ├── training_data.html
│   │   ├── selected_ideal_functions.html
│   │   └── test_mapping_results.html
│   ├── results.db
│   └── test_results.db
│
├── src
│   ├── base.py
│   ├── data_loader.py
│   ├── database.py
│   ├── exceptions.py
│   ├── function_selector.py
│   ├── mapper.py
│   ├── visualizer.py
│   └── main.py
│
├── tests
│   ├── test_database.py
│   ├── test_mapper.py
│   └── test_selector.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3.9
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Bokeh
* Pytest

---

## Object-Oriented Design

The project follows a modular object-oriented architecture.

### Base Class

* BaseComponent

### Derived Classes

* DataLoader
* DatabaseManager
* FunctionSelector
* Mapper
* Visualizer

Inheritance is implemented by extending the BaseComponent class.

---

## Methodology

### 1. Data Loading

The DataLoader class imports:

* train.csv
* ideal.csv
* test.csv

using Pandas DataFrames.

### 2. Ideal Function Selection

For each training function, all fifty ideal functions are evaluated using the least-squares criterion.

The ideal function with the smallest sum of squared errors is selected.

### 3. Test Data Mapping

Each test observation is assigned to the selected ideal function when:

* The deviation is smaller than or equal to the maximum deviation observed during training multiplied by √2.

### 4. Database Storage

All datasets and mapping results are stored in a SQLite database using SQLAlchemy.

Stored tables:

* training_data
* ideal_functions
* test_results

### 5. Visualization

The project generates three interactive Bokeh visualizations:

* Training Data
* Selected Ideal Functions
* Test Mapping Results

---

## Results

Selected ideal functions:

| Training Function | Ideal Function |
| ----------------- | -------------- |
| y1                | y13            |
| y2                | y24            |
| y3                | y36            |
| y4                | y40            |

Maximum deviations:

| Function | Maximum Deviation |
| -------- | ----------------- |
| y1       | 0.4992            |
| y2       | 0.4990            |
| y3       | 0.4989            |
| y4       | 0.4998            |

Mapping results:

* Total test points: 100
* Successfully mapped points: 34
* Unmapped points: 66

---

## Running the Project

Execute the workflow:

```bash
python -m src.main
```

---

## Running Unit Tests

Execute:

```bash
python -m pytest
```

Expected result:

```text
3 passed
```

---

## Exception Handling

The project implements custom exceptions:

* DataLoadError
* DatabaseError
* FunctionSelectionError
* MappingError

---

## Assignment Requirements Covered

* Object-Oriented Programming
* Inheritance
* Exception Handling
* Pandas Data Processing
* SQLAlchemy Database Integration
* SQLite Storage
* Least-Squares Function Selection
* Test Data Mapping
* Bokeh Visualization
* Unit Testing
* Documentation

