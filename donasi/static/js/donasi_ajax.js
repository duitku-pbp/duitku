async function getDonasiList() {
    return fetch("/donasi/show-json").then((res) => res.json())
}

async function refreshDonasiList() {
        document.getElementById("cards_ajax").innerHTML = ""
        const donasiList = await getDonasiList()
        let htmlString = ``
        donasiList.forEach((item) => {
        htmlString += `\n
        <center>
        <div class="card">
            <div class="container">
                <h4><b>Nama Donatur</b></h4>
                <p>${item.fields.name}</p>
                <h4><b>Nominal</b></h4>
                <p>Rp${item.fields.amount}</p>
                <h4><b>Tujuan Donasi</b></h4>
                <p>${item.fields.target}</p>
                <h4><b>Tanggal</b></h4>
                <p>${item.fields.date}</p>
                <button type="button" id="tombol-delete">
                  <a class="link" onclick="deleteDonasi(${item.pk})">Submit</a>
                </button>
            </div>
        </div>
        </center>
        ` 
        })
        document.getElementById("cards_ajax").innerHTML = htmlString
}

async function deleteDonasi(id) {
    let url = "/donasi/json/delete/" + id;
    fetch(url).then(refreshDonasiList)
  }

async function addDonasi() {
    fetch("/donasi/add/", {
        method: "POST",
        body: new FormData(document.querySelector('#form_donasi'))
    }).then(refreshDonasiList)
    return false
}
