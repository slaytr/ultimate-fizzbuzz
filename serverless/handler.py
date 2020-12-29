import json
import requests
import base64
import os


def update_fizzbuzz(event, context):
    token = os.environ['TOKEN']
    filename = "fizzbuzz.py"
    repo = "slaytr/ultimate-fizzbuzz"
    branch = "main"
    url = "https://api.github.com/repos/" + repo + "/contents/" + filename

    # Retrieve FizzBuzz
    data = requests.get(url + '?ref=' + branch, headers={"Authorization": "token " + token}).json()
    code = base64.b64decode(data['content']).decode('utf-8').split("\n")

    # Update FizzBuzz
    code.pop()
    max_num = int(code[-2].split(" ")[-1][:-1])
    increment_by = 10
    for i in range(max_num + 1, max_num + increment_by + 1):
        out_str = ""
        if i % 3 == 0:
            out_str += "Fizz"
        if i % 5 == 0:
            out_str += "Buzz"
        code.append(f"        if i == {i}:")
        if out_str:
            code.append(f"            print('{out_str}')")
        else:
            code.append(f"            print({i})")
    code.append("")

    # Encode content in base64 and prep github commit
    new_code = base64.b64encode("\n".join(code).encode('utf-8')).decode('utf-8')
    message = json.dumps({
        "message": f"Updated FizzBuzz support for {max_num + 1} to {max_num + increment_by}",
        "sha": data['sha'],
        "branch": branch,
        "content": new_code
    })

    # Commit FizzBuzz
    resp = requests.put(
        url,
        data=message,
        headers={
            "Content-Type": "application/json",
            "Authorization": "token " + token
        })
    body = {
        "message": "FizzBuzz Updated!",
        "event": resp.json()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
