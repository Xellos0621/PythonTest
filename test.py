eventName = "TagUser"

if eventName != "TagUser":
    # slack 으로 보낼 메세지 설정
    slack_message = {
        "channel": SLACK_CHANNEL,
        "attachments": [{
            "color": "#eb4034",
            "blocks": [{
                "type": "section",
                "fields": [{
                    "type": "mrkdwn",
                    "text": "*실행자*\n" + use_userName
                },
                    {
                        "type": "mrkdwn",
                        "text": "*리소스*\n" + event_source
                    },
                    {
                        "type": "mrkdwn",
                        "text": add_userName
                    },
                    {
                        "type": "mrkdwn",
                        "text": add_userPolicy
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*발생시간*\n" + nowDate
                    }
                ]
            }]
        }],
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ACCOUNT + ' 에서 ' + eventName + ' 이벤트가 발생되었습니다.'
            }
        }
        ]
    }
    print(slack_message)
    # slack 으로 요청보내기
    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    response = urlopen(req)
    response.read()
else:
    print("eventName != TagUser 끝")