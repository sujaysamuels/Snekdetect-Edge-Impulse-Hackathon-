# 🐍 SnekDetect – Edge AI Snake Detection System  
*A lightweight YOLO-based snake detection system built for rural safety and real-world deployment.*

---

## 🧠 Problem Statement – Snakebite Crisis in Developing Countries

Snakebites are a **massive but overlooked public health crisis**.

According to the **World Health Organization (WHO)**:

- 🐍 Around **5 million** snakebites occur each year  
- ⚠️ Up to **138,000 deaths** annually  
- ♿ Nearly **400,000 permanent disabilities**  
- 🚫 Many cases go **unreported** due to lack of medical access  

This threat is highest in:

- Villages  
- Farmlands  
- Forest edges  
- Low-light households  

People need **early warning**, not just treatment after a bite.

**SnekDetect solves this with real-time AI snake detection running on affordable hardware.**

---

## 🎯 Goal

Build a **compact, fast, offline snake detection system** using:

- Raspberry Pi  
- A tiny YOLO model  
- 160 × 160 image input  
- High generalization across grass, mud, and cluttered backgrounds  

---

## 📦 Dataset Preparation

We curated high-quality datasets from Kaggle:

- https://www.kaggle.com/datasets/sameeharahman/preprocessed-snake-images  
- https://www.kaggle.com/datasets/shouvikdey21/giant-snake-data60-species-kaggles-biggest  

### 📊 Dataset Size

We selected **~3700 images**, including:

- Multiple snake species  
- Different angles, lighting, backgrounds  
- Camouflage scenarios (grass, leaves, dark soil)  
- Background-only images for better negative training  

### 🛠 Preprocessing

- Resized all images to **160 × 160**  using a custom python script
- Annotated via **Edge Impulse OWL-ViT Auto-labeling**

  <img width="1488" height="896" alt="image" src="https://github.com/user-attachments/assets/fbda295a-9b79-4bca-bff6-9fd697bb1f5d" />

   **feature extraction for snake class**

  <img width="701" height="824" alt="image" src="https://github.com/user-attachments/assets/8199b4a7-cd59-45c7-a8d6-63844da85438" />

   **labelling snake cases with OWL-VIT**


---

## 🧰 Model Development (Edge Impulse)

All training was done using **Edge Impulse Studio**, focusing on object detection.

### 🐍 Model Type

- **YOLO (Edge Impulse Object Detection)**  
- Medium variant  
- INT8 quantized for lightweight deployment  

### 🧪 Experiments

| Attempt | Dataset Size | Model | Accuracy |
|--------|--------------|--------|----------|
| First Try | 500 images | YOLO small | ~70% |
| Final Try | 3700 images | YOLO small INT8 | **~80%** |
| FOMO | 3700 images | FOMO | ~25% |



<img width="690" height="619" alt="image" src="https://github.com/user-attachments/assets/7c54f8f2-12ac-4378-b055-3d6acb861921" />

**FOMO Performance- Very Poor- neglected**

<img width="694" height="813" alt="image" src="https://github.com/user-attachments/assets/cb3fbe35-2a78-4276-b5b2-6daa9f42041a" />

**YOLO performance- decently Good**

YOLO clearly outperformed others due to better detection of long thin structures like snakes.

---

## 🚀 Edge Inference Pipeline (Raspberry Pi)
<img width="856" height="113" alt="image" src="https://github.com/user-attachments/assets/fb811c01-d378-4af5-9f46-9678b844ead6" />


**Model specs- These can be fit to run on a Raspberry Pi**

Below is the pipeline:

Camera Frame → Resize to 160×160
→ YOLO Inference
→ Bounding Box Filtering
→ Snake Detected? → Trigger Alert
→ Display Output



### ⚡ Performance (Raspberry Pi 4)

- **~2 FPS** depending on lighting and camera  
- **450-500 ms** inference time  
- Fully offline processing  , no need for connectivity


---

## 📊 Performance Summary

- ✔ Effective for small and partially hidden snakes  
- ✔ Handles complex backgrounds like grass and foliage  
- ✔ Small quantized model runs fast on Raspberry Pi  
- ✔ Zero cloud dependency  
- ✔ High generalization due to diverse dataset  

---

## 💡 Why SnekDetect Matters

- 🪫 Low power usage  
- 🏡 Protects households and farms  
- 🚜 Useful for farmers, villagers, and outdoor workers  
- 🌐 Works offline in areas with no internet  
- 🚨 Prevents accidents *before* they happen  

---

## 🔭 Future Improvements

- Solar-powered standalone deployment  
- Infrared/Thermal camera support  
- Smartphone MQTT alerts (WhatsApp/Telegram)  
- On-device sound alarm  
- Multi-camera setups for large perimeter monitoring  
- Snake tracking across frames  

---

## 🏁 Conclusion

SnekDetect started as a hackathon idea but grew into a **practical, life-saving edge AI solution**.

With:

- A strong dataset  
- YOLO + Edge Impulse  
- Raspberry Pi deployment  





