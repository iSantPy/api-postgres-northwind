from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# --------------------------
# Categories
# --------------------------
class Category(Base):
    __tablename__ = "categories"

    CategoryID = Column("categoryid", Integer, primary_key=True, index=True)
    CategoryName = Column("categoryname", String(25), nullable=False)
    Description = Column("description", String(255))


# --------------------------
# Customers
# --------------------------
class Customer(Base):
    __tablename__ = "customers"

    CustomerID = Column("customerid", Integer, primary_key=True, index=True)
    CustomerName = Column("customername", String(50), nullable=False)
    ContactName = Column("contactname", String(50))
    Address = Column("address", String(50))
    City = Column("city", String(20))
    PostalCode = Column("postalcode", String(10))
    Country = Column("country", String(15))


# --------------------------
# Employees
# --------------------------
class Employee(Base):
    __tablename__ = "employees"

    EmployeeID = Column("employeeid", Integer, primary_key=True, index=True)
    LastName = Column("lastname", String(15), nullable=False)
    FirstName = Column("firstname", String(15), nullable=False)
    BirthDate = Column("birthdate", TIMESTAMP)
    Photo = Column("photo", String(25))
    Notes = Column("notes", String(1024))


# --------------------------
# Shippers
# --------------------------
class Shipper(Base):
    __tablename__ = "shippers"

    ShipperID = Column("shipperid", Integer, primary_key=True, index=True)
    ShipperName = Column("shippername", String(25), nullable=False)
    Phone = Column("phone", String(15))


# --------------------------
# Suppliers
# --------------------------
class Supplier(Base):
    __tablename__ = "suppliers"

    SupplierID = Column("supplierid", Integer, primary_key=True, index=True)
    SupplierName = Column("suppliername", String(50), nullable=False)
    ContactName = Column("contactname", String(50))
    Address = Column("address", String(50))
    City = Column("city", String(20))
    PostalCode = Column("postalcode", String(10))
    Country = Column("country", String(15))
    Phone = Column("phone", String(15))


# --------------------------
# Products
# --------------------------
class Product(Base):
    __tablename__ = "products"

    ProductID = Column("productid", Integer, primary_key=True, index=True)
    ProductName = Column("productname", String(50), nullable=False)
    SupplierID = Column("supplierid", Integer, ForeignKey("suppliers.supplierid"))
    CategoryID = Column("categoryid", Integer, ForeignKey("categories.categoryid"))
    Unit = Column("unit", String(25))
    Price = Column("price", Numeric)


# --------------------------
# Orders
# --------------------------
class Order(Base):
    __tablename__ = "orders"

    OrderID = Column("orderid", Integer, primary_key=True, index=True)
    CustomerID = Column("customerid", Integer, ForeignKey("customers.customerid"))
    EmployeeID = Column("employeeid", Integer, ForeignKey("employees.employeeid"))
    OrderDate = Column("orderdate", TIMESTAMP)
    ShipperID = Column("shipperid", Integer, ForeignKey("shippers.shipperid"))


# --------------------------
# OrderDetails
# --------------------------
class OrderDetail(Base):
    __tablename__ = "orderdetails"

    OrderDetailID = Column("orderdetailid", Integer, primary_key=True, index=True)
    OrderID = Column("orderid", Integer, ForeignKey("orders.orderid"))
    ProductID = Column("productid", Integer, ForeignKey("products.productid"))
    Quantity = Column("quantity", Integer)