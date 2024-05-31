def extract_and_sort_words_simple(text):
    # Chuyển tất cả chữ cái thành chữ thường và tách từ
    words = text.lower().split()
    # Loại bỏ dấu câu
    words = [word.strip('.,!;()[]') for word in words]
    # Loại bỏ các từ trùng lặp và sắp xếp
    sorted_unique_words = sorted(set(words))
    return sorted_unique_words

# Ví dụ sử dụng
input_text = input("Input text: ")
output = extract_and_sort_words_simple(input_text)
print(output)
