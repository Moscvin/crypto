import json  

import hashlib  

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
    return hashlib.sha256(binary_data).hexdigest()[:4] 

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
        if prev_block:
            actual_prev_hash = dataToHash(prev_block)
            recorded_prev_hash = block["prev_hash"] 
            if actual_prev_hash != recorded_prev_hash:
                print("Blockchain is invalid!, expected prev_hash:", actual_prev_hash, "but got:", recorded_prev_hash)
            else:
                print("Block is valid, prev_hash matches:", actual_prev_hash) 
        prev_block = block

addNewBlock("Alice", "Bob", 50.0)
addNewBlock("Bob", "Charlie", 25.0)
addNewBlock("Charlie", "Dave", 10.0)
print(json.dumps(blockchain, indent=4))
print("Validating blockchain...")
validateBlockchain()

block = 2 
amount = blockchain[block]["amount"]
expected_hash = blockchain[block+1]["prev_hash"]


hash = ""
 
while hash != expected_hash:
    amount += 1
    blockchain[block]["amount"] = amount
    hash = dataToHash(blockchain[block])
print("After adjusting amount to fix hash: , amount =", amount)
print(json.dumps(blockchain, indent=4))
validateBlockchain()

