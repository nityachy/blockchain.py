import hashlib as hasher

# each block needs to be stored with timestamp/index

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp 
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash))

        return sha.hexdigest()

#block structure done


import datetime as date 

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

#genesis block done - block of index 0 
#manually constructed in many cases

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is a Block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, last_block, this_hash)    

#function will take previous block in chain as parameter

#loop + add 30 blocks

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#30 blocks added after genesis block

num_of_blocks_to_add = 30

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = blockchain[len(blockchain) - 1]

    print "Block #{} has been added to this blockchain".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)

#error with print statements 
