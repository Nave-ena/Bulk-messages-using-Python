import pywhatkit
import pandas as pd

data = pd.read_csv("phones-template.csv", dtype="string")
# numbers = data['Number'].to_list()

for i, row in data.iterrows():
    message = open("messages/thank_you.txt").read()
    message = message.replace("{name}", row['Name'])
    print(row['Name'], str(row['Number']))
    pywhatkit.sendwhatmsg_instantly(
        phone_no=str(row["Number"]), 
        message=message,
    )