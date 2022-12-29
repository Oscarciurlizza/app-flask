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
    console.log(window.origin);
    let confirmPurchase = confirm("Are you sure? 🤭");
    if (confirmPurchase) {
      await fetch(`${window.origin}/buyBook`, {
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
          if (data.success) {
            alert("Purchase complete 😜");
          } else {
            alert("Error in purchase 😥");
          }
        })
        .catch((error) => {
          console.error(`Error: ${error}`);
        });
    } else {
      return null;
    }
  };
})();
