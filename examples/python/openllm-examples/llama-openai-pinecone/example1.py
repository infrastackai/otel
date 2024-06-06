#!pip3 install infrastack-otel
#!pip3 install llama-index
#!pip3 install llama-index-vector-stores-pinecone
#!pip3 install opentelemetry-sdk
#!pip3 install pinecone

import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter
)

OTEL_EXPORTER_OTLP_ENDPOINT = "collector-us1.infrastack.ai"
OTEL_EXPORTER_OTLP_HEADERS = "<INFRASTACK-API-KEY>"


os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = OTEL_EXPORTER_OTLP_ENDPOINT
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = OTEL_EXPORTER_OTLP_HEADERS

otlp_exporter = OTLPSpanExporter(
    endpoint = OTEL_EXPORTER_OTLP_ENDPOINT,
    headers=(tuple(OTEL_EXPORTER_OTLP_HEADERS.split("=")),)
)

processor = BatchSpanProcessor(otlp_exporter)
provider = TracerProvider(resource=Resource.create({"service.name": "python.RAGexample.traces"}))
provider.add_span_processor(processor)


# @title Instrumenting llama_index, openai and pinecone

from llama_index.core import Document, Settings, StorageContext, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec

from opentelemetry.instrumentation.llamaindex import LlamaIndexInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.pinecone import PineconeInstrumentor

# @title Instrumenting the frameworks

LlamaIndexInstrumentor().instrument(tracer_provider = provider)
OpenAIInstrumentor().instrument(tracer_provider = provider)
PineconeInstrumentor().instrument(tracer_provider = provider)

# @title Initializing the Prisma Doc retrieval engine

OPENAI_API_KEY="<OPENAI-API-KEY>"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
PINECONE_API_KEY= "<PINECONE-API-KEY>"

pc = Pinecone(api_key=PINECONE_API_KEY)

Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

my_vector_store = PineconeVectorStore(pc.Index("my-docs"))
my_index = VectorStoreIndex.from_vector_store(vector_store=my_vector_store)

# @title run the retriever

retriever = my_index.as_retriever(similarity_top_k=5)
results = retriever.retrieve("find my important docs")
