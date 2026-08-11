from flask import Flask, render_template, request
from models import (
    RollerCoaster,
    WaterBoom,
    Bianglala,
    Pengunjung,
    Tiket
)
from exceptions import TiketException
import os


# Lokasi folder project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Konfigurasi Flask
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "tampilan"),
    static_folder=os.path.join(BASE_DIR, "wajah")
)


# Daftar wahana
wahana_list = [
    RollerCoaster("Roller Coaster", 25000, "Ekstrem"),
    WaterBoom("WaterBoom", 30000, "Air"),
    Bianglala("Bianglala", 20000, "Keluarga")
]


@app.route("/")
def index():
    return render_template("index.html", wahana=wahana_list)


@app.route("/pesan", methods=["GET", "POST"])
def pesan():

    if request.method == "POST":

        try:
            nama = request.form["nama"]
            gender = request.form["gender"]
            pilihan = request.form["wahana"]
            jumlah = int(request.form["jumlah"])

            # Validasi nama
            if not nama.strip():
                raise TiketException("Nama pengunjung harus diisi.")

            # Validasi jumlah tiket
            Tiket.validasi_jumlah(jumlah)

            # Mengambil wahana yang dipilih
            wahana = wahana_list[int(pilihan)]

            # Membuat object Pengunjung
            pengunjung = Pengunjung(nama, gender)

            # Membuat object Tiket
            tiket = Tiket(pengunjung, wahana, jumlah)

            # Menampilkan hasil tiket
            hasil = tiket.tampilkan_tiket()

            return render_template(
                "tiket.html",
                tiket=hasil
            )

        except TiketException as e:
            return render_template(
                "pesan.html",
                wahana=wahana_list,
                error=str(e)
            )

        except ValueError as e:
            return render_template(
                "pesan.html",
                wahana=wahana_list,
                error=str(e)
            )

        except Exception as e:
            return render_template(
                "pesan.html",
                wahana=wahana_list,
                error="Terjadi kesalahan pada sistem."
            )

    return render_template(
        "pesan.html",
        wahana=wahana_list
    )


if __name__ == "__main__":
    app.run(debug=True)