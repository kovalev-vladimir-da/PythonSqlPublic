'''
# SQL Tasks for cadidate

## Notice

### Using stake
- Interpetator used: Python 3.11
- SQL Dialect: SQLite

### General info
- Today is 01.09.2023
- Datasets is representation of two groups of clients with debts, active or closed.

### Data
#### Overdraft
- Dataframe: overdraft_test_data.csv
- Columns: client_id, fromdate, todate, ovrdduration, debt

#### Credit
- Dataframe: credit_test_data.csv
- Columns: client_id, fromdate, todate, ovrdduration, debt

*in description, we will assume data types as it is real SQL Table or View.*
DESCRIPTION IS FOR BOTH DATASETS
- Description:
    - **CLIENT_ID (INTEGER):**
      unique client identification, key to credit_test_data
    - **FROMDATE (INTEGER):**
      date start for client account with overdraft (Using INTEGER due to SQLite restrictions, assume DATE)
    - **PLAN_TODATE (INTEGER):**
      date where client obliged to close the debt (Using INTEGER due to SQLite restrictions, assume DATE)
    - **TODATE (INTEGER):**
      date end for client account with overdraft (Using INTEGER due to SQLite restrictions, assume DATE)
      if still active debt - NaT or more then today date
    - **DEBT (REAL):**
      sum of debt owed by client
    - **CREDIT_TYPE (TEXT):**
      'type_0' for overdraft
      'type_1' for credit
      '''

import pandas as pd
import pandasql as ps
from check_answers import *

overdraft_df = pd.read_csv(
    'assets/overdraft_test_data.csv',
    index_col=0,
    dtype={
        'client_id': 'int',
        'debt': 'float',
        'credit_type': 'str'
    }
)
for col in ['fromdate', 'todate', 'plan_todate']:
    overdraft_df[col] = pd.to_datetime(overdraft_df[col])

credit_df = pd.read_csv(
 'assets/credit_test_data.csv',
 index_col=0,
 dtype={
  'client_id': 'int',
  'debt': 'float',
  'credit_type': 'str'
 }
)
for col in ['fromdate', 'todate', 'plan_todate']:
 credit_df[col] = pd.to_datetime(credit_df[col])

'''
# TASK #0
Assume that we using postgreSQL db for the moment, with sqlalchemy as lib to create engine.
Below is data for connect, your task is to create connection string from it.

NOTICE - you will use engine creation function as it already imported. No need to import again
'''

# GIVEN DATA

DD: str = 'postgresql+psycopg2' # dialect and driver
USERNAME: str = 'candidate'
PASSWORD: str = 'simplepass'
HOST: str = 'localhost'
PORT: str = '5432'
DATABASE: str = 'db'

# # UNCOMMENT AND ENTER YOUR SOLUTION AND RUN TO CHECK THE ANSWER
# create_engine(f'''''')

# # UNCOMMENT AND ENTER YOUR SOLUTION
# answer_df_1: pd.DataFrame = ps.sqldf(
#     '''
#
#     ''', locals()
# )

# UNCOMMENT AND RUN TO CHECK THE RESULTS

# check_answer_one(answer_df=answer_df_1)

# answer_df_2: pd.DataFrame = ps.sqldf(
#     '''
#
#     ''', locals()
# )

# UNCOMMENT AND RUN TO CHECK THE RESULTS

# check_answer_two(answer_df=answer_df_2)

# answer_df_3: pd.DataFrame = ps.sqldf(
#     '''
#
#     ''', locals()
# )

# UNCOMMENT AND RUN TO CHECK THE RESULTS

# check_answer_three(answer_df=answer_df_3)
