# Coffee Shop Management System

Welcome to the Coffee Shop Management System! This is a simple Python program that allows you to manage orders and menu items for a coffee shop.

## Features

- Add and display menu items with prices and descriptions.
- Take customer orders with item quantities.
- Display order summaries and total prices.
- Supports Indonesian Rupiah (IDR) currency.

## Getting Started

1. Clone the repository:
2. Run the Python script:
3. Follow the on-screen instructions to interact with the Coffee Shop Management System.

## Usage

1. Add menu items using the `add_menu_item` method.
2. Display the menu using the `display_menu` method.
3. Take orders from customers using the `take_order` method.
4. Display current orders using the `display_orders` method.

## Example

```python
# Create coffee shop instance
my_coffee_shop = CoffeeShop("Brewtopia")

# Add menu items with descriptions
my_coffee_shop.add_menu_item("Latte", 20000, "Smooth espresso with steamed milk")
my_coffee_shop.add_menu_item("Cappuccino", 18000, "Espresso topped with foamed milk")

# Display menu
my_coffee_shop.display_menu()

# Take orders
my_coffee_shop.take_order("Alice", "Latte:2, Cappuccino:1")

# Display orders
my_coffee_shop.display_orders()
```

# ================================================================

# Sistem Manajemen Coffee Shop

Selamat datang di Sistem Manajemen Coffee Shop! Ini adalah program sederhana berbasis Python yang memungkinkan Anda mengelola pesanan dan menu item untuk sebuah coffee shop.

## Fitur

- Tambahkan dan tampilkan menu item dengan harga dan deskripsi.
- Terima pesanan dari pelanggan dengan kuantitas item.
- Tampilkan ringkasan pesanan dan total harga.
- Mendukung mata uang Rupiah Indonesia (IDR).

## Memulai

1. Klon repositori:
2. Jalankan skrip Python:
3. Ikuti instruksi di layar untuk berinteraksi dengan Sistem Manajemen Coffee Shop.

## Penggunaan

1. Tambahkan menu item menggunakan metode `add_menu_item`.
2. Tampilkan menu menggunakan metode `display_menu`.
3. Terima pesanan dari pelanggan menggunakan metode `take_order`.
4. Tampilkan pesanan saat ini menggunakan metode `display_orders`.

## Contoh

```python
# Buat instansi coffee shop
my_coffee_shop = CoffeeShop("Brewtopia")

# Tambahkan menu item dengan deskripsi
my_coffee_shop.add_menu_item("Latte", 20000, "Espresso lembut dengan susu steam")
my_coffee_shop.add_menu_item("Cappuccino", 18000, "Espresso dengan susu berfoam")

# Tampilkan menu
my_coffee_shop.display_menu()

# Terima pesanan
my_coffee_shop.take_order("Alice", "Latte:2, Cappuccino:1")

# Tampilkan pesanan
my_coffee_shop.display_orders()
```
