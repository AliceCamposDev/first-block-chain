from blockchain import Blockchain

block_chain = Blockchain()

block_chain.add_block({
    "Name": "Alice",
    "Amount": 100,
    "Currency": "RXNC",
    "Type": "Deposit",
    "destination": "Main Wallet"
})

block_chain.add_block({
    "Name": "Lilly",
    "Amount": 35,
    "Currency": "RXNC",
    "Type": "Transfer",
    "to": "Alice",
    "message": "Payment for freelance job"
})

block_chain.add_block({
    "Name": "Carol",
    "Amount": 50,
    "Currency": "RXNC",
    "Type": "Withdrawal",
    "destination": "Bank Account"
})

for block in block_chain.chain:
    print(f"\nBlock #{block.index}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Data: {block.data}")
    print(f"Nonce: {block.nonce}")
    print(f"Timestamp: {block.timestamp}")

print("\nBlockchain valid?", block_chain.is_chain_valid())