from django.shortcuts import render

# Create your views here.
def indexfkip(request):
    judul = "SEJARAH"
    tentang = "Pada awal berdiri, Fakultas Keguruan dan Ilmu Pendidikan bermula dari STKIP dimana kegiatan perkuliahan dimulai pada 1 oktober 1982, yang terdiri dari 2 Prodi yaitu, Prodi IPPS-Pls dan Administrasi Pendidikan dengan jenjang pendidikan Sarjana (S.1)."

    konteks={
        'title': judul,
        'penjelasan': tentang,
    }
    return render(request, 'index-fkip.html', konteks)