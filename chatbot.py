from __future__ import unicode_literals, print_function
import io
import json
from tkinter import *
from snips_nlu import SnipsNLUEngine 
from snips_nlu.default_configs import CONFIG_EN
from googleapiclient.discovery import build


def google_search(search_term, **kwargs):
    api_key = "AIzaSyB0C9N0vgHs_sKTQ_497KaxL8-0AusOxQ8"
    cse_id = "003869999729551112699:0aizy1w_xcq"
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

with io.open("dataset.json") as f:
    sample_dataset = json.load(f)
    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine = nlu_engine.fit(sample_dataset)
    plain_question = input("What is your question? ex: I have a problem with the language php\n")
    parsing = nlu_engine.parse(plain_question)

print(parsing)

explicit_question = ""

if not parsing['slots'] == "[]":
    for slot in parsing['slots']:
        explicit_question += (slot['rawValue'] + ' ' + slot['slotName'] + ' ')

if explicit_question == "":
    explicit_question = plain_question

print(explicit_question)


g_results = json.loads(json.dumps(google_search(explicit_question)))
print("\n\n" + "*" * 30 + "\nYou can find help on the following links:")

for x in range(3):
    print("  -  " + g_results['items'][x]['title'] + " :\n" + g_results['items'][x]['link'])
