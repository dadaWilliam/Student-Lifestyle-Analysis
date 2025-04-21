# Student Lifestyle Analysis Dashboard

## Overview

This project provides an interactive data analysis dashboard that explores the relationship between student lifestyle factors and academic performance. The application allows users to visualize and explore correlations between various lifestyle elements (study hours, sleep patterns, physical activity, etc.) and student grades.

## Features

- **Interactive Filtering**: Use sliders to dynamically filter data based on various parameters
- **Multi-dimensional Analysis**: Examine relationships between different lifestyle factors
- **SQL Integration**: Includes examples of SQL queries for advanced data analysis
- **Correlation Analysis**: Visualize which lifestyle factors correlate most strongly with academic success

## Data Description

The dataset contains information about 2,000 students, including:

- Study hours per day
- Sleep hours per day
- Physical activity hours per day
- Social hours per day
- Extracurricular activity hours per day
- Stress level (categorical)
- Gender
- Grades (GPA)

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/student-lifestyle-analysis.git
   cd student-lifestyle-analysis
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install preswald pandas plotly
   ```

4. Place your dataset in the data directory:
   ```
   mkdir -p data
   # Copy your CSV file to data/student_lifestyle_dataset.csv
   ```

## Running the Application

1. Start the Preswald server:
   ```
   preswald run
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

## Project Structure

```
student-lifestyle-analysis/
│
├── data/
│   └── student_lifestyle_dataset.csv  # Dataset file
│
├── app.py                            # Main application code
├── preswald.toml                     # Preswald configuration
└── README.md                         # This file
```

## Using the Dashboard

The dashboard is organized into several sections:

1. **Dataset Overview**: View the raw data and basic statistics
2. **Grade Analysis**: Filter students by minimum grade and explore correlations
3. **Sleep Analysis**: Examine the relationship between sleep hours and academic performance
4. **Stress Level Analysis**: Compare students across different stress levels
5. **Physical Activity Analysis**: Investigate how exercise impacts grades
6. **Correlation Analysis**: See which factors most strongly correlate with academic success

Each section includes:
- Interactive filters (sliders)
- Data tables showing filtered results
- Visualizations of the relationships between variables



