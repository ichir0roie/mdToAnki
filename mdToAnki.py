import glob

pathImport = "importMd\\"
pathExport = "exportTxt\\"

files = glob.glob(pathImport+"*.md")

for filePath in files:
    print(filePath)

    with open(filePath, mode="r", encoding="utf-8")as f:
        text = f.read()

    items = text.split("# ")[1:]

    exportPath = filePath.replace(pathImport, pathExport)
    exportPath = exportPath.replace("md", "txt")

    with open(exportPath, mode="w", encoding="utf-8")as f:

        for item in items:
            item = item.replace("\n\n", "\n")
            front = item.split("\n")[0]  # type:str
            backLines = item.split("\n")[1:]

            text = front+"\t"

            if len(backLines) > 0:
                text += backLines[0]
            for back in backLines[1:]:
                if len(back) <= 0:
                    continue
                text += "<br><br>"+back

            f.write(text+"\n")
