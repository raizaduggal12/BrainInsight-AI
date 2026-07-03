"""
===========================================================
BrainInsight AI
Database Module
-----------------------------------------------------------
This module manages the SQLite database for storing
prediction history.

This file will:

Create the SQLite database automatically (if it doesn't exist)
Create the prediction_history table
Provide helper functions to:
Initialize the database
Insert a prediction
Retrieve prediction history
Delete history (optional, useful later)

This way, every API route can simply import these functions.

Author : Raiza Duggal
===========================================================
"""

import sqlite3
from pathlib import Path

# ==========================================================
# Database Path
# ==========================================================

DATABASE_PATH = Path(__file__).parent / "database.db"


# ==========================================================
# Create Connection
# ==========================================================

def get_connection():
    """
    Creates and returns a SQLite database connection.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# ==========================================================
# Initialize Database
# ==========================================================

def initialize_database():
    """
    Creates the prediction_history table if it does not exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_id TEXT NOT NULL,

            prediction TEXT NOT NULL,

            confidence REAL NOT NULL,

            severity TEXT NOT NULL,

            prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


# ==========================================================
# Insert Prediction
# ==========================================================

def insert_prediction(
        patient_id,
        prediction,
        confidence,
        severity
):
    """
    Inserts a prediction into the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            patient_id,
            prediction,
            confidence,
            severity
        )

        VALUES (?, ?, ?, ?)
        """,
        (
            patient_id,
            prediction,
            confidence,
            severity
        )
    )

    connection.commit()
    connection.close()


# ==========================================================
# Fetch Prediction History
# ==========================================================

def get_prediction_history():
    """
    Returns all prediction records.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM prediction_history
        ORDER BY prediction_date DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


# ==========================================================
# Delete History
# ==========================================================

def clear_history():
    """
    Deletes all prediction records.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM prediction_history")

    connection.commit()
    connection.close()

    print("Prediction history cleared.")


# ==========================================================
# Run Directly
# ==========================================================

if __name__ == "__main__":
    initialize_database()

print("=" * 50)
print("Database initialized successfully!")
print("Database Path:", DATABASE_PATH)
print("=" * 50)

# ==========================================================
# Get Latest Prediction by Patient ID
# ==========================================================

def get_prediction_by_patient(patient_id):
    """
    Returns latest prediction record for a patient.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            patient_id,
            prediction,
            confidence,
            severity,
            prediction_date
        FROM prediction_history
        WHERE patient_id = ?
        ORDER BY prediction_date DESC
        LIMIT 1
        """,
        (patient_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return {
        "patient_id": row[0],
        "prediction": row[1],
        "confidence": row[2],
        "severity": row[3],
        "prediction_date": row[4]
    }