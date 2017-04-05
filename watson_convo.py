import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='e98be26e-bd0b-4007-af94-9b3f36d9a01c',
    password='eOVbRtHWxtFP',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = 'e50eea38-c10e-4b78-8c96-a2222247504e'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'hello'})
print(json.dumps(response, indent=2))