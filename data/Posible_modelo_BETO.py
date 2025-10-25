#!/usr/bin/env python3
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

FILE = r"/mnt/data/muestra_aleatoria.xlsx"
COL = "OBSERVACION TERRENO"
MODEL = "dccuchile/bert-base-spanish-wwm-cased"  # BETO

# 1) Cargar datos
df = pd.read_excel(FILE)
df = df[[COL]].dropna().rename(columns={COL:"text"})

# 2) Etiquetado débil (palabras clave simples)
buckets = {'cambio_equipo': ['ont', 'router', 'modem', 'deco', 'cambiar', 'cambio', 'reemplazo'], 'provision_activacion': ['aprovision', 'provision', 'activar', 'activar', 'activar', 'alta', 'instalar', 'instalacion', 'provisionar'], 'paquetes_plan': ['paquete', 'paquetes', 'plan', 'subir', 'upgrade', 'speed', 'velocidad'], 'wifi_conectividad': ['wifi', 'inalambrica', 'ssid', 'clave', 'señal', 'intermitencia', 'lentitud'], 'averia_linea': ['fallo', 'falla', 'averia', 'daño', 'corte', 'sin', 'servicio', 'no navega', 'no internet'], 'administrativo': ['factura', 'pago', 'cobro', 'reclamo']}
def suggest_label(text):
    t = str(text).lower()
    scores = {k:0 for k in buckets}
    for k, kws in buckets.items():
        for kw in kws:
            if kw in t:
                scores[k] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "otros"

df["label_name"] = df["text"].apply(suggest_label)

# 3) Mapear etiquetas a ids
labels = sorted(df["label_name"].unique())
label2id = {name:i for i,name in enumerate(labels)}
id2label = {i:name for name,i in label2id.items()}
df["label"] = df["label_name"].map(label2id)

# 4) Split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])
train_ds = Dataset.from_pandas(train_df[["text","label"]].reset_index(drop=True))
test_ds  = Dataset.from_pandas(test_df[["text","label"]].reset_index(drop=True))

# 5) Tokenizador y modelo
tok = AutoTokenizer.from_pretrained(MODEL)
def tok_fn(batch):
    return tok(batch["text"], truncation=True, padding=True)

train_ds = train_ds.map(tok_fn, batched=True)
test_ds  = test_ds.map(tok_fn, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=len(labels), id2label=id2label, label2id=label2id)

# 6) Entrenamiento mínimo
args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    logging_steps=50,
    num_train_epochs=2,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,
    weight_decay=0.01
)

trainer = Trainer(model=model, args=args, train_dataset=train_ds, eval_dataset=test_ds)
trainer.train()

# 7) Ejemplo de inferencia
pred = trainer.predict(test_ds.select(range(min(5, len(test_ds)))))
import numpy as np
y = pred.predictions.argmax(axis=1)
print("\nEtiquetas: ", id2label)
print("Predicciones de ejemplo:", y.tolist())
