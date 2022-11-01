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

const updateWallet = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}
  let id

  formData.forEach((v, k) => {
    if (k === "wallet-id") id = v
    else data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch(`/wallet/api/${id}/`, {
    method: "PUT",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const deleteWallet = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}
  let id

  formData.forEach((v, k) => {
    if (k === "wallet-id") id = v
    else data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch(`/wallet/api/${id}/`, {
    method: "DELETE",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const renderTransactions = async () => {
  const res = await fetch("/wallet/api/transaction/")
  const transactions = await res.json()
  const totalBalance = transactions.reduce((total, transaction) => total + transaction.amount, 0)

  /* document.getElementsByClassName("wallet__transactions-total")[0].textContent = `Total: Rp. ${totalBalance}` */

  transactions.forEach(transaction => {
    document.getElementById("wallet__transactions").innerHTML += transactionCard(transaction)
  });
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

const editWalletDetailForm = (edit) => {
  if (edit) {
    document.getElementById("wallet__detail-option-btns").hidden = true 
    document.getElementById("wallet__detail-edit-btns").hidden = false

    document.querySelectorAll("#wallet__wallet-detail > *").forEach((element) => {
      element.removeAttribute("disabled")
    })
  } else {
    document.getElementById("wallet__detail-option-btns").hidden = false
    document.getElementById("wallet__detail-edit-btns").hidden = true

    document.querySelectorAll("#wallet__wallet-detail > :not(button)").forEach((element) => {
      element.setAttribute("disabled", true)
    })
  }
}
