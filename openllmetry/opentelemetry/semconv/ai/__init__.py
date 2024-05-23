from enum import Enum


class SpanAttributes:
    # Semantic Conventions for LLM requests, this needs to be removed after
    # OpenTelemetry Semantic Conventions support Gen AI.
    # Issue at https://github.com/open-telemetry/opentelemetry-python/issues/3868
    # Refer to https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/llm-spans.md
    # for more detail for LLM spans from OpenTelemetry Community.
    LLM_PROVIDER = "llm.provider"
    LLM_REQUEST_MODEL = "llm.model"
    LLM_REQUEST_MAX_TOKENS = "llm.request.max_tokens"
    LLM_REQUEST_TEMPERATURE = "llm.request.temperature"
    LLM_REQUEST_TOP_P = "llm.top_p"
    LLM_PROMPTS = "llm.prompt"
    LLM_COMPLETIONS = "llm.completion"
    LLM_RESPONSE_MODEL = "llm.response.model"
    LLM_USAGE_COMPLETION_TOKENS = "llm.completion_tokens"
    LLM_USAGE_PROMPT_TOKENS = "llm.prompt_tokens"
    # To be added
    # LLM_RESPONSE_FINISH_REASON = "llm.response.finish_reasons"
    # LLM_RESPONSE_ID = "llm.response.id"

    # LLM
    LLM_REQUEST_TYPE = "llm.request.type"
    LLM_USAGE_TOTAL_TOKENS = "llm.total_tokens"
    LLM_USER = "llm.user"
    LLM_HEADERS = "llm.headers"
    LLM_TOP_K = "llm.top_k"
    LLM_IS_STREAMING = "llm.is_streaming"
    LLM_FREQUENCY_PENALTY = "llm.frequency_penalty"
    LLM_PRESENCE_PENALTY = "llm.presence_penalty"
    LLM_CHAT_STOP_SEQUENCES = "llm.chat.stop_sequences"
    LLM_REQUEST_FUNCTIONS = "llm.request.functions"

    # Vector DB
    VECTOR_DB_VENDOR = "db.system"
    VECTOR_DB_QUERY_TOP_K = "db.vector.query.top_k"

    # Pinecone
    PINECONE_USAGE_READ_UNITS = "pinecone.usage.read_units"
    PINECONE_USAGE_WRITE_UNITS = "pinecone.usage.write_units"

    # LLM Workflows
    INFRASTACK_SPAN_KIND = "infrastack.span.kind"
    INFRASTACK_WORKFLOW_NAME = "infrastack.workflow.name"
    INFRASTACK_ENTITY_NAME = "infrastack.entity.name"
    INFRASTACK_ENTITY_INPUT = "infrastack.entity.input"
    INFRASTACK_ENTITY_OUTPUT = "infrastack.entity.output"
    INFRASTACK_ASSOCIATION_PROPERTIES = "infrastack.association.properties"

    # Deprecated
    INFRASTACK_CORRELATION_ID = "infrastack.correlation.id"

    # Watson/genai LLM
    LLM_DECODING_METHOD = "llm.watsonx.decoding_method"
    LLM_RANDOM_SEED = "llm.watsonx.random_seed"
    LLM_MAX_NEW_TOKENS = "llm.watsonx.max_new_tokens"
    LLM_MIN_NEW_TOKENS = "llm.watsonx.min_new_tokens"
    LLM_REPETITION_PENALTY = "llm.watsonx.repetition_penalty"


class Events(Enum):
    DB_QUERY_EMBEDDINGS = "db.query.embeddings"
    DB_QUERY_RESULT = "db.query.result"


class EventAttributes(Enum):
    # Query Embeddings
    DB_QUERY_EMBEDDINGS_VECTOR = "db.query.embeddings.vector"

    # Query Result (canonical format)
    DB_QUERY_RESULT_ID = "db.query.result.id"
    DB_QUERY_RESULT_SCORE = "db.query.result.score"
    DB_QUERY_RESULT_DISTANCE = "db.query.result.distance"
    DB_QUERY_RESULT_METADATA = "db.query.result.metadata"
    DB_QUERY_RESULT_VECTOR = "db.query.result.vector"
    DB_QUERY_RESULT_DOCUMENT = "db.query.result.document"


class LLMRequestTypeValues(Enum):
    COMPLETION = "completion"
    CHAT = "chat"
    RERANK = "rerank"
    EMBEDDING = "embedding"
    UNKNOWN = "unknown"


class InfrastackSpanKindValues(Enum):
    WORKFLOW = "workflow"
    TASK = "task"
    AGENT = "agent"
    TOOL = "tool"
    UNKNOWN = "unknown"
