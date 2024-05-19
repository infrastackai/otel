## Installation

```bash
pip install infrastack-sdk
```

## Example usage

This library allows tracing client-side calls to Chroma vector DB sent with the official [Chroma library](https://github.com/chroma-core/chroma).

```python
from opentelemetry.instrumentation.chromadb import ChromaInstrumentor

ChromaInstrumentor().instrument()
```

This library allows tracing complete LLM applications built with [Langchain](https://github.com/langchain-ai/langchain).


```python
from opentelemetry.instrumentation.langchain import LangchainInstrumentor

LangchainInstrumentor().instrument()
```

This library allows tracing complete LLM applications built with [LlamaIndex](https://github.com/run-llama/llama_index).

```python
from opentelemetry.instrumentation.llamaindex import LlamaIndexInstrumentor

LlamaIndexInstrumentor().instrument()
```

This library allows tracing OpenAI prompts and completions sent with the official [OpenAI library](https://github.com/openai/openai-python).

```python
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

OpenAIInstrumentor().instrument()
```

This library allows tracing client-side calls to Pinecone vector DB sent with the official [Pinecone library](https://github.com/pinecone-io/pinecone-python-client).

```python
from opentelemetry.instrumentation.pinecone import PineconeInstrumentor

PineconeInstrumentor().instrument()
```

This library allows tracing texte generation calls sent with the official [HuggingFace Transformers library](https://github.com/huggingface/transformers).

```python
from opentelemetry.instrumentation.transformers import TransformersInstrumentor

TransformersInstrumentor().instrument()
```

## Privacy

**By default, this instrumentation logs prompts, completions, and embeddings to span attributes**. This gives you a clear visibility into how your LLM application is working, and can make it easy to debug and evaluate the quality of the outputs.

However, you may want to disable this logging for privacy reasons, as they may contain highly sensitive data from your users. You may also simply want to reduce the size of your traces.

To disable logging, set the `TRACELOOP_TRACE_CONTENT` environment variable to `false`.

```bash
INFRASTACK_TRACE_CONTENT=false
```

# OpenTelemetry Semantic Conventions extensions for gen-AI applications

<a href="https://pypi.org/project/opentelemetry-semantic-conventions-ai/">
    <img src="https://badge.fury.io/py/opentelemetry-semantic-conventions-ai.svg">
</a>

This is an extension of the standard [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions) for gen AI applications. It defines additional attributes for spans that are useful for debugging and monitoring prompts, completions, token usage, etc.