const getCookie = (name) => {
  let cookie

  if (document.cookie) {
    const cookies = document.cookie.split(";")

    for (let i in cookies) {
      cookies[i] = cookies[i].trim()

      if (cookies[i].substring(0, name.length + 1) === name + '=') {
        cookie = decodeURIComponent(cookies[i].substring(name.length + 1))
        break
      }
    }
  }

  return cookie
}

const getLast12Months = () => {
  const now = new Date()
  let dates = []

  for (let i = 0; i > -12; i--) {
    const past = new Date(now.getFullYear(), now.getMonth() + i, 1);
    dates.push(past)
  }

  return dates
}

const restrictMaxDate = () => {
  const now = new Date()
  const maxDate = new Date(now.getFullYear(), now.getMonth() + 1, 0)

  const month = (maxDate.getMonth() + 1).toString().padStart(2, "0")
  const date = maxDate.getDate().toString().padStart(2, "0")
  const maxDateVal = maxDate.getFullYear() + "-" + month + "-" + date

  document.querySelectorAll(`input[type="date"]`).forEach((element) => {
    element.setAttribute('max', maxDateVal)
  })
}
