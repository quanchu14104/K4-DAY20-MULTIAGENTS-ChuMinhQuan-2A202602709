---
name: structured-log-parsing-and-normalization
description: Use when parsing log files into structured JSON to ensure correct schema versions, metadata keys, and service name transformations.
---
- Replace hyphens with underscores in service names when required by output specifications (e.g., `payment-service` becomes `payment_service`).
- Sort output lists by primary and secondary keys (e.g., service name then ascending UTC timestamp) exactly as requested.
- Ensure top-level JSON objects contain all mandatory header keys (e.g., `schema_version` and `generated_by`) with correct types and values.
