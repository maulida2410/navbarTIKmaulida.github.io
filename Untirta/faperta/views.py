from django.shortcuts import render

def indexfaperta(request):
    judul = "FAKULTAS PERTANIAN"
    tentang = "Fakultas Pertanian Untirta didirikan pada tanggal 31 Agustus 1984. Sejalan dengan tuntutan masyarakat dan kebutuhan akan perlunya sarjana pertanian bergerak dalam bidang produksi pertanian, maka Faperta membuka jurusan baru yaitu jurusan Agronomi tahun akademik 2000/2002. Sekarang jurusannya terdiri dari: ilmpu perikanan, agribisnis, agreoteknologi, teknologi pangan. Almaatnya di Kampus Pakupatan"
    konteks = {
        'title': judul,
        'penjelasan': tentang,
    }
    return render(request, 'faperta.html', konteks)

