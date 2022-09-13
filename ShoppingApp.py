#10/03/21
#AAT basket program Final Version - Tyler Tobin - MAC OS VERSION ONLY
#THIS VERSION IS ONLY COMPATIBLE WITH MAC OS

#First login screen credentials:
#user1
#pass1
#Admin login details:
#admin1
#pass1

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time;
import datetime
from datetime import datetime
import csv
from tkinter import Menu
import os
from tkinter import filedialog, messagebox, ttk
import tkinter.font as font
import random

#Imports from python libraries to use pre-made functions
#import of tkinter and messagebox are the key imports for the program as they provide the GUI for the program

#========================================================================================================================================= 
def main():
    root = Tk()
    app = Login(root)
#function outside of any class to begin the GUI from the tkinter 

class Login:
    '''
Class Login is the first class that is initilised when the program begins
This class can also be returned to from class Home to log out
    '''
    def __init__(self, master):
        #constructor method will create GUI layout for login screen such as: Frames, Buttons, Labels and entry boxes
        self.master = master
        self.master.title("AAT Services")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(background='gray60')
        self.frame.configure(background='gray60')

#=========================================================================================================================================

        '''
        These attributes store the user's input of username and password from the entry fields below
        They can be used within other classes or outside of classes if the data is needed elsewhere, for
        example displaying a welcome message in the class home
        '''
        self.usernameVerify = StringVar()
        self.passwordVerify = StringVar()

#=========================================================================================================================================

        '''
        The attributes created below are basic widgets setting the overall look and theme, the grids are created to seperate
        each section of the GUI for example a header as seen below and the entry fields
        '''

        self.header = Label(self.frame, text = "AAT", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange")
        self.header.grid(row = 0, column = 0, columnspan = 2, pady = 20)


        self.Loginframe = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge")
        self.Loginframe.grid(row = 1, column = 0, pady = 20)
        self.Loginframe.configure(background='gray60')
        self.Loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 5, relief = "ridge")
        self.Loginframe2.grid(row = 2, column = 0, pady = 20)
        self.Loginframe2.configure(bg = 'gray60')
        
        self.Loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge")
        self.Loginframe3.grid(row = 3, column = 0, pady = 20)
        self.Loginframe3.configure(background='gray60')


