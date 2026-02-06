# Lab 3.1: Event-Driven Cybersecurity Pipeline with Kafka and Jaeger
## Overview

In this lab, we implemented a decoupled, asynchronous cybersecurity data pipeline. The system simulates real-world security telemetry (Windows logs) being ingested, processed, and analyzed in a high-load environment. The architecture focuses on separation of concerns between data production and classification.

# Conceptual Questions

1\. Kafka used instead of direct function calls?

we use Kafka because, In high-load SOC systems, a direct function call (synchronous) creates a tight coupling where the producer must wait for the consumer to finish. Kafka provides Decoupling; the producer simply drops events into a topic and moves on. This also adds Fault Tolerance; if the classifier goes down, Kafka buffers the messages so no security data is lost.

2\. What happens if the consumer is slower than the producer?

If the classification stage is slower, a Backlog (lag) will start to build up in the Kafka topic. While this increases the end-to-end latency (the time it takes for a log to be classified), it prevents the system from crashing. The producer can continue at full speed without being throttled by the slower consumer.

3\. How does tracing help debug pipeline behavior?

Distributed tracing with Jaeger allowed me to see the "path" of a single event across different microservices. By using a shared trace\_id (derived from the event\_id), I could observe exactly how long each stage took—from ingestion to classification to storage. This is essential for identifying bottlenecks in complex, asynchronous pipelines.

4\. Which pipeline stages could be scaled independently?

The Consumer/Classifier is the most likely candidate for scaling. Since it is decoupled via Kafka, we can run multiple instances of the classifier to process the topic in parallel. We can also scale the Producer side by adding more log-forwarders without needing to change the analysis logic.

5\. How would this pipeline change in a real SOC system?

* **Ingestion**: Instead of one producer, we would have thousands of agents (EDR, Firewalls, Cloud Logs) requiring a normalization layer.
* **Classification**: Rule-based logic would be replaced or augmented by ML models and Correlation Engines to detect multi-stage attacks.
* **Storage**: Results would be sent to a high-performance indexed database (like Elasticsearch) rather than a local CSV.
* **Automation**: A real system would include a SOAR (Security Orchestration, Automation, and Response) layer to automatically block threats detected by the pipeline.

# Pipeline Execution Results

**Data Flow**: Verified via Redpanda Console, showing JSON events successfully entering the raw-events topic.

**Traces**: Captured full 5-span traces in Jaeger, confirming end-to-end execution from produce\_event to write\_csv.

**Analytics**: Generated class distribution plots in the Statistics notebook, mapping synthetic logs to MITRE ATT\&CK tactics like Execution and Credential Access.

# Evidence

### Kafka Traffic (Redpanda Console)

This screenshot shows the `raw-events` topic successfully receiving JSON logs from the Producer.

<img width="1489" height="797" alt="messagesRecord" src="https://github.com/user-attachments/assets/65b0ac08-f463-472d-a03f-69eaefd48b02" />

### Distributed Tracing (Jaeger)

This trace confirms the full end-to-end flow. It includes 5 spans, connecting the Producer's logic with the Consumer's classification and final storage.

<img width="1885" height="422" alt="timelineRecord" src="https://github.com/user-attachments/assets/9f650256-e28b-4c53-af55-5ab186be398e" />

### Data Analytics

The distribution of MITRE ATT\&CK tactics identified by the Consumer/Classifier.

<img width="1820" height="793" alt="StatisticsRecord" src="https://github.com/user-attachments/assets/f06d9817-4631-495f-98ff-8fdb16ac9777" />



