# Wikimedia Kafka, OpenSearch, and Spark Streaming Integration

This repository contains two main projects for streaming Wikimedia data using Kafka, processing it with Spark, and storing the data in OpenSearch.

## Projects Overview

### 1. Kafka Producer and OpenSearch Consumer
- **Kafka Producer**: Streams recent changes from Wikimedia using the Kafka producer.
- **OpenSearch Consumer**: Reads messages from Kafka and indexes them in OpenSearch for searching and analytics.

### 2. Spark Streaming with Kafka
- **Spark Streaming Application**: Reads data from Kafka, processes it to create various aggregations (bot edits, website edits, and time series data), and streams the results to new Kafka topics.

## Directory Structure
- `wikimedia_kafka_producer.py`: Kafka Producer code to stream data from Wikimedia.
- `wikimedia_opensearch_consumer.py`: Kafka Consumer code to consume data and store it in OpenSearch.
- `wikimedia_spark_streaming.py`: Spark Streaming code to process data in real-time.

## Screenshots

### Kafka Streams Application
![Kafka Streams Application](images/kafka_streams_application.png)

### Wikimedia Producer Setup
![Wikimedia Producer Setup](images/wikimedia_producer_setup.png)

### Kafdrop Kafka Cluster Overview
![Kafdrop Kafka Cluster Overview](images/kafdrop.png)

### OpenSearch Dashboards
![OpenSearch Dashboards](images/opensearch.png)
