import hashlib
import time
from typing import Dict, Any

class Block:
    def __init__(
        self,
        index: int,
        previous_hash: str,
        timestamp: float,
        data: Dict[str, Any],
        nonce: int = 0
    ) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = (
            str(self.index) +
            self.previous_hash +
            str(self.timestamp) +
            str(self.data) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()