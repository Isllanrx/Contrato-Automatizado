# CRIADO POR ISLLAN TOSO PEREIRA #########|
#PROJETO DE AUTOMATIZACAO DE CONTRATO ####|
##########################################|

import tkinter as tk
import textwrap
from tkinter import messagebox
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfFileWriter

# CRIACAO DA INTERFACE:
class ContratoCarro:
    def __init__(self, root):
        self.root = root
        self.root.title("Contrato Paulo Veiculos")

        self.create_widgets()
        # TAMANHO DA INTERFACE COM TITULO:
    def create_widgets(self):
        
        self.label_frame = tk.LabelFrame(self.root, text="Dados Cadastrais")
        self.label_frame.pack(padx=40, pady=20)

        #TODOS OS CAMPOS COM OS DEVIDOS NOMES:
        fields = ["Nome", "CPF","RG", "Telefone", "N°", "Rua", "Bairro", "Cidade", "Veiculo/ano", "Placa do Carro", "Renavam do Carro","Condicao", "Valor Final","Km Atual", "Dia de Venda"]
        
        self.entries = {field: tk.Entry(self.label_frame) for field in fields}
                   
        for i, field in enumerate(fields):
            tk.Label(self.label_frame, text=f"{field}:").grid(row=i, column=0, padx=10, pady=5)
            self.entries[field].grid(row=i, column=2, padx=10, pady=5)

        self.generate_button = tk.Button(self.root, text="Gerar Contrato em PDF", command=self.generate_pdf)
        self.generate_button.pack(pady= 20)
       
    # FUNCAO PARA GERAR O PDF:
    def generate_pdf(self):
        # Obtém os valores dos campos
        data = {field: self.entries[field].get() for field in self.entries}

        # Cria um PDF com as informações
        pdf_filename = "Contrato_Carro.pdf"
        pdf_canvas = canvas.Canvas(pdf_filename)

        
        # Adiciona informações do contrato em tópicos
        contract_text = self.generate_contract_text(data)
        pdf_canvas.setFont("Helvetica", 9)
        y_position = 800
        for line in contract_text.split('\n'):
            pdf_canvas.drawString(30, y_position, line)
            y_position -= 12

        pdf_canvas.save()
        messagebox.showinfo("PDF Gerado", f"Contrato gerado com sucesso")

    def generate_contract_text(self, data):
        
        # Texto do contrato com as cláusulas em tópicos
        contract_text = f"""
        CONTRATO DE COMPRA E VENDA
        
        IDENTIFICAÇÃO DAS PARTES CONTRATANTES
        VENDEDOR:
        - Nome completo: PAULO teste teste.
        - CNPJ: 00.000.006.0000-06.
        - Endereço: N° 00, Rua i, Bairro A, Cidade Vila Velha, Estado Espírito Santo, Brasil.

        COMPRADOR(A):
        - Nome: {data['Nome']}.
        - CPF: {data['CPF']}.
        - RG: {data['RG']}.
        - Endereço: N° {data['N°']}, Rua {data['Rua']}, Bairro {data['Bairro']}, Cidade {data['Cidade']}, Estado Espirito Santo, País Brasil.

        As partes abaixo qualificadas acordam um Contrato de Compra e Venda de Automóvel, regido pelas cláusulas 
        e condições descritas neste instrumento particular. Por meio deste instrumento, as partes estabelecem o que segue:

        CLÁUSULA 1ª - DO OBJETO: 
        - O objeto do presente contrato consiste na transação comercial de compra e venda do veículo {data['Veiculo/ano']} 
        devidamente identificado pela PLACA {data['Placa do Carro']} pelo RENAVAM {data['Renavam do Carro']}.

        CLÁUSULA 2ª - DA ENTREGA DE DOCUMENTOS: 
        - Constitui obrigação do vendedor a entrega do Documento Único de Transferência (DUT), devidamente assinado 
        e com firma reconhecida, ao comprador.

        CLÁUSULA 3ª - DA ENTREGA DO AUTOMÓVEL: 
        - É de responsabilidade do vendedor entregar o automóvel ao comprador, isento de quaisquer ônus ou encargos.

        CLÁUSULA 4ª - DOS IMPOSTOS E TAXAS: 
        - Após a assinatura deste instrumento, caberá ao comprador a responsabilidade pelo pagamento dos impostos e 
        taxas incidentes sobre o automóvel.
        
        CLÁUSULA 5ª - DO PREÇO: O comprador pagou no veículo {data['Veiculo/ano']} com {data['Condicao']}
        Totalizando o valor do veículo {data['Valor Final']}.
        
        CLÁUSULA 6ª - DO ESTADO DO VEÍCULO: O veículo é adquirido no estado em que se encontra, sem qualquer garantia 
        implícita ou explícita quanto ao seu estado de conservação ou funcionamento. O presente contrato entra em vigor 
        a partir da assinatura das partes envolvidas, estendendo-se aos herdeiros e sucessores das mesmas.

        CLÁUSULA 7ª - DA EXCLUSÃO DA GARANTIA: Todos os elementos relacionados ao acabamento do veículo 
        (tais como estofamentos, forrações, pintura e para-choques), além da caixa de direção e seus componentes, 
        o sistema de ar-condicionado, peças e componentes elétricos, e os pneus, exceto aqueles cuja condição possa ser 
        facilmente verificada por um leigo, estão excluídos da garantia. Ademais, o comprador expressamente concorda com o 
        atual estado em que se encontra o veículo.
        
        CLÁUSULA 8ª - DA GARANTIA: A loja Paulo Veículos assume a responsabilidade pelo reparo do veículo, caso ocorra 
        algum problema no motor ou na caixa durante um período de 90 dias ou 3 mil quilometro, contados a partir da 
        data de assinatura deste contrato.
        
        CLÁUSULA 9ª - DA INSTALAÇÃO DE KIT GNV: Caso o proprietário decida instalar um kit GNV, fica entendido 
        que a garantia mencionada anteriormente é totalmente invalidada para o veículo.
        
        CLÁUSULA 10ª - DA CONFIRMAÇÃO DO CONTRATO: Para que este contrato seja válido, é imprescindível que ambas as 
        partes estejam de acordo com os termos e condições financeiras, bem como com a garantia do motor e da caixa pelo 
        prazo de 90 dias ou 3 mil quilometro. Ademais, a quilometragem atual do veículo é de {data['Km Atual']}. 
        
        CLÁUSULA 11ª - DA DUPLICIDADE DO CONTRATO: As partes acordam em assinar o presente contrato em duas vias idênticas.
        
        As partes, reconhecendo a equidade das condições aqui estipuladas, firmam o presente instrumento em duas vias de igual 
        teor e forma, na cidade de Vila Velha {data['Dia de Venda']}.
        

        
        ASSINATURA DO VENDEDOR------------------------ASSINATURA DO COMPRADOR
        TELEFONE: +5527 9.0000-0000.----------------------TELEFONE: {data['Telefone']}.
        
        """
        formatted_contract_text = textwrap.dedent(contract_text)
        return formatted_contract_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ContratoCarro(root)
    root.mainloop()