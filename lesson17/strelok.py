import random
import time
print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")
input("нажми enter,чтобы продолжить")

print("время стрелять")
secundi = random.randint(1,5)
time.sleep(secundi)
start = time.time()
input("стреляй")
end = time.time() - start
print(end)
if end < 0.01:
    print("фальшстарт")
elif end > 0.5:
    print("🤢")
else:
    print("😊")