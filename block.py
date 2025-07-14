import hashlib
from typing import Dict, Any, List
from transaction import Transaction
import json


class Block:
    def __init__(
        self,
        index: int,
        previous_hash: str,
        timestamp: float,
        transactions: List[Transaction],
        nonce: int = 0,
    ) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self._hash = self.compute_hash()

    def compute_hash(self) -> str:
        transactions = [tx.to_dict() for tx in self.transactions]
        block_content = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": transactions,
            "nonce": self.nonce,
        }
        block_string = json.dumps(block_content, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def __repr__(self) -> str:
            return (f"Block(Index: {self.index}, Hash: {self._hash[:8]}..., "
                    f"Prev_Hash: {self.previous_hash[:8]}..., Nonce: {self.nonce}, "
                    f"Tx_Count: {len(self.transactions)})")