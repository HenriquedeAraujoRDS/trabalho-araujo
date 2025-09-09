#abra a pasta e instale a biblioteca
#pip install qrcode[pil]
import qrcode

#entrada do usuario
link=input("link ou texto para qrcode: ")

#criando o qrcode
qr = qrcode.qrcode(
    version=1, #tamanho do qrcode
    error correction=qrcode.constants.error correct_L,
    box_size=10, #tamanho de cada quadrinho
    border=4, #espesura da borda
)

qr.add_data(link)
qr.make(fit=True)

#criar a imagem
img = qr.make_image(fill_color="black" , back_color="White")

#salvar o arquivo
img = qr.save("qrcode.png")
print("QR code gerado: 'qrcode.png'")