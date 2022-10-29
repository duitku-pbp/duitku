const createWallet = async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  let data = {}

  formData.forEach((v, k) => {
    data[k] = v
  })

  const csrfToken = getCookie("csrftoken")

  res = await fetch("/wallet/api/create", {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrfToken
    },
    body: JSON.stringify(data)
  })

  window.location.assign(res.url)
}
