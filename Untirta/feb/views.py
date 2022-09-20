from django.shortcuts import render

# Create your views here.
def indexfeb(request):
    judul = "SEJARAH"
    tentang = "Pada tahun 1986, dengan dukungan para ulama dan tokoh masyarakat pada saat itu, seperti; Surjadi Sudirja, Tubagus M. Rais, Dorojatun Kuncoro Jakti, Tungki Ariwibowo, dan Sudarmono, pengembangan selanjutnya dilakukan untuk mendirikan Fakultas Ekonomi. Adapun jurusannya pada saat ini terdiri dari : DIII akuntansi, manajemen pemasaran, perpajakan, ekonomi pembangunan, manajemen, ekonomi syariah, keuangan perbankan, akuntansi "

    konteks={
        'title': judul,
        'penjelasan': tentang,
    }
    return render(request, 'index-feb.html', konteks)