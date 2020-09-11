from app import db, admin
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

class Suppliers(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    companyname = Column(String(50), nullable=False)
    contactname = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=True)
    address = Column(String(100), nullable=True)
    note = Column(String(50), nullable=True)
    products = relationship("Product", backref="suppliers", lazy=True)

    def __str__(self):
        return self.companyname

class Category(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship("Product", backref="category", lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    supplier_id = Column(Integer, ForeignKey(Suppliers.id), nullable=False)

    def __str__(self):
        return self.name

class Employees(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    lastname = Column(String(50), nullable=True)
    firstname = Column(String(50), nullable=False)
    birdthday = Column(Date, nullable=True)
    startdate = Column(Date, nullable=True)
    phone = Column(String(10), nullable=True)
    address = Column(String(50), nullable=True)
    photo = Column(String(255), nullable=True)
    note = Column(String(50), nullable=True)
    order = relationship("Orders", backref="employees", lazy=True)

    def __str__(self):
        return self.firstname

class Customers(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    lastname = Column(String(50), nullable=True)
    firstname = Column(String(50), nullable=False)
    birdthday = Column(Date, nullable=True)
    phone = Column(String(10), nullable=True)
    address = Column(String(100), nullable=True)
    order = relationship("Orders", backref="customers", lazy=True)

    def __str__(self):
        return self.firstname

class Orders(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    address = Column(String(100), nullable=False)
    customer_id = Column(Integer, ForeignKey(Customers.id), nullable=False)
    employee_id = Column(Integer, ForeignKey(Employees.id), nullable=False)

    def __str__(self):
        return self.address

class OrderDetail(db.Model):

    id1_pro = Column(Integer, ForeignKey(Product.id), primary_key=True)
    id2_ord = Column(Integer, ForeignKey(Orders.id), primary_key=True)
    price = Column(Float, default=0)
    quantity = Column(Integer, nullable=False, default=0)

class OrderInput(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    input_sup = Column(Integer, ForeignKey(Suppliers.id), nullable=False)
    input_emp = Column(Integer, ForeignKey(Employees.id))


class OrderInputDetail(db.Model):

    id1_pro = Column(Integer, ForeignKey(Product.id), primary_key=True)
    id2_ord_input = Column(Integer, ForeignKey(OrderInput.id), primary_key=True)
    price = Column(Float, default=0)
    quantity = Column(Integer, nullable=False, default=0)

class CategoryModelView(ModelView):
    column_display_pk = True
    form_columns = ('name',)

class ProductModelView(ModelView):
    column_display_pk = True
    can_export = True

class SupplierModelView(ModelView):
    column_display_pk = True
    can_export = True

class CustomerModelView(ModelView):
    column_display_pk = True
    can_export = True

class EmployeeModelView(ModelView):
    column_display_pk = True
    can_export = True

class OrderModelView(ModelView):
    column_display_pk = True
    can_export = True

class OrderInputModelView(ModelView):
    column_display_pk = True
    can_export = True
    form_columns = ('id', 'date', 'input_sup', 'input_emp')
    column_list = ('id', 'date', 'input_sup', 'input_emp')

class AboutUsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/about-us.html')


admin.add_view(CategoryModelView(Category, db.session, name='Loại sản phẩm'))
admin.add_view(ProductModelView(Product, db.session, name='Sản phẩm'))
admin.add_view(SupplierModelView(Suppliers, db.session, name='Nhà cung cấp'))
admin.add_view(CustomerModelView(Customers, db.session, name='Khách hàng'))
admin.add_view(EmployeeModelView(Employees, db.session, name='Nhân viên'))
admin.add_view(OrderModelView(Orders, db.session, name='Đơn bán hàng'))
admin.add_view(OrderInputModelView(OrderInput, db.session, name='Đơn nhập hàng'))
admin.add_view(AboutUsView(name='Liên hệ'))



if __name__ == "__main__":
    db.create_all()

