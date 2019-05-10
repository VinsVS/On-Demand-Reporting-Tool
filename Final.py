import decimal
import time
import win32com.client
import subprocess
import win32com.client as win32
import getpass
import pyodbc 
import csv
name=(getpass.getuser())


print("Goss Reporting : Hi, "+name)
print("")
print("Goss Reporting : Welcome to GOSS Reporting " )
print("")
print("Goss Reporting : Currently we are providing the following reports")
print("")   
print("Goss Reporting : please select the Report Serial No. you want to generate" )
print("")   
print("1. Aceyus SignIN SignOFF Report")
print("2. Moxie Chat Report")
print("3. SR Report-Upload")
print("4. Call Performance Report")
print("5. Monthly Agent Performance Report")
print("6. Service Quality Status-Reminder")
print("7. Global Upload Observation")
print("")
Report = input("Goss Reporting : Please enter the Report No. : ")
print("")
time.sleep(1)
print("You : "+Report )
print("")






if "1" in Report:
   try:
      
       print("Goss Reporting : You have selected Aceyus SignIN SignOFF Report " )
       print("")
       print("Goss Reporting : Your Request has been submitted " )
       x1= win32com.client.Dispatch('Excel.Application') 
       wb = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\\Macro\\Agent sign in off.xlsm")
       x1.Visible = False
       print("")
       print("Goss Reporting : Raw data is exracting from aceyus tool and saving in repository ")
       wb.Application.Run("importattachment")
       wb.Application.Run("Macro1")
       print("")
       print("Goss Reporting : Data is Importing")
       print("")
       wb.Application.Run("Macro2")
       print("Goss Reporting : Import done now data is Formatting")
       print("")
       wb.Application.Run("Macro3")
       print("Goss Reporting : Formatting done")
       print("")
       print("Goss Reporting : Report has been created and saved at location")
       print("")
       print("Goss Reporting : Report is uploading on Sharepoint site")
       print("")
       wb.Application.Run("Upload_Report")
       print("Goss Reporting : Report has been uploaded at sharepoint")
       print("")
       outlook = win32.Dispatch('outlook.application')
       subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
       Msg = outlook.CreateItem(0)
       Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
#       Msg.CC = "Vinay.K.Sharma@mercer.com"
       Msg.Subject = "Daily Aceyus SignIN SignOFF Report - Completed"
       Msg.Body = "mail sent through Self Service Tool"
       Msg.Send()
       response = input("Goss Reporting : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports:")
       print("")
       print("You : "+response)
       time.sleep(1)
       if response == "y":
                         wb.Application.Run("CloseBook")
                         exit()
       else:
            wb.Application.Run("CloseBook")           
            exit()
       
       
   except:
      print("There is some technical issue in report, Reporting team is working on it")
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "vinamra.srivastava@mercer.com"
      Msg.CC = "priyanka.lnu@mercer.com"
      Msg.Subject = "Confirmation Mail-Aceyus SignIN SignOff Report"
      Msg.Body =  """Hi,
The Daily Aceyus SignIN SignOFF Report is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool.""" 
      Msg.send()
      Msg.close()
 
    
    
    
    
    
    
    
    
    
    
elif "2" in Report:
  try:
      print("Goss Reporting : You have selected Moxie Chat Report " )
      print("")
      print("Goss Reporting : Your Request has been submitted " )
      print("")
      x1= win32com.client.Dispatch('Excel.Application') 
      wb = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\MoxieChat.xlsm",ReadOnly=1)
      x1.Visible = False
      print("Goss Reporting : Attactment is searching in Mailbox")
      time.sleep(1)
      print("")
      print("Goss Reporting : Attactment is saving in repository")
      print("")
      wb.Application.Run("importattachment")
      print("Goss Reporting : Report has been saved at specific location")
      print("")
      print("Goss Reporting : Please wait,Report is uploading on Sharepoint")
      print("")
      wb.Application.Run("Upload_Report")
      print("Goss Reporting : Report has been uploaded on Sharepoint")
      print("")
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
#      Msg.CC = "Vinay.K.Sharma@mercer.com"
      Msg.Subject = "Moxie Chat - Daily Summary Report-Done"
      Msg.Body = "mail sent through Self Service Tool"
      Msg.Send()
      response = input("Goss Reporting : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports:")
      print("")
      print("You : "+response)
      time.sleep(1)
      if response == "y":
                         wb.Application.Run("CloseBook")
                         exit()
      else:
           wb.Application.Run("CloseBook")
           exit()    
                            
  except:
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "vinamra.srivastava@mercer.com"
      Msg.CC = "priyanka.lnu@mercer.com"
      Msg.Subject = "Confirmation Mail-Moxie chat report"
      Msg.Body =  """Hi,
The Moxie chat report is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool.""" 
      Msg.Send()
      Msg.close()













