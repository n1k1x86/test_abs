class ATM():
    """
    The ATM class represents an automated teller machine that supports
    depositing and withdrawing money in specific nominals.

    Supported banknote denominations: 10, 50, 100, 200, and 500.
    """

    def __init__(self) -> None:
        """
        Initializes an empty ATM with zero banknotes of each denomination.

        :type banknotesTotal: List[int]: The count of banknotes of each denomination in the ATM.
        :type banknotesNominals: List[int]: The banknote denominations supported by the ATM.
        """
        self.banknotesTotal = [0,0,0,0,0]
        self.banknotesNominals = [10,50,100,200,500]

    def deposit(self, banknotesCount):
        """
        Deposite banknotes using banknotes list.

        :type banknotesCount: List[int]
        :rtype: None
        """
        for banknote_ind in range(len(banknotesCount)):
            self.banknotesTotal[banknote_ind] += banknotesCount[banknote_ind]
        
    def withdraw(self, amount):
        """
        Withdraw amount that you need, if it is impossible, method return [-1].

        :type amount: int
        :rtype: List[int]
        """
        banknotesWithdraw = [0 for _ in range(5)]

        if amount == 0:
            return banknotesWithdraw

        for ind in range(4, -1, -1):
            if self.banknotesNominals[ind] > amount:
                continue
            nominalAmount = amount // self.banknotesNominals[ind]
            if nominalAmount > self.banknotesTotal[ind]:
                nominalAmount = self.banknotesTotal[ind]
            banknotesWithdraw[ind] += nominalAmount
            amount -= nominalAmount * self.banknotesNominals[ind]

        if amount > 0:
            return [-1]
        
        for ind in range(len(banknotesWithdraw)):
            self.banknotesTotal[ind] -= banknotesWithdraw[ind]
        
        return banknotesWithdraw
    
if __name__ == '__main__':
    obj = ATM()

    obj.deposit([0,0,1,2,1])
    print(obj.withdraw(600))
    obj.deposit([0,1,0,1,1])
    print(obj.withdraw(600))
    print(obj.withdraw(550))