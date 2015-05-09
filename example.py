from elasticsearch import Elasticsearch

es = Elasticsearch()


def print_all_text():
    res = es.search(index="stg", body={"query": {"match_all": {}}})
    for hit in res['hits']['hits']:
        print "Chapter " + hit['_source']['chapter']
        print "verse " + hit['_source']['verse']
        print hit['_source']['text']

def search_all_text(key, value):
    res = es.search(index="stg", body={"query": {"match": {key:value}}})
    for hit in res['hits']['hits']:
        print "Chapter " + hit['_source']['chapter']
        print "verse " + hit['_source']['verse']
        print hit['_source']['text']

#print_all_text()
search_all_text("text", "desire")