elif "3" in Report:
 try:
     print("Goss Reporting : You have selected Daily SR Report- Upload " )
     print("")
     print("Goss Reporting : Your Request has been submitted " )
     print("")
     print("Goss Reporting: Please enetr your Login Credential")
     print("")
     print("Goss Reporting : Example: ID : Frist Name-Last Name")
     print("               Password : LAN Password") 
     id=input("Goss Reporting : ID -> ")
     print("")
     print("You : "+id)
     print("")
     password=input("Goss Reporting : Password -> ")
     print("")
     print("You : "+password)
     x1= win32com.client.Dispatch('Excel.Application') 
     wb = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\upload.xlsm")
     x1.Visible = False
     x1.Range("W2").Select()
     x1.ActiveCell.Value = id
     x1.Range("W3").Select()
     x1.ActiveCell.Value = password
     print("")
     print("Goss Reporting : Please wait, Files are moving to loaction")
     wb.Application.Run("MoveFiles")
     print("")
     print("Goss Reporting : Files have been moved to the location ")
     print("")
     print("Goss Reporting : Files are uploading at connect site, it will take 15 to 20 mins ")
     print("")
     wb.Application.Run("Sheet1.btnUpload_Click")
     print("Goss Reporting : Files are posted Successfully")
     outlook = win32.Dispatch('outlook.application')
     subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
     Msg = outlook.CreateItem(0)
     Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
#    Msg.CC = "Vinay.K.Sharma@mercer.com"
     Msg.Subject = "Confirmation Mail-Daily Sieble SR Report"
     Msg.Body ="""Hi,
The Daily Sieble SR Report is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool."""  
     Msg.Send()
     
     response = input("Bot : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports") 
     print("")
     print("You : "+response)
     time.sleep(1)
     if response == "y":
                        wb.Application.Run("CloseBook")
                        exit() 
     else:
          wb.Application.Run("CloseBook")
          exit()                   
 except:
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "vinamra.srivastava@mercer.com"
      Msg.CC = "priyanka.lnu@mercer.com"
      Msg.Subject = "Issue in SR Report-Upload"
      Msg.Body = "mail sent through Self Service Tool"
      Msg.Send()
      Msg.close()













elif "4" in Report:
  try:
      print("Goss Reporting : You have selected Call Performance" )
      print("")
      print("Goss Reporting : Your Request has been submitted " )
      Date=input("Goss Reporting : Enter the Date for the report in MM/DD/YYYY:")
      MDate=input("Goss Reporting : Enter the Starting Date of current Month MM/DD/YYYY:")
      YDate=input("Goss Reporting : Enter the Starting Date of current Year MM/DD/YYYY:")
      cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.23.84.15\SQL1;"
                      "Database=aceyus_edw;"
                      "Trusted_Connection=yes;")
      print("")
      print("Goss Reporting : Connecting to SQL Server")
      print("")
      print("Goss Reporting : Raw Data(Daily Calls) is fetching from Database")
      SQL="""
SELECT
CV.Loc AS [Site],
CV.Client+' '+CV.LOB AS[Client LOB],
--Used for any day prior to 10/1/2018
--sum(CTD.CallsOffered) as [Offered],
--sum(CTD.CallsHandled) as [Handled],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],
--case when sum(CTD.CallsOffered)>0 then 1.0*sum(CTD.TotalCallsAband)/sum(CTD.CallsOffered) else 0 end as [Abnd %],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.AnswerWaitTime)/sum(CTD.CallsHandled) else 0 end as [ASA],
--case when sum(CTD.ServiceLevelCallsOffered)>0 then 1.0*sum(CTD.ServiceLevelCalls)/sum(CTD.ServiceLevelCallsOffered) else 0 end as [SVL %],

--Used for any day post 10/1/2018
SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End) as [Offered],

SUM(CASE WHEN CV.RoutingCode IN ('D2A','CCB','QUE') Then CTD.CallsAnswered Else 0 End) as [Handled],

case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],

case when SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)=0 then 0 else 
1.0*sum(CTD.TotalCallsAband)/(SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)) 
end as [Abnd %],

case when (SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End))>0 then SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.AnswerWaitTime Else 0 End)/SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End) else 0 end  AS 'ASA',

case when (sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End))=0 then 0 
else 1.0*sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCalls Else 0 End)/(sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End)) 
end as [SVL %],
SUM(CTD.AnsInterval1) AS [Ans 0-15],
SUM(CTD.AnsInterval2) AS [Ans 16-20],
SUM(CTD.AnsInterval3) AS [Ans 21-30],
SUM(CTD.AnsInterval4) AS [Ans 31-45],
SUM(CTD.AnsInterval5) AS [Ans 46-60],
SUM(CTD.AnsInterval6) AS [Ans 61-90],
SUM(CTD.AnsInterval7) AS [Ans 91-180],
SUM(CTD.AnsInterval8) AS [Ans 181-600],
SUM(CTD.AnsInterval9) AS [Ans 601-1200],
SUM(CTD.AnsInterval10) AS [Ans 1201+],
SUM(CTD.AbandInterval1) AS [Abnd 0-15],
SUM(CTD.AbandInterval2) AS [Abnd 16-20],
SUM(CTD.AbandInterval3) AS [Abnd 21-30],
SUM(CTD.AbandInterval4) AS [Abnd 31-45],
SUM(CTD.AbandInterval5) AS [Abnd 46-60],
SUM(CTD.AbandInterval6) AS [Abnd 61-90],
SUM(CTD.AbandInterval7) AS [Abnd 91-180],
SUM(CTD.AbandInterval8) AS [Abnd 181-600],
SUM(CTD.AbandInterval9) AS [Abnd 601-1200],
SUM(CTD.AbandInterval10) AS [Abnd 1201+]

FROM
aceyus_edw.dbo.t_Call_Type_Daily CTD 
inner join aceyus_edw.dbo.cust_REF_CustomVariable CV on CTD.CallTypeID=CV.CustomID

WHERE
CTD.DateTime between '"""+Date+"""' and '"""+Date+"""'


Group by CV.Loc,CV.Client+' '+CV.LOB
order by 1,2
"""
      cursor = cnxn.cursor()
      cursor.execute(SQL)
