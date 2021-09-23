# Super-Calculator
# To know more how to use this calculator, and to see what it can do please visit https://www.wolframalpha.com/examples/


from difflib import get_close_matches
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QWidget
from CalculatorGUI import *
import time
from PyQt5.QtCore import *
import wolframalpha
import math
import json
import requests
import urllib.request
from PIL import Image
try:
    from PyQt5 import sip
except ImportError:
    import sip
#     Add your own dictionary json file path (data.json)
data = json.load(open("/home/rawbeen/Desktop/Python/NEW PYQT5/data.json"))

sin = math.sin
cos = math.cos
tan = math.tan
arcsin = math.asin
arccos = math.acos
arctan = math.atan
LCM = math.lcm
HCF = math.gcd
sqrt = math.sqrt
deg = math.degrees
rad = math.radians
log = math.log10
ln = math.log
e = math.exp
REM = math.remainder
factorial = math.factorial


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton1.clicked.connect(self.action1)
        self.ui.pushButton2.clicked.connect(self.action2)
        self.ui.pushButton3.clicked.connect(self.action3)
        self.ui.pushButton4.clicked.connect(self.action4)
        self.ui.pushButton5.clicked.connect(self.action5)
        self.ui.pushButton6.clicked.connect(self.action6)
        self.ui.pushButton7.clicked.connect(self.action7)
        self.ui.pushButton8.clicked.connect(self.action8)
        self.ui.pushButton9.clicked.connect(self.action9)
        self.ui.pushButton0.clicked.connect(self.action0)
        self.ui.pushButton00.clicked.connect(self.action00)
        self.ui.pushButtonDecimal.clicked.connect(self.actionDecimal)
        self.ui.pushButtonPlus.clicked.connect(self.actionplus)
        self.ui.pushButtonMinus.clicked.connect(self.actionminus)
        self.ui.pushButtonMultiply.clicked.connect(self.actionmultiply)
        self.ui.pushButtonDivide.clicked.connect(self.actiondivide)
        self.ui.pushButtonCancel.clicked.connect(self.actioncancel)
        self.ui.pushButtonOpen.clicked.connect(self.actionopen)
        self.ui.pushButtonsin.clicked.connect(self.actionsin)
        self.ui.pushButtoncos.clicked.connect(self.actioncos)
        self.ui.pushButtontan.clicked.connect(self.actiontan)
        self.ui.pushButtonClose.clicked.connect(self.actionclose)
        self.ui.pushButtonsinInv.clicked.connect(self.actionsinInv)
        self.ui.pushButtoncosInv.clicked.connect(self.actioncosInv)
        self.ui.pushButtontanInv.clicked.connect(self.actiontanInv)
        self.ui.pushButtonpi.clicked.connect(self.actionpi)
        self.ui.pushButtonSqrt.clicked.connect(self.actionsqrt)
        self.ui.pushButtonCubeRoot.clicked.connect(self.actioncuberoot)
        self.ui.pushButtonDeg.clicked.connect(self.actiondeg)
        self.ui.pushButtonRad.clicked.connect(self.actionrad)
        self.ui.pushButtonlog.clicked.connect(self.actionlog)
        self.ui.pushButtonNaturalLog.clicked.connect(self.actionln)
        self.ui.pushButtonexp.clicked.connect(self.actionexponential)
        self.ui.pushButtonrem.clicked.connect(self.actionremainder)
        self.ui.pushButtonLCM.clicked.connect(self.actionLCM)
        self.ui.pushButtonHCF.clicked.connect(self.actionHCF)
        self.ui.pushButtoncomma.clicked.connect(self.actioncomma)
        self.ui.pushButtonpower.clicked.connect(self.actionpower)
        self.ui.pushButtonEXP.clicked.connect(self.actionexpconst)
        self.ui.pushButtonfactorial.clicked.connect(self.actionfactorial)
        self.ui.pushButtonIntegration.clicked.connect(self.actionIntegral)
        self.ui.pushButtonDerivative.clicked.connect(self.actionDerivative)
        self.ui.pushButtonDel.clicked.connect(self.actionDelete)
        self.ui.pushButtonEquals_3.clicked.connect(self.answer)
        self.ui.pushButtonEquals.clicked.connect(self.actionequals)
        self.ui.pushButtonGo.clicked.connect(self.go)
        self.ui.pushButtonGet.clicked.connect(self.get)

        self.ui.pushButtonStepWiseCalculus.clicked.connect(
            self.stepWiseCalculus)
        self.ui.pushButtonStepWiseAlgebra.clicked.connect(self.stepWiseAlgebra)
        self.ui.pushButtonStepWiseQueries.clicked.connect(self.stepWiseQueries)
        self.ui.pushButtonPlot.clicked.connect(self.plots)

    def keyPressEvent(self, event):
        keys = event.key()

        if keys == 48:
            self.action0()
        if keys == 49:
            self.action1()
        if keys == 50:
            self.action2()
        if keys == 51:
            self.action3()
        if keys == 52:
            self.action4()
        if keys == 53:
            self.action5()
        if keys == 54:
            self.action6()
        if keys == 55:
            self.action7()
        if keys == 56:
            self.action8()
        if keys == 57:
            self.action9()
        if keys == 43:
            self.actionplus()
        if keys == 95:
            self.actionminus()
        if keys == 42:
            self.actionmultiply()
        if keys == 63:
            self.actiondivide()
        if keys == Qt.Key_Space:
            self.actionequals()
        if keys == 16777220:
            self.actionequals()
        if keys == Qt.Key_Backspace:
            self.actionDelete()
        if keys == Qt.Key_Delete:
            self.actioncancel()
        if keys == Qt.Key_I:
            self.actionIntegral()
        if keys == Qt.Key_D:
            self.actionDerivative()
        if keys == Qt.Key_S:
            self.actionsin()
        if keys == Qt.Key_C:
            self.actioncos()
        if keys == Qt.Key_T:
            self.actiontan()
        if keys == Qt.Key_X:
            self.action00()
        if keys == Qt.Key_Comma:
            self.actioncomma()
        if keys == Qt.Key_Period:
            self.actionDecimal()
        if keys == 41:
            text = self.ui.lineEditDisplay.toPlainText()
            self.ui.lineEditDisplay.setText(text + ")")
        if keys == 40:
            text = self.ui.lineEditDisplay.toPlainText()
            self.ui.lineEditDisplay.setText(text + "(")

    def weather(self, city):
        try:
            api_address = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            url = api_address + city
            json_data = requests.get(url).json()
            kelvin_res = json_data["main"]["temp"]
            feels_like = json_data["main"]["feels_like"]
            description = json_data["weather"][0]["description"]
            celcius_res = kelvin_res - 273.15
            max_temp = json_data["main"]["temp_max"]
            min_temp = json_data["main"]["temp_min"]
            visibility = json_data["visibility"]
            pressure = json_data["main"]["pressure"]
            humidity = json_data["main"]["humidity"]
            wind_speed = json_data["wind"]["speed"]
            self.ui.lineEditDisplay.setText(
                f"The current temperature of {city} is {round(celcius_res, 2)} °C with {description}\n"
                f"maximum temperature: {round(max_temp-273.15, 2)} °C \nminimum temperature: {round(min_temp-273.15, 2)} °C\n"
                f"visibilty: {visibility}m\n"
                f"pressure: {pressure}\n"
                f"humidity: {humidity}\n"
                f"wind speed: {wind_speed}m/s")
        except KeyError:
            self.ui.lineEditDisplay.setText("Please check your city name")
        except:
            self.ui.lineEditDisplay.setText("Please check your input")

    def go(self):
        query = self.ui.textEditAsk.toPlainText()
        try:
            if "meaning of" in query:

                query = query.split(" ")
                indx = query.index("meaning")
                query = query[indx+2]
                keys = data.keys()
                close_words = get_close_matches(f"{query}", keys, cutoff=0.75)
                if query in data.keys():
                    result_list = (data[query])
                    Delimiter = " "
                    final_result = Delimiter.join(result_list)
                    self.ui.lineEditDisplay.setText(final_result)
                else:
                    self.ui.lineEditDisplay.setText(
                        f"sorry, can't find the meaning of {query} right now\n"
                        f"try searching for {close_words} instead")
            elif "weather of" in query:
                query = query.split()
                indx = query.index("weather")
                city = query[indx+2:]
                city = " ".join(city)
                self.weather(city)
            elif "temperature of" in query:
                indx = query.index("temperature of")
                city = query[indx+15:]
                city = "".join(city)
                self.weather(city)

            elif "weather in" in query:
                query = query.split()
                indx = query.index("weather")
                city = query[indx+2:]
                city = " ".join(city)
                self.weather(city)

            elif "find" in query or "solve" in query or "evaluate" in query or "calculate" in query or "value" in query or "convert" in query or "simplify" in query or "generate" in query:
        #  Please use your own API key.. you can get it from wolframalpha site.
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                query = query.split()[1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                answer = answer.replace("sqrt", "√")

                self.ui.lineEditDisplay.setText(answer)
            elif "who" in query or "what" in query or "how" in query or "when" in query:
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                answer = next(res.results).text
                answer = answer.replace("sqrt", "√")

                self.ui.lineEditDisplay.setText(answer)

                self.ui.lineEditDisplay.setText(answer)
            else:
                self.ui.lineEditDisplay.setText("Cannot perfom operation!\n"
                                                "Please use any of these keywords at the beginning(solve, find, calculate, evaluate, value)")

        except:
            self.ui.lineEditDisplay.setText(
                "Sorry cannot perfom operation! Check your input or try again later")

    def get(self):
        query = self.ui.textEditAsk.toPlainText()
        query = query.replace("+", "%2B")
        try:
            query = query.replace("+", "%2B")
            api_address = f"http://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&output=json&format=plaintext"
            json_data = requests.get(api_address).json()
            ans1 = json_data["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
            ans1 = ans1.replace("sqrt", "√")
            ans2 = json_data["queryresult"]["pods"][1]["subpods"][1]["plaintext"]
            ans2 = ans2.replace("sqrt", "√")
            self.ui.lineEditDisplay.setText(f"{ans1}\n {ans2}")
        except:
            pass

    def stepWiseCalculus(self):
        self.ui.lineEditDisplay.clear()
        query = self.ui.textEditAsk.toPlainText()
        query = query.replace("+", "%2B")
        try:
            try:
                api_address = f"https://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Step-by-step%20solution&output=json&format=plaintext"
                json_data = requests.get(api_address).json()
                answer = json_data["queryresult"]["pods"][0]["subpods"][1]["plaintext"]
                answer = answer.replace("integral", "∫")
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()
                self.ui.lineEditDisplay.setText(text + answer)
            except:
                pass
            try:
                api_address = f"http://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Result__Step-by-step+solution&format=plaintext&output=json"
                json_data = requests.get(api_address).json()
                answer = json_data["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
                answer = answer.replace("sqrt", "√")
                answer = answer.replace("integral", "∫")
                text = self.ui.lineEditDisplay.toPlainText()
                self.ui.lineEditDisplay.setText(text + answer)
            except:
                try:
                    answer = json_data["queryresult"]["pods"][1]["subpods"][1]["plaintext"]
                    answer = answer.replace("sqrt", "√")
                    answer = answer.replace("integral", "∫")
                    text = self.ui.lineEditDisplay.toPlainText()
                    self.ui.lineEditDisplay.setText(text+answer)

                except:
                    self.ui.lineEditDisplay.setText(
                        "Cannot find stepwise solution of this problem")
        except:
            self.ui.lineEditDisplay.setText(
                "Cannot find stepwise solution of this problem")

    def stepWiseAlgebra(self):
        self.ui.lineEditDisplay.clear()
        query = self.ui.textEditAsk.toPlainText()
        query = query.replace("+", "%2B")
        api_address = f"http://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Result__Step-by-step+solution&format=plaintext&output=json"
        json_data = requests.get(api_address).json()
        print(json_data)
        try:
            try:

                answer = json_data["queryresult"]["pods"][1]["subpods"][4]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()
                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass
            try:
                answer = json_data["queryresult"]["pods"][1]["subpods"][3]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()
                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass

            try:

                answer = json_data["queryresult"]["pods"][1]["subpods"][2]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass

            try:

                answer = json_data["queryresult"]["pods"][1]["subpods"][1]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass

            try:

                answer = json_data["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                self.ui.lineEditDisplay.setText(
                    "Cannot find stepwise solution of this problem")
        except:
            self.ui.lineEditDisplay.setText(
                "Cannot find stepwise solution of this problem")

    def stepWiseQueries(self):
        self.ui.lineEditDisplay.clear()
        query = self.ui.textEditAsk.toPlainText()
        query = query.replace("+", "%2B")
        api_address = f"http://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Result__Step-by-step+solution&format=plaintext&output=json"
        json_data = requests.get(api_address).json()
        try:
            try:
                answer = json_data["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass
            try:
                answer = json_data["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                pass
            try:
                answer = json_data["queryresult"]["pods"][1]["subpods"][1]["plaintext"]
                answer = answer.replace("sqrt", "√")
                text = self.ui.lineEditDisplay.toPlainText()

                self.ui.lineEditDisplay.setText(text+answer)
            except:
                self.ui.lineEditDisplay.setText(
                    "Cannot find stepwise solution of this problem")
        except:
            self.ui.lineEditDisplay.setText(
                "Cannot find stepwise solution of this problem")

    def plots(self):
        try:
            query = self.ui.textEditAsk.toPlainText()
            if "plot" in query or "parametric" in query or "polar plot" in query:
                self.ui.lineEditDisplay.clear()
                query = query.replace("+", "%2B")
                api_address = f"http://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Result__Step-by-step+solution&format=image&output=json"
                json_data = requests.get(api_address).json()
                img_src = json_data["queryresult"]["pods"][1]["subpods"][0]["img"]["src"]
                urllib.request.urlretrieve(img_src, "plot.png")
                img = Image.open("plot.png")
                img.show()
            else:
                self.ui.lineEditDisplay.setText(
                    "Cannot plot this graph! Check your input")

        except:
            self.ui.lineEditDisplay.setText("Cannot plot this graph")

    def action1(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "1")

    def action2(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "2")

    def action3(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "3")

    def action4(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "4")

    def action5(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "5")

    def action6(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "6")

    def action7(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "7")

    def action8(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "8")

    def action9(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "9")

    def action0(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "0")

    def action00(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "x")

    def actionDecimal(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + ".")

    def actionplus(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "+")

    def actionminus(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "-")

    def actionmultiply(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "*")

    def actiondivide(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "/")

    def actionfactorial(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "factorial(")

    def actioncancel(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.clear()

    def actionopen(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "(")

    def actionclose(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + ")")

    def actionsin(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "sin(")

    def actioncos(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "cos(")

    def actiontan(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "tan(")

    def actionsinInv(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "arcsin(")

    def actioncosInv(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "arcsin(")

    def actiontanInv(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "arctan(")

    def actionsqrt(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "sqrt(")

    def actioncuberoot(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "cubert(")

    def actionpi(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "3.14159")

    def actiondeg(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "deg(")

    def actionrad(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "rad(")

    def actionLCM(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "LCM(")

    def actionHCF(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "HCF")

    def actionlog(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "log(")

    def actionln(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "ln(")

    def actionexponential(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "e(")

    def actionpower(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "pow(")

    def actionremainder(self):
        self.ui.lineEditDisplay.clear()
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "REM(")

    def actioncomma(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + ",")

    def actionIntegral(self):
        try:
            x = self.ui.lineEditDisplay.toPlainText()
            inp = "find integration of" + x
            app_id = "Y98QH3-24PWX83VGA"
            client = wolframalpha.Client(app_id)
            indx = inp.split().index('find')
            inp = inp.split()[indx + 1:]
            res = client.query(' '.join(inp))
            text = next(res.results).text
            text = text.split()[1:]
            text = " ".join(text)
            self.ui.lineEditDisplay.setText(text.replace("constant", "c"))
        except:
            self.ui.lineEditDisplay.clear()

    def actionDerivative(self):
        x = self.ui.lineEditDisplay.toPlainText()
        inp = "find derivative of" + x
        app_id = "Y98QH3-24PWX83VGA"
        client = wolframalpha.Client(app_id)
        indx = inp.split().index('find')
        inp = inp.split()[indx + 1:]
        res = client.query(' '.join(inp))
        text = next(res.results).text
        self.ui.lineEditDisplay.setText(text)

    def actionDelete(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text[:len(text)-1])

    def answer(self):
        try:
            text = self.ui.lineEditDisplay.toPlainText()
            self.ui.lineEditDisplay.setText(text + str(ans))
        except:
            pass

    def actionexpconst(self):
        text = self.ui.lineEditDisplay.toPlainText()
        self.ui.lineEditDisplay.setText(text + "2.71828182845")

    def actionequals(self):
        text = self.ui.lineEditDisplay.toPlainText()
        global ans
        try:
            if len(self.ui.lineEditDisplay.toPlainText()) != 0:
                ans = eval(text)
                self.ui.lineEditDisplay.setText(str(ans))
            else:
                self.ui.lineEditDisplay.setText("")
        except ZeroDivisionError:
            self.ui.lineEditDisplay.setText("Math Error!\n"
                                            "Cannot divide by zero")
        except ValueError:
            self.ui.lineEditDisplay.setText("Math domain error!")
        except SyntaxError:
            self.ui.lineEditDisplay.setText("Syntax Error! Invalid Syntax")
        except:
            self.ui.lineEditDisplay.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
