import sys, requests, json

# UPDATE THESE VARIABLES FIRST! Make sure each remains within the double quotes!
world_id = "CHANGEME"
xAuthToken = "CHANGEME"
xAppKey = "CHANGEME"

url = "https://www.worldanvil.com/api/aragorn/world/" + world_id
query = ""
for arg in sys.argv:
    if ".py" not in arg and "python" not in arg:
        query = query + "%20" + arg

query = query[3:]
search = url + "/articles?term=" + query

headers = {
"x-auth-token" : xAuthToken,
"x-application-key" : xAppKey,
"Content-type" : "application/json",
"User-Agent" : "Alfred-WorldAnvil User Agent 1.0"
}

r = requests.get(search, headers=headers)
r = json.loads(r.text)

alfred = {"items": [ ]}
for article in r['articles']:
    a_id = article['id']
    a_title = article['title']
    a_type = article['template_type']
    a_view_url = article['url']
    a_edit_url = "https://www.worldanvil.com/world/" + a_type + "/" + a_id + "/edit"

    arg = a_view_url + "-+-" + a_edit_url + "-+-" + a_id + "-+-" + a_type

    item = {
		"title" : a_title,
        "subtitle" : a_view_url,
		"arg" : arg,
	}
    alfred['items'].append(item)

print json.dumps(alfred)	