#columns = ['Site']
      row = cursor.fetchall()
      with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\Call Performance\\2014-CiscoDaily.csv', 'w', newline= '') as f:
          a = csv.writer(f, delimiter=',')
          a.writerow(["Site","Client LOB","Offered","Handled","AHT","Abnd %","ASA","SVL %","Ans 0-15","Ans 16-20","Ans 21-30","Ans 31-45","Ans 46-60","Ans 61-90","Ans 91-180","Ans 181-600","Ans 601-1200","Ans 1201+","Abnd 0-15","Abnd 16-20","Abnd 21-30","Abnd 31-45","Abnd 46-60","Abnd 61-90","Abnd 91-180","Abnd 181-600","Abnd 601-1200","Abnd 1201+"])  
          a.writerows(row)
      cursor.close()
      print("")
      print("Goss Reporting : Raw Data(Monthly Calls) is fetching from Database")
      SQL="""
SELECT
CV.Loc AS [Site],
CV.Client+' '+CV.LOB AS[Client LOB],
--Used for any day prior to 10/1/2018
--sum(CTD.CallsOffered) as [Offered],
--sum(CTD.CallsHandled) as [Handled],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],
--case when sum(CTD.CallsOffered)>0 then 1.0*sum(CTD.TotalCallsAband)/sum(CTD.CallsOffered) else 0 end as [Abnd %],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.AnswerWaitTime)/sum(CTD.CallsHandled) else 0 end as [ASA],
--case when sum(CTD.ServiceLevelCallsOffered)>0 then 1.0*sum(CTD.ServiceLevelCalls)/sum(CTD.ServiceLevelCallsOffered) else 0 end as [SVL %],

--Used for any day post 10/1/2018
SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End) as [Offered],

SUM(CASE WHEN CV.RoutingCode IN ('D2A','CCB','QUE') Then CTD.CallsAnswered Else 0 End) as [Handled],

case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],

case when SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)=0 then 0 else 
1.0*sum(CTD.TotalCallsAband)/(SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)) 
end as [Abnd %],

case when (SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End))>0 then SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.AnswerWaitTime Else 0 End)/SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End) else 0 end  AS 'ASA',

case when (sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End))=0 then 0 
else 1.0*sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCalls Else 0 End)/(sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End)) 
end as [SVL %],
SUM(CTD.AnsInterval1) AS [Ans 0-15],
SUM(CTD.AnsInterval2) AS [Ans 16-20],
SUM(CTD.AnsInterval3) AS [Ans 21-30],
SUM(CTD.AnsInterval4) AS [Ans 31-45],
SUM(CTD.AnsInterval5) AS [Ans 46-60],
SUM(CTD.AnsInterval6) AS [Ans 61-90],
SUM(CTD.AnsInterval7) AS [Ans 91-180],
SUM(CTD.AnsInterval8) AS [Ans 181-600],
SUM(CTD.AnsInterval9) AS [Ans 601-1200],
SUM(CTD.AnsInterval10) AS [Ans 1201+],
SUM(CTD.AbandInterval1) AS [Abnd 0-15],
SUM(CTD.AbandInterval2) AS [Abnd 16-20],
SUM(CTD.AbandInterval3) AS [Abnd 21-30],
SUM(CTD.AbandInterval4) AS [Abnd 31-45],
SUM(CTD.AbandInterval5) AS [Abnd 46-60],
SUM(CTD.AbandInterval6) AS [Abnd 61-90],
SUM(CTD.AbandInterval7) AS [Abnd 91-180],
SUM(CTD.AbandInterval8) AS [Abnd 181-600],
SUM(CTD.AbandInterval9) AS [Abnd 601-1200],
SUM(CTD.AbandInterval10) AS [Abnd 1201+]

FROM
aceyus_edw.dbo.t_Call_Type_Daily CTD 
inner join aceyus_edw.dbo.cust_REF_CustomVariable CV on CTD.CallTypeID=CV.CustomID

WHERE
CTD.DateTime between '"""+MDate+"""' and '"""+Date+"""'


Group by CV.Loc,CV.Client+' '+CV.LOB
order by 1,2
"""
      cursor = cnxn.cursor()
      cursor.execute(SQL)
