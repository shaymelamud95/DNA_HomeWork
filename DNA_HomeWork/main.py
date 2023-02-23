### 1. מידי שעה מוזרמים בבת אחת תוך עד 5 דקות 6,000 קבצי לוג שיכולים להיות ב 3 מבנים
### שונים, אך אותו מידע בכולם.
### א. csv
### ב. json
### ג. Xml
### 
### לכל הלוגים יש סיומת זהה log.
### עליך לזהות את המבנה על ידי ניתוח הקובץ באופן המהיר והיעיל ביותר שניתן.
### רמזים: לא לקרוא קובץ אחר קובץ. לא לקרוא את כל הקובץ.
### 
### 2. בנפרד: לכל אלו שאינם במבנה json להפוך את כאותם ל json ולשמור אותם עם אותו שם
### בסיומת json. את האחרים שהם כן json יש לשמור כמו שהם רק עם סיומת json.
### 
### 3. יש להסיר &#39;רשומות&#39; כפולות מכל קובץ אם מופיעים יותר מפעם אחת באותו קובץ.
### 
### 4. שאלת בונוס: יש להסיר כפילות אם רשומה מופיעה ביותר מקובץ אחד.

#1.אני אזהה את המבנה של הקובץ ע"י קריאת התו הראשון בכל קובץ:
# קבצי גייסון מתחילים עם {
# קבצי אקסמל מתחילים עם >
# קבצי סיאסווי מתחילים בטקסט
import os, json, xmltodict
import pandas as pd


def readFirstChar(filename):
    with open(filename) as f:
        c = f.read(1)
        # if c:
        #     print("Read a character:", c)
    return c

def firsEx(c):
        if c.isalpha():
            return("csv")
        match c:
            case '<':
                return("xml")
            case '{' | '[':
                return("json")   

#check:             
for filename in os.listdir("files"):
        relativePath = os.path.join(os.getcwd(), f"files\{filename}")
        c = readFirstChar(relativePath)
        if c:
            print(f"file type is : {firsEx(c)}")

# pip install xmltodict ----> is required
# pip install pandas    ----> is required
def secondEx():
    for filename in os.listdir("files"):
        relativePath = os.path.join(os.getcwd(), f"files\{filename}")
        c = readFirstChar(relativePath)
        fileNameNoExt = os.path.splitext(filename)[0]
        fileType = firsEx(c)
        match fileType:
            case "xml":
                xmlToJson(relativePath,fileNameNoExt)
            case "csv":
                csvToJson(relativePath,fileNameNoExt)
            # case "json":
            #     saveJson(relativePath,fileNameNoExt)

def saveJson(relativePath,fileNameNoExt):
    with open(relativePath, "r") as f:
            data = json.loads(f.read())
    with open(f"newFiles\{fileNameNoExt}.json", "w") as json_file:
        json_file.write(data)

def csvToJson(relativePath,fileNameNoExt):            
    csv_file = pd.DataFrame(pd.read_csv(relativePath, sep = ";", header = 0))
    # print(csv_file) # to see how the table look
    # I chose orient = "index" there are several allowed values: {‘split’, ‘records’, ‘index’, ‘table’}
    csv_file.to_json(f"newFiles\{fileNameNoExt}.json", orient = "index", date_format = "epoch", 
                     double_precision= 10, force_ascii = True, date_unit = "ms", default_handler = None)


def xmlToJson(relativePath,fileNameNoExt):
    with open(relativePath) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)
    with open(f"newFiles\{fileNameNoExt}.json", "w") as json_file:
        json_file.write(json_data)       

#check:             
# secondEx()

def thirdEx(relativePath):
    with open(relativePath, "r") as f:
        data = json.loads(f.read())
    # היה אפשר להשתמש בסט אולי זה היה יותר קריא אבל גם המפתחות של המילון הם סט
    unique = { each['name'] : each for each in data }.values()
    print(unique)
    json_data = json.dumps(unique)
    with open(relativePath, "w") as json_file:
        json_file.write(json_data)

#check: 
# relativePathCheck = os.path.join(os.getcwd(), f"files\JSON.log")
# thirdEx(relativePathCheck)

#bonus
def forthEx():
    seen = set()
    for filename in os.listdir("newFiles"):
        relativePath = os.path.join(os.getcwd(), f"newFiles\{filename}")
        with open(relativePath, "r") as f:
            data = json.loads(f.read())
        for x in data:
            if x in seen:
                data.remove(x)
            else:
                seen.add(x)
        with open(relativePath, "w") as json_file:
            json_file.write(data)


# check
# forthEx()