import pandas as pd
import datetime
import smtplib

gmail_id='birariakshay0@gmail.com'
gmail_psd='AkshAy1701@'

def sendEmail(to,sub,msg):
    print(f"Email is sent to {to} with subject {sub} and message {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(gmail_id,gmail_psd)
    s.sendmail(gmail_id,to,"hii")
    s.quit()


if __name__ == '__main__':
    # sendEmail(gmail_id,"hhii","working bro")
    # exit()
    df=pd.read_excel("Birthday_data.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    Current_year=datetime.datetime.now().strftime("%Y")
    # print(Current_year)
    year_List=[]
    for index,item in df.iterrows():
        # print(index,item["Birthday"])
        bday=item["Birthday"].strftime("%d-%m")
        # print(bday)
        if today==bday and Current_year not in str(item["year"]):
            sendEmail(to=item["email"],sub="Happy Birthday bhai",msg=item["Dialouge"])
            year_List.append(index)
    # print(year_List)
    for i in year_List:
        yr=df.loc[i,'year']
        # print(yr)
        df.loc[i,'year']=str(yr) + "," + str(Current_year)
        # print(df.loc[i, 'year'])
        print(df)
        df.to_excel("Birthday_data.xlsx",index=False)