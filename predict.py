from ultralytics import YOLO

# model = YOLO(r"runs\detect\train28\weights\best.onnx")
# results = model.predict(task='detect',source=r"img\Casingdamage(1).jpg",save=True, show=True)
if __name__ == '__main__':
    model = YOLO(r"../runs\detect\输电线路_yolov8n_batch-1\weights\best.pt")
    imgpth = r'E:\guizhoudianwang\result\20180522134303.jpg'
    results = model.predict(device=['cpu'],task='detect', source=imgpth, save=True, show=False, iou=0.5, save_txt=True,name='name',project='/')
    for result in results:
        # print(dir(result))
        pass