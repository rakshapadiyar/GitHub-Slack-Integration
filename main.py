import requests
from requests.structures  import CaseInsensitiveDict
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    print("Github Webhook Received")
    url = "https://hooks.slack.com/services/*******/***********/******************"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{"text":"Some changes detected in the Github Repository"}'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)