from django.shortcuts import render

def indexuniversitas(request):
    judul = "Tentang"
    tentang = " Universitas Sultan Ageng Tirtayasa disingkat Untirta, adalah PTN (Perguruan Tinggi Negeri) yang terdapat di Provinsi Banten, Indonesia. Dengan kampus utama di Serang, kampus Fakultas Teknik yang berada di Cilegon dan Fakultas Keguruan yang berada di Ciwaru."

    konteks={
        'title': judul,
        'penjelasan': tentang,
    }

    return render(request, 'univ.html', konteks)
