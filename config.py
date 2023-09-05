from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo


INITIAL_PEERS = PUBLIC_INITIAL_PEERS

MODELS = [
    ModelInfo(
        dht_prefix="StableBeluga2-hf",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="CodeLlama-34b-Instruct-hf",
        repository="https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf",
        n_blocks=48,
    ),   
    ModelInfo(
        dht_prefix="WizardCoder-Python-34B-V1_0-hf",
        repository="https://huggingface.co/WizardLM/WizardCoder-Python-34B-V1.0",
        n_blocks=48,
    ),
    ModelInfo(
        dht_prefix="WizardCoder-Python-13B-V1-0-hf",
        repository="https://huggingface.co/WizardLM/WizardCoder-Python-13B-V1.0",
        n_blocks=36,
    ),
    ModelInfo(
        dht_prefix="WizardCoder-3B-V1_0",
        repository="https://huggingface.co/WizardLM/WizardCoder-3B-V1.0",
        n_blocks=48,
    ),
    ModelInfo(
        dht_prefix="Llama-2-70b-chat-hf",
        repository="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="Llama-2-70b-hf",
        repository="https://huggingface.co/meta-llama/Llama-2-70b-hf",
        num_blocks=80,
    ),
    # ModelInfo(
    #     dht_prefix="llama-65b-hf",
    #     repository="https://huggingface.co/huggyllama/llama-65b",
    #     num_blocks=80,
    # ),
    # ModelInfo(
    #     dht_prefix="bigscience/bloomz-petals",
    #     repository="https://huggingface.co/bigscience/bloomz",
    #     num_blocks=70,
    # ),
    # ModelInfo(
    #     dht_prefix="bigscience/bloom-petals",
    #     repository="https://huggingface.co/bigscience/bloom",
    #     num_blocks=70,
    # ),
]
