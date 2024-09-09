class person:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

class User(person):
    def __init__(self,name,email,password,address,accountType):
        super().__init__(name,email,password)
        self.address=address
        self.accountType=accountType
        self.accountNo= self.name+self.email
        self.balance=0
        self.loan=0
        self.depositebal=0
        self.withdrawbal=0
    
    def deposite(self,amount,bank):
        if amount>0:
            self.balance=self.balance+amount
            self.depositebal=self.depositebal+amount
            bank.balance=bank.balance+amount
            print(f'Successfully deposite.')
    
    def withdraw(self,amount,bank):
        if bank.bankrupt==True:
            print(f'The bank is bankrupt.')
        elif amount>self.balance:
            print(f'You have not enough balance to withdraw.')
        else:
            self.balance=self.balance-amount
            self.withdrawbal=self.withdrawbal+amount
            bank.balance=bank.balance-amount
            print(f'Successfully withdraw.')
    
    def check_balance(self):
        print(f'Your account balance is {self.balance}')
    
    def History(self):
        print(f'Your Total Deposite Amount is {self.depositebal}')
        print(f'Your Total Withdraw Amount is {self.withdrawbal}')
    
    def take_loan(self,amount,bank):
        if bank.loan=='off':
            print(f'This bank can not give loan.')
        elif self.loan<2:
            self.balance=self.balance+amount
            bank.loan_amount=bank.loan_amount+amount
            self.loan=self.loan+1
            print(f'loan get successfully.')
        else:
            print(f'You can not get loan.')

    def tansfer(self,user,bank,amount):
        if bank.bankrupt==True:
            print(f'The bank is bankrupt.')
        elif user not in bank.accounts:
            print(f'This account is not exists.')
        elif amount>self.balance:
            print(f'Withdrawal amount exceeded')
        else:
            user.balance=user.balance+amount
            user.depositebal=user.depositebal+amount
            self.balance=self.balance-amount
            self.withdrawbal=self.withdrawbal+amount
            print(f'Transfer Successfully.')

class admin(person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    
    def delet_account(self,useraccno,bank):
        dell=False
        for acnt in bank.accounts:
            if acnt.accountNo==useraccno:
                bank.accounts.remove(acnt)
                dell=True
                print(f'account deleted successfully.')
        if dell==False:
            print(f'account does not exists.')
    
    def user_account_list(self,bank):
        if len(bank.accounts)>0:
            print(f'Account Lists:')
            for acnt in bank.accounts:
                print(f'User Name:{acnt.name},Account type:{acnt.accountType}')
        else:
            print(f'Have no account.')
    
    def available_balance(self,bank):
        print(f'The available balance of the Bank is :{bank.balance}')
    
    def loan_amount(self,bank):
        print(f'The Total loan amount is :{bank.loan_amount}')
    
    def change_loan_feather(self,bank,status):
        bank.loan=status
    
    def change_bank_status(self,bank,status):
        bank.bankrupt=status

class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
        self.balance=0
        self.loan_amount=0
        self.loan='on'
        self.bankrupt=False
        self.admin=None
    
    def create_account(self,name,email,password,address,accountType):
        user=User(name,email,password,address,accountType)
        self.accounts.append(user)
        print(f'account created successfully.')
    
    def create_admin(self,name,email,password):
        adm=admin(name,email,password)
        self.admin=adm
        print(f'Admin added successfully.')



def main_page():
    print(f'Main Page:')
    print(f'press 1 for sign up as a user')
    print(f'press 2 for sign up as a admin')
    print(f'press 3 for log in')
    print(f'press 4 for log out')

def login(bank):
    print(f'Please Log in')
    print(f'press 1 for user')
    print(f'press 2 for admin')
    op=int(input('Enter your option:'))
    u=None
    if op==1:
        ck=False
        e=input('Enter your email:')
        p=input('Enter your password:')
        for acc in bank.accounts:
            if acc.email==e and acc.password==p:
                ck=True
                u=acc
                print(f'Logged in successfully.')
                break
        if ck==False:
            main_page()
        else:
            print(f'1.Deposite Money')
            print(f'2.withdraw amount:')
            print(f'3.check balance')
            print(f'4.check transation history')
            print(f'5.take loan')
            print(f'6.transfer money')
            print(f'7.back to main page')
            while(True):
                opp=int(input('Enter the option:'))
                if opp==1:
                    amt=int(input('Enter the amount:'))
                    u.deposite(amt,bank)
                elif opp==2:
                    amt=int(input('Enter the amount:'))
                    u.withdraw(amt,bank)
                elif opp==3:
                    u.check_balance()
                elif opp==4:
                    u.History()
                elif opp==5:
                    amt=int(input('Enter the amount:'))
                    u.take_loan(amt,bank)
                elif opp==6:
                    accno=input('Enter the account number:')
                    amt=int(input('Enter the amount:'))
                    ck=False
                    for acc in bank.accounts:
                        if acc.accountNo==accno:
                            u.tansfer(acc,bank,amt)
                            ckk=True
                    if ck==False:
                        print(f'Account does not exist')
                else:
                    main_page()
                    break
    elif op==2:
        ck=False
        e=input('Enter your email:')
        p=input('Enter your password:')
        if bank.admin.email==e and bank.admin.password==p:
            u=bank.admin
            ck=True
            print(f'Admin Logged in successfully.')

        if ck==False:
            main_page()
        else:
            print(f'1.delete user account')
            print(f'2.see all user account')
            print(f'3.total balance of the bank:')
            print(f'4.total loan amount')
            print(f'5.change loan feature')
            print(f'6.back to main page')
            while(True):
                opp=int(input('Enter your option:'))
                if opp==1:
                    accno=input('Enter your account no:')
                    u.delet_account(accno,bank)
                elif opp==2:
                    u.user_account_list(bank)
                elif opp==3:
                    u.available_balance(bank)
                elif opp==4:
                    u.loan_amount(bank)
                elif opp==5:
                    status=input('Loan Feature (on/off):')
                    u.change_loan_feather(bank,status)
                else:
                    main_page()
                    break

def main():
    print(f'Main Function Started.........')
    bank=Bank('Sonali Bank Ltd')
    main_page()
    while(True):
        option=int(input('Enter the option:'))
        if option==1:
            # name,email,password,address,accountType
            n=input('Enter your name:')
            e=input('Enter your email:')
            p=input('Enter your password:')
            a=input('Enter your address:')
            at=input('Enter your account type:(Savings/Cuurent)')
            bank.create_account(n,e,p,a,at)
            login(bank)
        elif option==2:
            n=input('Enter your name:')
            e=input('Enter your email:')
            p=input('Enter your password:')
            bank.create_admin(n,e,p)
            login(bank)
        elif option==3:
            login(bank)
        else:
            break

if __name__=='__main__':
    main()
