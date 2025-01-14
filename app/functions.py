from app.utils import db_connection
import sqlalchemy

db_connection = db_connection.Dbconnection()


class Registration:
    def __init__(self):
        pass

    def insert_employee(self, dicobj):
        pool = db_connection.connect_tcp_socket()
        # connect to connection pool
        with pool.connect() as db_conn:

            # insert data into our ratings table
            insert_stmt = sqlalchemy.text(
                "INSERT INTO employee.emp_tbl (emp_id, emp_name, emp_designation) VALUES (:emp_id, :emp_name, :emp_designation)",
            )

            # insert entries into table
            db_conn.execute(
                insert_stmt,
                parameters={
                    "emp_id": {dicobj.get("emp_id")},
                    "emp_name": {dicobj.get("emp_name")},
                    "emp_designation": {dicobj.get("emp_designation")},
                },
            )

            # commit transactions
            db_conn.commit()

            # query and fetch ratings table
            results = db_conn.execute(
                sqlalchemy.text("SELECT * FROM employee.emp_tbl")
            ).fetchall()

            # show results
            for row in results:
                print(row)

        return "row inserted"