#=========================================================================================================================================
        #This section provides the user the ability to enter their credentials
        self.labelUsername = Label(self.Loginframe, text = "Username:", font = ("arial", 30, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.labelUsername.grid(row = 0, column = 0)

        self.textUsername = Entry(self.Loginframe, textvariable = self.usernameVerify, bd = 5)
        self.textUsername.grid(row = 0, column = 1)

        
        self.labelPassword = Label(self.Loginframe, text = "Password:", font = ("arial", 30, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.labelPassword.grid(row = 1, column = 0)

        self.textPassword = Entry(self.Loginframe, textvariable = self.passwordVerify, bd = 5)
        self.textPassword.grid(row = 1, column = 1)

#=========================================================================================================================================
        #Once the credentials are entered then the button below will be pressed initiating a method
        self.loginButton = Button(self.Loginframe2, text = "Log In", command = self.Login_system, width = 20, font = ("arial", 20, "bold") , fg = "orange")
        self.loginButton.grid(row = 0, column = 0)

        self.resetButton = Button(self.Loginframe2, text = "Clear/Log Out", command = self.reset, width = 20, font = ("arial", 20, "bold"), fg = "orange").grid(row = 0, column = 1)
        self.exitButton = Button(self.Loginframe2, text = "Exit", command = exit, width = 20, font = ("arial", 20, "bold"), bg = "gray25", fg = "orange").grid(row = 0, column = 3)

#=========================================================================================================================================

        self.manageButton = Button(self.Loginframe3, text = "Go Home", command = self.Home_window, width = 20, font = ("arial", 20, "bold"), state = DISABLED, fg = "orange")
        self.manageButton.grid(row = 0, column = 0)
        self.manageButton.configure(background='gray25')
        
    def Login_system(self):
        #This is the login method that is called when the button from the constructor method "self.loginButton" is pressed

        user = (self.usernameVerify.get())
        pas = (self.passwordVerify.get())
        #The two variables above store the data retrieved from the entry boxes in the GUI
        
        print(user, "data inside")
        print(pas, "data inside")
        #These print statements are used for me while writing the progra to test if the data has been retrieved by the method

        if user == "user1":
            
            print("correct username")
            if pas == "pass1":
                self.manageButton.config(state = NORMAL)
                print("correct password")
            else:
                tkinter.messagebox.askokcancel("AAT ADMIN", "Username or password is incorrect!")
        else:
            tkinter.messagebox.askokcancel("AAT ADMIN", "Username or password is incorrect!")
            #This message box uses the import fromm the start of the code to create an alert when the user has entered an incorrect password or username

            print(user, "data inside")
            print(pas, "data inside")
            print("Incorrect")
            #These print statements are used for me while writing the progra to test if the data has been retrieved by the method

#=========================================================================================================================================
    def reset(self):
        self.manageButton.config(state = DISABLED)

        self.usernameVerify.set("")
        self.passwordVerify.set("")

    def Home_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Home(self.newWindow)

#The section below is where others features can be inserted
#------------------------------------------------------------------------------->
#Home class can be inherited to use its methods to return back home or to a certain feature
#This class combines all of the features in one menu
#Class Home has been designed to allow seperate programs to be combined easily
class Home():

    def __init__(self, master):
        self.master = master
        self.master.title("AAT Home Page")
        self.master.geometry('720x500+0+0')
        self.master.configure(bg = "gray60")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.frame.configure(bg = "gray60")

        self.Homeframe = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge")
        self.Homeframe.grid(row = 1, column = 0, pady = 20)
        self.Homeframe.configure(bg = "gray60")
        self.Homeframe2 = Frame(self.frame, width = 1000, height = 100, bd = 5, relief = "ridge")
        self.Homeframe2.grid(row = 2, column = 0, pady = 10)
        self.Homeframe2.configure(bg = "gray60")
        
        self.header = Label(self.Homeframe, text = "AAT Home Screen", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0)

        self.AdminButton = Button(self.Homeframe2, text = "Admin", command = self.loadAdmin, width = 15, height = 2, font = ("arial", 20, "bold"), bd = 2, fg = "orange")
        self.AdminButton.grid(row = 0, column = 0, pady = 5, padx = 2)

        self.CatalogueButton = Button(self.Homeframe2, text = "Catalogue", command = self.loadCatalogue, width = 15, height = 2, font = ("arial", 20, "bold"), bd = 2, fg = "orange")
        self.CatalogueButton.grid(row = 1, column = 0, pady = 5, padx = 2)

        self.BasketButton = Button(self.Homeframe2, text = "Basket", command = self.loadBasket, width = 15, height = 2, font = ("arial", 20, "bold"), bd = 2, fg = "orange")
        self.BasketButton.grid(row = 2, column = 0, pady = 5, padx = 2)

        self.exitButton = Button(self.Homeframe2, text = "Exit", command = exit, width = 15, height = 2, font = ("arial", 20, "bold"), bd = 2, fg = "orange")
        self.exitButton.grid(row = 3, column = 0, pady = 5, padx = 2)

        #Encapsulation of the time that the user has logged in, this data is private so it is encapsulated
        self.now = datetime.now()
        self.__timeOfLogin = self.now.strftime("%H:%M:%S")
        
        self.timeStamp = Label(self.frame, text = "Logged in at: " + str(self.__timeOfLogin))
        self.timeStamp.grid(row = 3, column = 0)

    #The below methods can be called from within the whole program if the class is inherited
    #These methods will load the selected class
    def loadAdmin(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Admin(self.newWindow)

    def loadCatalogue(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Application(self.newWindow)

    def loadBasket(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Basket(self.newWindow)

    def returnHome(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Home(self.newWindow)
        


    
#=========================================================================================================================================
#F1 - Tyler Tobin
class Admin(Home):
    #Admin window that is loaded after an administrator has logged in
    def __init__(self, master):
        self.master = master
        self.master.title("AAT Administration")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.frame.configure(bg = "gray60")
        self.master.configure(bg = "gray60")

#=========================================================================================================================================

        self.usernameVerify = StringVar()
        self.passwordVerify = StringVar()




#=========================================================================================================================================

        self.header = Label(self.frame, text = "AAT Administration Features", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.Loginframe = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.Loginframe.grid(row = 1, column = 0)
        self.Loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 5, relief = "ridge", bg = "gray60")
        self.Loginframe2.grid(row = 2, column = 0)
        self.Loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.Loginframe3.grid(row = 3, column = 0, pady = 2)

#=========================================================================================================================================
        
        self.labelUsername = Label(self.Loginframe, text = "Username:", font = ("arial", 30, "bold"), bd = 22, bg = "gray60", fg = "orange").grid(row = 0, column = 0)
        self.textUsername = Entry(self.Loginframe, textvariable = self.usernameVerify, bd = 5)
        self.textUsername.grid(row = 0, column = 1)

        
        self.labelPassword = Label(self.Loginframe, text = "Password:", font = ("arial", 30, "bold"), bd = 22, bg = "gray60", fg = "orange").grid(row = 1, column = 0)
        self.textPassword = Entry(self.Loginframe, textvariable = self.passwordVerify, bd = 5)
        self.textPassword.grid(row = 1, column = 1)

#=========================================================================================================================================

        self.loginButton = Button(self.Loginframe2, text = "Log In", command = self.Login_system, width = 20, font = ("arial", 20, "bold"), fg = "orange").grid(row = 0, column = 0)
        self.resetButton = Button(self.Loginframe2, text = "Clear/Log Out", command = self.reset, width = 20, font = ("arial", 20, "bold"), fg = "orange").grid(row = 0, column = 1)
        self.exitButton = Button(self.Loginframe2, text = "Back", command = self.returnHome, width = 20, font = ("arial", 20, "bold"), fg = "orange").grid(row = 0, column = 2)

#=========================================================================================================================================

        self.manageButton = Button(self.Loginframe3, text = "Add Stock", command = self.management_window, font = ("arial", 20, "bold"), state = DISABLED, fg = "orange")
        self.manageButton.grid(row = 0, column = 0)
        self.stockButton = Button(self.Loginframe3, text = "View Stock", command = self.stock_window, font = ("arial", 20, "bold"), state = DISABLED, fg = "orange")
        self.stockButton.grid(row = 0, column = 1)

#=========================================================================================================================================

    def Login_system(self):

        user = (self.usernameVerify.get())
        pas = (self.passwordVerify.get())
        
        print(user, "data inside")
        print(pas, "data inside")

        if user == "admin1":
            self.manageButton.config(state = NORMAL)
            print("correct username")
            if pas == "pass1":
                self.stockButton.config(state = NORMAL)
                print("correct password")
                

            
        else:
            tkinter.messagebox.askokcancel("AAT ADMIN", "Username or password is incorrect!")

            print(user, "data inside")
            print(pas, "data inside")
            print("Incorrect")


#=========================================================================================================================================
    def reset(self):
        #Logs the user out by disabling the buttons until they log in again
        self.manageButton.config(state = DISABLED)
        self.stockButton.config(state = DISABLED)
        #Clears the entry field to allow the user to re-enter a value
        self.usernameVerify.set("")
        self.passwordVerify.set("")


    #The methods below create new windows over the top layer of the GUI
    def management_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Control(self.newWindow)

    def stock_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Stock(self.newWindow)

#=========================================================================================================================================


class Control(Home):
    #This is the class that is initialised when the user presses the add stock button, this will allow them to add stock to the database

    
    
    def __init__(self, master):
        self.master = master
        self.master.title("Add Stock")
        self.master.geometry('1080x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(bg = "gray60")
        self.frame.configure(bg = "gray60")


        #Creating the string variables needed to save data in to from the entry fields
        
        self.catName = StringVar()
        self.proName = StringVar()
        self.proPrice = StringVar()
        self.proCode = StringVar()
        self.proQty = StringVar()

#=========================================================================================================================================


        self.header = Label(self.frame, text = "Management", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.manframe2 = Frame(self.frame, width = 1000, height = 200, bd = 20, relief = "ridge", bg = "gray60")
        self.manframe2.grid(row = 1, column = 0)
        self.backBtn = Button(self.frame, text = "Back", command = self.master.destroy, width = 20, font = ("arial", 20, "bold"), fg = "orange")
        self.backBtn.grid(row = 2, column = 0)



#=========================================================================================================================================

        self.prodTitle = Label(self.manframe2, text = "Product", font = ("arial", 20, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.prodTitle.grid(row = 0, column = 0, sticky = W)

        
        
        self.prodAddBtn = Button(self.manframe2, text = "Add/Update", command = self.productAdd, font = ("arial", 20, "bold"), fg = "orange")
        self.prodAddBtn.grid(row = 0, column = 1)

        self.catNameLbl = Label(self.manframe2, text = "Category Name:", font = ("arial", 15, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.catNameLbl.grid(row = 1, column = 0)

        self.catNameEnt = Entry(self.manframe2, textvariable = self.catName, bd = 10)
        self.catNameEnt.grid(row = 1, column = 1)

        self.prodNameLbl = Label(self.manframe2, text = "Product Name:", font = ("arial", 15, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.prodNameLbl.grid(row = 2, column = 0)

        self.prodNameEnt = Entry(self.manframe2, textvariable = self.proName, bd = 10)
        self.prodNameEnt.grid(row = 2, column = 1)

        self.prodCodeLbl = Label(self.manframe2, text = "Product Code:", font = ("arial", 15, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.prodCodeLbl.grid(row = 3, column = 0)

        self.prodCodeEnt = Entry(self.manframe2, textvariable = self.proCode, bd = 10)
        self.prodCodeEnt.grid(row = 3, column = 1)

        self.prodPriceLbl = Label(self.manframe2, text = "Product Price:", font = ("arial", 15, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.prodPriceLbl.grid(row = 4, column = 0)

        self.prodPriceEnt = Entry(self.manframe2, textvariable = self.proPrice, bd = 10)
        self.prodPriceEnt.grid(row = 4, column = 1)

        self.prodQtyLbl = Label(self.manframe2, text = "Product Quantity:", font = ("arial", 15, "bold"), bd = 22, bg = "gray60", fg = "orange")
        self.prodQtyLbl.grid(row = 5, column = 0)

        self.prodQtyEnt = Entry(self.manframe2, textvariable = self.proQty, bd = 10)
        self.prodQtyEnt.grid(row = 5, column = 1)



    def productAdd(self):
        #this method saves the entries from each field
        self.catSaveFromEnt = str(self.catName.get())
        self.nameSaveFromEnt = str(self.proName.get())
        self.priceSaveFromEnt = int(self.proPrice.get())
        self.codeSaveFromEnt = int(self.proCode.get())
        self.qtySaveFromEnt = int(self.proQty.get())


        #Below is the code for checking if the category entered already exists
        #It begins by opening the stock file and converting it in to a list
        file = open('stock.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)

        #It will then loop in a range of how many elements are in the list
        for x in list(range(0, len(self.fileData))):

            #If the entry is equal to the first column in each row of the list then it will alert the user that it is infact in the database
            if self.catSaveFromEnt == self.fileData[x][0]:
                tkinter.messagebox.askokcancel("AAT ADMIN", "This category already exists!")
                break
            #If it is not then it will tell the user that it is not in the database
            else:
                
                print("continue!!!")
                break

        #This code will save the entries that were just retrieved in to the csv file
        with open ("stock.csv", "a+") as csvfile:
            groupWriter = csv.writer(csvfile, delimiter = ",")
            groupWriter.writerow([self.catSaveFromEnt, self.nameSaveFromEnt, self.priceSaveFromEnt, self.codeSaveFromEnt, self.qtySaveFromEnt])



        

class Stock(Home):
    #The stock class will be a way for the admin user to access all products and categories within the database aswell as delete them
    def __init__(self, master):
        self.master = master
        self.master.title("Stock")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(bg = "gray60")
        self.frame.configure(bg = "gray60")
        
        self.header = Label(self.frame, text = "Stock", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0, pady = 20, columnspan = 2)

        self.stoframe0 = Frame(self.frame, width = 1000, height = 100, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe0.grid(row = 2, column = 0, pady = 2, padx = 2, columnspan = 2)
        self.stoframe = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe.grid(row = 1, column = 0, pady = 2, padx = 2)
        self.stoframe2 = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe2.grid(row = 1, column = 1, pady = 2, padx = 2)

        file = open('stock.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)

        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][1])
            print(self.fileData[x][1])


        self.userStockChoice = Listbox(self.stoframe)
        self.userStockChoice.grid(row = 0, column = 0)
        #This code is inserting the data to the list box for the first time of loading the window
        for x, y in enumerate(self.listOfData):
            self.userStockChoice.insert(x, y)

        self.updateButton = Button(self.stoframe0, text = "view", command = self.updateStock, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.updateButton.grid(row = 0, column = 0, padx = 5)

        self.DeleteButton = Button(self.stoframe0, text = "Delete", command = self.deleteStock, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.DeleteButton.grid(row = 0, column = 1, padx = 5)

        self.SaveButton = Button(self.stoframe0, text = "Save Report", command = self.saveStockReport, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.SaveButton.grid(row = 0, column = 2, padx = 5)

        self.backButton = Button(self.stoframe0, text = "Back", command = self.master.destroy, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.backButton.grid(row = 0, column = 3, padx = 5)




        self.categoryLabel = Label(self.stoframe2, text = "Category:", bg = "gray60", fg = "orange")
        self.categoryLabel.grid(row = 0, column = 0)

        self.nameLabel = Label(self.stoframe2, text = "Name:", bg = "gray60", fg = "orange")
        self.nameLabel.grid(row = 1, column = 0)

        self.priceLabel = Label(self.stoframe2, text = "Price:", bg = "gray60", fg = "orange")
        self.priceLabel.grid(row = 2, column = 0)

        self.codeLabel = Label(self.stoframe2, text = "Code:", bg = "gray60", fg = "orange")
        self.codeLabel.grid(row = 3, column = 0)

        self.quantityLabel = Label(self.stoframe2, text = "Quantity:", bg = "gray60", fg = "orange")
        self.quantityLabel.grid(row = 4, column = 0)

        self.stockLabel = Label(self.stoframe2, text = "Stock Low:", bg = "gray60", fg = "orange")
        self.stockLabel.grid(row = 5, column = 0)





        self.categoryLabelData = Label(self.stoframe2, text = "--------", bg = "gray60", fg = "orange")
        self.categoryLabelData.grid(row = 0, column = 1)

        self.nameLabelData = Label(self.stoframe2, text = "--------", bg = "gray60", fg = "orange")
        self.nameLabelData.grid(row = 1, column = 1)

        self.priceLabelData = Label(self.stoframe2, text = "£xxxx", bg = "gray60", fg = "orange")
        self.priceLabelData.grid(row = 2, column = 1)

        self.codeLabelData = Label(self.stoframe2, text = "----", bg = "gray60", fg = "orange")
        self.codeLabelData.grid(row = 3, column = 1)

        self.quantityLabelData = Label(self.stoframe2, text = "xxx", bg = "gray60", fg = "orange")
        self.quantityLabelData.grid(row = 4, column = 1)

        self.stockLowLabelData = Label(self.stoframe2, text = "yes/no", bg = "gray60", fg = "orange")
        self.stockLowLabelData.grid(row = 5, column = 1)

        file = open('stock.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)
        timeDate = datetime.now()
        timestamp = str(timeDate)
        self.listOfData = []
        stockQueryCounter = 0
        #If the stock is low while opening the window it will create a list and append all the product codes that are low on stock
        stockLowList = list()
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][1])
            stockQueryCounter = stockQueryCounter + 1
            #Validating whether the stock of the item from the list created is under 20
            if int(self.fileData[x][4]) < 20:
                print("An item is low on stock")
                stockLowList.append(self.fileData[x][3])
                print(stockLowList)
                tkinter.messagebox.askokcancel("AAT ADMIN", "Item(s)" + str(stockLowList) + "Low")
            else:
                print("stock good")
                
    def updateStock(self):
        #Below i have encased the block of code in an exception handler which was very useful while I was testing the code to see where i had an error occuring
        try:
            self.index = self.userStockChoice.curselection()[0]
            print(self.index)
            self.categoryLabelData.config(text = self.fileData[self.index][0])
            self.nameLabelData.config(text = self.fileData[self.index][1])
            self.priceLabelData.config(text = "£" + self.fileData[self.index][2])
            self.codeLabelData.config(text = self.fileData[self.index][3])
            self.quantityLabelData.config(text = self.fileData[self.index][4]) 
            if int(self.fileData[self.index][4]) <= 19:
                print("stock low")
                self.stockLowLabelData.config(text = "Yes")    
            else:
                print("stock good")
                self.stockLowLabelData.config(text = "No")
            return None
        except ValueError:
            print("Error Execpetion caught!")

    def deleteStock(self):
        #Getting the list index from the where the user has pressed on an option from the listbox
        self.index = self.userStockChoice.curselection()[0]
        self.indexCode = str(self.fileData[self.index][3])
        print(self.indexCode)
        tempList = list()
        with open('stock.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                tempList.append(row)
                for field in row:
                    if field == self.indexCode:
                        tempList.remove(row)
        with open('stock.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(tempList)
        print("stock successfully deleted")
        file = open('stock.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)
        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][0])
            print(self.fileData[x][0])
        self.userStockChoice = Listbox(self.stoframe)
        self.userStockChoice.grid(row = 0, column = 0)
        #Inserting the data from listOfData in to the list box
        for x, y in enumerate(self.listOfData):
            self.userStockChoice.insert(x, y)

    def saveStockReport(self):
        #This method returns a file containing a report generated by the user using txt files

        #To begin the file is opened using the csv reader function
        file = open('stock.csv')
        reader = csv.reader(file)
        #I then put the data read by python in to a list by row
        self.fileData = list(reader)
        #Using the datetime library I can retrieve the date and time at which the file was created
        timeDate = datetime.now()
        timestamp = str(timeDate)
        #Creating an empty list to be used later
        self.listOfData = []
        file.close()

        #Now I am opening the file where the data can be written to, the file name contains the date and time
        f = open("stockReport" + timestamp + ".txt", "a")
        f.write(timestamp + "\n")
        f.write("Product : qty : code\n")
        #A for loop is used to append data to listOfData from the rows stored in the csv file, this is done by finding the length of the elements inside the list.
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][1])
            
            
            f.write(str(self.fileData[x][1]) + " " + str(self.fileData[x][4]) + " " + str(self.fileData[x][3]) + "\n")
        
        f.close()
        tkinter.messagebox.askokcancel("AAT ADMIN", "Report Saved!")
        
        
#===========================================================================================
#F2 Radu Pop

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1080x720+0+0')
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.menu_bar.add_command(label='Exit', command=quit)
        self.category_entry = globals()
        self.searchValue = StringVar()

     #counter variables
        self.counter = 0
        self.counterLength = 0
     #adding frames
        self.top = Frame(master,height=200, bg='lightgrey')
        self.top.pack(fill=X)

        self.bottom = Frame(master,height=500, bg='#03c6fc')
        self.bottom.pack(fill=X)

        self.entry_label = Entry(self.top, textvariable=self.searchValue)
        self.entry_label.place(x=140, y=90, width=100, height=25)

        self.type_category = Label(self.top, text="Type a category", font='arial 12 bold')
        self.type_category.place(x=0, y=90)
        self.button = Button(self.top, text='Press to search', font='arial 12 bold', command=self.categoryType)
        self.button.place(x=0, y=50)
        self.button = Button(self.top, text='Browse for toys', font='arial 12 bold', command=self.browseToys)
        self.button.place(x=0, y=10)
        self.productList = list()

        #self.my_img1 = PhotoImage(file="icons/ginger bread.png")
        #self.my_img1_label=Label(self.top, image=self.my_img1)
        #self.my_img1_label.place(x=300, y=20)

        #self.my_img2 = PhotoImage(file="icons/old car.png")
        #self.my_img2_label = Label(self.top, image=self.my_img2)
        #self.my_img2_label.place(x=400, y=20)

        #self.my_img3 = PhotoImage(file="icons/horse.png")
        #self.my_img3_label = Label(self.top, image=self.my_img3)
        #self.my_img3_label.place(x=500, y=20)

        self.soft_toy = Label(self.top,text="Soft Toy",font="arial 10 bold",)
        self.soft_toy.place(x=300,y=90)

        self.soft_toy = Label(self.top, text="Mechanical", font="arial 10 bold", )
        self.soft_toy.place(x=400, y=90)

        self.soft_toy = Label(self.top, text="Clay Toy", font="arial 10 bold", )
        self.soft_toy.place(x=500, y=90)

        self.productName=Label(self.bottom, text='Name',font='arial 12 bold',bg='lightblue', width=10, height=1, fg="blue" )
        self.productName.place(x=5, y=120)

        self.productPrice = Label(self.bottom, text='Price', font='arial 12 bold',bg='lightblue', width=10, height=1, fg= "blue")
        self.productPrice.place(x=5, y=160)

        self.productStock = Label(self.bottom, text='Stock', font='arial 12 bold', bg='lightblue', width=10, height=1,fg= "blue")
        self.productStock.place(x=5, y=200)

        self.productNameInfo = Label(self.bottom, text='_______', font='arial 12 bold', bg='lightblue', width=10, height=1, fg="blue")
        self.productNameInfo.place(x=100, y=120)

        self.productPriceInfo = Label(self.bottom, text='£______', font='arial 12 bold', bg='lightblue', width=10,
                                      height=1, fg="blue")
        self.productPriceInfo.place(x=100, y=160)

        self.productStockInfo = Label(self.bottom, text='_______', font='arial 12 bold', bg='lightblue', width=10,
                                     height=1, fg="blue")
        self.productStockInfo.place(x=100, y=200)

        self.selectProduct = Button(self.bottom, text='Select Product', font='arial 12 bold', width=12, height=2,
                                    fg="blue", command=self.select_product)
        self.selectProduct.place(x=230, y=150)

        self.button = Button(self.bottom, text='Next   ', font='arial 12 bold', width=10, height=1,
                             command=lambda: self.forward)
        self.button.place(x=200, y=50)

        self.button = Button(self.bottom, text='Previous', font='arial 12 bold', width=10, height=1,
                             command=lambda: self.back_button())
        self.button.place(x=30, y=50)

    def categoryType(self):
        self.counter = 0
        self.counterLength = 0
        file = open('stock.csv')
        reader = csv.reader(file)
        self.productList = list()

        for row in reader:
            if self.searchValue.get() == row[0]:
                print(row)
                self.productList.append(row[3])
                print(self.productList)

        self.counterLength = int(len(self.productList))

        file = open('stock.csv')
        reader = csv.reader(file)

        for row in reader:

            if self.productList[self.counter] == row[3]:
               self.productNameInfo.config(text=row[1])
               self.productPriceInfo.config(text=row[2])
               print(row[1])
               if int(row[4]) < 20:
                self.productStockInfo.config(text="Stock is low", bg="white")

               elif int(row[4]) > 20:
                    self.productStockInfo.config(text="In stock")
               elif int(row[4]) == 0:
                    self.productStockInfo.config(text="Out of stock")

    def select_product(self):
        self.productWindow = Toplevel(self.master)
        self.app = Product(self.productWindow)
        self.productCode=self.productList[self.counter]

    def browseToys(self):
        self.counter = 0
        self.counterLength = 0
        file = open('stock.csv')
        reader = csv.reader(file)
        self.productList = list()

        for row in reader:

            self.productList.append(row[1])
            print(self.productList)
        self.counterLength = int(len(self.productList))

        file = open('stock.csv')
        reader = csv.reader(file)
        for row_second in reader:
            if self.productList[self.counter] == row_second[1]:
                self.productNameInfo.config(text=row_second[1])
                self.productPriceInfo.config(text=row_second[2])
                if int(row_second[4]) < 20:
                    self.productStockInfo.config(text="Stock is low", bg="white")

                elif int(row_second[4]) > 20:
                    self.productStockInfo.config(text="In stock")
                elif int(row_second[4]) == 0:
                    self.productStockInfo.config(text="Out of stock")

class Product(Application):
    def __init__(self, master):
        self.master = master
        self.master.title("Product  Details")
        self.master.geometry('700x500+350+200')
        self.top = Frame(master, height=200, bg='#03c6fc')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='lightgrey')
        self.bottom.pack(fill=X)

        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.menu_bar.add_command(label='Exit', command=self.master.destroy, font="arial 10  bold")

        self.button = Button(self.top, text='Product Description', font='arial 12 bold', command="")
        self.button.place(x=0, y=150)

        self.leftFrame = Frame(self.bottom,height=300,width=200,bg='lightgreen')
        self.leftFrame.grid(row=0,column=0)

        self.middleFrame = Frame(self.bottom, height=300, width=200, bg='lightblue')
        self.middleFrame.grid(row=0, column=1)

        self.rightFrame = Frame(self.bottom, height=300, width=200, bg='gray')
        self.rightFrame.grid(row=0, column=2)

        self.descriptionInfo=Label(self.leftFrame,text='test')
        self.descriptionInfo.grid(row=0,column=0)

        self.prodPrice = StringVar()
        self.prodName = StringVar()
        self.category_type = StringVar()

        self.productName = Label(self.top, text='Name', font='arial 12 bold', bg='lightblue', width=10, height=1,
                                 fg="blue")
        self.productName.place(x=5, y=50)

        self.productPrice = Label(self.top, text='Price', font='arial 12 bold', bg='lightblue', width=10, height=1,
                                  fg="blue")
        self.productPrice.place(x=5, y=100)

        self.productNameInfo = Label(self.top, text='_______', font='arial 12 bold', bg='lightblue', width=10,
                                     height=1, fg="blue")
        self.productNameInfo.place(x=100, y=50)

        self.productPriceInfo = Label(self.top, text='£______', font='arial 12 bold', bg='lightblue', width=10,
                                      height=1, fg="blue")
        self.productPriceInfo.place(x=100, y=100)

        self.readReview = Button(self.top, text='Read Reviews', font='arial 12 bold', width=12, height=1,
                                    fg= "black", command="")
        self.readReview.place(x=210, y=150)

        self.writeReview = Button(self.top, text='Write Reviews', font='arial 12 bold', width=12, height=1,
                                 fg="black", command="")
        self.writeReview.place(x=380, y=150)
        self.counter = 0
        self.counterLength = 0
        file = open('stock.csv')
        reader = csv.reader(file)
        self.productList = list()
        self.productNamelist = list()
        self.productPricelist=list()
        self.productDescriptionlist=list()

        for row in reader:
            self.productList.append(row[3])
            self.productNamelist.append(row[1])
            self.productPricelist.append(row[2])
            self.productDescriptionlist.append(row[5])

        self.productCode = self.productList[self.counter]
        #if self.productCode == 7894:
        self.productNameInfo.config(text=self.productNamelist[0])
        self.productPriceInfo.config(text=self.productPricelist[0])
        self.descriptionInfo.config(text=self.productDescriptionlist[0])

#F3================================================================================================

class Basket(Home):
    def __init__(self, master, totalPrice = 0):
        self.master = master
        self.master.title("Basket")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(bg = "gray60")
        self.frame.configure(bg = "gray60")

        #The total price is encapsulated to stop the user changing the balance of what they have to pay
        self.__totalPrice = totalPrice
        
        self.header = Label(self.frame, text = "Basket", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0, pady = 20, columnspan = 2)

        self.stoframe0 = Frame(self.frame, width = 1000, height = 100, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe0.grid(row = 2, column = 0, pady = 2, padx = 2, columnspan = 2)
        self.stoframe = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe.grid(row = 1, column = 0, pady = 2, padx = 2)
        self.stoframe2 = Frame(self.frame, width = 1000, height = 200, bd = 5, relief = "ridge", bg = "gray60")
        self.stoframe2.grid(row = 1, column = 1, pady = 2, padx = 2)

        file = open('basket.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)

        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][2])
            print(self.__totalPrice)
            self.__totalPrice = self.__totalPrice + int(self.fileData[x][2])
        print("price is:",self.__totalPrice)


        self.priceLabel = Label(self.frame, text = "Total: £" + str(self.__totalPrice), font = ("arial", 25, "bold"), bd = 20, bg = "gray60", fg = "orange")
        self.priceLabel.grid(row = 3, column = 0, pady = 20, columnspan = 2)

        file = open('basket.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)

        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][1])
            print(self.fileData[x][1])


        self.userStockChoice = Listbox(self.stoframe)
        self.userStockChoice.grid(row = 0, column = 0)
        #This code is inserting the data to the list box for the first time of loading the window
        for x, y in enumerate(self.listOfData):
            self.userStockChoice.insert(x, y)

        self.updateButton = Button(self.stoframe0, text = "view", command = self.updateItem, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.updateButton.grid(row = 0, column = 0, padx = 5)

        self.DeleteButton = Button(self.stoframe0, text = "Delete", command = self.deleteItem, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.DeleteButton.grid(row = 0, column = 1, padx = 5)

        self.AddItemButton = Button(self.stoframe0, text = "Add Items", font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.AddItemButton.grid(row = 0, column = 2, padx = 5)

        self.PayButton = Button(self.stoframe0, text = "Pay", command = self.Proceed, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.PayButton.grid(row = 0, column = 3, padx = 5)

        self.backButton = Button(self.stoframe0, text = "Back", command = self.returnHome, font = ("arial", 15, "bold"), width = 10, height = 2, fg = "orange")
        self.backButton.grid(row = 0, column = 4, padx = 5)




        self.categoryLabel = Label(self.stoframe2, text = "Category:", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.categoryLabel.grid(row = 0, column = 0)

        self.nameLabel = Label(self.stoframe2, text = "Name:", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.nameLabel.grid(row = 1, column = 0)

        self.priceLabel = Label(self.stoframe2, text = "Price:", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.priceLabel.grid(row = 2, column = 0)

        self.codeLabel = Label(self.stoframe2, text = "Code:", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.codeLabel.grid(row = 3, column = 0)

        self.quantityLabel = Label(self.stoframe2, text = "Quantity:", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.quantityLabel.grid(row = 4, column = 0)


        self.categoryLabelData = Label(self.stoframe2, text = "--------", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.categoryLabelData.grid(row = 0, column = 1)

        self.nameLabelData = Label(self.stoframe2, text = "--------", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.nameLabelData.grid(row = 1, column = 1)

        self.priceLabelData = Label(self.stoframe2, text = "£xxxx", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.priceLabelData.grid(row = 2, column = 1)

        self.codeLabelData = Label(self.stoframe2, text = "----", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.codeLabelData.grid(row = 3, column = 1)

        self.quantityLabelData = Label(self.stoframe2, text = "xxx", bg = "gray60", fg = "orange", font = ("arial", 15, "bold"))
        self.quantityLabelData.grid(row = 4, column = 1)

        file = open('basket.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)

        self.listOfData = []
        stockQueryCounter = 0
        #If the stock is low while opening the window it will create a list and append all the product codes that are low on stock
        stockLowList = list()
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][1])
            stockQueryCounter = stockQueryCounter + 1


    
                
    def updateItem(self):
        #Below i have encased the block of code in an exception handler which was very useful while I was testing the code to see where i had an error occuring
        self.index = self.userStockChoice.curselection()[0]
        print(self.index)
        self.categoryLabelData.config(text = self.fileData[self.index][0])
        self.nameLabelData.config(text = self.fileData[self.index][1])
        self.priceLabelData.config(text = "£" + self.fileData[self.index][2])
        self.codeLabelData.config(text = self.fileData[self.index][3])
        self.quantityLabelData.config(text = self.fileData[self.index][4]) 


    def deleteItem(self):
        #Getting the list index from the where the user has pressed on an option from the listbox
        self.index = self.userStockChoice.curselection()[0]
        self.indexCode = str(self.fileData[self.index][3])
        print(self.indexCode)
        tempList = list()
        with open('basket.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                tempList.append(row)
                for field in row:
                    if field == self.indexCode:
                        tempList.remove(row)
        with open('basket.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(tempList)
        print("stock successfully deleted")
        file = open('basket.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)
        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][0])
            print(self.fileData[x][0])
        self.userStockChoice = Listbox(self.stoframe)
        self.userStockChoice.grid(row = 0, column = 0)
        #Inserting the data from listOfData in to the list box
        for x, y in enumerate(self.listOfData):
            self.userStockChoice.insert(x, y)

    
            
    def Proceed(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Payment(self.newWindow)
        

class Payment(Basket):
    def __init__(self, master):
        self.master = master
        self.master.title("Payment")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(bg = "blue")
        self.frame.configure(bg = "blue")

        self.billing = StringVar()

        #open basket csv file calculate pricee here and display
        
        self.header = Label(self.frame, text = "VISA CHECK", font = ("arial", 50, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 0, column = 0, pady = 20, columnspan = 2)

        self.billingLabel = Label(self.frame, text = "Shipping Address:", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 1, column = 0, pady = 5, columnspan = 1)

        self.billingLabel2 = Label(self.frame, text = "683 JEFFERSON STREET, TIBURON CA", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 1, column = 1, pady = 5, columnspan = 1)
        

        self.cardLabel = Label(self.frame, text = "Payment Method:", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 2, column = 0, pady = 1, columnspan = 1)

        self.cardLabel2 = Label(self.frame, text = "PAYPAL 868412", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 2, column = 1, pady = 1, columnspan = 1)

        self.discountLabel = Label(self.frame, text = "Discount:", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 3, column = 0, pady = 1, columnspan = 1)

        self.discountLabel2 = Label(self.frame, text = "£0.00", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 3, column = 1, pady = 1, columnspan = 1)

        self.totalLabel = Label(self.frame, text = "Total:", font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 4, column = 0, pady = 1, columnspan = 1)

        #insert cost calculation:
        file = open('basket.csv')
        reader = csv.reader(file)
        self.fileData = list(reader)
        self.__totalPrice = 0

        self.listOfData = []
        for x in list(range(0, len(self.fileData))):
            self.listOfData.append(self.fileData[x][2])
            print(self.__totalPrice)
            self.__totalPrice = self.__totalPrice + int(self.fileData[x][2])
        

        self.totalLabel2 = Label(self.frame, text = "£" + str(self.__totalPrice), font = ("arial", 20, "bold"), bd = 20, bg = "blue", fg = "white").grid(row = 4, column = 1, pady = 1, columnspan = 1)

        self.checkoutButton = Button(self.frame, text = "CHECKOUT", command = self.checkout, font = ("arial", 15, "bold"), width = 20, height = 2, fg = "black")
        self.checkoutButton.grid(row = 5, column = 0, pady = 5, columnspan = 2)

        self.cancelButton = Button(self.frame, text = "Cancel", command = self.master.destroy, font = ("arial", 15, "bold"), width = 20, height = 2, fg = "black")
        self.cancelButton.grid(row = 6, column = 0, pady = 5, columnspan = 2)


    def checkout(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = Order(self.newWindow)

        
class Order(Home):
    def __init__(self, master):
        self.master = master
        self.master.title("Order")
        self.master.geometry('1080x720+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(bg = "gray60")
        self.frame.configure(bg = "gray60")
            
        self.header = Label(self.frame, text = "Order Confirmation", font = ("arial", 50, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 0, column = 0, pady = 20, columnspan = 2)


        self.rand1 = str(random.randint(0,9))
        self.rand2 = str(random.randint(0,9))
        self.rand3 = str(random.randint(0,9))
        self.rand4 = str(random.randint(0,9))
        self.rand5 = str(random.randint(0,9))
        self.rand6 = str(random.randint(0,9))
        self.rand7 = str(random.randint(0,9))
        self.rand8 = str(random.randint(0,9))
        
        self.orderNumber = "AAT" + self.rand1 + self.rand2 + self.rand3 + self.rand4 + self.rand5 + self.rand6 + self.rand7 + self.rand8

        self.orderLabel = Label(self.frame, text = self.orderNumber, font = ("arial", 20, "bold"), bd = 20, bg = "gray60", fg = "orange").grid(row = 1, column = 0, pady = 5, columnspan = 2)

        self.finishButton = Button(self.frame, text = "FINISH", command = self.returnHome, font = ("arial", 15, "bold"), width = 20, height = 2, fg = "black")
        self.finishButton.grid(row = 2, column = 0, pady = 5, columnspan = 2)
            


        
#if __name__ == '__main__':
    #The main program function is run from this code block
main()



























    
