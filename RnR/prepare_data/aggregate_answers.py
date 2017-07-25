import pandas
import math

WORKING_FOLDER='/home/ivp/dev/work/watson-SO/data/v2/'
INPUT_FILE=WORKING_FOLDER + 'answers.csv'
OUTPUT_FILE=WORKING_FOLDER + 'ground_truth.csv'

# read input
answers = pandas.read_csv(INPUT_FILE)

# compute relevance of answer
answers["Relevance"] = answers["Score"].map(lambda x: -1 if x < 0 else x).map(lambda x: x + 1)
answers["RelevanceRef"] = answers["PostId"].map(str) + '|' + answers["Relevance"].map(str)

# aggregate answers references
RelevanceRefs_string = answers.groupby('ParentId')['RelevanceRef'].apply(lambda x: '|'.join(x))
RelevanceRefs_list = RelevanceRefs_string.map(lambda x: x.split('|'))

# unfold answers references to columns
number_of_answers_per_question = RelevanceRefs_list.map(lambda x: len(x))
number_of_additional_columns = number_of_answers_per_question.max()
additional_columns_names = ['c' + str(i) for i in range(number_of_additional_columns)]
ground_truth = pandas.DataFrame({'QuestionId': RelevanceRefs_list.index, 'RelevanceRefs': RelevanceRefs_list.values})
ground_truth[additional_columns_names] = pandas.DataFrame([x for x in ground_truth.RelevanceRefs])
ground_truth = ground_truth.drop('RelevanceRefs', axis=1)

# write results
ground_truth.to_csv(OUTPUT_FILE)