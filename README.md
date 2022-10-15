# duitku

<!-- Tags and Links -->

[tests]: https://github.com/duitku-pbp/duitku/actions/workflows/test.yml/badge.svg?branch=main
[production deployment tag]: https://github.com/duitku-pbp/duitku/actions/workflows/deploy.yml/badge.svg?branch=main
[link to site]: https://duitku.nairlangga.com

![Tests]
![Production Deployment Tag]

[Link to Site]

## Members

- Arya Daffa Athaillah
- Andrew Jeremy
- Nataya Shafira
- Cinthya Yosephine Depari
- Nanda Tristan Ardiansyah
- Nayyara Airlangga Raharjo

## Story

Salah satu isu yang diangkat pada G20 adalah financial inclusion. Financial inclusion adalah kesetaraan peluang dalam mengakses layanan keuangan. G20 ingin meningkatkan financial inclusion. And that’s where we come in.

Duitku adalah aplikasi yang bertujuan untuk meningkatkan financial inclusion dengan memanfaatkan media digital yang sudah ada saat ini. Duitku menyediakan berbagai layanan untuk mendukung tujuan tersebut seperti manajemen uang, berita terkait dunia keuangan, blog keuangan, dll. Dengan berbagai layanan yang disediakan, kami berharap masyarakat dapat lebih mudah mengedukasi diri dan mengakses berbagai layanan keuangan yang ada

## Modules

- Wallet - Angga<br>
  Fitur yang merepresentasikan dompet-dompet/tabungan seorang pengguna. Pengguna dapat memasukkan dan mengeluarkan uang ke dalam dompet-dompetnya setiap kali terjadi transaksi pemasukan dan pengeluaran. Fitur ini bertujuan agar pengguna dapat lebih terbiasa untuk melacak pemasukan dan pengeluarannya agar bisa lebih mengontrol keuangan mereka sendiri dan bisa lebih percaya diri dalam membeli/menjual instrumen keuangan yang sesuai dengan kondisi keuangan mereka.
- Blog - Andrew<br>
  Fitur ini akan menampilkan berbagai artikel informatif mengenai dunia keuangan untuk meningkatkan financial literacy masyarakat.
- Donasi - Arya
- Financial News - Cinthya
- Investasi - Tristan

## User Roles

### Normal Users

- Authenticated
  - Mengakses fitur wallet, membuat dompet dan transaksi, melihat report dari wallet
  - Mengakses halaman blog dan halaman detailnya
  - Mengakses dan melakukan donasi
  - Mengakses berita-berita financial
  - Melakukan investasi
- Unauthenticated
  - Melihat halaamn utama dan login/registrasi

### Admin/Super Users

- Melakukan administrasi dan pemantauan data via dashboard admin
- Mengunggah blog post baru serta update berita-berita
