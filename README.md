# Health Data Analyzer

## Overview
Health Data Analyzer is a beginner Python project that reads health measurements from a CSV file and generates a simple statistical report.

## Features
- Reads age, heart rate, and temperature data from a CSV file.
- Handles missing and invalid numeric entries.
- Calculates average, minimum, and maximum measurements.
- Counts and displays measurements above configurable thresholds.
- Uses reusable functions to avoid duplicated analysis code.

## Technologies
- Python
- CSV file handling
- Python fundamentals: functions, lists, loops, conditionals, exception handling, and built-in functions.

## How to Run
1. Install Python 3.
2. Place `health_data_analyzer.py` and `health_data.csv` in the same folder.
3. Run the program:

   ```bash
   python health_data_analyzer.py
   ```

## Input Format
The CSV file must contain these column names:

`age,heart_rate,temperature`

Each row represents a measurement record. Missing or invalid numeric values are skipped.

## Limitations
This is an educational project, not a medical diagnostic tool. It does not validate whether measurements are medically plausible, and its thresholds are simplified examples.

## Future Improvements
- Validate measurement ranges.
- Add unit tests.
- Visualize measurement trends.
