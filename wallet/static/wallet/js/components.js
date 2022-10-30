const walletCard = (wallet) => `
  <div class="wallet__wallet">
    <p class="wallet__wallet-name">
      <a href="/wallet/${wallet.id}">${wallet.name}</a>
    </p>
    <p class="wallet__wallet-text">Rp. ${wallet.balance}</p>
  </div>
`
