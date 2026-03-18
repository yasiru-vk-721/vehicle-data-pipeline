# 🚗 Vehicle Sensor Data Engineering Pipeline

## 📌 Project Overview

This project demonstrates a complete **Data Engineering pipeline** that processes vehicle sensor data using Python, PostgreSQL, and ETL principles.

The pipeline extracts raw sensor data, transforms and cleans it, and loads it into a PostgreSQL database for analytical querying.

---

## 🏗 Architecture

```
CSV Data Source
      │
      ▼
Python ETL Pipeline
(Extract → Transform → Load)
      │
      ▼
PostgreSQL Database
      │
      ▼
Analytics Queries
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Git & GitHub

---

## 📂 Project Structure

```
vehicle-data-pipeline
│
├── data
│   └── sensor_data.csv
│
├── etl
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── warehouse
│   └── schema.sql
│
└── README.md
```

---

## 🔄 ETL Pipeline

### 1. Extract

* Reads raw CSV sensor data using Pandas

### 2. Transform

* Cleans missing values
* Converts timestamps
* Performs data transformations

### 3. Load

* Loads data into PostgreSQL using SQLAlchemy

---

## 🗃 Database

Database: `vehicle_db`

Table: `vehicle_sensor_raw`

---

## ▶️ How to Run

1. Install dependencies:

```
pip install pandas sqlalchemy psycopg2-binary
```

2. Update PostgreSQL connection in `load.py`

3. Run pipeline:

```
python etl/pipeline.py
```

---

## 📊 Example Query

```
SELECT vehicle_id,
       AVG(engine_temp)
FROM vehicle_sensor_raw
GROUP BY vehicle_id;
```

---

## 🎯 Key Learnings

* Built an end-to-end ETL pipeline
* Connected Python to PostgreSQL
* Performed data cleaning and transformation
* Designed a basic data warehouse structure

---

## 🚀 Future Improvements

* Add Apache Airflow for orchestration
* Implement star schema (fact & dimension tables)
* Add real-time streaming (Kafka)
* Use Spark for large-scale processing

---

## 👨‍💻 Author

Yasiru Katuwandeniya

