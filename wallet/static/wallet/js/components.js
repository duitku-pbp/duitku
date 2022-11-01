const walletCard = (wallet) => `
  <div class="wallet__wallet">
    <p class="wallet__wallet-name">
      <a href="/wallet/${wallet.id}">${wallet.name}</a>
    </p>
    <p class="wallet__wallet-text">Rp. ${wallet.balance}</p>
  </div>
`

const transactionCard = (transaction) => `
  <div class="wallet__transaction">
    <p class="wallet__transaction-desc">
      <a href="/wallet/transaction/${transaction.id}">${transaction.description}</a>
    </p>
    <p class="wallet__transaction-text" style="color: ${transaction.type === 'INCOME' ? "green" : "red"};">
      Rp. ${transaction.type === "INCOME" ? "+" : "-"}${transaction.amount}
    </p>
  </div>
`
