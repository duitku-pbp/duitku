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
