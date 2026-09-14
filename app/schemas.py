from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

# ==================== User Schemas ====================
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: str = "cashier"

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ==================== Category Schemas ====================
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ==================== Product Schemas ====================
class ProductBase(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category_id: int
    purchase_price: float
    selling_price: float
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    purchase_price: Optional[float] = None
    selling_price: Optional[float] = None
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    category: CategoryResponse
    
    class Config:
        from_attributes = True

# ==================== Transaction Schemas ====================
class TransactionItemBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class TransactionItemCreate(TransactionItemBase):
    pass

class TransactionItemResponse(TransactionItemBase):
    id: int
    subtotal: float
    product: ProductResponse
    created_at: datetime
    
    class Config:
        from_attributes = True

class TransactionBase(BaseModel):
    payment_method: str
    discount: float = 0.0
    notes: Optional[str] = None

class TransactionCreate(TransactionBase):
    items: List[TransactionItemCreate]

class TransactionUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class TransactionResponse(TransactionBase):
    id: int
    transaction_number: str
    subtotal: float
    tax: float
    total: float
    status: str
    cashier_id: int
    cashier: UserResponse
    items: List[TransactionItemResponse]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ==================== Stock Movement Schemas ====================
class StockMovementBase(BaseModel):
    product_id: int
    movement_type: str
    quantity: int
    reference_id: Optional[str] = None
    notes: Optional[str] = None

class StockMovementCreate(StockMovementBase):
    pass

class StockMovementResponse(StockMovementBase):
    id: int
    created_at: datetime
    product: ProductResponse
    
    class Config:
        from_attributes = True

# ==================== Report Schemas ====================
class ReportResponse(BaseModel):
    id: int
    report_type: str
    period_start: datetime
    period_end: datetime
    total_transactions: int
    total_sales: float
    total_tax: float
    total_discount: float
    created_at: datetime
    
    class Config:
        from_attributes = True

# ==================== Auth Schemas ====================
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
