
#%%
from sklearn.feature_extraction.text import TfidfTransformer
import os
import pickle
import pandas as pd
import numpy as np
path_training_data = os.getcwd()+'/training_data.tsv'
path_test_data = os.getcwd()+'/eval_data.txt'


#%%
import regex_generator

regex_generator.main_regex_generator(path_training_data)
####### regex extraction ######
import regex_matcher

print('inside_extration')
extractions_from_regex = regex_matcher.main_regex_matcher(path_test_data)
print('extracted')


#%%

import training_classifier
training_classifier.main_ML_model()

f = open('svm_classifier.pickle', 'rb')
clf = pickle.load(f)
f.close()

f = open('mlp_classifier.pickle', 'rb')
mlp = pickle.load(f)
f.close()


f = open('my_vectorizer.pickle', 'rb')
vectorizer = pickle.load(f)
f.close()


#%%

###### loading data ######
data=[]
master_data = open(path_test_data, 'r')
for sent in master_data:
    data.append(' '.join(sent.split()))#using ' '.join(sent.split()) to remove the \n from the txt file 
print(data)


#%%
df = pd.DataFrame(data) # loading data to the dataframe
df=df[0]# getting the dimentions right for prediction
#
clean_test_data = []
for i in df:
    clean_test_data.append(i)
# print (clean_train_data)

# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_data)
np.asarray(test_data_features)

tfidf_transformer = TfidfTransformer()
X_test_tfidf = tfidf_transformer.fit_transform(test_data_features)



#%%
###### predicting from the classifier ######

result1 = clf.predict(X_test_tfidf)
result2 = mlp.predict(X_test_tfidf)

###### saving the result in a dataframe ######

output1 = pd.DataFrame(data={"sent": df, "label": result1})
output2 = pd.DataFrame(data={"sent": df, "label": result2})
predicted_result1 = list(result1) # converting the n dimentional array into a list
predicted_result2 = list(result2)
###### output of the classisfier using BOW model ######
output1.to_csv(('Bag_of_Words_model_new_svm.csv'), index=False, quoting=3, escapechar='\\')
output2.to_csv(('Bag_of_Words_model_new_mlp.csv'), index=False, quoting=3, escapechar='\\')
###### final submission ######
final_result1=[]
for idx, prediction in enumerate(predicted_result1):
    if (prediction=='Not Found'):
        final_result1.append('Not Found') # if classifier identifies the sentence to be labled as Not Found it has power to over write the extracter
    else:
        final_result1.append(extractions_from_regex[idx])# if the classifier identifies it to have a phrase then we use the extracted phrase

final_result2=[]
for idx, prediction in enumerate(predicted_result2):
    if (prediction=='Not Found'):
        final_result2.append('Not Found') # if classifier identifies the sentence to be labled as Not Found it has power to over write the extracter
    else:
        final_result2.append(extractions_from_regex[idx])
###### loading the final output into df ######
final_output1 = pd.DataFrame(data={"sent": df, "label": final_result1})
final_output2 = pd.DataFrame(data={"sent": df, "label": final_result2})
###### Final submission ######
final_output1.to_csv(('submission_svm.csv'), index=False, quoting=3, escapechar='\\')
final_output2.to_csv(('submission_mlp.csv'), index=False, quoting=3, escapechar='\\')
print("submission done")


#%%



