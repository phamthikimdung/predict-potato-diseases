#Khai báo các thư viện cần thiết 
from fastapi import FastAPI, File, UploadFile,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

#Kết nối thử api
@app.get("/ping")
async def ping():
    return "Hello"

# Kết nối tới frontend
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})



#Tải model dự đoán đã xây dựng và lưu trong thư mục models 
#(model dự đoán được xây dựng tại thư mục tranning trong file tranning.ipynb)
MODEL = tf.keras.models.load_model("D:/potato_project/models/1.keras")

#Định nghĩa các lớp dự đoán
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Đọc file hình ảnh tải lên
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Tiến hành dự đoán dựa trện model đã tải lên và trả về kết quả 
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    
    predictions = MODEL.predict(img_batch) 

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])] 
    confidence = 100*(np.max(predictions[0]))
    return {
        'class': predicted_class,
        'confidence': float(confidence) 
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)