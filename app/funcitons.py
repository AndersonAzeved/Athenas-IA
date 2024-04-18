import cv2
import pytesseract
import re
from validate_docbr import CPF

def pegarCpfImagem(imagem_path):
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    if imagem is None:
        return("Erro ao carregar a imagem")
    else:
        imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
        imagem = cv2.medianBlur(imagem, 3)
        imagem = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)

        texto_encontrado = pytesseract.image_to_string(imagem)

        cpf = re.findall(r'\d{3}.\d{3}.\d{3}-\d{2}', texto_encontrado)
        
        return cpf
        

def validaCpf(cpf):
    useCpf = CPF()
    return useCpf.validate(cpf)