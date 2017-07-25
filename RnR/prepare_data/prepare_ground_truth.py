import pandas
import math

WORKING_FOLDER = '/home/ivp/dev/work/watson-SO/data/v2/'
ANSWERS_FILE = WORKING_FOLDER + 'answers.csv'
QUESTIONS_FILE = WORKING_FOLDER + 'questions.csv'
OUTPUT_FILE = WORKING_FOLDER + 'ground_truth.csv'

# read input
answers = pandas.read_csv(ANSWERS_FILE)

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

with_unfolded_refs = pandas.DataFrame({'QuestionId': RelevanceRefs_list.index, 'RelevanceRefs': RelevanceRefs_list.values})
with_unfolded_refs[additional_columns_names] = pandas.DataFrame([x for x in with_unfolded_refs.RelevanceRefs])
with_unfolded_refs = with_unfolded_refs.drop('RelevanceRefs', axis=1)

# add questions text
questions = pandas.read_csv(QUESTIONS_FILE)

ground_truth = pandas	\
			.merge(questions, with_unfolded_refs, right_on = 'QuestionId', left_on = 'PostId', how = 'right') \
			.drop(['Title', 'AcceptedAnswerId', 'CreationDate', 'QuestionId', 'PostId'], axis=1) \
			.rename(columns={'Body': 'Text'})

# write results
ground_truth.to_csv(OUTPUT_FILE, index=False)