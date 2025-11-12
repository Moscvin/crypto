import json  # Importăm modulul json

import hashlib  # Importăm modulul hashlib pentru funcții de hash

blockchain = [
    {
        "from": "",
        "to": "",
        "amount": 0.0 
    },
] 

def dataToHash(data):
    json_data = json.dumps(data, sort_keys=True)
    binary_data = json_data.encode()
    return hashlib.sha256(binary_data).hexdigest()[:10] # Returnează primele 10 caractere ale hash-ului

def addNewBlock(from_address, to_address, amount):
    prev_block = blockchain[-1]
    prev_hash = dataToHash(prev_block)
    new_block = {
        "from": from_address,
        "to": to_address,
        "amount": amount,
        "prev_hash": prev_hash
    }
    blockchain.append(new_block)
def validateBlockchain():
    prev_block = None
    for block in blockchain:
        if prev_block is not None:
            expected_prev_hash = dataToHash(prev_block)
            if block.get("prev_hash") != expected_prev_hash:
                return False
        prev_block = block
    return True

addNewBlock("Alice", "Bob", 50.0)
addNewBlock("Bob", "Charlie", 25.0)
addNewBlock("Charlie", "Dave", 10.0)
print(json.dumps(blockchain, indent=4))
