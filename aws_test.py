import boto3
from openpyxl import Workbook
from datetime import datetime


def test():
    data_list = []

    # profile name 지정
    session = boto3.Session()
    client = session.client('ec2')
    paginator = client.get_paginator('describe_instances')
    response_iterator = paginator.paginate()

    # page별 반복
    for page in response_iterator:
    # page 내의 Reservations 내의 Instances 반복하며 인스턴스 정보 출력
        for j in page['Reservations']:
            for i in j['Instances']:

                NameTag = ''
                # 인스턴스 정보 안에 Tags 정보가 있는 경우만
                if 'Tags' in i:
                    # Tags 정보 중 Name Key를 찾아 Value값 반환해서 저장
                    for tag in i['Tags']:
                        if tag['Key'] == 'Name':
                            NameTag = tag['Value']

                data_tuple = (
                    # instance id
                    i['InstanceId'],
                    # instance platform (ex, linux/unix)
                    i['PlatformDetails'],
                    # instance type (ex, t3.medium)
                    i['InstanceType'],
                    # 생성 시간 > time형식 변경 필요
                    i['LaunchTime'].strftime('%Y-%m-%d'),
                    # Name Tag 값
                    NameTag,
                    # 현재 State (ex, running)
                    i['State']['Name']
                )
                data_list.append(data_tuple)

    print(data_list)


def main():
    test()


if __name__ == '__main__':
    main()
