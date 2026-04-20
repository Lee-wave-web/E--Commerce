document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("productForm");

    if (!form) return;   // Stop if form not found

    form.addEventListener("submit", async function (e) {

        e.preventDefault();   // Stop normal form submit

        // 1.Get form values
        const name = document.getElementById("name").value;
        const category = document.getElementById("category").value;
        const price = document.getElementById("price").value;
        const stock = document.getElementById("stock").value;

        // 2.Decide API URL
        let url = "/api/product/create/";   // Default → Add

        if (window.location.pathname.includes("edit-product")) {
            const id = window.location.pathname.split("/")[2];      ["", 'edit-product', "5", ""]
            url = `/api/product/update/${id}/`;
        }

        // 3.Send data to backend
        try {

            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({
                    name: name,
                    category: category,
                    price: price,
                    stock: stock
                })
            });

            if (!response.ok) {
                throw new Error("Server error");
            }

            alert("Saved Successfully!");
            // window.location.href = "/";

        } catch (error) {

            alert("Something went wrong!");
            console.log(error);

        }

    });

});

