import requests
from bs4 import BeautifulSoup
import re

def get_qa_pair(qlink, topic):
    ### extract the question and answer pair from the question page
    page_q = requests.get("https://www.quora.com"+qlink)
    soup_q = BeautifulSoup(page_q.content, 'html.parser')
    
    question = ""
    answer = ""
    i = 0
    
    qset = set([])
    for qtext in soup_q.find_all('span', class_='rendered_qtext'):
        ''' 0 is the question itself, 1 is empty, 2 is the topmost answer '''
        
        text = re.sub(r'[^\x00-\x7f]',r'', qtext.get_text()) # remove non-ascii characters
        
        if i==0:
            question = text
        elif i==2:
            answer = text
        # all answers
        #if not text.endswith('?') and i is not 1:
        #   faa.write(text+"\n\n")
        i = i + 1
    # cleaning question and answer from commas because they mess csv output
    question = question.replace(",",";")
    answer = answer.replace(",",";")
    
    # do not add duplicates
    if question not in qset:
        f1a.write(question+','+answer+','+topic+'\n')
        qset.add(question)
#faa.write(question+"\n"+topic+"\n")


f1a = open("q-1a.csv", "w")

topics = ['Economics', 'Psychology-of-Everyday-Life', 'Psychology','Interpersonal-Interaction']
#topic = 'Understanding-Human-Behavior-1'
#topic_text = 'Psychology'

topic = 'Molecular-Biology'
topic_text = 'Biology'

page_t = requests.get("https://www.quora.com/topic/"+topic)
soup_t = BeautifulSoup(page_t.content, 'html.parser')

i = 0
for link in soup_t.find_all('a', class_="question_link"):
    qlink = link.get('href')
    print(str(i)+" "+qlink)
    get_qa_pair(qlink, topic_text)
    i = i + 1
f1a.close()


