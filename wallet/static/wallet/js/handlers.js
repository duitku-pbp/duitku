const renderWallets = async () => {
  const res = await fetch("/wallet/api/")
  const wallets = await res.json()
  const totalBalance = wallets.reduce((total, wallet) => total + wallet.balance, 0)

  document.getElementsByClassName("wallet__wallets-total-balance")[0].textContent = `Total: Rp. ${totalBalance}`

  wallets.forEach(wallet => {
    document.getElementById("wallet__wallets").innerHTML += walletCard(wallet)
  });
}

const createWallet = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}

  formData.forEach((v, k) => {
    data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch("/wallet/api/create/", {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const createTransaction = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}

  formData.forEach((v, k) => {
    data[k] = v
  }) 

  const csrfToken = getCookie("csrftoken")

  res = await fetch("/wallet/api/transaction/create/", {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const loadWalletsInDropdown = (wallets) => {
  wallets.forEach(wallet => {
    document.getElementById('wallet').innerHTML += `
<option value=${wallet.id}>${wallet.name} (${wallet.balance})</option>
`
  })
}
