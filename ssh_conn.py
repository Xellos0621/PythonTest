import paramiko


def nascheck(find_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect("ip주소", port=9022, username="계정", password="비밀번호")
    print('ssh connected.')

    message = "없음"

    stdin, stdout, stderr = ssh.exec_command("ls -l")
    lines = stdout.readlines()

    stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")
    lines = stdout.readlines()
    for i in lines:
        re = str(i).replace('\n', '')
        sp = re.split(':')
        if sp[4] == find_name:
            message = 'NAS에 존재함, ' + sp[0]
    print(message)
    ssh.close()


def main():
    find_name = input('찾는 사람의 이름을 입력해 주세요 : ')
    nascheck(find_name)


if __name__ == '__main__':
    main()
