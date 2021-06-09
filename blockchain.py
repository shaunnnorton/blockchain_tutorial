import time
import json
import hashlib


class BlockChain():
    def __init__(self) -> None:
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """Creates a new block and adds to the existing chain"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            "transactons": self.current_transactions,
            previous_hash: previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Adds a new transaction to already existing transactions"""
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            }
        )
        return self.lastblock['index'] + 1

    @staticmethod
    def hash(block):
        """Hashes a block"""
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string).hexdigest

    @property
    def lastblock(self):
        """Calls and returns the last block of the chain."""
        return self.chain[-1]

    def register_node():
        '''Registers a new node and adds to the network'''
        pass

    def valid_chain():
        '''Checks if subsequent blocks in the chain are vaild or not'''
        pass

    def proof_of_work(self, last_proof):
        """This method is where you the consensus algorithm is implemented.
        It takes two parameters including self and last_proof"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """This method validates the block"""
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexigest()
        return guess_hash[:4] == "0000"
