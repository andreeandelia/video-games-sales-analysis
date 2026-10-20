<div align="center">

# 🎮 Analiza Vânzărilor de Jocuri Video

**Aplicație web interactivă pentru analiza, vizualizarea și modelarea datelor VGChartz**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

</div>

---

## 📑 Cuprins

- [📖 Descriere](#-descriere)
- [📊 Setul de date](#-setul-de-date)
- [✨ Funcționalități](#-funcționalități)
- [🗂️ Structura proiectului](#️-structura-proiectului)
- [🧰 Tehnologii](#-tehnologii)
- [🚀 Instalare și rulare](#-instalare-și-rulare)
- [🧭 Flux recomandat în aplicație](#-flux-recomandat-în-aplicație)
- [💡 Observații](#-observații)

---

## 📖 Descriere

Acest proiect este o **aplicație web interactivă** dezvoltată în **Python** cu **Streamlit**, pentru analiza setului de date **VGChartz** (`video-games-sales.csv`).

Aplicația acoperă un flux complet de data science: de la încărcarea și curățarea datelor, la analiză exploratorie, pregătire pentru machine learning și antrenarea mai multor modele, totul direct din browser.

---

## 📊 Setul de date

📁 Fișierul folosit în proiect: `video-games-sales.csv`

Exemple de coloane relevante:

| Categorie | Coloane |
|---|---|
| 💰 Vânzări globale și regionale | `total_sales`, `na_sales`, `pal_sales`, `jp_sales`, `other_sales` |
| 🕹️ Informații despre joc | `title`, `genre`, `console`, `publisher`, `developer`, `release_date` |
| ⭐ Scoruri | `critic_score`, `user_score` |

---

## ✨ Funcționalități

### 1️⃣ 📥 Introducere și încărcare date

- 📤 Upload CSV din interfața Streamlit
- 👀 Afișare date brute și dimensiunea dataset-ului
- 💾 Persistența datelor în sesiune prin `st.session_state`

### 2️⃣ 🧹 Preprocesare

- 🗑️ Eliminare coloane irelevante
- 🔄 Reset dataset la forma inițială
- 🔍 Analiza valorilor lipsă (număr + procent NaN)
- ✂️ Ștergere rânduri/coloane cu valori lipsă după selecție
- 🩹 Imputare interactivă:
  - 🔢 numeric: `0`, medie, mediană
  - 🔤 categoric: `Necunoscut`, mod
- 📈 Analiza outliers:
  - metoda **IQR** (raport tabelar)
  - **boxplot** pe variabila selectată
- 📦 Export dataset preprocesat (`dataset_preprocesat.csv`)

### 3️⃣ 🔎 Analiza exploratorie (EDA)

- 🏆 Top jocuri după vânzări globale
- 📅 Evoluția vânzărilor în timp (pe ani)
- 🔥 Heatmap vânzări pe console și genuri
- 🌍 Comparație regională între două piețe (scatter)
- 🔗 Matrice de corelație pentru variabile numerice

### 4️⃣ 🛠️ Pregătirea datelor pentru ML

- 🚫 Eliminare automată a coloanelor text greu modelabile direct (`title`, `release_date`)
- 🏷️ Codificare variabile categorice:
  - One-Hot Encoding
  - Label Encoding
  - Frequency Encoding
  - Target Encoding
- ⚖️ Scalare variabile numerice cu `StandardScaler`
- 📦 Export dataset gata pentru ML (`dataset_ml_ready.csv`)

### 5️⃣ 🤖 Modelare ML

<details>
<summary><b>🎯 5.1 Clusterizare KMeans</b></summary>

<br>

- ✅ Selecție variabile numerice
- 📉 Opțiune **PCA** înainte de KMeans
- 🔢 Selecție `K` (numărul de clustere)
- 📏 Evaluare cu **Silhouette Score**
- 🧩 Profilare clustere + vizualizare + export (`dataset_clusterizat_kmeans.csv`)

</details>

<details>
<summary><b>📐 5.2 Regresie liniară multiplă</b></summary>

<br>

- 🎯 Selecție variabilă țintă numerică și predictori
- ✂️ Split train/test configurabil
- 📊 Metrici: **MAE**, **RMSE**, **R²**
- 🧮 Coeficienți model (scikit-learn) + semnificație statistică (statsmodels)
- 📦 Export predicții (`rezultate_regresie_liniara.csv`)

</details>

<details>
<summary><b>🌲 5.3 Random Forest Regressor</b></summary>

<br>

- 🎯 Selecție țintă/predictori
- ⚙️ Hiperparametri configurabili (`n_estimators`, `max_depth`)
- 📊 Metrici: **MAE**, **RMSE**, **R²**
- 🏅 Importanța variabilelor + comparație real/predicție
- 📦 Export predicții (`rezultate_random_forest.csv`)

</details>

<details>
<summary><b>🧪 5.4 Regresie logistică (clasificare binară)</b></summary>

<br>

- 🔀 Transformarea unei variabile numerice într-o țintă binară pe baza unui prag (mediana sau prag personalizat)
- ✂️ Split train/test stratificat
- 📊 Metrici: **Accuracy**, **Precision**, **Recall**, **F1**
- 🧱 Matrice de confuzie + coeficienți model

</details>

---

## 🗂️ Structura proiectului

```text
📦 video-games-sales-analysis
 ┣ 📜 app.py                 # aplicația principală Streamlit
 ┣ 📄 video-games-sales.csv  # datasetul de intrare
 ┣ 🖼️ ps4-console.png        # imagine folosită în interfață
 ┗ 📘 README.md              # documentația proiectului
```

---

## 🧰 Tehnologii

| | Bibliotecă | Rol |
|---|---|---|
| 🌐 | `streamlit` | interfața web interactivă |
| 🐼 | `pandas`, `numpy` | manipulare și calcul numeric |
| 📊 | `matplotlib`, `seaborn`, `plotly` | vizualizări |
| 🖼️ | `pillow` | procesare imagini |
| 🤖 | `scikit-learn` | preprocesare și modele ML |
| 📐 | `statsmodels` | semnificație statistică |

**Cerințe:** 🐍 Python 3.10+ (recomandat)

---

## 🚀 Instalare și rulare

**1️⃣ (Opțional) Creează și activează un mediu virtual**

```bash
python -m venv venv
```

**2️⃣ Instalează dependențele**

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly pillow scikit-learn statsmodels
```

**3️⃣ Rulează aplicația**

```bash
streamlit run app.py
```

**4️⃣ Deschide în browser**

🌐 Pagina Streamlit se deschide automat, de obicei la `http://localhost:8501`.

---

## 🧭 Flux recomandat în aplicație

1. 📥 **Introducere:** încarcă CSV-ul
2. 🧹 **Preprocesare:** tratează NaN/outliers și exportă dacă este nevoie
3. 🔎 **EDA:** analizează pattern-urile principale
4. 🛠️ **Pregătire ML:** codifică + scalează datele
5. 🤖 **Modelare:** rulează unul sau mai multe modele ML în secțiunile dedicate

---

## 💡 Observații

- 💾 Aplicația folosește `st.session_state`, deci datele procesate sunt păstrate pe parcursul navigării între secțiuni.
- ✅ Pentru rezultate ML relevante, este recomandat să finalizezi preprocesarea înainte de modelare.

---

<div align="center">

⭐ Dacă ți-a plăcut proiectul, lasă un star pe GitHub!

</div>
