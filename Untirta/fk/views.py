from django.shortcuts import render

# Create your views here.
def indexfk(request):
    judul = "SEJARAH"
    tentang = "Fakultas Kedokteran UNTIRTA merupakan fakultas baru di universitas Sultan Ageng Tirtayasa yang terbentuk sejak program studi pendidikan dokter disahkan berdasarkan SK Menteri Riset Teknologi dan Pendidikan Tinggi Republik Indonesia Nomor 283/KPT/I/2019. Program studi Kedokteran Untirta saat ini dibawah pengampuan FK UI. Program Studi: Prodi Kedokteran, Prodi Keperawatan S1, Prodi Keperawatan D3, Prodi Ilmu Gizi, Prodi Ilmu Keolahragaan"

    konteks={
        'title': judul,
        'penjelasan': tentang,
    }
    return render(request, 'index-fk.html', konteks)