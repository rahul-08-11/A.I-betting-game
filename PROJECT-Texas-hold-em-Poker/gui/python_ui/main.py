import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QStackedWidget


from gamescreenupdate import GameScreenOperation
from mainscreenupdates import MainScreenOperation


user_selected_bot_and_amount=[]
won_or_lost=[]

class MainScreen(QMainWindow,MainScreenOperation):
    def __init__(self):
        super(MainScreen,self).__init__()
        loadUi("mainscreen.ui",self)
        self.startbettingbtn.clicked.connect(self.checking_for_valid_inputs)



    def checking_for_valid_inputs(self):
        self.update_wining()
        self._inputs_manupulation()
        self._gotoScreenTwo()

    def update_wining(self):
        winbalance=int(self.winamount.text())
        if True in won_or_lost:
            winbalance=winbalance+2*user_selected_bot_and_amount[1]
            self.winamount.setText(str(winbalance))

        elif False in won_or_lost:
            winbalance=winbalance-user_selected_bot_and_amount[1]
            self.winamount.setText(str(winbalance))
        user_selected_bot_and_amount.clear()
        won_or_lost.clear()   

          
    def _inputs_manupulation(self):
        bot_name=self.bot_selection_and_validation()
        bet_amount=self._updating_balance()
        user_selected_bot_and_amount.extend([bot_name,bet_amount])
        
    def _gotoScreenTwo(self):
        screen2=ScreenTwo()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ScreenTwo(QMainWindow,GameScreenOperation):
    label_of_bot=None

    def __init__(self):
        super(ScreenTwo,self).__init__()
        loadUi("gamescreen.ui",self)

        self.beginbtn.clicked.connect(self._winner)
        self.betagainbtn.clicked.connect(self._outputmanipulation)

    def _outputmanipulation(self):

        self.label_of_bot.setStyleSheet("background-color: white")
        self._gotoMainWindow()
    
    def _gotoMainWindow(self):
        Mainwindow=MainScreen()
        widget.addWidget(Mainwindow)
        widget.setCurrentIndex(widget.currentIndex()-1)

    def _winner(self):
        winner=self._finding_winner()
        bot_label={"A.I 1":self.a1label,"A.I 2":self.a2label,"A.I 3":self.a3label,"A.I 4":self.a4label}
        if winner in bot_label and user_selected_bot_and_amount[0]==winner:
            bot_label[winner].setStyleSheet("background-color: lightgreen")
            self.winnerboard.setText(f"Winner is {winner} bot!You've won your bet!Congratulation!")
            self.label_of_bot=bot_label[winner]
            won_or_lost.append(True)
        else:
            self.winnerboard.setText(f"Winner is {winner} bot!You've lost!")
            bot_label[winner].setStyleSheet("background-color: red")
            self.label_of_bot=bot_label[winner]
            won_or_lost.append(False)

app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainScreen()
gamescreen=ScreenTwo()
widget.addWidget(mainwindow)
widget.addWidget(gamescreen)
widget.setFixedHeight(599)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")