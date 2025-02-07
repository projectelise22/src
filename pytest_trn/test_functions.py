# Create Functions for Assertions
# For example, find the correct response when given a key domain
def outputResponse(key: str) -> str:
    AssistantResponses = {"weather": "The weather today is",
                          "message_complete": "Sent."}
    return AssistantResponses[key]