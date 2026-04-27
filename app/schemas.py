from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

# --------------------------
# Categories
# --------------------------
class CategorySchema(BaseModel):
    CategoryID: int
    CategoryName: str
    Description: Optional[str] = None

    class Config:
        orm_mode = True

# --------------------------
# Customers
# --------------------------
class CustomerSchema(BaseModel):
    CustomerID: int
    CustomerName: str
    ContactName: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None

    class Config:
        orm_mode = True

# --------------------------
# Employees
# --------------------------
class EmployeeSchema(BaseModel):
    EmployeeID: int
    LastName: str
    FirstName: str
    BirthDate: Optional[datetime] = None
    Photo: Optional[str] = None
    Notes: Optional[str] = None

    class Config:
        orm_mode = True

# --------------------------
# Shippers
# --------------------------
class ShipperSchema(BaseModel):
    ShipperID: int
    ShipperName: str
    Phone: Optional[str] = None

    class Config:
        orm_mode = True

# --------------------------
# Suppliers
# --------------------------
class SupplierSchema(BaseModel):
    SupplierID: int
    SupplierName: str
    ContactName: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    Phone: Optional[str] = None

    class Config:
        orm_mode = True

# --------------------------
# Products
# --------------------------
class ProductSchema(BaseModel):
    ProductID: int
    ProductName: str
    SupplierID: Optional[int] = None
    CategoryID: Optional[int] = None
    Unit: Optional[str] = None
    Price: Optional[Decimal] = None

    class Config:
        orm_mode = True

# --------------------------
# Orders
# --------------------------
class OrderSchema(BaseModel):
    OrderID: int
    CustomerID: Optional[int] = None
    EmployeeID: Optional[int] = None
    OrderDate: Optional[datetime] = None
    ShipperID: Optional[int] = None

    class Config:
        orm_mode = True

# --------------------------
# OrderDetails
# --------------------------
class OrderDetailSchema(BaseModel):
    OrderDetailID: int
    OrderID: Optional[int] = None
    ProductID: Optional[int] = None
    Quantity: Optional[int] = None

    class Config:
        orm_mode = True