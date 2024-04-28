import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1,
                  error_corrrection = qrcode.constants.ERROR_CORRECT_H,
                  box_size = 10, border=4,)
qr.add_data("https://www.linkedin.com/in/mohammad-ali-sk-316508240/")
