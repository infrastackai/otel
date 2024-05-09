
# InfraStack .NET Getting Started

OpenTelemetry .NET SDK provides a comprehensive toolkit for collecting telemetry data within your .NET applications, serving as a core component of our monitoring infrastructure, 
InfraStack. By integrating OpenTelemetry, we leverage its flexible and powerful capabilities to gather insights on application performance and health, ensuring that we can effectively monitor and optimize our systems. 
This documentation outlines the setup of the SDK and its fundamental applications, enabling us to maintain high performance and reliability across all services.

## Setup

### Step 1: Adding Packages and Configuration

To integrate OpenTelemetry into your .NET application, you need to add the following NuGet packages to your project:

```shell
dotnet add package OpenTelemetry
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
```

### Step 2: Telemetry Configuration

Depending on how you want to collect and send telemetry data in your application, configure your `Program.cs` file as follows:

```csharp
var builder = WebApplication.CreateBuilder(args);

// OpenTelemetry configuration
builder.Services.AddOpenTelemetry()
      .WithTracing(tracing => tracing
      .ConfigureResource(resource => resource.AddService(serviceName: "my-first-app"))
          .AddAspNetCoreInstrumentation()
          .AddOtlpExporter(opt =>
          {
              opt.Endpoint = new Uri("https://collector-us1.infrastack.ai");

              string headerKey = "infrastack-api-key";
              string headerValue = "<API-KEY>";
              opt.Headers = $"{headerKey}={headerValue}";
          }));
```

**`<API-KEY>`**: Replace this with your API key. This ensures that the transmitted data is associated with your account, securing and authenticating the data transmission.

**`serviceName`**: Set this to the name of your application or service. It uniquely identifies the source of telemetry data, aiding in easier monitoring and analysis across multiple services.

If you prefer to send your telemetry data over gRPC, update your OTLP exporter settings as follows:

```csharp
            ...
            opt.Headers = $"{headerKey}={headerValue}";
            opt.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.Grpc;
        }));
```

### Step 3: Running the .NET application 

```shell
dotnet build
dotnet run
```

### Step 4: Check your application trace data

You can monitor and analyze the telemetry data collected by visiting the [InfraStack Dashboard](https://app.infrastack.ai/), providing a comprehensive view of your application's performance and health.


## Additional Instrumentation Options

OpenTelemetry provides specialized instrumentation options for various libraries. For example:

- **HTTP requests**: To monitor client and server HTTP requests, use `OpenTelemetry.Instrumentation.Http`.
- **SQL database queries**: For monitoring interactions with SQL databases, use `OpenTelemetry.Instrumentation.SqlClient`.
- **gRPC calls**: To track gRPC requests, use `OpenTelemetry.Instrumentation.GrpcNetClient`.

> [!NOTE]
> You can find all the information about [OpenTelemetry and SDK](https://opentelemetry.io/docs/).

These instrumentations allow you to collect detailed data from different components of your application, which is critical for performance analysis and troubleshooting.


