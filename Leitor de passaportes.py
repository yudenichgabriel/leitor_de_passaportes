from PIL import Image 
import pytesseract
import textwrap

# Caminho da Biblioteca do pytesseract no OS Windows.
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Aqui é onde o caminho do passaporte deve estar, como o meu passaporte está na
# mesma pasta que o script, armazenei o nome dele como "doc.jpeg".
imagem = 'doc.jpeg'

# A variável "resultado" é a responsável por trazer o resultado da conversão de imagem
# da biblioteca pytesseract para "data".
resultado = pytesseract.image_to_data(Image.open(imagem))

# Aqui é onde o fatiamento para armazenar dados ocorre, parte dos passaportes 
# brasileiros iniciam com a sigra do país, neste caso BRA seria de Brasil.

locA = resultado.find('<BRA') 

locB = locA + 48 

locA = locA + 4 

# Logo após, temos a variável "line_result" que nos dará o resultado dos itens dentro do fatiamento
# das variáveis locA e locB

line_result = resultado[locA:locB]

# O resultado parcial me deu uma boa ideia do que estava sendo fatiado e 
# é mostrado no console, seguindo a ideia dos caracteres "especiais" serem 
# retirados para exibição

resultado_parcial = line_result.replace('<', ' ').replace('¢', ' ').replace('�', ' ')
print(resultado_parcial) # Resultado do console

# Com o fatiamento bem exercido, o que é mostrado no console nos dá uma ideia 
# de conseguir fatiar os sobrenomes e os nomes separadamente para um melhor 
# resultado e melhor entrega de dados para uma plataforma
sobrenome_localization = resultado_parcial.find('  ')
sobrenome_parcial = resultado_parcial[:sobrenome_localization]
nome_parcial = resultado_parcial[sobrenome_localization:].replace("4", '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')

# E então o código é finalizado trazendo os dados do passaporte em imagem para texto e entregando efetivamente
# completando sua missão...
print(textwrap.dedent('Nome: "{}"'.format(nome_parcial)))
print('Sobrenome: "{}"'.format(sobrenome_parcial))
