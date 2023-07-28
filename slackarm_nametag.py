import boto3
def get_instance_name(session,instance_id):
    """
    인스턴스 ID를 사용하여 인스턴스의 이름 태그를 반환하는 함수
    """
    ec2 = session.resource('ec2')
    instance = ec2.Instance(instance_id)
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'Name tag not found'

## 사용 예시
## boto3 세션 접속필요
session = boto3.session.Session(aws_access_key_id="액세스키", aws_secret_access_key="시크릿키",  region_name="리전")

## 인스턴스 id 기입
ec2_id = "인스턴스 ID"

## 함수 호출
## 인스턴스 id 비교 후 인스턴스 nametag 변환 
ec2_name = get_instance_name(session,ec2_id)