(function () {
  const btnsBuyBook = document.querySelectorAll(".btnBuyBook");
  let isbn = null;
  const csrf_token = document.querySelector("[name='csrf-token']").value;
  btnsBuyBook.forEach((btn) => {
    btn.addEventListener("click", function () {
      isbn = this.id;
      confirmPurchase();
    });
  });

  const confirmPurchase = async () => {
    await fetch("http://127.0.0.1:5000/buyBook", {
      method: "POST",
      mode: "same-origin",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": csrf_token,
      },
      body: JSON.stringify({
        isbn,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          console.error(response);
        } else {
          return response.json();
        }
      })
      .then((data) => {
        console.log("libro comprado");
      })
      .catch((error) => {
        console.error(`Error: ${error}`);
      });
  };
})();
