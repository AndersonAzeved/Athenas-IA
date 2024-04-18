import cv2
import pytesseract
import re
from validate_docbr import CPF

def pegarCpfImagem(imagem_path):
    imagem = cv2.imread(imagem_path)

    if imagem is None:
        return("Erro ao carregar a imagem")
    else:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

        imagem_sem_ruido = cv2.medianBlur(imagem_binaria, 1)

        alpha = 1.5  
        beta = 50    
        imagem_processada = cv2.convertScaleAbs(imagem_sem_ruido, alpha=alpha, beta=beta)

        texto_encontrado = pytesseract.image_to_string(imagem_processada)

        cpf = re.findall(r'\d{3}.\d{3}.\d{3}-\d{2}', texto_encontrado)
        
        if cpf == '':
            return 'Não possível reconhecer cpf'
        return cpf
        

def validaCpf(cpf):
    useCpf = CPF()
    return useCpf.validate(cpf)