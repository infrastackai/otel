'use strict'
 
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
 
import {
    SEMRESATTRS_SERVICE_NAME,
    SEMRESATTRS_SERVICE_VERSION,
    SEMRESATTRS_SERVICE_INSTANCE_ID,
    SEMRESATTRS_SERVICE_NAMESPACE,
    SEMRESATTRS_K8S_NAMESPACE_NAME,
    SEMRESATTRS_K8S_POD_NAME
  } from '@opentelemetry/semantic-conventions';
import { Resource } from '@opentelemetry/resources';
 
const traceExporter = new OTLPTraceExporter();
 
const sdk = new NodeSDK({
    resource: new Resource({
        [SEMRESATTRS_SERVICE_NAME]: 'your-service-name', // Change this to your service name
        [SEMRESATTRS_SERVICE_VERSION]: "0.0.1", // Change this to your service version
        [SEMRESATTRS_SERVICE_INSTANCE_ID]: process.env.POD_NAME ?? "", // you can use uuid if pod name is not available
        [SEMRESATTRS_K8S_NAMESPACE_NAME]: process.env.POD_NAMESPACE ?? "",
        [SEMRESATTRS_K8S_POD_NAME]: process.env.POD_NAME ?? "",
        "project.id": "your-project-id", // Change this to your project id to filter traces, metrics, and logs by project
    }),
    traceExporter,
    instrumentations: [
      getNodeAutoInstrumentations({
        '@opentelemetry/instrumentation-fs': {
          requireParentSpan: true,
        },
      })
    ],
});
  
sdk.start(); 
