import random

def simulate_celebrity_recognition(image_path):
    # Lista de celebridades fictícias para simulação
    celebrities = [
        {"Name": "Emma Watson", "Confidence": random.uniform(85, 99.9)},
        {"Name": "Leonardo DiCaprio", "Confidence": random.uniform(85, 99.9)},
        {"Name": "Dwayne Johnson", "Confidence": random.uniform(85, 99.9)},
        {"Name": "Beyoncé", "Confidence": random.uniform(85, 99.9)},
        {"Name": "Tom Holland", "Confidence": random.uniform(85, 99.9)}
    ]
    
    # Simula a detecção aleatória de uma celebridade
    detected = random.choice(celebrities) if random.random() > 0.3 else None
    
    # Retorna um resultado parecido com o da AWS Rekognition
    if detected:
        return {
            "Image": image_path,
            "CelebrityMatches": [
                {
                    "Name": detected["Name"],
                    "Confidence": round(detected["Confidence"], 2)
                }
            ]
        }
    else:
        return {"Image": image_path, "CelebrityMatches": []}

# Simulação
test_image = "celebrity_sample.jpg"
result = simulate_celebrity_recognition(test_image)
print(result)

