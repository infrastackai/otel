"""Unit tests configuration module."""

import os
import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.pinecone import PineconeInstrumentor

pytest_plugins = []


@pytest.fixture(scope="session")
def exporter():
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)

    provider = TracerProvider()
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    OpenAIInstrumentor().instrument()
    PineconeInstrumentor().instrument()

    return exporter


@pytest.fixture(autouse=True)
def clear_exporter(exporter):
    exporter.clear()


@pytest.fixture(autouse=True)
def environment():
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = "test_api_key"
    if "PINECONE_API_KEY" not in os.environ:
        os.environ["PINECONE_API_KEY"] = "test_api_key"
    if "PINECONE_ENVIRONMENT" not in os.environ:
        os.environ["PINECONE_ENVIRONMENT"] = "gcp-starter"


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["authorization"]}
