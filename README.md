# fibonacci with Sub-millisecond latency(for large number)

When a user query for the Fibonacci result for a particular number; 
First it searches that number in the cache, if that number does not exist in the cache
then it serves the result from backend and also reinsert all result from backend to cache.
If query search does not exist in backend also then it calculates the result for that number 
and also set cache for all number before to query number.
