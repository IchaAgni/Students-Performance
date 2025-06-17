# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
### Latar Belakang Bisnis
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat juga jumlah siswa yang cukup signifikan tidak menyelesaikan pendidikannya alias dropout.

Tingginya angka *dropout* menjadi masalah serius karena dapat memengaruhi citra dan kualitas akademik institusi. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secara dini siswa-siswa yang berpotensi mengalami *dropout*, sehingga dapat diberikan bimbingan dan intervensi yang tepat.

Dalam rangka mendukung pengambilan keputusan yang lebih baik dan berbasis data, pihak institusi ingin memanfaatkan teknologi data science dan visualisasi data dalam bentuk **dashboard pemantauan performa siswa**. Dengan adanya dashboard ini, pihak manajemen dan tenaga pengajar dapat lebih mudah memantau perkembangan siswa, mengenali pola-pola *dropout*, dan melakukan tindakan preventif.

### Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang ingin diselesaikan:

1. Tingginya Angka Dropout
    Banyak siswa tidak menyelesaikan pendidikannya, yang berdampak buruk pada reputasi dan kualitas akademik institusi.
2. Kebutuhan Deteksi Dini Siswa Berisiko Dropout
    Institusi ingin mengetahui lebih awal siswa-siswa yang berpotensi dropout agar bisa dilakukan intervensi.
3. Kurangnya Sistem Pemantauan Berbasis Data
    Saat ini belum tersedia alat berbasis data yang efektif untuk memantau performa siswa secara menyeluruh dan real-time.
4. Kebutuhan Pengambilan Keputusan yang Cepat dan Tepat
    Manajemen dan tenaga pengajar membutuhkan informasi yang mudah dipahami agar bisa mengambil langkah preventif dengan cepat.
5. Minimnya Visualisasi Data
    Informasi penting masih dalam bentuk mentah, tidak disajikan dalam visualisasi yang mudah dipahami oleh staf non-teknis.

### Cakupan Proyek
Proyek ini bertujuan untuk membantu **Jaya Jaya Institut** dalam menurunkan tingkat *dropout* siswa melalui pendekatan berbasis data dan visualisasi interaktif. Cakupan proyek difokuskan pada pemanfaatan data performa siswa, analisis prediktif, serta pengembangan dashboard pemantauan performa yang informatif dan mudah digunakan. Berikut adalah ruang lingkup yang dikerjakan dalam proyek ini:
- Melakukan eksplorasi dan analisis data performa siswa.
- Membangun model machine learning untuk memprediksi kemungkinan dropout.
- Membuat dashboard visual interaktif untuk monitoring performa siswa.
- Menyusun rekomendasi berbasis data untuk pengambilan keputusan.

### Persiapan

**Sumber Data:**  

Dataset yang digunakan dalam proyek ini dapat diakses melalui tautan berikut:  
[Students Performance Data - Dicoding Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment: Anaconda
```
conda create --name ds-expert python=3.12.4 -y
conda activate ds-expert
D:
cd D:\DSExpert-JJI
pip install -r requirements.txt 
```

## Business Dashboard
Dashboard dibuat dengan menggunakan Google Looker Studio untuk menampilkan distribusi data dan pengaruh variabel-variabel data terhadap Student Performance. Dashboard dapat diakses pada link berikut ini:
```
https://lookerstudio.google.com/s/hfrI8pmx_RM
```
![ichaa_agni-dashboard](https://github.com/IchaAgni/Students-Performance/blob/main/ichaa_agni-dashboard.jpg)

## Menjalankan Sistem Machine Learning
*Prototype* Sistem *Machine Learning* ini dibuat dengan *Streamlit* yang dapat diakses pada *link* berikut ini:
```
http://194.233.88.134:3005/
```


## Conclusion
- Komposisi siswa terdiri dari 66% Laki-laki dan 34% Perempuan dengan distribusi usia tertinggi pada rentang 17-23 tahun.
- Tingkat kelulusan siswa (Graduation Rate) sebesar 60.85%% sedangkan tingkat ketidaklulusan (Dropout Rate) sebesar 39,14% dari 3.630 siswa
- Tingkat ketidaklulusan cukup seimbang antara siswa Laki-laki (19.83%) dan siswa Perempuan (19.31%)
- Dari 969 penerima beasiswa terdapat 134 siswa yang dropout (13.83%) dan 835 siswa yang berhasil lulus (86.17%)
- Dari 1.421 siswa yang dropout terdapat 1.214 siswa (85.43%) yang mengikuti kelas pagi dan 207 siswa (14.57%) yang mengikuti kelas malam
Selain itu, faktor curricular units dan tuition fees juga cukup berpengaruh pada tingkat kelulusan siswa.

### Rekomendasi Action Items

Beberapa rekomendasi action items yang harus dilakukan institusi guna menyelesaikan permasalahan atau mencapai target mereka.

Memberikan bimbingan dan dukungan tambahan kepada siswa penerima beasiswa untuk membantu mereka mengatasi tantangan akademik dan non-akademik.
Meninjau kembali kurikulum yang ada untuk memastikan bahwa apakah masih relevan, menantang, dan sesuai dengan kebutuhan siswa.
Menyediakan tutor atau mentor, kelas remedial, bimbingan akademik, dan dukungan psikologis bagi siswa yang membutuhkannya.
Mengembangkan program pendidikan / kelas alternatif yang dapat menjangkau siswa yang mungkin kesulitan menghadiri kelas pada waktu reguler, seperti program jarak jauh.
