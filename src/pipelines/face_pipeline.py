import dlib
import numpy as np
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        descriptor = facerec.compute_face_descriptor(image_np, shape, 1)
        encodings.append(np.array(descriptor))

    return encodings


@st.cache_resource
def get_trained_model():

    student_db = get_all_students()

    if not student_db:
        return None

    X = []
    y = []

    for student in student_db:

        embedding = student.get("face_embedding")

        if embedding is not None:

            X.append(np.array(embedding))
            y.append(student["student_id"])

    if len(X) == 0:
        return None

    return {
        "X": X,
        "y": y
    }


def train_classifier():
    st.cache_resource.clear()
    return get_trained_model()


def predict_attendance(class_image_np):

    encodings = get_face_embeddings(class_image_np)

    detected_students = {}

    model = get_trained_model()

    if model is None:
        return detected_students, [], len(encodings)

    X_train = model["X"]
    y_train = model["y"]

    threshold = 0.55

    for encoding in encodings:

        distances = []

        for emb in X_train:
            dist = np.linalg.norm(emb - encoding)
            distances.append(dist)

        best_index = np.argmin(distances)
        best_distance = distances[best_index]

        print("Best Distance:", best_distance)

        if best_distance < threshold:

            student_id = y_train[best_index]

            detected_students[student_id] = True

    return detected_students, y_train, len(encodings)

