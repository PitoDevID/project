from django.db import models

class Barang(models.Model):
    kode_barang = models.CharField(max_length=8)
    nama_barang = models.CharField(max_length=75)
    stok_barang = models.IntegerField()
    harga_barang = models.BigIntegerField()
    link_gambar = models.TextField(max_length=150, blank=True)
    tgl_input = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nama_barang
    
class Jenis(models.Model):
    nama = models.CharField(max_length=78)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama