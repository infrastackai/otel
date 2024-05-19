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

OTEL_EXPORTER_OTLP_ENDPOINT = "https://collector-us1.infrastack.ai"
OTEL_EXPORTER_OTLP_HEADERS = "infrastack-api-key=your-infrastack-key"

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

from opentelemetry.instrumentation.llamaindex import LlamaIndexInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.pinecone import PineconeInstrumentor

from pinecone import Pinecone, ServerlessSpec


# @title Initializing the Prisma Doc retrieval engine

OPENAI_API_KEY="your-openai-key"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
PINECONE_API_KEY= "your-pinecone-key"

pc = Pinecone(api_key=PINECONE_API_KEY)
prisma_index = pc.Index("example-index")

Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

prisma_vector_store = PineconeVectorStore(pc.Index("example-index"))
prisma_index = VectorStoreIndex.from_vector_store(vector_store=prisma_vector_store)

# Retrieve pinecode documents
prisma_retriever = prisma_index.as_retriever(similarity_top_k=5)
results = prisma_retriever.retrieve("What are the relevant documents?")