# DB: MariaDB
#   - type: 관계형 데이터베이스(RDB)

# parkjh7764.tistory.com/123
# root password 1234 , modify, use UTF8 두개만 체크 enable은 체크 굳이 X
# service Name : chosun 으로 설정 나머지 그대로 install as service, enable networking 체크


# **root 계정
#   - 신급 권한을 가지는 계정
#   - RDB는 반드시 root 계정 생성
#   - "DB 관리자" -> root 사용 X, NEW 계정(권한 많이 부여)

# 예) 문서확인 불가(제 등급으로는 확인이 안됩니다.)
# 신입사원 -> 회원가입 개발 -> DB계정 생성(권한: 회원테이블 읽기, 쓰기)


# python - pymysql ----------------------- Database

import pymysql


def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            db="simple",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.Error as e:
        print(f"MARIADB 연결 실패 {e}")