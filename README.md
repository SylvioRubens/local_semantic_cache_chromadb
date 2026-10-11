This project focus in tests and learnings about semantic cache.

We know that in nowadays, one of the most important steps of governance for an AI project is the cost associated to LLMs in order to process the natural language questions and retrieval the answer. 

With this in mind, the idea of this project is to build a simple structure of a Q&A agent with local stored cache using ChromaDB. This project's only purpose is to practice de development of applications that could take advantege of semantic cache, making it possible to receive the question and instead of passing it directly to our LLM, verify if we could answer this question looking at the cache, bringing the same answer as in the past.

This project may help us understanding: 
- how the semantic cache works;
- How to setup a threshold of accuracy and retrieve the right answers from cache;
- How this impacts in our cost prediction;