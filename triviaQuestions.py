import urllib.request
import json
import ssl
import random

categories = {
"mythology": 20,
"general knowledge": 9,
"entertainment": 10,
}
for catagory in categories:
    print(catagory)
cat_answer = input('Which catagory would you like?')
trivia_url = f"https://opentdb.com/api.php?amount=10&category={categories[cat_answer]}&difficulty=medium&type=multiple"

ssl._create_default_https_context = ssl._create_unverified_context

def get_trivia_questions():
    response = urllib.request.urlopen(trivia_url)

    #convert from Json to Python
    json_data = response.read()
    python_data = json.loads(json_data)

    return python_data
trivia_questions = get_trivia_questions()

results = trivia_questions["results"]
score = 0
for result in results:
    print()
    print(result["question"])
    print()
    result["incorrect_answers"].append(result["correct_answer"])
    all_answers = result["incorrect_answers"]
    random.shuffle(all_answers)
    print(all_answers)
    print()
    us_answer = input('What do you think is the correct answer?')
    if us_answer == result["correct_answer"]:
        print('Correct! Great Job!')
    else:
        print("That was incorrect. Sorry, maybe you'll do better on the next one.")
    print()
