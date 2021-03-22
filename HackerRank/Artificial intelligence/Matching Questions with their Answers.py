'''ref:https://www.hackerrank.com/challenges/matching-questions-answers/problem'''
import string
import regex as re
import sys

def similarity(s1,s2):
    s1_tokens= set(s1.split(' '))
    s2_tokens= set(s2.split(' '))
    score= float(len(s1_tokens.intersection(s2_tokens)))/ len(s2_tokens)
    return score

if __name__=='__main__':
    f= open('text','r')
    content=f.readlines()
    questions=[]
    stop_words = [ u'which', u'who', u'how', u'what', u'i', u'me', u'my', u'myself', u'we', u'our',
                  u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his',
                  u'himself', u'she',  u'her', u'hers', 'of', u'herself', u'it', u'its', u'itself',
                  u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this',
                  u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have',
                  u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but',
                  u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about',
                  u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below',
                  u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further',
                  u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both',
                  u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own',
                  u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should',
                  u'now']
    stop_words.extend([u'zebra',u'zebras'])
    for i in range(len(content)):
        if i==0:
            sentences=[x.replace("\n","").lower() for x in content[i].split(".")]
        elif i>0 and i <len(content)-1:
            questions.append(content[i].replace('\n',''))
        elif i ==len(content)-1:
            answerset=(content[i].replace('\n','')).split(";")
    #preprocessing
    # print(sentences)
    processed_sentence=[]
    for sentence in sentences:
        processed_sentence.append(" ".join([re.sub("[^a-zA-Z]","",x).lower()for x in sentence.split(" ") if not x.lower() in stop_words]))

    # print(processed_sentence)
    processed_questions = []
    for question in questions:
        processed_questions.append(" ".join([re.sub("[^a-zA-Z]","",x).lower() for x in question.split(" ") if not x.lower() in stop_words]))
    # print(processed_questions)
    processed_answerset=[]
    for answer in answerset:
        processed_answerset.append(" ".join([re.sub("[^a-zA-Z]","",x).lower() for x in answer.split(" ") if not x.lower() in stop_words]))
    # print(processed_answerset)

    match_case={}
    for i in range(len(processed_questions)):
        max_score=0
        for j in range(len(processed_answerset)):
            for sentence in processed_sentence:
                score= similarity(sentence,processed_answerset[j])* similarity(sentence,processed_questions[i])
                if score>max_score:
                    max_score=score
                    match_case[i]=j

    for i in range(len(processed_questions)):

        print(answerset[match_case[i]])






    # print(sentences)




