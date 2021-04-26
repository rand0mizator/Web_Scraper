import requests

url = input()
r = requests.get(url)
status_code = r.status_code

if status_code != 200:
    print(f'The URL returned {status_code}')
else:
    page_content = r.content
    file = open('source.html', 'wb')
    file.write(page_content)
    file.close()
    print("Content saved")
