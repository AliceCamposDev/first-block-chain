from block import Block
from time import time
from typing import Dict, Any, List, Optional
from transaction import Transaction

class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 1
        self.difficulty = 2

    def create_genesis_block(self) -> Block:
        return Block(0, "0", float(time()), [Transaction("System","Genesis",0)], 0)

    def get_last_block(self) -> Block:
        return self.chain[-1]
    
            
    def mine_pending_transactions(self, miner_address: str) -> Optional[Block]:
        if not self.pending_transactions:
            print("No pending transactions to mine.")
            return None

        mine_reward_transaction = Transaction("System", miner_address, self.mining_reward)
        transactions_to_mine = [mine_reward_transaction] + self.pending_transactions

        last_block = self.get_last_block()
        index = len(self.chain)
        timestamp = float(time())
        nonce = 0

        print(f"\nStarting to mine Block {index}...")
        print(f"  Transactions to include: {len(transactions_to_mine)}")
        print(f"  Difficulty: {self.difficulty}")

        while True:
            block = Block(index, last_block._hash, timestamp, transactions_to_mine, nonce)
            if block._hash.startswith('0' * self.difficulty):
                print(f"Block {index} mined successfully! Hash: {block._hash[:15]}...")
                self.chain.append(block)
                self.pending_transactions = []
                return block
            nonce += 1
            
            
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr._hash != curr.compute_hash():
                return False
            if curr.previous_hash != prev._hash:
                return False
        return True
    
    def get_balance(self, address: str) -> float:
        balance = 0.0
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.recipient == address:
                    balance += tx.amount
        return balance
        
    #TODO: float to int or decimal or string, i will decide later
    def add_transaction(self, sender: str, recipient: str, amount: float) -> bool:
        if amount <= 0:
            print("Not enough funds or invalid amount")
            return False
        
        if sender == recipient:
            print("Sender and recipient cannot be the same")
            return False
        
        if sender != "System" and self.get_balance(sender) < amount:
            print(f"Insufficient funds for {sender}. Balance: {self.get_balance(sender)}, Attempted: {amount}")
            return False

        new_transaction = Transaction(sender, recipient, amount)
        self.pending_transactions.append(new_transaction)
        print(f"Transaction added: {new_transaction}")
        return True
    
    def display_chain(self) -> None:
        print("\n--- Blockchain ---")
        for block in self.chain:
            print(block)
            for tx in block.transactions:
                print(f"  - {tx}")
        print("------------------\n")