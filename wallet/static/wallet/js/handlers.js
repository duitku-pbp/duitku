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

const fromWalletOnChange = async () => {
  const walletId = document.getElementById('from-wallet').value

  await renderTransactions(walletId)
}

const renderTransactions = async (wallet="all") => {
  const fromWallet = wallet === "all" ? "from-wallet=all" : "from-wallet=" + wallet
  const res = await fetch("/wallet/api/transaction/?" + fromWallet)
  const transactions = await res.json()
  const totalBalance = transactions.reduce((total, transaction) => {
    let trxTotal = 0

    transaction["transactions"].forEach((trx) => {
      trxTotal += trx.type === "INCOME" ? trx.amount : -1 * trx.amount
    })

    return total + trxTotal
  }, 0)

  document.getElementsByClassName("wallet__transaction-total")[0].textContent = `Rp. ${totalBalance}`
  document.getElementById("wallet__transactions").innerHTML = ""

  transactions.forEach(transaction => { 
    document.getElementById("wallet__transactions").innerHTML += transactionsDateGroup(transaction["date"])

    const trxs = transaction["transactions"]

    trxs.forEach((trx) => {
      document.getElementById("wallet__transaction-" + transaction["date"]).innerHTML += transactionCard(trx, wallet)
    })
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

const updateTransaction = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}
  let id

  formData.forEach((v, k) => {
    if (k === "transaction-id") id = v
    else data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch(`/wallet/api/transaction/${id}/`, {
    method: "PUT",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const deleteTransaction = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}
  let id

  formData.forEach((v, k) => {
    if (k === "transaction-id") id = v
    else data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch(`/wallet/api/transaction/${id}/`, {
    method: "DELETE",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}

const loadWalletsInDropdown = (wallets, id='wallet', showBalance=false) => {
  wallets.forEach(wallet => {
    document.getElementById(id).innerHTML += `
<option value=${wallet.id}>${wallet.name} ${ showBalance ? `(${wallet.balance})` : ""}</option>
`
  })
}

const editTransactionDetailForm = (edit) => {
  if (edit) {
    document.getElementById("wallet__detail-option-btns").hidden = true 
    document.getElementById("wallet__detail-edit-btns").hidden = false

    document.querySelectorAll("#wallet__transaction-detail > :not(select[id=\"wallet\"])").forEach((element) => {
      element.removeAttribute("disabled")
    })
  } else {
    document.getElementById("wallet__detail-option-btns").hidden = false
    document.getElementById("wallet__detail-edit-btns").hidden = true

    document.querySelectorAll("#wallet__transaction-detail > :not(button)").forEach((element) => {
      element.setAttribute("disabled", true)
    })
  }
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
