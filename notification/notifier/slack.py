import urllib
import json
import requests

API_CHAT_URL = 'https://slack.com/api/chat.postMessage?token={token}&channel={channel}&text={text}'
DEFAULT_TIMEOUT = 10

class Response(object):
    def __init__(self, body):
        self.raw = body
        self.body = json.loads(body)
        self.successful = self.body['ok']
        self.error = self.body.get('error')

class SlackNotifier:

    def __init__(self, config):
        self.__config = config

    def notify(self, notification):

        channel = urllib.quote_plus(notification.user_to_notify.profile.slack_room_name)
        token = self.__config['apikey']
        text = notification.message
        response = requests.get(token, channel=channel, text=text),
                          timeout=DEFAULT_TIMEOUT)

        response.raise_for_status()

        response = Response(response.text)
        if not response.error:
            print "Slack message sent"
        else:
            print "Failed to send Slack message"
