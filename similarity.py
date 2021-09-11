import pandas as pd
from itertools import combinations
from collections import Counter


def read_file(file, cols):
    return pd.read_csv(file, usecols=cols)


def remove_dislikes(df, col):
    return df[df[col].values]


def merge_dfs(df_1, df_2):
    return pd.merge(left=df_1, right=df_2)


def get_groupings(df, col_1, col_2):
    return df.groupby(col_1).apply(lambda x: x[col_2].unique())


def get_values_list(df):
    return [x for x in df.values]


def get_score(list):
    count = Counter()
    for sublist in list:
        count.update(combinations(sublist, 2))
    return count.most_common()[0]


reactions = read_file('data/reactions.csv', [
    'user_id', 'job_id', 'direction', 'time'
])

jobs = read_file('data/jobs.csv', [
    'job_id', 'company_id'
])

merged = merge_dfs(jobs, remove_dislikes(reactions, 'direction'))
grouped_jobs = get_groupings(merged, 'job_id', 'user_id')
grouped_companies = get_groupings(merged, 'user_id', 'company_id')
user_score = get_score(get_values_list(grouped_jobs))
company_score = get_score(get_values_list(grouped_companies))

print('User score: ', user_score)
print('Company score: ', company_score)
