## Description
This repo contains a small implementation of a Proof of History (PoH) clock. Proof of History is a mechanism designed to order the set of transactions in the cryptocurrency [Solana](https://solana.com/). It involves the sequential hashing of an input with a non-reversible cryptographic hash function. 

The correctness of the sequence is easy to verify; given a set of hash digests D, it can be proven that a digest d<sub>i</sub> &isin; D existed prior to the creation of some d<sub>j</sub> &isin; D such that i &lt; j.