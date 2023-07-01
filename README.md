# Advanced Databases Class
University of Aveiro

I am the author of those solutions for NoSQL databases laboratory mini-projects. In some places they are not the best in terms of syntax or efficiency, but show the general concept very well.

# Purpose
Those materials might be helpful in the future, e.g. queries, or docker compose files.

# Redis
Redis is an in-memory data store that primarily focuses on key-value storage.
It excels at handling high-speed data operations, such as caching, session management, and real-time analytics.
Redis supports various data structures like strings, lists, sets, and hashes.
It lacks built-in data persistence and durability, but offers options for data persistence through snapshots or replication.
Redis is known for its exceptional performance and low latency, making it suitable for use cases that require rapid data access.

# MongoDB
MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents.
It provides high scalability, automatic sharding, and horizontal scaling, making it suitable for handling large volumes of data.
MongoDB's flexible schema allows for easy data modeling and handling of unstructured and semi-structured data.
It offers rich query capabilities, including support for indexing, ad hoc queries, and aggregation pipelines.
MongoDB supports data replication and high availability through replica sets.
It is commonly used in web applications, content management systems, and real-time analytics.

# Cassandra
Cassandra is a distributed and highly scalable NoSQL database designed for handling large amounts of data across multiple nodes.
It provides high availability, fault tolerance, and linear scalability by distributing data across a cluster of nodes.
Cassandra's data model is based on columns and column families, allowing for flexible schema design.
It is optimized for write-heavy workloads and can handle high-speed data ingestion and retrieval.
Cassandra offers tunable consistency levels and eventual consistency, making it suitable for applications that prioritize availability and partition tolerance over strict consistency.

# Neo4j
Neo4j is a graph database that focuses on managing and analyzing highly connected data.
It excels at handling complex relationships and graph-based queries, making it ideal for applications involving social networks, recommendation engines, and knowledge graphs.
Neo4j uses a property graph model, where data is represented as nodes, relationships, and properties.
It provides a query language called Cypher, which allows for expressive and efficient querying of graph data.
Neo4j offers ACID transactions and supports data replication and clustering for high availability.

# Summary
It is commonly used in use cases involving time series data, high write and read throughput, and distributed data storage.
Overall, the choice between Redis, MongoDB, Neo4j, and Cassandra depends on the specific requirements of your application, such as data model, query patterns, scalability needs, and the nature of your data relationships.