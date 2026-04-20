from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, Customer, Order
import json

# ---------------- PRODUCT LIST ----------------
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})

# ---------------- ADD PRODUCT PAGE ----------------
def add_product(request):
    return render(request, "store/product_form.html")

# ---------------- EDIT PRODUCT PAGE ----------------
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "store/product_form.html", {"product": product})

# ---------------- DELETE PRODUCT ----------------
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("product_list")

# ---------------- ADD CUSTOMER ----------------
def add_customer(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")

        if name and email:
            Customer.objects.create(name=name, email=email, city=city)
            return redirect("product_list")

    return render(request, "store/customer_form.html")

# ---------------- ADD ORDER ----------------
def add_order(request):

    customers = Customer.objects.all()
    products = Product.objects.all()

    if request.method == "POST":

        customer_id = request.POST.get("customer")
        product_id = request.POST.get("product")
        quantity = request.POST.get("quantity")

        if not quantity:
            return redirect("add_order")

        quantity = int(quantity)

        product = get_object_or_404(Product, id=product_id)

        if product.stock >= quantity:

            Order.objects.create(
                customer_id=customer_id,
                product_id=product_id,
                quantity=quantity
            )

            product.stock -= quantity
            product.save()

        return redirect("order_list")

    return render(request, "store/order_form.html", {
        "customers": customers,
        "products": products
    })

# ---------------- ORDER LIST ----------------
def order_list(request):
    orders = Order.objects.select_related("customer", "product")
    return render(request, "store/order_list.html", {"orders": orders})

# ---------------- API: CREATE PRODUCT ----------------
def product_create_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        Product.objects.create(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            stock=data["stock"]
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "invalid request"}, status=400)

# ---------------- API: UPDATE PRODUCT ----------------
def product_update_api(request, id):

    if request.method == "POST":

        data = json.loads(request.body)
        product = get_object_or_404(Product, id=id)

        product.name = data["name"]
        product.category = data["category"]
        product.price = data["price"]
        product.stock = data["stock"]
        product.save()

        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "invalid request"}, status=400)

# ---------------- API: DELETE PRODUCT ----------------
def product_delete_api(request, id):

    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        product.delete()
        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "invalid request"}, status=400)
