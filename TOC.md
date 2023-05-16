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
## Decomposing the Monolith
## Deploying and Maintaining Microservices