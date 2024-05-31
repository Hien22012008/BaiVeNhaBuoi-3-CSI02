def wrap_text(text, k):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        # Kiểm tra nếu thêm từ vào dòng hiện tại có vượt quá k ký tự không
        if len(current_line) + len(word) + (1 if current_line else 0) <= k:
            current_line += (" " + word if current_line else word)
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)  # Thêm chuỗi cuối cùng vào danh sách

    return lines

# Ví dụ sử dụng
input_text = input("Input text: ")
max_width = int(input("Input max width: "))
output = wrap_text(input_text, max_width)
print(output)