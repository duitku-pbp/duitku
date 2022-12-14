// Removes base title
document.getElementsByTagName('title')[0].remove()

document.onreadystatechange = () => {
  if (document.readyState === 'complete') {
    document.getElementById("wallet__loading").hidden = true
    document.getElementById("wallet__container").hidden = false
  } else {
    document.getElementById("wallet__loading").hidden = false
    document.getElementById("wallet__container").hidden = true
  }
}


document.addEventListener('DOMContentLoaded', async () => {
  const csrftoken = getCookie('csrftoken')
  const route = window.location.pathname

  if (route === '/wallet/transaction/create/') {
    const res = await fetch("/wallet/api/", {
      headers: {
        'X-CSRFTOKEN': csrftoken
      }
    })

    const wallets = await res.json()
    loadWalletsInDropdown(wallets, 'wallet', true)
  }

  if (route === '/wallet/') {
    loadMonthsInReportDropdown()

    const period = document.getElementById('report-month').value
    loadReportForCurrentPeriod(period)

    await renderWallets()
  }

  if (route === '/wallet/transaction/') {
    const res = await fetch("/wallet/api/", {
      headers: {
        'X-CSRFTOKEN': csrftoken
      }
    })

    const wallets = await res.json()
    loadWalletsInDropdown(wallets, 'from-wallet')

    await renderTransactions()
  }

  restrictMaxDate()
})

