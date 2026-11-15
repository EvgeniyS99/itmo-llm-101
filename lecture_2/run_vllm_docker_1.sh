#!/usr/bin/env bash
set -euo pipefail

# Requires Docker and NVIDIA Container Toolkit.
MODEL_NAME="${MODEL_NAME:-Qwen/Qwen2.5-1.5B-Instruct}"
PORT="${PORT:-11001}"
CACHE_DIR="${HF_HOME:-$HOME/.cache/huggingface}"
mkdir -p "$CACHE_DIR"

docker run --rm --gpus all --ipc=host \
  -v "$CACHE_DIR:/root/.cache/huggingface" \
  -e "HF_TOKEN=${HF_TOKEN:-}" \
  -p "${PORT}:8000" \
  vllm/vllm-openai:latest \
  --model "$MODEL_NAME" \
  --dtype half \
  --max-model-len 2048 \
  --gpu-memory-utilization 0.75
