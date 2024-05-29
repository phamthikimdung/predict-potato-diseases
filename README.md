# Phân loại Bệnh lá Cây Khoai

Dự án này nhằm mục đích xây dựng một hệ thống phân loại hình ảnh để dự đoán các loại bệnh lá của khoai sử dụng các kỹ thuật máy học.

## Tổng quan

![Screenshot 2024-05-23 103553](https://github.com/phamthikimdung/DATA_SUMMARIZATION/assets/169218029/833915d2-cd5b-4f4c-a61c-97f3b5cae974)


Dự án bao gồm các bước sau:

1. **Xây dựng Mô hình**: Trong tệp Jupyter Notebook `training.ipynb`, tôi đã xây dựng một mô hình phân loại hình ảnh sử dụng TensorFlow và Keras. Mô hình này được đào tạo trên tập dữ liệu về các loại bệnh lá của cây khoai.

2. **API Backend**: Tôi đã xây dựng một API bằng framework FastAPI để cung cấp các dịch vụ phân loại hình ảnh. API này có thể nhận hình ảnh lá khoai từ người dùng, dự đoán loại bệnh và trả về kết quả.

3. **Giao diện người dùng Web**: Giao diện web cho phép người dùng tương tác với hệ thống phân loại hình ảnh. Người dùng có thể tải lên hình ảnh của lá khoai thông qua một biểu mẫu đơn giản và nhận kết quả dự đoán trực tuyến.

## Cài đặt

1. Cài đặt TensorFlow và matplotlib:

    ```bash
    pip install tensorflow
    pip install matplotlib
    ```

2. Chạy tệp `training.ipynb` để đào tạo mô hình phân loại hình ảnh.

3. Chạy API backend bằng cách chạy tệp `main.py`.

## Sử dụng

1. Truy cập giao diện web bằng cách mở trình duyệt và điều hướng đến `http://localhost:8000`.

2. Tải lên hình ảnh lá khoai và nhận kết quả dự đoán trực tuyến.

## Nội dung

- `main.py`: Mã code API backend sử dụng FastAPI.
- `training.ipynb`: Tệp Jupyter Notebook chứa mã code để xây dựng và đào tạo mô hình phân loại hình ảnh.
- `models/`: Thư mục chứa các phiên bản mô hình đã lưu.


