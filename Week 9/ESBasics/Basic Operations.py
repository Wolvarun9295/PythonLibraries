from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es)

e1 = {
    "first_name": "varun",
    "last_name": "nagrare",
    "age": 25,
    "about": "Love watching movies",
    "interests": ['games', 'music'],
}
print(e1)

# Creating the index and inserting document
res = es.index(index='bridgelabz', doc_type='fellowship', id=1, body=e1)

e2 = {
    "first_name": "niharika",
    "last_name": "gupta",
    "age": 32,
    "about": "I like to collect rock albums",
    "interests": ["music"]
}
e3 = {
    "first_name": "Rahul",
    "last_name": "Gidde",
    "age": 25,
    "about": "I like to build cabinets",
    "interests": ["forestry"]
}

# Inserting documents
res = es.index(index='bridgelabz', doc_type='fellowship', id=2, body=e2)
print(e2)
res = es.index(index='bridgelabz', doc_type='fellowship', id=3, body=e3)
print(e3)

# Retrieving document
res = es.get(index='bridgelabz', doc_type='fellowship', id=1)
print(res)

# Delete document
res = es.delete(index='bridgelabz', doc_type='fellowship', id=3)
print(res)

# Search Operation
hits = es.search(index='bridgelabz', body={'query': {'match_all': {}}})
print(f"Got {hits['hits']['total']} hits")

# Match Operation
match = es.search(index='bridgelabz', body={'query': {'match': {'first_name': 'varun'}}})
print(match['hits']['hits'])

# Filter Operation
fil = es.search(index='bridgelabz', body={
    'query': {
        'bool': {
            'must': {
                'match': {
                    'first_name': 'varun'
                }
            },
            "filter": {
                "range": {
                    "age": {
                        "gt": 21
                    }
                }
            }
        }
    }
})
print(fil['hits']['hits'])

# # Aggregation Operation
agg = es.search(index='bridgelabz', doc_type='fellowship',
                body={'query': {"match_all": {}}, "aggs": {"allAges": {"terms": {"field": "age"}}}})
print(agg)


# Bulk Operation
def gendata():
    mywords = ['foo', 'bar', 'baz']
    for word in mywords:
        yield {
            "_index": "bridgelabz",
            "doc": {"fellowship": word},
        }


bk = helpers.bulk(es, gendata())
print(bk)

# Scan Operation
sc = helpers.scan(es, query={"query": {"match": {"name": "rahul"}}}, index="bridgelabz", doc_type="fellowship")
print(sc)

# Response Filtering
fil = es.search(index='bridgelabz', filter_path=['hits.hits._id', 'hits.hits._type'])
print(fil)
