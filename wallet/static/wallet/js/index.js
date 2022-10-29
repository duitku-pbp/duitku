// Removes base title
document.getElementsByTagName('title')[0].remove()

document.addEventListener('DOMContentLoaded', async () => {
  const csrftoken = getCookie('csrftoken')

  if (window.location.pathname === '/wallet/transaction/create/') {
    const res = await fetch("/wallet/api/", {
      headers: {
        'X-CSRFTOKEN': csrftoken
      }
    })

    const wallets = await res.json()
    loadWalletsInDropdown(wallets)
  }
})

