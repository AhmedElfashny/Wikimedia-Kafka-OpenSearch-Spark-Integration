import time
from kafka import KafkaProducer
from sseclient import SSEClient  # For handling server-sent events (SSE) from the Wikimedia stream

# Kafka broker configuration
KAFKA_SERVER = '127.0.0.1:9092'
TOPIC = 'wikimedia.recentchange'

# Initialize the Kafka producer without custom serializers to handle encoding ourselves
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

def send_to_kafka():
    url = "https://stream.wikimedia.org/v2/stream/recentchange"
    client = SSEClient(url)

    # Get the current time to enforce a 1-minute limit
    start_time = time.time()
    max_duration = 60  # 1 minute in seconds

    # Iterate over events directly from SSEClient
    for event in client:
        # Check if the time limit has been exceeded
        if time.time() - start_time > max_duration:
            print("Time limit reached. Stopping the stream.")
            break

        try:
            # Ensure the event data is a non-empty string
            if event.data:
                # Encode the data as bytes and send it to Kafka
                encoded_data = event.data.encode('utf-8')  # Manually encoding here
                producer.send(TOPIC, value=encoded_data)
                print("Event sent to Kafka:", event.data)  # Optional: print data for debugging
            else:
                print("Skipping event with None or empty data")  # Skip if data is None or empty
        except Exception as e:
            print(f"Error sending event: {e}")

# Run the event handler function and limit runtime to 1 minute
try:
    send_to_kafka()  # Start sending events to Kafka
except KeyboardInterrupt:
    print("Stream interrupted")
finally:
    producer.close()  # Close the Kafka producer after completion
    print("Producer closed")
