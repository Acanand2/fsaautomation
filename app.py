from flask import Flask, render_template, request

application = Flask(__name__)


def start(c):
    if c == '0':
        fsa = 0
    elif c == '1':
        fsa = 1
    else:
        fsa = -1
    return fsa


def state1(c):
    if c == '0':
        fsa = 2
    elif c == '1':
        fsa = 3
    else:
        fsa = -1
    return fsa


def state2(c):
    if c == '0':
        fsa = 4
    elif c == '1':
        fsa = 3
    else:
        fsa = -1
    return fsa


def state3(c):
    if c == '0':
        fsa = 0
    elif c == '1':
        fsa = 4
    else:
        fsa = -1
    return fsa


def state4(c):
    if c == '0':
        fsa = 3
    elif c == '1':
        fsa = 4
    else:
        fsa = -1
    return fsa


def isBinary(string):
    for c in string:
        if c != '0' and c != '1':
            return False
    return True

def isDecimal(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    

def decimalToBinary(decimal):
    binary = bin(decimal)[2:]
    return binary

def get_image(fsa):
    if fsa == 0:
        return ("Mawar resize.jpeg", "Bunga mawar dikenal sebagai simbol sebagai cinta dan kasih sayang. Namun, arti bunga mawar ini bisa berbeda, tergantung pada warna dan budaya, khususnya mawar merah, dikenal sebagai simbol romansa, cinta, dan kasih sayang.")
    elif fsa == 1:
        return ("Anggrek resize.jpeg", "Bunga anggrek putih seringkali dianggap sebagai simbol kemurnian serta kepolosan. Kamu bisa memberikan anggrek putih sebagai bentuk rasa hormat, penghargaan atau penghormatan.")
    elif fsa == 2:
        return ("Matahari resize.jpeg", "Selain kesetiaan, bunga matahari juga memiliki simbol kehidupan. Bunga matahari melambangkan energi pemberi kehidupan yang ditemukan di alam.")
    elif fsa == 3:
        return ("Higanbana resize.jpeg", "Higanbana berasal dari kata higan yang berarti 'pantai yang lain'. Kata ini diartikan sebagai alam baka, tempat berkumpulnya roh-roh yang sudah meninggalkan dunia manusia.")
    elif fsa == 4:
        return ("Telang resize.jpeg", "Bunga telang mengandung bioflavonoid dan anthocyanin, senyawa yang dikenal untuk meningkatkan sirkulasi darah di kepala dan dapat menjaga kesehatan kulit kepala serta mampu mengatasi kerontokan rambut serta mengurangi munculnya uban.")
    else:
        return ("", "")


def allStateBinary(string):
    length = len(string)
    fsa = start(string[0])  # Memulai dengan state awal berdasarkan input pertama
    images = [get_image(fsa)]  # Menambahkan gambar state awal ke dalam list
    for i in range(1, length):  # Dimulai dari indeks 1 karena state awal sudah ditambahkan sebelumnya
        if fsa == -1:
            return []
        elif fsa == 1:
            fsa = state1(string[i])
        elif fsa == 2:
            fsa = state2(string[i])
        elif fsa == 3:
            fsa = state3(string[i])
        elif fsa == 4:
            fsa = state4(string[i])
        images.append(get_image(fsa))
    return images




@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_string = request.form['input_string']
        input_type = request.form['input_type']

        if input_type == 'binary':
            if not isBinary(input_string):
                result = "Input tidak valid karena bukan bilangan biner"
                image = ""
            else:
                result = ""
                images = allStateBinary(input_string)
                if images:
                    image = images[-1]  # Mengambil gambar terakhir dari list
                else:
                    image = ""
            
        elif input_type == 'decimal':
            if not isDecimal(input_string):
                result = "Input tidak valid karena bukan bilangan decimal"
                image = ""
            else:
                binary = decimalToBinary(int(input_string))
                result = f"Biner: {binary}"
                images = allStateBinary(binary)
                if images:
                    image = images[-1]  # Mengambil gambar terakhir dari list
                else:
                    image = ""        
        
        else:
            result = ""
            image = ""

        return render_template('index.html', result=result, image=image)
    else:
        return render_template('index.html', result='', image='')



if __name__ == '__main__':
    application.run(debug=True)



