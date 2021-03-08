# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel,  QLineEdit, QPushButton
from validaDoc import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        # Cálculo dos digitos do CPF:

        texto = self.lineEdit.text()
        #print(f"Texto:{texto}")
        numeralAchado = find_numbers(texto)

        for i in range(0, len(numeralAchado)): 
            numeralAchado[i] = int(numeralAchado[i])
        checagem = validaCPF(numeralAchado)
       
        # Trazendo o cálculo para o Label 03:
        if texto:
            self.label_3.setText(f"{checagem[0]}\n{checagem[1]}\n{checagem[2]}\n{checagem [3]}" )
            
        else:
            self.label_3.setText("Digite o numeral novamente.")
    
# Fim da definição de click

    
#Fim das minhas definições
    
#Nova Mudança

def find_numbers(string):
    hit_list = [i[1] for i in enumerate(string) if i[1].isdigit()]
    return hit_list
# Calcula o algoritmo do CPF

def validaCPF(numero):
    ListaKeyDicionarios = [ 'd0', 'd1' , 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10']
    CPF_dictionary = dict(zip(ListaKeyDicionarios, numero))
    Modificadores_01 = CPF_dictionary
    Modificadores_02 = CPF_dictionary
    
    if ( (CPF_dictionary['d0'] == CPF_dictionary['d1']) and (CPF_dictionary['d0'] == CPF_dictionary['d2'] )
        and (CPF_dictionary['d0']  == CPF_dictionary['d3']) and (CPF_dictionary['d0'] == CPF_dictionary['d4']) 
        and (CPF_dictionary['d0'] == CPF_dictionary['d5']) and (CPF_dictionary['d0'] == CPF_dictionary['d6'] )
        and (CPF_dictionary['d0'] == CPF_dictionary['d7']) and (CPF_dictionary['d0'] == CPF_dictionary['d8'] )
        and (CPF_dictionary['d0'] == CPF_dictionary['d9']) and (CPF_dictionary['d0'] == CPF_dictionary['d10']) ):
            Confirma_01 = "Número Inválido!"
            return Confirma_01 ,  Confirma_01,  Confirma_01,  Confirma_01
    else:
# Cálculo para o Primeiro Digito Verificador:
#  d0 = d0 * 1
#  d1 = d1 * 2
#  d2 = d2 * 3
#  d3 = d3 * 4
#  d4 = d4 * 5
#  d5 = d5 * 6
#  d6 = d6 * 7
#  d7 = d7 * 8
#  d8 = d8 * 9
        soma = 0
        multiplicador = 1
        for chave, valor in Modificadores_01.items():
            if (chave != 'd9' and chave != 'd10'):
                valor = valor * multiplicador
                multiplicador += 1
                soma += valor
        resto = soma % 11
        #print(f"Resto:{resto}")
        primeiroDigitoVerificador = resto
        if ( primeiroDigitoVerificador == CPF_dictionary['d9']):
            Confirma_01 = "Valor do Primeiro Digito Verificador Confirmado."
            #print( Confirma_01)
        else:
            Confirma_01 = "Valor do Primeiro Digito Verificador Não-Confirmado."
            #print(Confirma_01)
 
  # Cálculo para o Segundo Digito Verificador:
#  d0 = d0 * 0
#  d1 = d1 * 1
#  d2 = d2 * 2
#  d3 = d3 * 3
#  d4 = d4 * 4
#  d5 = d5 * 5
#  d6 = d6 * 6
#  d7 = d7 * 7
#  d8 = d8 * 8
#  d9 = primeiroDigitoVerificador * 9
        soma_02 = 0
        multiplicador_02 = 1
        for chave_02, valor_02 in Modificadores_02.items():
            if (chave_02 != 'd0' and chave_02 != 'd10'):
                valor_02 *= multiplicador_02
                multiplicador_02 += 1
                soma_02 += valor_02
        resto = soma_02 % 11
        #print(f"Resto:{resto}")
        SegundoDigitoVerificador = resto
        if ( SegundoDigitoVerificador == CPF_dictionary['d10']):
            Confirma_02 = "Valor do Segundo Digito Verificador Confirmado."
            #print(Confirma_02)
        else:
            Confirma_02 = "Valor do Segundo Digito Verificador Não-Confirmado."
            #print(Confirma_02)
 # Verificando o Estado com o 9 digito verificador:
        if ( CPF_dictionary['d8'] == 1 ):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "DF-GO-MS-MT-TO"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 2):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "AC-AM-AP-PA-RO-RR"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 3):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "CE-MA-PI"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 4):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "AL-PB-PE-RN"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 5):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "BA-SE"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 6):
            Oriundo = "O CPF é oriundo do seguinte Estado:"
            Estados = "MG"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 7):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "ES-RJ"
            #print(f"{Oriundo} : {Estados}")
        elif ( CPF_dictionary['d8'] == 8):
            Oriundo = "O CPF é oriundo do seguinte Estado:"
            Estados = "SP"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 9):
            Oriundo = "O CPF é oriundo de um dos seguintes Estados:"
            Estados = "PR-SC"
            #print(f"{Oriundo}  {Estados}")
        elif ( CPF_dictionary['d8'] == 0):
            Oriundo = "O CPF é oriundo do seguinte Estado:"
            Estados = "RS"
            #print(f"{Oriundo}  {Estados}")
    return Confirma_01,  Confirma_02,  Oriundo,  Estados

#Fim da Nova Mudança

if __name__ == "__main__":
   
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    #ui.showFullScreen()
    ui.show()
       
    sys.exit(app.exec_())