#columns = ['Site']
      row = cursor.fetchall()
      with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\Call Performance\\2014-CiscoMTD.csv', 'w', newline= '') as f:
          a = csv.writer(f, delimiter=',')
          a.writerow(["Site","Client LOB","Offered","Handled","AHT","Abnd %","ASA","SVL %","Ans 0-15","Ans 16-20","Ans 21-30","Ans 31-45","Ans 46-60","Ans 61-90","Ans 91-180","Ans 181-600","Ans 601-1200","Ans 1201+","Abnd 0-15","Abnd 16-20","Abnd 21-30","Abnd 31-45","Abnd 46-60","Abnd 61-90","Abnd 91-180","Abnd 181-600","Abnd 601-1200","Abnd 1201+"])  
          a.writerows(row)
      cursor.close()
      print("")
      print("Goss Reporting : Raw Data(Yearly Calls) is fetching from Database")
      SQL="""
SELECT
CV.Loc AS [Site],
CV.Client+' '+CV.LOB AS[Client LOB],
--Used for any day prior to 10/1/2018
--sum(CTD.CallsOffered) as [Offered],
--sum(CTD.CallsHandled) as [Handled],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],
--case when sum(CTD.CallsOffered)>0 then 1.0*sum(CTD.TotalCallsAband)/sum(CTD.CallsOffered) else 0 end as [Abnd %],
--case when sum(CTD.CallsHandled)>0 then sum(CTD.AnswerWaitTime)/sum(CTD.CallsHandled) else 0 end as [ASA],
--case when sum(CTD.ServiceLevelCallsOffered)>0 then 1.0*sum(CTD.ServiceLevelCalls)/sum(CTD.ServiceLevelCallsOffered) else 0 end as [SVL %],

--Used for any day post 10/1/2018
SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End) as [Offered],

SUM(CASE WHEN CV.RoutingCode IN ('D2A','CCB','QUE') Then CTD.CallsAnswered Else 0 End) as [Handled],

case when sum(CTD.CallsHandled)>0 then sum(CTD.HandleTime)/sum(CTD.CallsHandled) else 0 end as [AHT],

case when SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)=0 then 0 else 
1.0*sum(CTD.TotalCallsAband)/(SUM(CASE WHEN CV.RoutingCode = 'QUE' Then CTD.TotalCallsAband Else 0 End)+SUM(CASE WHEN CV.RoutingCode IN ('QUE','CCB','D2A') Then CTD.CallsAnswered Else 0 End)) 
end as [Abnd %],

case when (SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End))>0 then SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.AnswerWaitTime Else 0 End)/SUM(CASE WHEN CV.RoutingCode Not In ('D2A') Then CTD.CallsAnswered Else 0 End) else 0 end  AS 'ASA',

case when (sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End))=0 then 0 
else 1.0*sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCalls Else 0 End)/(sum(CASE WHEN CV.RoutingCode IN ('QUE','CCB') Then CTD.ServiceLevelCallsOffered Else 0 End)) 
end as [SVL %],
SUM(CTD.AnsInterval1) AS [Ans 0-15],
SUM(CTD.AnsInterval2) AS [Ans 16-20],
SUM(CTD.AnsInterval3) AS [Ans 21-30],
SUM(CTD.AnsInterval4) AS [Ans 31-45],
SUM(CTD.AnsInterval5) AS [Ans 46-60],
SUM(CTD.AnsInterval6) AS [Ans 61-90],
SUM(CTD.AnsInterval7) AS [Ans 91-180],
SUM(CTD.AnsInterval8) AS [Ans 181-600],
SUM(CTD.AnsInterval9) AS [Ans 601-1200],
SUM(CTD.AnsInterval10) AS [Ans 1201+],
SUM(CTD.AbandInterval1) AS [Abnd 0-15],
SUM(CTD.AbandInterval2) AS [Abnd 16-20],
SUM(CTD.AbandInterval3) AS [Abnd 21-30],
SUM(CTD.AbandInterval4) AS [Abnd 31-45],
SUM(CTD.AbandInterval5) AS [Abnd 46-60],
SUM(CTD.AbandInterval6) AS [Abnd 61-90],
SUM(CTD.AbandInterval7) AS [Abnd 91-180],
SUM(CTD.AbandInterval8) AS [Abnd 181-600],
SUM(CTD.AbandInterval9) AS [Abnd 601-1200],
SUM(CTD.AbandInterval10) AS [Abnd 1201+]

FROM
aceyus_edw.dbo.t_Call_Type_Daily CTD 
inner join aceyus_edw.dbo.cust_REF_CustomVariable CV on CTD.CallTypeID=CV.CustomID

WHERE
CTD.DateTime between '"""+YDate+"""' and '"""+Date+"""'


Group by CV.Loc,CV.Client+' '+CV.LOB
order by 1,2
"""
      cursor = cnxn.cursor()
      cursor.execute(SQL)
