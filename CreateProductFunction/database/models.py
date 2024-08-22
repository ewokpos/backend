# Definiciones de modelos de datos en SQL puro
# Este archivo puede contener sentencias SQL para crear y manipular tablas

CREATE_PRODUCTS_TABLE_SQL = """
                CREATE TABLE IF NOT EXISTS ProductsTable (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    name VARCHAR(255) NOT NULL,
                    category VARCHAR(100),
                    price DECIMAL(10, 2) NOT NULL,
                    stock INT NOT NULL DEFAULT 0,
                    description TEXT,
                    sku VARCHAR(50),
                    barcode VARCHAR(50),
                    created_at TIMESTAMPTZ DEFAULT current_timestamp(),
                    updated_at TIMESTAMPTZ DEFAULT current_timestamp()
                );
            """


class Product:
    def __init__(self, id, name, category, price, stock, description, sku, barcode):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description
        self.sku = sku
        self.barcode = barcode

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock,
            'description': self.description,
            'sku': self.sku,
            'barcode': self.barcode
        }