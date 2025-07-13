from blockchain import Blockchain
from transaction import Transaction # Ensure Transaction is imported if used in genesis block directly
from time import time # Ensure time is imported if used in genesis block

def test_blockchain() -> None:
    # 1. Create the blockchain (genesis block)
    print("🧱 Creating blockchain...")
    my_chain = Blockchain()
    assert len(my_chain.chain) == 1
    assert my_chain.chain[0].index == 0
    assert my_chain.chain[0].previous_hash == "0"
    # Note: If your genesis block's transaction sender is 'System', ensure it matches.
    assert my_chain.chain[0].transactions[0].sender == "System"
    print("Blockchain created with Genesis Block.")


    # 2. Test: try to mine without pending transactions
    print("\n🚫 Attempting to mine without pending transactions...")
    assert my_chain.mine_pending_transactions("minerX") is None
    print("Successfully prevented mining with no pending transactions.")

    # 3. Test: add invalid transaction (negative amount)
    print("\n❌ Testing invalid transaction: negative amount")
    assert not my_chain.add_transaction("alice", "bob", -10)
    print("Negative amount transaction rejected.")

    # 4. Test: transaction with sender == recipient
    print("\n❌ Testing invalid transaction: sender == recipient")
    assert not my_chain.add_transaction("alice", "alice", 5)
    print("Sender and recipient cannot be the same. Transaction rejected.")

    # 5. Test: transaction without sufficient balance
    print("\n💸 Testing transaction without sufficient balance")
    assert not my_chain.add_transaction("alice", "bob", 10) # Alice has 0 balance initially
    print("Transaction rejected due to insufficient funds.")

    # 6. Add a 'System' type transaction (no balance check)
    # This is typically handled internally by mine_pending_transactions as a reward
    # but for testing, we can add it directly to simulate initial funds for 'alice'.
    # In a real system, you wouldn't directly add System transactions like this outside of mining.
    print("\n✅ Adding initial reward transaction for Alice (System to Alice)")
    # Note: Your `mine_pending_transactions` already adds a 'System' transaction.
    # Adding another one here directly can inflate balance if not careful.
    # This step might be redundant or confusing if `mine_pending_transactions` is the primary way coins enter.
    # For this test, let's assume it's just to give Alice some initial coin *outside* of mining the first block.
    # If the intent is for Alice to get funds *only* from mining, skip this `add_transaction`.
    # However, if it's meant to test a `System` originating transaction, it's fine.
    assert my_chain.add_transaction("System", "alice", 20)
    print("System-originated transaction for Alice added to pending.")


    # 7. Mine block with 1 transaction (System -> alice) + miner reward
    print("\n⛏️ Mining block with pending transactions and miner reward...")
    # 'miner1' will mine the block and get a reward (1 coin as per your `mining_reward = 1`)
    # and the (System -> alice, 20) transaction will be included.
    block1 = my_chain.mine_pending_transactions("miner1")
    assert block1 is not None
    assert len(my_chain.chain) == 2 # Genesis + Block1
    print(f"Block 1 (Index: {block1.index}) mined by miner1.")


    # 8. Check Alice's balance (should be 20 + miner1's reward if miner1 == alice)
    # Let's clarify: miner1 gets 1, Alice gets 20 from System.
    print("\n💰 Checking Alice's balance")
    # Alice's balance: 20 (from System)
    assert my_chain.get_balance("alice") == 20
    print(f"Alice's balance: {my_chain.get_balance('alice')}")
    # Miner1's balance: 1 (from mining Block 1)
    assert my_chain.get_balance("miner1") == 1
    print(f"Miner1's balance: {my_chain.get_balance('miner1')}")


    # 9. Create new transaction (alice -> bob) and mine
    print("\n✅ New transaction: alice → bob")
    assert my_chain.add_transaction("alice", "bob", 5)
    # Now, miner1 mines again, getting another reward
    my_chain.mine_pending_transactions("miner1")
    print("Alice to Bob transaction mined.")


    # 10. Check updated balances
    print("\n💰 Checking updated balances")
    # Alice's balance: 20 (from System) - 5 (to Bob) = 15
    assert my_chain.get_balance("alice") == 15
    # Bob's balance: 5 (from Alice)
    assert my_chain.get_balance("bob") == 5
    # Miner1's balance: 1 (from Block 1) + 1 (from Block 2) = 2
    assert my_chain.get_balance("miner1") == 2
    print(f"Alice's balance: {my_chain.get_balance('alice')}")
    print(f"Bob's balance: {my_chain.get_balance('bob')}")
    print(f"Miner1's balance: {my_chain.get_balance('miner1')}")

    # 11. Verify chain integrity
    print("\n🔍 Verifying blockchain integrity")
    assert my_chain.is_chain_valid()
    print("Blockchain is valid.")

    # 12. Try transaction with amount exceeding current balance
    print("\n❌ Transaction exceeding balance")
    assert not my_chain.add_transaction("bob", "alice", 100) # Bob only has 5
    print("Transaction rejected as expected.")

    # 13. Display the blockchain
    print("\n📦 Displaying blockchain:")
    my_chain.display_chain()

    print("\n✅ All tests passed.")

if __name__ == "__main__":
    test_blockchain()