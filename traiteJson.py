json = {'input': 'help language php question problem', 'intent': {'intentName': 'help', 'probability': 0.882000032404141}, 'slots': [{'range': {'start': 14, 'end': 17}, 'rawValue': 'php', 'value': {'kind': 'Custom', 'value': 'php'}, 'entity': 'language', 'slotName': 'language'}, {'range': {'start': 27, 'end': 34}, 'rawValue': 'problem', 'value': {'kind': 'Custom', 'value': 'problem'}, 'entity': 'helpEntity', 'slotName': 'help'}]}

for slot in json['slots']:
    print(slot['rawValue'])
