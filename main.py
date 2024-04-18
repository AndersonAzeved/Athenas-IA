import cv2
import pytesseract

# Carregar a imagem
image = cv2.imread('cpf.webp')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar thresholding para binarizar a imagem
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Opcional: Aplicar operações morfológicas para melhorar o reconhecimento
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Salvar a imagem processada (opcional, apenas para verificação)
cv2.imwrite('imagem_processada.webp', processed_image)

# Usar pytesseract para reconhecer texto na imagem processada
recognized_text = pytesseract.image_to_string(processed_image)

print('Texto reconhecido:', recognized_text)

