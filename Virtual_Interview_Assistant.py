import pandas as pd
from pyscript import document
import random

def onConfirmSkill(event):
  selected_skill = document.querySelector("#uiskill")
  global skill
  skill = selected_skill.value
  output_div = document.querySelector("#output_skill")
  valid_skill = ['Excel', 'Tableau', 'SQL', 'Python', 'HTML', 'POWER-BI']
  if skill in valid_skill:
    output_div.innerText = f'{skill} Skill is confirmed for your Virtual Test.'
  else:
    output_div.innerText = 'Please Select a Skill from the above Drop-Down.'
  event.preventDefault()


def onFetchQuestions(event):
  try:
    global df
    if skill == 'Excel':
      
      df = pd.read_json("./Excel_Interview_Virtual_Assistant.json")
    elif skill == 'Tableau':
      df = pd.read_json("./Tableau_Interview_Virtual_Assistant.json")
    elif skill == 'SQL':
      df = pd.read_json("./SQL_Interview_Virtual_Assistant.json")
    elif skill == 'Python':
      df = pd.read_json("./PYTHON_Interview_Virtual_Assistant.json")
    elif skill == 'HTML':
      df = pd.read_json("./HTML_Interview_Virtual_Assistant.json")
    elif skill == 'POWER-BI':
      df = pd.read_json("./PowerBI_Interview_Virtual_Assistant.json")

    # global df
    # df = pd.read_json("./Excel_Interview_Virtual_Assistant.json")
    output_div_2 = document.querySelector("#output_fetchquestions")
    output_div_2.innerText = f'Total {df.shape[0]} Questions Sucessfully Fetched from the server.'
  except:
    output_div_2 = document.querySelector("#output_fetchquestions")
    output_div_2.innerText = 'Unable to Fetch Data from the server. Please Contact Mohammad Dawood.'
  event.preventDefault()


global v
v = 0

def onClickedNextQuestion(event):
  
  global v
  global v1
  v = random.randint(0, (df.shape[0]-1))
  question = df['Questions'][v]
  output_div3 = document.querySelector("#output_nextquestion")
  output_div3.innerText = question


  event.preventDefault()

def onClickedNextAnswer(event):
  
  answer = df['Answers'][v]
  output_div3 = document.querySelector("#output_nextanswer")
  output_div3.innerText = answer


  event.preventDefault()
