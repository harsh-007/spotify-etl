# Spotify Data Engineering Project

## **Overview**
This project extracts, cleans, transforms, and loads Spotify data using Kaggle's API. The processed data is stored in a database and queried for insights.

## **Process Workflow**
1. **Download Data**:  
   - Use the Kaggle API to fetch the `Spotify Dataset 2023`.  
   - Extract and save the dataset locally.  

2. **Clean and Transform Data**:  
   - Remove unnecessary columns.  
   - Handle missing values.  
   - Convert data types for consistency.  

3. **Load and Query Data**:  
   - Store the transformed data in an SQLite database.  
   - Run SQL queries for analysis and visualization.  

## **Requirements**
- Python 3.x  
- Libraries: `kaggle`, `pandas`, `sqlite3`, `os`

## Testing
- To verify data processing and transformations, run the unit tests:


## **Setup Instructions**
1. Install dependencies:  
   ```bash
   pip install kaggle pandas
