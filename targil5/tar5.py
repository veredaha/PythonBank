
import numpy as np
import statistics
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
import os
import pprint
import xmltodict
import sys

class PersonalInfo:
  def __init__(self ,Name:str , id :str ,Phone_number:str,Email_address:str) -> None: 
    """
    function creates class PersonalInfo
    :return: None
    """
    self.Name = Name
    self.id = id
    self.Phone_number =Phone_number
    self.Email_address =Email_address
  
class BankAccount(PersonalInfo):
 def __init__(self ,Name:str , id :str ,Phone_number:str,Email_address:str,Balance:int) -> None:
    """
    function creates class BankAccount , inherents from personalinfo
    :return: None
    """
    PersonalInfo.__init__(self,Name , id  ,Phone_number,Email_address)
    self.Balance =Balance
 
 def __str__(self)-> str:
    """
    function that prints bankaccount information
    :return:str
    """
    return "Name: " + str(self.Name)+" ,ID: " +str(self.id)+" Phone numbe: "+str(self.Phone_number)+" Email: "+str(self.Email_address)+" Balance: "+ str(self.Balance)
 
 def Deposit(self,depositamount:int)->None:
   """
    function deposits money to balance
    :param depositamount: int example -> 500
    :return: None
    """
   commision = 1.75
   self.Balance = self.Balance + int(depositamount) - int(commision)
   

def Withdraw(self,withdrawamount:int)->None:
    """
    function withdraws money from balance
    :param withdrawamount: int example -> 500
    :return: None
    """
    commision = 1.75
    self.Balance = self.Balance - int(withdrawamount) - int(commision)

class StudentBankAccount(BankAccount):
    def __init__(self ,Name:str , id :str ,Phone_number:str,Email_address:str,Balance:int,college_name:str) -> None:
     """
    function creates class StudentBankAccount , inherents from BankAccount
    :return: None
    """
     BankAccount.__init__(self ,Name , id  ,Phone_number,Email_address,Balance)
     self.college_name = college_name
    def __str__(self)-> str:
     """
     function that prints studentbankaccount information
     :return:str
     """
     return "Name: " + str(self.Name)+" ,ID: " +str(self.id)+" Phone number: "+str(self.Phone_number)+" Email: "+str(self.Email_address)+" Balance: "+ str(self.Balance)+" College name: "+str(self.college_name)
    
    def Deposit_Student(self,depositamount:int)->None:
        """
    function deposits money to balance in student bank acoount
    :param depositamount: int example -> 500
    :return: None
    """
        commision = 1.75
        self.Balance =self.Balance + int(depositamount) - int(commision)
    
    def Withdraw_Student(self,withdrawamount:int)->None:
        """
    function withdraws money from balance in student bank acoount
    :param withdrawamount: int example -> 500
    :return: None
    """
        commision = 1.75
        if ( self.Balance - int(withdrawamount) - int(commision)) < 0:
            print("Student account cant be negative")
        else:
         self.Balance =self.Balance - int(withdrawamount) - int(commision)

class business_info:
    def __init__(self,buisnum:str) -> None:
      """
     function creates class business_info
     :return: None
     """
      self.buisnum =buisnum

class BusinessBankAccount(BankAccount,business_info):
    def __init__(self ,Name:str , id :str ,Phone_number:str,Email_address:str,Balance:int,buisnum:str) -> None:
     """
     function creates class BusinessBankAccount
     :return: None
     """
     BankAccount.__init__(self,Name , id  ,Phone_number,Email_address,Balance)
     business_info.__init__(self,buisnum)
    
    def Withdraw_Buissnes(self,withdrawamount:int)->None:
     """
    function withdraws money from balance in buissnes bank acoount
    :param withdrawamount: int example -> 500
    :return: None
    """
     commision = 1.75 *1.5
     self.Balance = self.Balance - int(withdrawamount) - int(commision)
    
    def Deposit_Buissnes(self,depositamount:int)->None:
      """
    function deposits money to balance in buissnes bank acoount
    :param depositamount: int example -> 500
    :return: None
    """
      commision = 1.75 *1.5
      self.Balance = self.Balance + int(depositamount) - int(commision)

class Bank(BusinessBankAccount,StudentBankAccount):
 def __init__(self ,Name:str , id :str ,Phone_number:str,Email_address:str,Balance:int,buisnum:str, college_name:str,accounttype:str) -> None:
     """
     function creates class Bank
     :return: None
     """
     if not buisnum == "-":
      BusinessBankAccount.__init__(self,Name , id ,Phone_number,Email_address,Balance, buisnum)
      self.college_name = "-"
      self.accounttype = accounttype
     elif not college_name == "-":
      StudentBankAccount.__init__(self ,Name , id  ,Phone_number,Email_address,Balance, college_name)
      self.buisnum ="_"
      self.accounttype = accounttype
     else:
        BankAccount.__init__(self ,Name , id  ,Phone_number,Email_address,Balance)
        self.buisnum ="-"
        self.college_name = "-"
        self.accounttype = accounttype
 
 def __str__(self) -> str:
     """
     function that prints studentbankaccount information
     :return:str
     """
     return "Name: " + str(self.Name)+" ,ID: " +str(self.id)+" Phone number: "+str(self.Phone_number)+" Email: "+str(self.Email_address)+" Balance: "+ str(self.Balance)+" Buisness number: " + str(self.buisnum) +"College name: "+str(self.college_name) + " Type: " + str(self.accounttype)

    
 def add_new_account(self)-> 'Bank':
     """
    function adds a new account to account list
    :return: Bank
    """
     if not isinstance(self.Name,str) or len(self.id)>8 or len(self.Phone_number)>11 or not isinstance(self.Email_address,str) or not isinstance(self.Balance,int) or len(self.buisnum) >8 or not isinstance(self.college_name,str) or not isinstance(self.accounttype,str):
        return "Bank details is not valid"
     else:
      b = Bank(self.Name,self.id,self.Phone_number,self.Email_address,self.Balance,self.buisnum,self.college_name,self.accounttype)
      return b
 
