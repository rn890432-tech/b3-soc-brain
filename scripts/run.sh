#!/usr/bin/env bash
# Run the B3 SOC Brain API server.
set -euo pipefail

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
RELOAD="${RELOAD:-false}"

RELOAD_FLAG=""
if [ "$RELOAD" = "true" ]; then
  RELOAD_FLAG="--reload"
fi

exec uvicorn src.api.main:app --host "$HOST" --port "$PORT" ${RELOAD_FLAG:+"$RELOAD_FLAG"}
