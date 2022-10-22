from errorclass import BotSelectionError,AmountError,BalanceLimit

class MainScreenOperation():

    def bot_selection_and_validation(self): 
        checkboxes_with_bots={
            "A.I 1":self.a1checkbox.isChecked(),
            "A.I 2":self.a2checkbox.isChecked(),
            "A.I 3":self.a3checkbox.isChecked(),
            "A.I 4":self.a4checkbox.isChecked()
        }

        list_of_checkbox_truthy_falsy=list(checkboxes_with_bots.values())
        list_of_bot_names=list(checkboxes_with_bots.keys())


        if list_of_checkbox_truthy_falsy.count(True)==1:
            truth_at_index=list_of_checkbox_truthy_falsy.index(True)
            bot_name=list_of_bot_names[truth_at_index]
            botname=bot_name
            # self._updating_balance()
            return bot_name
        else:
            raise BotSelectionError("Please select one bot to start betting.")


    def _updating_balance(self):
        balance=int(self.balanceamount.text())
        bet_amount=int(self.inputbetamount.text())
        if bet_amount<100:
            raise AmountError("Betting Amount should be greater than 200$.")
        elif bet_amount >balance:
            raise BalanceLimit("Please check your account balance and try again.")
        else:
            balance=balance-bet_amount
            self.balanceamount.setText(str(balance))
           
        return bet_amount





        
    




            
            


        
