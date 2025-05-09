# download_llama.py
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="meta-llama/Llama-2-7b-chat-hf",
    repo_type="model",
    local_dir="models/llama-2-7b-chat-hf"
)
