import requests
from bs4 import BeautifulSoup

def get_qa_pair(qlink, topic):
    ### extract the question and answer pair from the question page
    page_q = requests.get("https://www.quora.com"+qlink)
    soup_q = BeautifulSoup(page_q.content, 'html.parser')
    
    question = ""
    answer = ""
    i = 0
    for block in soup_q.find_all('div', class_='answer'):
        for qtext in block.find_all('span', class_='rendered_qtext'):
            ''' 0 is the question itself, 1 is empty, 2 is the topmost answer '''
            text = qtext.get_text()
            if i==0:
                question = text
            elif i==2:
                answer = text
                continue
            # all answers
            #if not text.endswith('?') and i is not 1:
            #   faa.write(text+"\n\n")
            i = i + 1
    # TODO clean question and answer from commas because they mess csv output
    # TODO remove duplicates
    f1a.write(question+','+answer+','+topic+'\n')
#faa.write(question+"\n"+topic+"\n")



f1a = open("q-1a.csv", "w")

topics = ['Economics', 'Psychology', 'Marriage']
topic = topics[2]

page_t = requests.get("https://www.quora.com/topic/"+topic)
soup_t = BeautifulSoup(page_t.content, 'html.parser')

i = 0
for link in soup_t.find_all('a', class_="question_link"):
    qlink = link.get('href')
    if not qlink.startswith('/unanswered'):
        print(str(i)+" "+qlink)
        get_qa_pair(qlink, topic)
    i = i + 1

f1a.close()

#faa = open("q-all-a.txt", "w")
#faa.close()