def Withdraw_by_user_id(withdrawamount:int,lst:list,id:str)->list:
   """
    function withdraws money by id number
    :param withdrawamount: int example -> 500
    :param lst: list (list of all accounts)
    :param id: str example ->'1234567'
    :return: list
    """
   for l in lst:
        if l.id == id:
            if l.accounttype == 'StudentBankAccount':
                l.Withdraw_Student(withdrawamount)
            elif l.accounttype == 'BuisnessBankAccount':
                l. Withdraw_Buissnes(withdrawamount)
            else:
                l.Withdraw(withdrawamount)

            return lst

def Deposit_by_user_id(depositamount:int,lst:list,id:str)->list:
   """
    function withdraws money by id number
    :param depositamount: int example -> 500
    :param lst: list (list of all accounts)
    :param id: str example ->'1234567'
    :return: list
    """
   for l in lst:
        if l.id == id:
            if l.accounttype == 'StudentBankAccount':
                l.Deposit_Student(depositamount)
            elif l.accounttype == 'BuisnessBankAccount':
                l. Deposit_Buissnes(depositamount)
            else:
                l.Deposit(depositamount)

            return lst

def calc_balance_statistics(lst:list)->str:
    """
    function calculates median, avarage, 10th percentile and 90th percentile
    :param lst: list (list of all accounts)
    :return: str
    """
    sum = 0
    arr = []
    for l in lst:
        arr.append(l.Balance)

    med = statistics.median(arr)
    mean = statistics.mean(arr)
    pten = np.percentile(arr, 10)
    pninty = np.percentile(arr, 90)
    return "The median is : " + str(med) + " mean is: " + str(mean) + " 10th percentile : " + str(pten) + "90th percentile : " + str(pninty)
        



def delete_by_userID(lst:list,id:str)->list:
    """
    Deletes user from account list by id number
    :param lst: list (list of all accounts)
    :param id: str example ->'1234567'
    :return: list
    """
    for l in lst:
        if l.id == id:
            lst.remove(l)
            return lst

def load_and_parse_init_data(path:str)->list:
   """
    Parse and load the data from xml file
    :param path: have the path for init.xml file
    :return: list
    """
   tree = ET.parse(path)
   root = tree.getroot()
   lst = []
   add = []

   for item in root:

      dict_of_items = {}
      dict_of_items.update(item.attrib)
      

      for elem in item:
          for sub in elem:
                dict_of_items[sub.tag] = sub.text
      lst.append(dict_of_items)  
   for n in lst:

    name =n['name']
    id = n['id']
    phone = n['phone']
    email = n['email']
    Balance =int(n['Balance'])
    buisnum =n['buisnum']
    type =n['accounttype']
    coll = '-'
    addxml = Bank(name,id,phone,email,Balance,buisnum,type,coll)
    add.append(addxml)

   
   return add

def __str__(list:list)->str:
    """
    Returns a string with information about all already added clients 
    :param list: list of all clients
    :return: str
    """
    for n in list:
     print(n.__str__())
 
def main():
    
 arg = sys.argv[1]
 printxml = (load_and_parse_init_data(arg))
 list =[]
 #adss to list
 for p in printxml:
    p= p.add_new_account()
    list.append(p)
 Bank1 = Bank('Vered Aharonov','1235684','0535226617','vered@gmail.com',1000,'-','-','BankAccount')
 Bank2 = Bank('Lili Cohen','1232222','0535222597','LI@gmail.com',10000,'-','Ruppin','StudentBankAccount')
 Bank3 = Bank('Anna Li','1232525','0545226619','ann@gmail.com',-500,'12345678','-','BuisnessBankAccount')
 add1 = Bank1.add_new_account()
 add2 = Bank2.add_new_account()
 add3 = Bank3.add_new_account()
 #adds all new accounts to list
 list.append(add1)
 list.append(add2)
 list.append(add3)
 #printing before activating functions
 print("Before actions:")
 __str__(list)
 #delete account with '1235684' id
 delete_by_userID(list,'1235684')
 #withdraw 500 in account with '1232222' id
 Withdraw_by_user_id(500,list,'1232222')
 #deposit 11000 in account with '1232222' id
 Deposit_by_user_id(11000,list,'1232222')
 calc =calc_balance_statistics(list)
 print(calc)
 #printing after activating functions
 print("after actions:")
 __str__(list)


if __name__ == '__main__':
    main()
 