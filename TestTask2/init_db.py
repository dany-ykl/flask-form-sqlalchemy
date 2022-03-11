import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="test_task2",
        user="postgres",
        password=os.getenv('PSQL_PW')
        )

cur = conn.cursor()

cur.execute("insert into auth_type (guid, enumname, enumorder) values (uuid_in(md5(random()::text || clock_timestamp()::text)::cstring),'NoAuth',1);\
insert into auth_type (guid, enumname, enumorder) values (uuid_in(md5(random()::text || clock_timestamp()::text)::cstring),'ApiKey',2);\
insert into auth_type (guid, enumname, enumorder) values (uuid_in(md5(random()::text || clock_timestamp()::text)::cstring),'BearerToken',3);\
insert into auth_type (guid, enumname, enumorder) values (uuid_in(md5(random()::text || clock_timestamp()::text)::cstring),'BasicAuth',4);\
")

conn.commit()
cur.close()
conn.close()