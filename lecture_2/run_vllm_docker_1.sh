MODEL_NAME="Qwen/Qwen2.5-1.5B-Instruct-AWQ"
IMAGE_NAME="vllm/vllm-openai:latest"
PORT=11001
HUGGINGFACE_TOKEN=""
CACHE_DIR="$HOME/.cache/huggingface"
CUDA_VISIBLE_DEVICES=3

docker run --gpus all \
    -v ${CACHE_DIR}:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=${HUGGINGFACE_TOKEN}" \
    --env "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}" \
    -p ${PORT}:8000 \
    --ipc=host \
    ${IMAGE_NAME} \
    --model ${MODEL_NAME} \
    --enable-auto-tool-choice \
    --tool-call-parser=hermes \
    --gpu-memory-utilization 0.7
