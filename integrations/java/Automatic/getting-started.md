# InfraStack Java(mvn) Spring Boot Auto-instrumentation Getting Started

OpenTelemetry Java SDK provides a comprehensive toolkit for collecting telemetry data within your Java applications, serving as a core component of our monitoring infrastructure, 
InfraStack. By integrating OpenTelemetry, we leverage its flexible and powerful capabilities to gather insights on application performance and health, ensuring that we can effectively monitor and optimize our systems. 
This documentation outlines the setup of the SDK and its fundamental applications, enabling us to maintain high performance and reliability across all services.

---

OpenTelemetry provides client libraries and agents for most of the popular programming languages. There are two types of instrumentation:


- [Auto-instrumentation](https:google.com/)

  OpenTelemetry can collect data for many popular frameworks and libraries automatically. You don’t have to make any code changes.

- [Manual instrumentation](https:google.com/)

  If you want more application-specific data, OpenTelemetry SDK provides you with the capabilities to capture that data using OpenTelemetry APIs and SDKs.


For Java Spring Boot applications, leveraging the OpenTelemetry Java Agent offers a streamlined and efficient way to automatically instrument your application. This automatic instrumentation capability is essential for capturing telemetry data without the need for manual coding.

**Why Use Automatic Instrumentation?**
Automatic instrumentation simplifies the process of integrating telemetry collection into your applications. With the OpenTelemetry Java Agent, you can automatically capture detailed performance metrics and traces from various popular libraries and frameworks that are commonly used in Spring Boot applications. This includes, but is not limited to, Spring Web, Spring Data, and Spring Kafka.

## Setup

### Step 1: Download 'opentelemetry-javaagent.jar' Package
Download link: [opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases)

**Why is it necessary?**
`opentelemetry-javaagent.jar` provides automatic instrumentation for Java applications. This agent detects popular libraries and frameworks and instruments them without the need for any additional code. It enables the collection of traces and logs from your application to gather performance metrics.

### Step 2: Configure and Launch Your Application
Start command:
```bash
java -javaagent:path/to/opentelemetry-javaagent.jar -Dotel.service.name=my-first-app -jar myapp.jar
```

**Why is this configuration necessary?**
This configuration adds the `javaagent` to the JVM startup arguments, enabling automatic instrumentation. This allows your application to collect telemetry data such as monitoring, logging, and error analysis while it is running.

### Step 3: Set Environment Variables
Examples for setting up based on the operating system:

**Why Environment Variables?**
Environment variables provide necessary configurations for the agent to send telemetry data to the InfraStack destination. This includes security keys, target endpoints, and other crucial configurations.

**Linux & MacOS:**
```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=https://collector-us1.infrastack.ai
export OTEL_EXPORTER_OTLP_HEADERS="infrastack-api-key=<API-KEY>"
```

**Windows:**
```cmd
set OTEL_EXPORTER_OTLP_ENDPOINT=https://collector-us1.infrastack.ai
set OTEL_EXPORTER_OTLP_HEADERS="infrastack-api-key=<API-KEY>"
```

**Docker:**
```dockerfile
ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://collector-us1.infrastack.ai
ENV OTEL_EXPORTER_OTLP_HEADERS="infrastack-api-key=<API-KEY>"
```

### Step 4: Run Your App

After configuring the OpenTelemetry Java agent and setting the necessary environment variables or properties, you are now ready to run your application. This step is crucial as it integrates all the setup and configurations you've done so far, allowing the telemetry data to be collected and sent to your observability platform.

To run your application, use the following command, which assumes that all configurations are correctly set:

```bash
java -jar myapp.jar
```

### Step 5: Check Your Application Trace Data
To monitor the data, visit the InfraStack Dashboard: [InfraStack Dashboard](https://app.infrastack.ai/)


### Configuring the OpenTelemetry Java Agent

The OpenTelemetry Java agent is highly configurable through several methods. Below are some examples of different configuration approaches you can take.

### Configuration via Command Line Arguments

You can pass configuration properties directly via the `-D` flag. This is useful for setting up basic configurations without needing environment variables or external configuration files. For example, to configure a service name and specify InfraStack as the trace exporter, you would use:

```bash
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -Dotel.service.name=your-service-name \
     -jar myapp.jar
```

#### Configuration via Java Properties File

For more complex configurations, or when you want to keep your configuration version-controlled, you can use a Java properties file. This file can then be referenced at runtime:

```bash
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -Dotel.javaagent.configuration-file=path/to/properties/file.properties \
     -jar myapp.jar
```

### Further Configuration
To explore the full range of configuration options available with the OpenTelemetry Java agent, refer to the official [Agent Configuration documentation](https://opentelemetry.io/docs/languages/java/automatic/configuration/)




