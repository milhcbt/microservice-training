# MicroServices Tranning
## The Emergence of Microservices Architecture
Why Microservices /what Microservice Promise? 
- Microservices are a way of breaking large software projects into loosely coupled modules, which communicate with each other through simple APIs.
- Microservices are small, modular, and independently deployable services.
- Microservices allow large systems to be built up from a number of collaborating components.
- Microservices can be developed by small teams.
- Microservices can be deployed independently.
- Microservices can be written in different programming languages.
- Microservices can be managed by different teams.
- Microservices can use different data storage technologies.
- Microservices can be scaled independently.
- Microservices can be tested independently.
...
How to build Microservices?
there is at least two ways to build Microservices:
- Top-down approach: 
    - Start with a monolithic application and break it down into smaller services.
    - This approach is more suitable for existing applications.
- Bottom-up approach:
    - Start with a small service and build more services around it.
    - This approach is more suitable for new applications.
What is Microservices Architecture?
- Microservices architecture is a style of building software applications as a suite of independently deployable, small, modular services.
- Each service runs a unique process and communicates through a well-defined, lightweight mechanism to serve a business goal.
- Microservices are built around business capabilities.
## Microservice Design Principles
### Basic Principles needed for understanding Microservices concepts
#### SOLID Principles
    - Single Responsibility Principle
    SRP states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. 
    example classes that  do not follow SRP:
    ```java
    public class Employee {
        public Money calculatePay() {...}
        public void save() {...}
        public String describeEmployee() {...}
    }
    ```  
    why this class does not follow SRP?
    - It has more than one responsibility: payroll and persistence.
    - It has more than one reason to change: changes in payroll calculations and changes in persistence.
    - It is difficult to reuse: payroll calculations are needed by other classes, and persistence is used by other classes.
    - It is difficult to test: testing payroll calculations requires access to a database.
    - It has a high coupling: payroll calculations and persistence are tightly coupled.
    - It has a low cohesion: payroll calculations and persistence are not closely related.
    let's refactor this class to follow SRP:
    ```java 
    public class Employee {
        public Money calculatePay() {...}
    }
    public class EmployeeRepository {
        public void save(Employee employee) {...}
    }
    public class EmployeeReporter {
        public String describeEmployee(Employee employee) {...}
    }
    ```
    why these classes better?
    - Each class has a single responsibility.
    - Each class has a single reason to change.
    - Each class is easier to reuse.
    - Each class is easier to test.
    - Each class has a low coupling.
    - Each class has a high cohesion.

    - Open-Closed Principle

    - Liskov Substitution Principle
    - Interface Segregation Principle
    - Dependency Inversion Principle
#### DRY Principle
DRY Principle is an acronym for Don’t Repeat Yourself. It states that every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
- KISS Principle
- YAGNI Principle
- DD Principles
    - Domain-Driven Design
    - Bounded Context
    - Ubiquitous Language
    - Context Map
    - Core Domain
    - Subdomain
    - Generic Subdomain
    - Supporting Subdomain
    - Anti-Corruption Layer
    - Shared Kernel
    - Customer/Supplier Development
    - Conformist
    - Separate Ways
    - Open Host Service
    - Published Language
    - Partnership
    - Shared Kernel
    - Customer/Supplier Development
## Integrating Microservices
## Microservice Technologies
Some teachs that enabling microservices

| Technology               | Year of Release | Role in Microservices Architecture                                         | Description                                                                                                                                                                                                         |
|--------------------------|-----------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTP/HTTPS               | 1991            | Communication Protocol                                                      | HTTP/HTTPS are the backbone of data communication on the World Wide Web, crucial for services interaction in a microservices architecture.                                                                          |
| Java                     | 1995            | Development Language                                                        | Java provides platform independence, which is crucial in a microservices environment. Many microservices frameworks are based on Java.                                                                              |
| XML                      | 1998            | Data Interchange Format                                                     | XML is used to encode documents in a format that is both human-readable and machine-readable, useful for data exchange between microservices.                                                                       |
| JSON                     | 2001            | Data Interchange Format                                                     | JSON is a lightweight data-interchange format that is easy to read and write. It's often used for asynchronous browser/server communication in microservices, alongside XML.                                         |
| Hardware Virtualization  | 2005            | Infrastructure Management                                                   | Hardware Virtualization allows running multiple operating systems on a single physical hardware resource, improving the efficiency and scalability of microservices deployments.                                     |
| Apache Kafka             | 2011            | Real-time Data Streaming Platform                                           | Kafka is used for building real-time data pipelines and streaming apps, which is critical in ensuring smooth data flow between microservices.                                                                       |
| Docker                   | 2013            | Containerization                                                            | Docker provides an efficient way to package and run applications as lightweight, portable containers, ideal for deploying microservices.                                                                            |
| Netflix Zuul             | 2013            | API Gateway                                                                 | Netflix Zuul is a gateway service that provides dynamic routing, monitoring, resiliency, and security for microservice applications.                                                                                |
| Consul by HashiCorp      | 2014            | Service Discovery and Configuration                                         | Consul enables discovering and configuring services in your infrastructure. It's crucial for inter-service communication in microservices.                                                                         |
| AWS Lambda               | 2014            | Serverless Computing                                                        | AWS Lambda lets you run code without provisioning or managing servers, enabling easy and quick development of individual microservices.                                                                            |
| Spring Boot              | 2014            | Microservices Framework                                                     | Spring Boot is a popular Java-based framework that simplifies the setup and development of Spring applications, ideal for microservices.                                                                            |
| gRPC                     | 2015            | Remote Procedure Call (RPC) framework                                       | gRPC allows for communication between microservices. It is language-agnostic and enables high-performance communication.                                                                                           |
| Kubernetes               | 2015            | Container Orchestration                                                     | Kubernetes helps in managing, scaling, and maintaining containerized applications, which is important in a microservices architecture.                                                                              |
| Envoy                    | 2016            | Service Proxy                                                               | Envoy is a high-performance proxy and provides the foundation for a service mesh, enabling resilient and robust inter-service communication.                                                                        |
| Istio                    | 2017            | Service Mesh                                                                | Istio provides a complete solution for managing network communication, observability, and security between microservices.                                                                                           |
| AWS Fargate              | 2017            | Serverless Compute Engine for Containers                                    | AWS Fargate allows you to run containers without managing the underlying infrastructure, providing flexibility and scalability for deploying microservices.                                                        |
| Prometheus               | 2015            | Monitoring System and Time Series Database                                  | Prometheus is an open-source monitoring system with a dimensional data model, flexible query language, efficient storage and integration with many popular visualization tools. It's often used in microservices. |


## Decomposing the Monolith
## Deploying and Maintaining Microservices