#columns = ['Site']
      row = cursor.fetchall()
      with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\Call Performance\\2014-CiscoYTD.csv', 'w', newline= '') as f:
         a = csv.writer(f, delimiter=',')
         a.writerow(["Site","Client LOB","Offered","Handled","AHT","Abnd %","ASA","SVL %","Ans 0-15","Ans 16-20","Ans 21-30","Ans 31-45","Ans 46-60","Ans 61-90","Ans 91-180","Ans 181-600","Ans 601-1200","Ans 1201+","Abnd 0-15","Abnd 16-20","Abnd 21-30","Abnd 31-45","Abnd 46-60","Abnd 61-90","Abnd 91-180","Abnd 181-600","Abnd 601-1200","Abnd 1201+"])  
         a.writerows(row)
      cursor.close()


      print("")
      print("Goss Reporting : Raw Data are saving at loaction")
      x1= win32com.client.Dispatch('Excel.Application') 
      wb = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\Callperfmacro.xlsm")
      x1.Visible = False
      wb.Application.Run("csvToxls")
#wb.Application.Run("CloseBook")
      print("")
      print("Goss Reporting : Raw Data has been saved")
      print("")
      wb1 = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\call_performance.xlsm")
      x1.Visible = False
      print("Goss Reporting : Data is importing, it will take 1-2 minutes")
      wb1.Application.Run("call_perf")
      print("")
      print("Goss Reporting :Report has been created and saved at location")
      print("")
      print("Goss Reporting :Report has been uploaded on Sharepoint")
      time.sleep(4)
      
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
#    Msg.CC = "Vinay.K.Sharma@mercer.com"
      Msg.Subject = "Daily Call Performance Report - Completed"
      Msg.Body = "mail sent through Self Service Tool"
      Msg.Send()
      response = input("Bot : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports") 
      print("")
      print("You : "+response)
      time.sleep(1)
      if response == "y":
                        wb.Application.Run("CloseBook")
                        wb1.Application.Run("CloseBook")
                        exit() 
      else:
          wb.Application.Run("CloseBook")
          wb1.Application.Run("CloseBook")
          exit() 
      
      
  except:
      outlook = win32.Dispatch('outlook.application')
      subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
      Msg = outlook.CreateItem(0)
      Msg.To = "vinamra.srivastava@mercer.com"
      Msg.CC = "priyanka.lnu@mercer.com"
      Msg.Subject = "Confirmation Mail-Call Performance Report"
      Msg.Body ="""Hi,
The Daily Call Performance Report is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool."""
      Msg.Send()
      Msg.close()














