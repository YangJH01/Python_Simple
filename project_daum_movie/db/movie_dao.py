from db.common.connection import connection
# 우리는 main.py에서 실행하기에 main.py 기준으로 찾아가야해서 db를 붙이는것임.
# db없으면 여기서는 되도 main.py에서 실행할때 오류뜸.


# 리뷰 저장
def add_review(data):
    # 1.Connection
    conn = connection()

    try:
        # 2.일꾼 생성
        curs = conn.cursor()
        # 3.JOB 생성(SQL) -> INSERT, DELETE, UPDATE, SELECT
        sql = """
                INSERT INTO tbl_review(title, review, score, writer, reg_date)
                VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s)
              """
        # 4.작업 시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        # 5.자원 해제
        conn.close()