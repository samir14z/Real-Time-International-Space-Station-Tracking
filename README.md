# International Space Station (ISS) Tracker

The International Space Station (ISS) Tracker is a project that utilizes Apache Kafka and Apache Spark to continuously track the real-time latitude and longitude coordinates of the ISS.

## Project Overview

The ISS Tracker project aims to retrieve the current location of the International Space Station by making requests to the Open Notify API and publish it to a Kafka topic using the Kafka producer. The Spark streaming data consumer then consumes the data from the Kafka topic, performs real-time data processing and analysis, and writes the output to CSV files and the console.

## Prerequisites

Before running the ISS Tracker project, make sure you have the following components and dependencies set up:

- Apache Kafka: Install and configure Kafka on your local machine. Make sure it is running on `localhost` with the default port `9092`.
- Apache Spark: Install Spark and set up the necessary environment variables.
- Python: Ensure that Python is installed, along with the required dependencies: `kafka-python`, `requests`, and `json`.

## Usage

1. Start Apache Kafka and ensure it is running on `localhost:9092`.
2. Install the required Python dependencies by running the following command:
3. Run the Kafka data producer script (`your_script_name.py`) to retrieve data from the Open Notify API and publish it to a Kafka topic. Replace `my-topic` with the desired topic name.
4. Run the Spark streaming data consumer code to consume data from the Kafka topic, filter it, and perform real-time data analysis. Ensure that you replace `my-topic` with the same Kafka topic name used in the producer script. Customize the file paths and options according to your preferences.
5. The consumer will write the filtered data to CSV files and display it on the console. The CSV files will be stored in the specified output directory.