elif "5" in Report:
    try:
        print("Goss Reporting : You have selected Monthly Agent Performance Report " )
        print("")
        print("Goss Reporting : Your Request has been submitted " )
        print("")
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.23.84.15\SQL1;"
                      "Database=aceyus_edw;"
                      "Trusted_Connection=yes;")
        MSDate=input("Goss Reporting: Enter the first Business date of the Month in MM/DD/YYYY:")
        MEDate=input("Goss Reporting:Enter the last Business date of the Month MM/DD/YYYY:")
        
        cursor = cnxn.cursor()
        print("")
        print("Goss Reporting :Connecting to SQL Server")
        print("")
        print("Goss Reporting :Raw Data is fetching from Database")
        print("")
        sql = """select
 DateTime,
CAST(replace(ATM.AgentTeamID,'1000','') as varchar (8))+' - '+REPLACE(REPLACE(AT.EnterpriseName,'MHRS.',''),'MHRO.','') as 'TEAM'
,replace(A.PeripheralNumber,'1000','') as 'AGENT ID'
,REPLACE(REPLACE(A.EnterpriseName,'MHRS.',''),'MHRO.','') as 'PSR NAME'
,MAX(ISNULL(ASGD.LoggedOnTime,0)) as 'LOGGED ON TIME'
,SUM(ISNULL(ASGD.CallsHandled,0)) as 'HANDLED CALLS'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.TalkInTime,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as 'TALK TIME'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE (SUM(ISNULL(ASGD.HandledCallsTime,0))-(SUM(ISNULL(ASGD.IncomingCallsOnHoldTime,0))+SUM(ISNULL(ASGD.HandledCallsTalkTime,0))))/SUM(ISNULL(ASGD.CallsHandled,0)) END as 'WRAPUP TIME'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.IncomingCallsOnHoldTime,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as 'HOLD TIME'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.HandledCallsTime,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as 'AHT'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE 1.00*(3600*SUM(ISNULL(ASGD.CallsHandled,0)))/MAX(ISNULL(ASGD.LoggedOnTime,0)) END as 'CALLS PER SIGNON HOUR'
,CASE WHEN SUM(ISNULL(ASGD.IncomingCallsOnHold,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.IncomingCallsOnHoldTime,0))/SUM(ISNULL(ASGD.IncomingCallsOnHold,0)) END as 'AVG HOLD PER CALL HELD'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE 1.00*SUM(ISNULL(ASGD.IncomingCallsOnHold,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as '% CALLS HELD'
,SUM(ISNULL(ASGD.AgentOutCalls,0)) as 'OUTBOUND CALLS'
,CASE WHEN SUM(ISNULL(ASGD.AgentOutCalls,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.AgentOutCallsTime,0))/SUM(ISNULL(ASGD.AgentOutCalls,0)) END as 'OUTBOUND AHT'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE 1.00*SUM(ISNULL(ASGD.AgentOutCalls,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as '% OF CALLS OUTBOUND'
,SUM(ISNULL(ASGD.InternalCalls,0)) as 'INSIDE CALLS'
,CASE WHEN SUM(ISNULL(ASGD.InternalCalls,0))=0 THEN 0 ELSE SUM(ISNULL(ASGD.InternalCallsTime,0))/SUM(ISNULL(ASGD.InternalCalls,0)) END as 'INSIDE AHT'
,CASE WHEN SUM(ISNULL(ASGD.CallsHandled,0))=0 THEN 0 ELSE 1.00*SUM(ISNULL(ASGD.InternalCalls,0))/SUM(ISNULL(ASGD.CallsHandled,0)) END as '% OF CALLS INSIDE'
,CASE WHEN MAX(ISNULL(ASGD.LoggedOnTime,0))=0 THEN 0 ELSE 1.00*MAX(ISNULL(ASGD.NotReadyTime,0))/MAX(ISNULL(ASGD.LoggedOnTime,0)) END as 'NOT READY TIME'
,CASE WHEN MAX(ISNULL(ASGD.LoggedOnTime,0))=0 THEN 0 ELSE 1.00*MAX(ISNULL(ASGD.AvailTime,0))/MAX(ISNULL(ASGD.LoggedOnTime,0)) END as 'AVAIL TIME'
,CASE WHEN MAX(ISNULL(ASGD.LoggedOnTime,0))=0 THEN 0 ELSE 1.00*SUM(ISNULL(ASGD.WorkNotReadyTime,0)+ISNULL(ASGD.WorkReadyTime,0))/MAX(ISNULL(ASGD.LoggedOnTime,0)) END as 'WRAPUP %'
,CASE WHEN MAX(ISNULL(ASGD.LoggedOnTime,0))=0 THEN 0 ELSE 1.00*(SUM(ISNULL(ASGD.TalkInTime,0))+SUM(ISNULL(ASGD.IncomingCallsOnHoldTime,0))+MAX(ISNULL(ASGD.AvailTime,0)))/MAX(ISNULL(ASGD.LoggedOnTime,0)) END as '% WORKING'

from aceyus_edw.dbo.t_Agent_Skill_Group_Monthly ASGD
--aceyus_edw.dbo.t_Agent_Skill_Group_Daily ASGD



inner join aceyus_edw.dbo.t_Skill_Group SG on SG.SkillTargetID = ASGD.SkillGroupSkillTargetID 
inner join aceyus_edw.dbo.t_Agent A on A.SkillTargetID = ASGD.SkillTargetID
inner join aceyus_edw.dbo.t_Agent_Team_Member ATM on A.SkillTargetID = ATM.SkillTargetID
inner join aceyus_edw.dbo.t_Agent_Team AT on AT.AgentTeamID = ATM.AgentTeamID

where 
ASGD.DateTime between '"""+MSDate+"""' and '"""+MEDate+"""'
GROUP BY  DateTime,
CAST(replace(ATM.AgentTeamID,'1000','') as varchar (8))+' - '+REPLACE(REPLACE(AT.EnterpriseName,'MHRS.',''),'MHRO.',''),A.PeripheralNumber
,REPLACE(REPLACE(A.EnterpriseName,'MHRS.',''),'MHRO.','')

order by 1,3
"""
        cursor.execute(sql)

        row = cursor.fetchall()
        

        with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\APR\\Texas.csv', 'w', newline= '') as f:
            a = csv.writer(f, delimiter=',')
            a.writerow(["DateTime","TEAM","AGENT ID","PSR NAME","LOGGED ON TIME","HANDLED CALLS","TALK TIME","WRAPUP TIME","HOLD TIME","AHT","CALLS PER SIGNON HOUR","AVG HOLD PER CALL HELD","% CALLS HELD","OUTBOUND CALLS","OUTBOUND AHT","% OF CALLS OUTBOUND","INSIDE CALLS","INSIDE AHT","% OF CALLS INSIDE","NOT READY TIME","AVAIL TIME","WRAPUP %","% WORKING"])  
            a.writerows(row)


        cursor.close() 
        x1= win32com.client.Dispatch('Excel.Application') 
        wb = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\apr.xlsm")
        x1.Visible = False
       
        wb.Application.Run("csvToxls")
        print("Goss Reporting :Raw data Saved at Loaction " )
        print("")
        wb1 = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\APR_Month_final.xlsm")
        x1.Visible = False
        print("Goss Reporting :Data is importing,it will take 1-2 minutes")
        wb1.Application.Run("APR_final")
        print("")
        print("Goss Reporting :Report has been created and saved at location")
        print("")
        print("Goss Reporting :File has been uploaded on Sharepoint")
        time.sleep(4)
        outlook = win32.Dispatch('outlook.application')
        subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
        Msg = outlook.CreateItem(0)
        Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
        Msg.CC = ""
        Msg.Subject = "Monthly Agent Performance Report-Completed"
        Msg.Body = "mail sent through Self Service Tool"
        Msg.Send()
        response = input("Goss Reporting : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports:")
        print("")
        print("You : "+response)
        time.sleep(1)
        if response == "y":
                         wb.Application.Run("CloseBook")
                         wb1.Application.Run("CloseBook")
                         exit()
        else:
            wb.Application.Run("CloseBook") 
            wb1.Application.Run("CloseBook")
            exit()
        
        
        
    except:
          outlook = win32.Dispatch('outlook.application')
          subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
          Msg = outlook.CreateItem(0)
          Msg.To = "vinamra.srivastava@mercer.com"
          Msg.CC = "priyanka.lnu@mercer.com"
          Msg.Subject = "Confirmation Mail-Monthly Agent Performance Report"
          Msg.Body = """Hi,
The Monthly Agent Performance Report is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool."""
          Msg.Send()
          Msg.close()        












