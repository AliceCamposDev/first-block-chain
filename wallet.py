from time import time
import hashlib
from blockchain import Blockchain

class Wallet:
    def __init__(self, address: str):
        self.address = address

    def get_balance(self, blockchain: 'Blockchain') -> float:
        return blockchain.get_balance(self.address)

    def __repr__(self) -> str:
        return f"Wallet({self.address[:8]}...)"

def generate_address() -> str:
    return hashlib.sha256(str(time()).encode()).hexdigest()