import tempfile
from smb.SMBConnection import SMBConnection
import platform
import pandas as pd


user = '계정명'
pssward = '비밀번호'
sharName = 'devops'
ip = 'ip번호'
path = '/폴더'
extension = 'xlsx'

def make_datapath_list(conn, sharName, path, extension):
    """
    서버의 폴더 하위의 모든 파일중 extension을 포함하는 해당하는 리스트를 만든다
    extension: 이름의 일부분이나 확장자를 주면됨
    """
    path_list = []

    dir = conn.listPath(sharName, path)

    for e in dir:
        if e.isDirectory and e.filename not in ['.', '..']:
            filepath = path + '/' +e.filename
            path_list.extend(make_datapath_list(conn, sharName, filepath, extension))
        elif extension in e.filename:
            path_list.append(path + '/' +e.filename)
    return path_list

if __name__ == '__main__':
    #SMB 연결
    conn = SMBConnection(user, pssward, platform.uname().node, sharName, domain='WORKGROUP', use_ntlm_v2=True)
    conn.connect(ip, port=139)

    #파일 목록 구하기

    path_list = make_datapath_list(conn, sharName, path, extension)

    for i in path_list:
       print(i)

    conn.close()