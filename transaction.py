import hashlib
import json
from typing import Dict, Any
from time import time

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float) -> None:
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = float(time())
        self._hash = ""
        
    @property
    def hash(self) -> str:
        return self.compute_hash()

    def compute_hash(self) -> str:
        transaction_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(transaction_string).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        return{
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

    def __repr__(self) -> str:
        return f"Tx({self.sender[:10]}... -> {self.recipient[:10]}...: {self.amount})"


