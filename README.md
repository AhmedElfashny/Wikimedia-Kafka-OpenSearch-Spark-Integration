# Wikimedia Kafka, OpenSearch, and Spark Streaming Integration

This repository is a follow-up project from the course [Apache Kafka Series - Learn Apache Kafka for Beginners v3](https://www.udemy.com/course/apache-kafka/) by Stephane Maarek, provided by Conduktor Kafkademy. In the course, two main projects were introduced, which I have implemented here using Python to connect with Kafka and OpenSearch.

## Projects Overview

### 1. Kafka Producer and OpenSearch Consumer
In this first project, we created a Kafka topic named `wikimedia.recentchange`, which consists of a single partition. The **Kafka Producer** streams recent changes from Wikimedia, and the **OpenSearch Consumer** reads these messages from Kafka and indexes them in OpenSearch for search and analytics.

- **Producer**: Uses Wikimedia API to stream data to Kafka topic `wikimedia.recentchange`.
- **Consumer**: Reads from `wikimedia.recentchange` topic and sends the data to an OpenSearch index for further exploration.

I utilized [Kafdrop](https://github.com/obsidiandynamics/kafdrop) as the Kafka UI to monitor the Kafka cluster and inspect topics.

### 2. Spark Streaming with Kafka
In the second project, instead of using Kafka Streams as demonstrated in the course, I implemented **Spark Streaming** to connect to Kafka, process data, and create additional Kafka topics. This project includes real-time processing and aggregation of the data streamed from Wikimedia.

- **Spark Streaming Application**: Reads data from the `wikimedia.recentchange` Kafka topic and performs the following aggregations:
  - **Bot Edits**: Aggregates bot edits over time and publishes results to a new topic `wikimedia.stats.bots`. This topic can be used to monitor bot activity on Wikimedia in real time, providing insights into the frequency and scale of bot-driven changes.
  - **Website Edits**: Tracks the number of edits per website, streaming results to `wikimedia.stats.website`. This topic allows users to observe editing trends across different Wikimedia projects (like Wikipedia and Wikimedia Commons) and analyze which sites receive the most updates.
  - **Time Series Edits**: Aggregates edit counts by type over time and sends output to `wikimedia.stats.timeseries`. This topic is useful for time-based analysis, enabling the identification of patterns and spikes in editing activity by different types, such as new articles or modifications.

## Directory Structure
- `wikimedia_kafka_producer.py`: Kafka Producer code to stream data from Wikimedia to the Kafka topic.
- `wikimedia_opensearch_consumer.py`: Kafka Consumer code to consume data from Kafka and index it in OpenSearch.
- `wikimedia_spark_streaming.py`: Spark Streaming code to process data in real-time from Kafka and publish aggregated results back to Kafka.

## Screenshots

### Kafka Streams Application
This diagram illustrates the Kafka Streams setup, with the Kafka Producer feeding data to the `wikimedia.recentchange` topic and Spark processing and producing aggregated results.

![Kafka Streams Application](images/kafka_streams_application.png)

### Wikimedia Producer Setup
The producer configuration for streaming data from Wikimedia into Kafka.

![Wikimedia Producer Setup](images/wikimedia_producer_setup.png)

### Kafdrop Kafka Cluster Overview
This shows the Kafka topics and partitions using [Kafdrop](https://github.com/obsidiandynamics/kafdrop) as the Kafka UI.

![Kafdrop Kafka Cluster Overview](images/kafdrop.png)

### OpenSearch Dashboards
A sample view from OpenSearch Dashboards showing indexed data from Wikimedia.

![OpenSearch Dashboards](images/opensearch.png)

## Additional Notes
- **Kafka and Python Integration**: I used Python along with the Kafka connector to implement these projects.
- **Kafdrop UI**: Kafdrop provided an easy-to-use interface to view Kafka topics, partitions, and messages.
  
> **Note**: This repository does not include the setup instructions for Kafdrop UI, OpenSearch, or preparing the Python environment. Before writing the code, I ensured that my Python environment was ready, Kafdrop was up and running, and OpenSearch was properly configured.
  
This project demonstrates the use of Apache Kafka for real-time data streaming, with processing and storage facilitated by Spark and OpenSearch, respectively. Each component was implemented with Python for ease of integration and flexibility.
