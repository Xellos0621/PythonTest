import json
from datetime import datetime
from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
# aws.ec2
# aws.s3
# aws.backup
# aws.iam1

eventSource = 'aws.ec2'
eventRegion = 'ap-northeast-2'
eventDetailType = 'AWS API Call via CloudTrail'
HOOK_URL = 'webhook url'
SLACK_CHANNEL = '채널명'
ACCOUNT = '계정명'
COLOR = '#FF8C00'


def list_to_string(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()


def message(event_source, event_region, nowdate):
    message = {
        "channel": SLACK_CHANNEL,
        "attachments": [{
            "color": COLOR,
            "blocks": [{
                "type": "section",
                "fields": [{
                    "type": "mrkdwn",
                    "text": "*계정*\n" + ACCOUNT
                },
                    {
                        "type": "mrkdwn",
                        "text": "*실행자*\n" + "use_userName"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*리소스*\n" + event_source
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*이벤트*\n" + "eventName"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*리전*\n" + event_region
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*인스턴스*\n" + "insName"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*발생시간*\n" + nowdate
                    },
                    {
                        "type": "mrkdwn",
                        "text": "scalingString"
                    }
                ]
            }]
        }],
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "eventName" + ' 이벤트가 발생되었습니다.'
            }
        }]
    }
    return message


def now_date():
    now = datetime.now()
    nowdatetime = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " KST"
    return nowdatetime


def main():

    if eventDetailType == 'AWS API Call via CloudTrail':
        event_type = 'AssumedRole'

        if event_type != 'AssumedRole':
            print(now_date())
            if eventSource == 'aws.ec2':
                print(eventSource)
            elif eventSource == 'aws.s3':
                print(eventSource)
            elif eventSource == 'aws.backup':
                print(eventSource)
            elif eventSource == 'aws.iam':
                print(eventSource)
            else:
                print("예외")
        else:
            print("event_type != AssumedRole 끝")
    else:
        print("eventDetailType == AWS API Call via CloudTrail 끝")
    slack_message = message(eventSource, eventRegion, now_date())

    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))

    response = urlopen(req)
    response.read()
    print("Message posted to %s", slack_message['channel'])


if __name__ == '__main__':
    main()
