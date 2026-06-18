def main():
    # 6. Dữ liệu khởi tạo mẫu chứa các Object Drink
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]

    while True:
        # 7. Hiển thị Menu chương trình
        print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()

        # CHỨC NĂNG 1: XEM DANH SÁCH ĐỒ UỐNG
        if choice == "1":
            print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
            print(f"{'Mã món':<7} | {'Tên món':<18} | {'Giá bán':<7} | Trạng thái")
            print("-" * 52)
            for drink in menu:
                # Chuyển đổi hiển thị trạng thái Boolean sang Tiếng Việt
                status_str = "Đang bán" if drink.is_available else "Ngừng bán"
                # Giá bán bắt buộc phải gọi qua property .price
                print(f"{drink.code:<7} | {drink.name:<18} | {drink.price:<7} | {status_str}")

        # CHỨC NĂNG 2: THÊM ĐỒ UỐNG MỚI
        elif choice == "2":
            print("\n--- THÊM ĐỒ UỐNG MỚI ---")
            code = input("Nhập mã món: ").strip().upper() # Tự động viết hoa mã món

            # Kiểm tra bẫy dữ liệu trùng mã món
            is_duplicate = any(drink.code == code for drink in menu)
            if is_duplicate:
                print("[LỖI]: Mã món đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên món: ").strip()

            try:
                price = int(input("Nhập giá bán: ").strip())
                # Kiểm tra bẫy dữ liệu giá bán hợp lệ phải > 0
                if price <= 0:
                    print("[LỖI]: Giá bán không hợp lệ! (Giá phải lớn hơn 0)")
                    continue
            except ValueError:
                print("[LỖI]: Giá bán phải là một số nguyên hợp lệ!")
                continue

            # Tạo Object mới từ Class Drink và thêm vào list menu
            new_drink = Drink(code, name, price)
            menu.append(new_drink)
            print(f"Thành công: Đã thêm món {name} vào thực đơn!")

        # CHỨC NĂNG 3: CẬP NHẬT TRẠNG THÁI KINH DOANH
        elif choice == "3":
            print("\n--- CẬP NHẬT TRẠNG THÁI KINH DOANH ---")
            code_to_update = input("Nhập mã món cần cập nhật: ").strip().upper()

            # Tìm kiếm đối tượng đồ uống tương ứng với mã vừa nhập
            target_drink = next((drink for drink in menu if drink.code == code_to_update), None)

            if target_drink is None:
                print("[LỖI]: Không tìm thấy món có mã này!")
            else:
                # Gọi Instance Method để đảo trạng thái kinh doanh
                target_drink.toggle_available()
                status_str = "Đang bán" if target_drink.is_available else "Ngừng bán"
                print(f"Đã cập nhật trạng thái món {target_drink.code}.")
                print(f"Trạng thái hiện tại: {status_str}")

        # CHỨC NĂNG 4: THOÁT CHƯƠNG TRÌNH
        elif choice == "4":
            print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        else:
            print("[CẢNH BÁO]: Vui lòng nhập đúng số chức năng từ 1 đến 4!")

if __name__ == "__main__":
    main()