elif "6" in Report:
    try:
        print("Goss Reporting : You have selected Service Quality Status-Reminder " )
        print("")
        print("Goss Reporting : Your Request has been submitted " )
        Mondaydate=input('Goss Reporting : Enter the Report Extraction Date(mm/dd/yy):')
        Fridaydate=input('Goss Reporting : Enter the Database Update Date(mm/dd/yy):')
        outlook = win32.Dispatch('outlook.application')
        subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
        Msg = outlook.CreateItem(0)
        Msg.To = "#GOSS_OPS_Reporting@hub.wmmercer.com"
#       Msg.CC = "Vinay.K.Sharma@mercer.com"
        Msg.Subject = "ACTION REQUIRED: Service Quality Status - Executive Summary Dashboard - Weekly update for CSM assessments"
        Msg.Body = """Hi Everyone,       

We will be extracting a report on """+Mondaydate+""" from the below Connect database to update the CSM assessments for Admin Team Assessment Current, Admin Team Assessment Future, Team Resources and Status of Upgrades / Projects. Also, please populate the “Date Updated” field. If this field is not populated, the client will be “Red” for these assessments. 
In addition:
1)	If your client is Red or Yellow, you are required to complete the 2 new fields – Key Issues and Current Update. Please keep your updates at an Executive level. 
2)	If your client is going through a deconversion, please update the 2 new fields – Deconverting and Deconversion date.  The fields are defaulted to “N” and blank currently.

Please ensure you update the database by 5:00 PM ET on Friday """+Fridaydate+""". 
Once report is extracted, no exceptions will be made to rerun on Monday.

DB/HB
Client Governance/ Operations Scorecard/ CS Executive Summary Data(DB/HB)
https://connectv7.mercer.com/eRoom/Southwest/ClientGovernanceDeck/0_119b5b


Mail Sent through Self Servicing Tool"""
        Msg.Send()
    except:
          outlook = win32.Dispatch('outlook.application')
          subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.EXE'])
          Msg = outlook.CreateItem(0)
          Msg.To = "vinamra.srivastava@mercer.com"
          Msg.CC = ""
          Msg.Subject = "Confirmation Mail-Service Quality Status-Reminder"
          Msg.Body = """"Hi,
The Service QUALITY Status-Reminder is Completed.
Please check the report.
      
      
Mail sent through Self Servicing tool."""
          Msg.Send()
          Msg.close()
          
          
          









