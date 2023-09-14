from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

UPDATE_PERIOD = 10
INITIAL_PEERS = PUBLIC_INITIAL_PEERS

INITIAL_PEERS = [
    "/ip4/20.101.62.76/tcp/31337/p2p/QmRHP8PQbGCHV7zwBWH2bPipsYfJx44Eo87kdgyteug5Bs",
    "/ip4/92.247.170.10/tcp/31337/p2p/QmSXEQzmS61WcFF6PaFu4NJdwGwtDSPQ67ErGKjTkcTSay",
    "/ip4/192.168.0.10/tcp/31337/p2p/QmSXEQzmS61WcFF6PaFu4NJdwGwtDSPQ67ErGKjTkcTSay",
]
MODELS = [
    # ModelInfo(
    #     dht_prefix="StableBeluga2-hf",
    #     repository="https://huggingface.co/petals-team/StableBeluga2",
    #     num_blocks=80,
    # ),
    # ModelInfo(
    #     dht_prefix="CodeLlama-34b-Instruct-hf",
    #     repository="https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf",
    #     num_blocks=80,
    # ),   
    # ModelInfo(
    #     dht_prefix="WizardCoder-Python-34B-V1_0-hf",
    #     repository="https://huggingface.co/WizardLM/WizardCoder-Python-34B-V1.0",
    #     num_blocks=80,
    # ),
    ModelInfo(
        dht_prefix="WizardCoder-Python-13B-V1-0-hf",
        repository="https://huggingface.co/WizardLM/WizardCoder-Python-13B-V1.0",
        num_blocks=40,
    ),
    # ModelInfo(
    #     dht_prefix="WizardCoder-3B-V1-0-hf",
    #     repository="https://huggingface.co/WizardLM/WizardCoder-3B-V1.0",
    #     num_blocks=20,
    # ),
    # ModelInfo(
    #     dht_prefix="Llama-2-70b-chat-hf",
    #     repository="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf",
    #     num_blocks=80,
    # ),
    # ModelInfo(
    #     dht_prefix="Llama-2-70b-hf",
    #     repository="https://huggingface.co/meta-llama/Llama-2-70b-hf",
    #     num_blocks=80,
    # ),
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
