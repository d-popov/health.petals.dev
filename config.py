from dataclasses import dataclass

from petals.constants import PUBLIC_INITIAL_PEERS


@dataclass
class ModelInfo:
    dht_prefix: str
    name: str
    href: str
    n_blocks: int
    production: bool


INITIAL_PEERS = PUBLIC_INITIAL_PEERS

MODELS = [
    ModelInfo(
        dht_prefix="Llama-2-70b-chat-hf",
        name="meta-llama/Llama-2-70b-chat-hf",
        href="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf",
        n_blocks=80,
        production=True,
    ),
    ModelInfo(
        dht_prefix="Llama-2-70b-hf",
        name="meta-llama/Llama-2-70b-hf",
        href="https://huggingface.co/meta-llama/Llama-2-70b-hf",
        n_blocks=80,
        production=True,
    ),
    ModelInfo(
        dht_prefix="llama-65b-hf",
        name="enoch/llama-65b-hf",
        href="https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md",
        n_blocks=80,
        production=True,
    ),
    ModelInfo(
        dht_prefix="bigscience/bloom-petals",
        name="bigscience/bloom",
        href="https://huggingface.co/bigscience/bloom",
        n_blocks=70,
        production=True,
    ),
    ModelInfo(
        dht_prefix="bigscience/bloomz-petals",
        name="bigscience/bloomz",
        href="https://huggingface.co/bigscience/bloomz",
        n_blocks=70,
        production=True,
    ),
]
