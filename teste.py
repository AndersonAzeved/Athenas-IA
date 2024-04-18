import cv2
import pytesseract
import re


imagem_path = 'cpf.png'
imagem = cv2.imread(imagem_path)

if imagem is None:
    print("Erro ao carregar a imagem")
else:
    print("Imagem carregada")
    
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

_, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

imagem_sem_ruido = cv2.medianBlur(imagem_binaria, 1)

alpha = 1.5  
beta = 50    
imagem_processada = cv2.convertScaleAbs(imagem_sem_ruido, alpha=alpha, beta=beta)
cv2.imwrite('imagem_pr.webp', imagem_processada)

recognized_text = pytesseract.image_to_string(imagem_processada)
print('Texto reconhecido:', recognized_text)

texto_filtrado = re.findall(r'\d{3}.\d{3}.\d{3}-\d{2}', recognized_text)
print(f'Texto Filtrado: {texto_filtrado}')

