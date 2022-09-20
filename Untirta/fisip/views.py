from django.shortcuts import render

# Create your views here.
def indexfisip(request):
    judul = "SEJARAH"
    tentang = "Pada tanggal 10 Juni 2003 dikeluarkan Surat Keputusan dari DIRJEN DIKTI DEPDIKNAS dengan nomor 1179/D/ T/2003 tentang izin operasional program studi Ilmu Administrasi Negara dan Ilmu Komunikasi, seiring dengan operasional program studi maka Fakultas Ilmu Sosial dan Ilmu Politik didirikan pada tahun akademik 2002/2003  yang mendapat legitimasi menjadi bagian dari Untirta dengan surat keputusan nomor 124/0/2004 sesuai dengan SOTK. Adapun jurusannya yaitu ilmu pemerintahan, administrasi pblik, dan ilmu komunikasi"

    konteks={
        'title': judul,
        'penjelasan': tentang,
    }
    
    return render(request, 'index-fisip.html', konteks)