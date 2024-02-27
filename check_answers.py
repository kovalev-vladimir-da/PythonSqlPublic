import pandas as pd


def create_engine(
        answer: str
) -> None:
  correct_answer: str = "postgresql+psycopg2://candidate:simplepass@localhost:5432/db"
  if answer == correct_answer:
    print('Test passed, answer is correct')
  else:
    print(f'Test NOT passed, correct answer is {correct_answer}')


def check_answer_one(
        *,
        answer_df: pd.DataFrame
) -> None:
  correct_sum_ovrd: float = 33247727.0
  correct_num_rows: int = 213430
  answer_df.columns = [x.lower() for x in answer_df.columns]
  if answer_df.loc[:, 'ovrdduration'].sum() == correct_sum_ovrd:
    print('Test_1 passed, answer is correct')
  else:
    print(
      f'Test_1 NOT passed, answer is wrong, correct sum of overdduration is {correct_sum_ovrd}, diff is '
      f'{answer_df.loc[:, "ovrdduration"].sum() - correct_sum_ovrd}'
    )
  if len(answer_df['client_id']) == correct_num_rows:
    print('Test_2 passed, answer is correct')
  else:
    print(
      f'Test_2 NOT passed, answer is wrong, correct number of rows is {correct_num_rows}, '
      f'diff is {len(answer_df["client_id"]) - correct_num_rows}'
    )


def check_answer_two(
        *,
        answer_df: pd.DataFrame
) -> None:
  correct_sum_ovrd: float = 537.0
  correct_num_rows: int = 2
  answer_df.columns = [x.lower() for x in answer_df.columns]

  if answer_df['max_ovrd'].sum() == correct_sum_ovrd:
    print('Test_1 passed, answer is correct')
  else:
    print(
      f'Test_1 NOT passed, answer is wrong, correct sum of overdduration is {correct_sum_ovrd}, '
      f'diff is {answer_df["max_ovrd"].sum() - correct_sum_ovrd}'
    )
  if len(answer_df.index) == correct_num_rows:
    print('Test_2 passed, answer is correct')
  else:
    print(
      f'Test_2 NOT passed, answer is wrong, correct number of rows is {correct_num_rows}, '
      f'diff is {len(answer_df.index) - correct_num_rows}'
    )


def check_answer_three(
        *,
        answer_df: pd.DataFrame
) -> None:
  correct_first_value: int = 35
  correct_last_value: int = 39995
  correct_row_num: int = 1111

  if answer_df.iloc[0, 0] == correct_first_value:
    print('Test_1 passed, answer is correct')
  else:
    print(
      f'Test_1 NOT passed, answer is wrong, correct first value is {correct_first_value}, '
      f'diff is {answer_df.iloc[0, 0] - correct_first_value}'
    )
  if answer_df.iloc[-1, 0] == correct_last_value:
    print('Test_2 passed, answer is correct')
  else:
    print(
      f'Test_2 NOT passed, answer is wrong, correct last value is {correct_last_value}, '
      f'diff is {answer_df.iloc[-1, 0] - correct_last_value}'
    )
  if len(answer_df) == correct_row_num:
    print('Test_3 passed, answer is correct')
  else:
    print(
      f'Test_3 NOT passed, answer is wrong, correct row numbers is {correct_row_num}, '
      f'diff is {len(answer_df) - correct_row_num}'
    )
