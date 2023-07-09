import gradio as gr
import torch

model = torch.hub.load("./", "custom", path="runs/train/exp9/weights/best.pt", source="local")

title = "基于Gradio的YOLOv5演示项目"
desc = "简单的演示"


def det_image(img, conf, iou):
    model.conf = conf
    model.iou = iou
    return model(img).render()[0]


gr.Interface(inputs=["image", "slider", "slider"],
             outputs=["image"],
             fn=lambda img: model(img).render()[0],
             title=title,
             description=desc).launch()

# desc = "这是一个基于Gradio的YOLOv5演示项目，非常简洁，非常方便！"

# base_conf, base_iou = 0.25, 0.45

# def det_image(img, conf_thres, iou_thres):
#     model.conf = conf_thres
#     model.iou = iou_thres
#     return model(img).render()[0]

# gr.Interface(inputs=["image", gr.Slider(minimum=0, maximum=1, value=base_conf), gr.Slider(minimum=0, maximum=1, value=base_iou)], 
#              outputs=["image"], 
#              fn=det_image,
#              title=title,
#              description=desc,
#              live=True, 
#              examples=[["./datasets/images/train/30.jpg", base_conf, base_iou], ["./datasets/images/train/900.jpg", 0.3, base_iou]]).launch(share=True)