elif "7" in Report:
  try:  
    print("Goss Reporting : You have selected Global Upload Observation " )
    print("")
    
    Gdate=input("Enter the Previous Working Date in(YYYYMMDD) : " )
    G1date=input("Enter the Previous Working Date in(YYYY-MM-DD) : " )
    print("")
    print("Goss Reporting : Connecting to SQL Server")
    print("")
    print("Goss Reporting : Call Center Data is fetching from Database")
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=USFKL14DB13V;"
                      "Database=DEV_MMMart;"
                      "Trusted_Connection=yes;")

    cursor = cnxn.cursor()
    sql = """Select 


fact.calldtid as [CalendarDt],
SUM(fact.[AWLTotal])as[AWLTotal],
Convert(Date,fact.Loaddttm) as [Loaddttm],
Count(EmployeeID) as[Employee], 
Count(fact.[Quotes])as[Quotes], 
SUM(fact.[ACDCalls])as[ACDCalls],
SUM(fact.[ExpectedHandleTime])as[ExpectedHandleTime],
Sum(fact.[ACDTime])as[ACDTime],
SUM(fact.[ACWTime])as[ACWTime],
SUM(fact.[HoldTime])as[HoldTime],
SUM(fact.[AvailTime])as[AvailTime], 
SUM(fact.[StaffTime])as[StaffTime],
SUM(fact.[AUXTime])as[AUXTime],
SUM(fact.[TimeInADH])as[TimeInADH], 
SUM(fact.[TimeOutADH])as[TimeOutADH],
SUM(fact.[SurveyAcc])as[SurveyAcc],
SUM(fact.[SurveyCount])as[SurveyCount],
SUM(fact.[QualityScore])as[QualityScore], 
SUM(fact.[QualityEvals])as[QualityEvals],
SUM(fact.[TimeinCon])as[TimeinCons],
SUM(fact.[SchOpenTime])as[SchOpenTime],
SUM(fact.[ExtnOutCalls])as[ExtnOutCalls]







from 
[mm_glb_orarpt].[DimEmployeeID] EEID
inner join [mm_glb_orarpt].[FactAgentCall] fact  on fact.EmployeeSeqID=EEID.EmployeeSeqID




where
fact.[CallDtID] like '"""+Gdate+"""%'  




group by fact.calldtid,fact.Loaddttm
"""
    cursor.execute(sql)

    row = cursor.fetchall()

    with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\Global Upload\\Raw.csv', 'w', newline= '') as f:
        a = csv.writer(f, delimiter=',')
        a.writerow(["CalendarDt","AWLTotal","Loaddttm","Employee","Quotes","ACDCalls","ExpectedHandleTime","ACDTime","ACWTime","HoldTime","AvailTime","StaffTime","AUXTime","TimeInADH","TimeOutADH","SurveyAcc","SurveyCount","QualityScore","QualityEvals","TimeinCons","SchOpenTime","ExtnOutCalls"])  
        a.writerows(row)


    cursor.close() 

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=USFKL14DB13V;"
                      "Database=DEV_MMDataCollection;"
                      "Trusted_Connection=yes;")

    cursor = cnxn.cursor()
    sql = """Select GC.FileType,GC.Loaddttm,

SUM(GC.TimeInADH) As Time_In_ADH,
SUM(GC.ExpectedHandleTime) AS Exp_Handle_Time,
SUM(GC.ACDCalls) AS ACD_Calls,
SUM(GC.SurveyCount) AS SurveyCount,
CONVERT(Date,GC.CalendarDt,103)as CalendarDt
FROM dca_orarpt.GlobalCallCenterReference GR 
INNER JOIN dca_orarpt.GlobalCallCenter GC ON GR.SysID = GC.SysID


Where CalendarDt='"""+G1date+"""'  
GROUP BY GC.FileType, GC.CalendarDt, GC.Loaddttm


Having ((GC.fileType)=1 or (GC.fileType)=4 or (GC.fileType)=5 or (GC.fileType)=6)
"""
    cursor.execute(sql)

    row = cursor.fetchall()

    with open('J:\\Teams\\Reporting\\Self Servicing Tool\\Raw Data\\Global Upload\\Raw1.csv', 'w', newline= '') as f:
        a = csv.writer(f, delimiter=',')
        a.writerow(["FileType","Loaddttm","Time_In_ADH","Exp_Handle_Time","ACD_Calls","SurveyCount","CalendarDt"])  
        a.writerows(row)


    cursor.close() 
    x1=win32com.client.Dispatch('Excel.Application')
    wb1 = x1.Workbooks.Open("J:\\Teams\\Reporting\\Self Servicing Tool\\Macro\\global upload1 .xlsm")
    x1.Visible = False
    print("")
    print("Goss Reporting : Mail has been framed and ready to send " )
    print("")
    wb1.Application.Run("globa")
  except:
     response = input("Goss Reporting : Press any key to Close the Self Service Tool and click on Chat Now button to make others reports:")
     print("")
     print("You : "+response)
     time.sleep(1)
     if response == "y":
                       exit()
     else:
        exit()





else:
     print("")
     print("Goss Reporting : Sorry the Report name not found" ) 
     print("")
     response = input("Goss Reporting : Press any key to Close the Self Service Tool and click on Chat Now button to make other reports:") 
     print("")
     print("You : "+response)
     time.sleep(1)
     exit()

    