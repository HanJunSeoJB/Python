import webbrowser
name = input("챔피언 이름 검색\n")
line = input("챔피언 라인 \n")
url = "https://www.op.gg/champion/" + name + "/statistics/" + line + "/build"
webbrowser.open(url)

