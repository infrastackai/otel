import logging

from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler


from opentelemetry.sdk.resources import Resource

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


# Creates a resource and adds it to the tracer provider
resource = Resource.create({"service.name": "python.console.traces"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Adds span processor with the OTLP exporter to the tracer provider
provider.add_span_processor(
    SimpleSpanProcessor(OTLPSpanExporter(endpoint="https://collector-us1.infrastack.ai/v1/traces", headers=(("infrastack-api-key", "sk-1d5737ca07c8cbdab10aeb80900e8cbedc99040051e4266d"),)))
)
tracer = trace.get_tracer(__name__)

#Starts and sets an attribute to a span
with tracer.start_as_current_span("HelloWorldSpan") as span:
    span.set_attribute("foo", "bar")
    print("Hello world")

app = FastAPI()

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "python.console.traces",
            "service.instance.id": "test",
        }
    ),
)
from opentelemetry.instrumentation.logging import LoggingInstrumentor

set_logger_provider(logger_provider)
exporter = OTLPLogExporter(endpoint="https://collector-us1.infrastack.ai/v1/logs", headers=(("infrastack-api-key", "sk-1d5737ca07c8cbdab10aeb80900e8cbedc99040051e4266d"),))
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

# Attach OTLP handler to root logger
logging.getLogger().addHandler(handler)

@app.get("/")
async def foobar():
    with tracer.start_as_current_span("foo"):
        # Do something
        logging.error("This is a log message")
        current_span = trace.get_current_span()
        current_span.add_event("This is a span event")
        logging.error("This is a log error message")
        # raise HTTPException(status_code=501, detail="Frank Fatal Error")
        return {"message": "hello world"}


LoggingInstrumentor().instrument()
FastAPIInstrumentor.instrument_app(app)


