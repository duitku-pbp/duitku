const walletCard = (wallet) => `
  <div class="wallet__wallet">
    <p class="wallet__wallet-name">
      <a href="/wallet/${wallet.id}">${wallet.name}</a>
    </p>
    <p class="wallet__wallet-text">Rp. ${wallet.balance}</p>
  </div>
`

const transactionsDateGroup = (date) => {
  const formattedDate = new Date(date).toLocaleDateString("en-US", {
    day: "numeric",
    month: "short",
    year: "numeric",
    weekday: "short",
  })

  return `
  <div class="wallet__transaction-date-group" id="wallet__transaction-${date}">
    <h1 class="wallet__transaction-date">${formattedDate}</h1>
  </div>
`
}

const transactionCard = (transaction, view='all') => `
  <div class="wallet__transaction">
    <p class="wallet__transaction-desc">
      <a href="/wallet/transaction/${transaction.id}">${transaction.description}</a>
    </p>
    ${view === 'all' ? `
    <p class="wallet__transaction-text">${transaction.wallet.name}</p>
    `: ""} 
    <p class="wallet__transaction-text" style="color: ${transaction.type === 'INCOME' ? "green" : "red"};">
      Rp. ${transaction.type === "INCOME" ? "+" : "-"}${transaction.amount}
    </p>
  </div>
`
