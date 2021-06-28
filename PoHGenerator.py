from hashlib import sha256
from itertools import accumulate

class PoHGenerator():

	def __init__(self, seed):
		self.seed = seed
		self.state = sha256(seed).digest()
	
	def sha(self, state):
		return sha256(state).digest()

	def tick(self, txs):
		''' Create the clock history for the set of transactions '''
		# add the initial state to the beginning of the transaction set
		txs = [self.state] + txs
		# iterate through transactions to produce a history
		return accumulate(txs, lambda state, tx: self.sha(state + self.sha(tx)))


if __name__ == "__main__":
	poh = PoHGenerator(b'hello there! this is a PoH seed!!!')
	txs = [b'tx1', b'tx2', b'tx3']
	print(f'{poh.seed}\n{poh.state}')

	clock_history = poh.tick(txs)

	for tx in txs: print(sha256(tx))

	print('\n\nClock History:')
	for interval in clock_history: print(interval.hex())
