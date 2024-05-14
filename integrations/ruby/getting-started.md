
# InfraStack Ruby Getting Started

OpenTelemetry Ruby SDK provides a comprehensive toolkit for collecting telemetry data within your applications, serving as a core component of our monitoring infrastructure, InfraStack. By integrating OpenTelemetry, we leverage its flexible and powerful capabilities to gather insights on application performance and health, ensuring that we can effectively monitor and optimize our systems. This documentation outlines the setup of the SDK and its fundamental applications, enabling us to maintain high performance and reliability across all services.

## Setup

### Step 1: Adding Packages and Configuration

To integrate OpenTelemetry into your Ruby application, you need to add the following gem packages to your project:

```ruby
gem 'opentelemetry-sdk'
gem 'opentelemetry-instrumentation-rack'
gem 'opentelemetry-exporter-otlp'
```

Add these lines to your `Gemfile` and then install the packages:

```shell
bundle install
```

### Step 2: Telemetry Configuration

Configure your application to collect and send telemetry data. Add the following settings to your `config.ru` or `application.rb` file:

```ruby
require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/rack'
require 'opentelemetry/exporter/otlp'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'my-first-app'
  c.use 'OpenTelemetry::Instrumentation::Rack'
  c.add_span_processor(
    OpenTelemetry::SDK::Trace::Export::SimpleSpanProcessor.new(
      OpenTelemetry::Exporter::OTLP::Exporter.new(
        endpoint: 'https://collector-us1.infrastack.ai',
        headers: { 'infrastack-api-key' => '<API-KEY>' }
      )
    )
  )
end
```

**`<API-KEY>`**: Replace this with your API key. This ensures that the transmitted data is associated with your account, securing and authenticating the data transmission.

**`service_name`**: Set this to the name of your application or service. It uniquely identifies the source of telemetry data, aiding in easier monitoring and analysis across multiple services.

### Step 3: Running the Application

```shell
rackup
```

or

```shell
rails server
```

### Step 4: Check Your Application Trace Data

You can monitor and analyze the telemetry data collected by visiting the [InfraStack Dashboard](https://app.infrastack.ai/), providing a comprehensive view of your application's performance and health.

## Additional Instrumentation Options

OpenTelemetry provides specialized instrumentation options for various libraries. For example:

- **HTTP requests**: To monitor HTTP requests, use `opentelemetry-instrumentation-http`.
- **SQL database queries**: To monitor interactions with SQL databases, use `opentelemetry-instrumentation-active_record`.

> [!NOTE]
> You can find all the information about [OpenTelemetry and SDK](https://opentelemetry.io/docs/).

These instrumentations allow you to collect detailed data from different components of your application, which is critical for performance analysis and troubleshooting.

### Advanced Configuration

OpenTelemetry Ruby SDK is highly configurable through several methods. Here are some examples of different configuration approaches:

#### Configuration via Command Line Arguments

You can pass some configuration properties directly via the `rackup` or `rails` command line arguments. For example, to configure a service name and specify InfraStack as the trace exporter:

```shell
OTEL_SERVICE_NAME=my-first-app rackup
```

or

```shell
OTEL_SERVICE_NAME=my-first-app rails server
```

#### Configuration via Environment Variables

Environment variables provide necessary configurations for the agent. For example:

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

#### Configuration with Docker

If you are using Docker, you can add the necessary environment variables to your Dockerfile or Docker Compose file:

```dockerfile
ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://collector-us1.infrastack.ai
ENV OTEL_EXPORTER_OTLP_HEADERS="infrastack-api-key=<API-KEY>"
```

### Running Your Application

After correctly configuring the agent and setting the environment variables or properties, you are ready to run your application. For example:

```shell
rackup
```

or

```shell
rails server
```

To monitor and analyze the telemetry data collected, visit the [InfraStack Dashboard](https://app.infrastack.ai/).
