def retrieve(query, collection, n=3):
    res = collection.query([query], n_results=n)
    return res["documents"][0]
