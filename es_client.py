import json
import requests


def get_sorted_contents(params):
    contents = []
    es_url = "http://localhost:9200/contents/_search/template"
    with requests.Session() as session:
        response = session.post(es_url, data=json.dumps(params), headers={"Content-Type":"application/json"})
        for hit in response.json()["hits"]["hits"]:
            contents.append(hit['_source'])
    return contents

def main():
    es_params = {
        "id": "sort-contents",
        "params": {
            "content_type": "movie",
            "genre": "action",
            "sort": "view_count",
            "order": "desc"
        }
    }
    contents = get_sorted_contents(es_params)
    for content in contents:
        print(content['title'], content['view_count'])

if __name__ == '__main__':
    main()
