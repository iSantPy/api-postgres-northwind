from datetime import date

from sqlalchemy import func
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Customer, Employee, Supplier, Category,
    Product, Shipper, Order, OrderDetail
)
from app.schemas import (
    CustomerSchema, EmployeeSchema, SupplierSchema,
    CategorySchema, ProductSchema, ShipperSchema,
    OrderSchema, OrderDetailSchema
)

app = FastAPI(title="Northwind API")

# --------------------------
# Customers
# --------------------------
@app.get("/customers", response_model=list[CustomerSchema])
def get_customers(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Customer)
        .join(Order, Customer.CustomerID == Order.CustomerID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Employees
# --------------------------
@app.get("/employees", response_model=list[EmployeeSchema])
def get_employees(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Employee)
        .join(Order, Employee.EmployeeID == Order.EmployeeID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Suppliers
# --------------------------
@app.get("/suppliers", response_model=list[SupplierSchema])
def get_suppliers(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Supplier)
        .join(Product, Supplier.SupplierID == Product.SupplierID)
        .join(OrderDetail, Product.ProductID == OrderDetail.ProductID)
        .join(Order, OrderDetail.OrderID == Order.OrderID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Categories
# --------------------------
@app.get("/categories", response_model=list[CategorySchema])
def get_categories(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Category)
        .join(Product, Category.CategoryID == Product.CategoryID)
        .join(OrderDetail, Product.ProductID == OrderDetail.ProductID)
        .join(Order, OrderDetail.OrderID == Order.OrderID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Products
# --------------------------
@app.get("/products", response_model=list[ProductSchema])
def get_products(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Product)
        .join(OrderDetail, Product.ProductID == OrderDetail.ProductID)
        .join(Order, OrderDetail.OrderID == Order.OrderID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Shippers
# --------------------------
@app.get("/shippers", response_model=list[ShipperSchema])
def get_shippers(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Shipper)
        .join(Order, Shipper.ShipperID == Order.ShipperID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# Orders
# --------------------------
@app.get("/orders", response_model=list[OrderSchema])
def get_orders(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(Order)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )

# --------------------------
# OrderDetails
# --------------------------
@app.get("/orderdetails", response_model=list[OrderDetailSchema])
def get_orderdetails(
    order_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(OrderDetail)
        .join(Order, OrderDetail.OrderID == Order.OrderID)
        .filter(func.date(Order.OrderDate) == order_date)
        .all()
    )