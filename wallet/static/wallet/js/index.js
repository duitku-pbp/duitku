// Removes base title
document.getElementsByTagName('title')[0].remove()

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
    loadWalletsInDropdown(wallets)
  }

  if (route === '/wallet/') {
    await renderWallets()
  }
})

