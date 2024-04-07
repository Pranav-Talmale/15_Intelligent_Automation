# # Import python packages
# import streamlit as st

# # ======= BEGIN VANNA SETUP =======

# from vanna.remote import VannaDefault
# from vanna.ollama import Ollama
# from vanna.vannadb.vannadb_vector import VannaDB_VectorStore

# class MyVanna(VannaDB_VectorStore, Ollama):
#     def __init__(self, config=None):
#         MY_VANNA_MODEL = "chinnok"
#         VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key="b74e1cedb9064cc0ba33b7d4fb2e47c9", config=config)
#         Ollama.__init__(self, config=config)

# vn = MyVanna(config={'model': 'mistral'})

# #Connect to DB
# vn.connect_to_mysql(
#     host="localhost",
#     dbname="emp_database",
#     user="root",
#     password="12345",
#     port=3306
# )

# # ======= END VANNA SETUP =======

# my_question = st.session_state.get("my_question", default=None)

# if my_question is None:
#     my_question = st.text_input(
#         "Ask me a question about your data",
#         key="my_question",
#     )
# else:
#     st.text(my_question)
    
#     sql = vn.generate_sql(my_question)

#     st.text(sql)

#     df = vn.run_sql(sql)    
        
#     st.dataframe(sql, use_container_width=True)

#     #code = vn.generate_plotly_code(question=my_question, sql=sql, df=df)

#     #fig = vn.get_plotly_figure(plotly_code=code, df=df)

#     summary = vn.allow_llm_to_see_data(question=my_question, df=df)

#     st.plotly_chart(fig, use_container_width=True)


# # Import python packages
# import streamlit as st
# import pymysql

# # ======= BEGIN VANNA SETUP =======

# from vanna.remote import VannaDefault
# from vanna.ollama import Ollama
# from vanna.vannadb.vannadb_vector import VannaDB_VectorStore

# class MyVanna(VannaDB_VectorStore, Ollama):
#     def __init__(self, config=None):
#         MY_VANNA_MODEL = "chinnok"
#         VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key="b74e1cedb9064cc0ba33b7d4fb2e47c9", config=config)
#         Ollama.__init__(self, config=config)

# vn = MyVanna(config={'model': 'mistral'})

# # Connect to DB
# db_params = {
#     'host': "localhost",
#     'user': "root",
#     'password': "12345",
#     'database': "emp_database",
#     'charset': 'utf8mb4',
#     'cursorclass': pymysql.cursors.DictCursor  # Return results as dictionaries
# }

# # ======= END VANNA SETUP =======

# # Function to execute SQL queries
# def execute_query(sql):
#     try:
#         # Initialize connection within try block to ensure it's defined for the finally block
#         connection = pymysql.connect(**db_params)
#         with connection.cursor() as cursor:
#             cursor.execute(sql)
#             if sql.strip().upper().startswith('SELECT'):
#                 result = cursor.fetchall()
#                 return {'success': True, 'data': result}
#             else:
#                 connection.commit()
#                 return {'success': True, 'rows_affected': cursor.rowcount}
#     except pymysql.MySQLError as e:
#         return {'success': False, 'error': str(e)}
#     finally:
#         if connection:
#             connection.close()

# # Function to clean and extract the SQL query
# def clean_sql_query(sql):
#     # Find the position of the first semicolon and substring to that position
#     semicolon_index = sql.find(';')
#     if semicolon_index != -1:
#         return sql[:semicolon_index + 1]  # Include the semicolon
#     return sql  # Return the original string if no semicolon found

# # Streamlit app logic
# my_question = st.session_state.get("my_question", default=None)

# if my_question is None:
#     my_question = st.text_input("Ask me a question about your data", key="my_question")
# else:
#     st.text(my_question)
    
#     # Generate SQL and clean it
#     sql = vn.generate_sql(my_question)
#     clean_sql = clean_sql_query(sql)
#     st.text(clean_sql)

#     # Execute SQL query and handle the response
#     response = execute_query(clean_sql)
#     if response['success']:
#         if 'data' in response:
#             df = response['data']
#             st.dataframe(df, use_container_width=True)
#         elif 'rows_affected' in response:
#             st.write(f"Rows affected: {response['rows_affected']}")
#     else:
#         st.error(f"Error executing query: {response['error']}")
        
#     # Assuming the rest of your code uses 'df' when 'data' is present in the response
#     # if 'data' in response:
#     #     summary = vn.allow_llm_to_see_data(question=my_question, df=response['data'])
#     #     # Code to display summary, plots, etc., should go here
#     #     # Ensure you handle cases where 'df' might not be defined

# Import python packages
import streamlit as st
import pymysql

# ======= BEGIN VANNA SETUP =======

from vanna.remote import VannaDefault
from vanna.ollama import Ollama
from vanna.vannadb.vannadb_vector import VannaDB_VectorStore

class MyVanna(VannaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        MY_VANNA_MODEL = "chinnok"
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key="b74e1cedb9064cc0ba33b7d4fb2e47c9", config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={'model': 'mistral'})

# Connect to DB
db_params = {
    'host': "localhost",
    'user': "root",
    'password': "12345",
    'database': "emp_database",
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# ======= END VANNA SETUP =======

# Function to execute SQL queries
def execute_query(sql):
    try:
        connection = pymysql.connect(**db_params)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            if sql.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return {'success': True, 'data': result}
            else:
                connection.commit()
                return {'success': True, 'rows_affected': cursor.rowcount}
    except pymysql.MySQLError as e:
        return {'success': False, 'error': str(e)}
    finally:
        if connection:
            connection.close()

# Function to clean and extract the SQL query
def clean_sql_query(sql):
    semicolon_index = sql.find(';')
    if semicolon_index != -1:
        return sql[:semicolon_index + 1]
    return sql

# App title and description
st.title("Employee Management Chatbot")
st.markdown("This application allows you to ask questions about your organisation and view the results directly.")

# Streamlit app layout and logic
with st.sidebar:
    st.header("Query Settings")
    st.markdown("### Instructions")
    st.markdown("Enter a question about your data in the input below. The system will generate and execute the corresponding SQL query.")

my_question = st.text_input("Enter your question:", key="my_question", help="Type your data-related question here.")

if my_question:
    st.subheader("Generated SQL Query")
    sql = vn.generate_sql(my_question)
    clean_sql = clean_sql_query(sql)
    st.code(clean_sql, language='sql')
    
    with st.expander("See execution details"):
        response = execute_query(clean_sql)
        if response['success']:
            if 'data' in response:
                st.subheader("Query Results")
                st.dataframe(response['data'])
                st.success(f"Rows returned: {len(response['data'])}")
            elif 'rows_affected' in response:
                st.success(f"Rows affected: {response['rows_affected']}")
        else:
            st.error(f"Error executing query: {response['error']}")

