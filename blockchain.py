from block import Block
from time import time
from typing import Dict, Any

class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self) -> Block:
        return Block(0, "0", float(time()), {"Message": "Genesis Block"}, 0)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]) -> None:
        last_block = self.get_last_block()
        new_block = self.mine_block(data, last_block.hash)
        self.chain.append(new_block)

    def mine_block(self, data: Dict[str,Any], previous_hash: str) -> Block:
        index = len(self.chain)
        timestamp = float(time())
        nonce = 0

        while True:
            block = Block(index, previous_hash, timestamp, data, nonce)
            if block.hash.startswith('0' * self.difficulty):
                print(f"Block mined: {block.hash}")
                return block
            nonce += 1
            
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.compute_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True