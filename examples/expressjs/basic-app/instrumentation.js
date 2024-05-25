require('dotenv').config()

"use strict";
const process = require("process");
const opentelemetry = require("@opentelemetry/sdk-node");
const {
  getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");
const {
  OTLPTraceExporter,
} = require("@opentelemetry/exporter-trace-otlp-grpc");
const { Resource } = require("@opentelemetry/resources");
const {
  SemanticResourceAttributes,
} = require("@opentelemetry/semantic-conventions");
 
const exporterOptions = {
  url: `${process.env.OTEL_EXPORTER_OTLP_ENDPOINT}/v1/traces`,
  headers: { 'infrastack-api-key': process.env.OTEL_EXPORTER_OTLP_HEADERS.split('=')[1] },
  compression: 'gzip',
}

const traceExporter = new OTLPTraceExporter(exporterOptions);
 
const sdk = new opentelemetry.NodeSDK({
  traceExporter,
  instrumentations: [getNodeAutoInstrumentations()],
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: "{{YOUR_SERVICE_NAME}}",
    [SemanticResourceAttributes.SERVICE_VERSION]: "{{YOUR_SERVICE_VERSION}}",
    [SemanticResourceAttributes.SERVICE_INSTANCE_ID]: process.env.POD_NAME ?? `uuidgen`
  }),
});
 
// initialize the SDK and register with the OpenTelemetry API
sdk.start();
 
// gracefully shut down the SDK on process exit
process.on("SIGTERM", () => {
  sdk
    .shutdown()
    .then(() => console.log("Tracing terminated"))
    .catch((error) => console.log("Error terminating tracing", error))
    .finally(() => process.exit(0));
});
