class BankAccount:
    def __init__(self):
        self.__balance = 0  # 잔액을 private으로 설정

    def deposit(self, amount): ##입금
        if amount > 0:
            self.__balance += amount 
            print(f"통장에 {amount}원이 입금되었습니다.")

    def withdraw(self, amount): ##출금
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"통장에서 {amount}원이 출금되었습니다.")
        else:
            print("잔액이 부족합니다.")

    def display_balance(self):## 잔약 표시
        print(f"현재 잔액: {self.__balance}원")


account = BankAccount()
account.withdraw(100)  #
account.deposit(10)
account.withdraw(100)
account.display_balance()
