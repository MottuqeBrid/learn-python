import os


for i in range(0,100):
    os.rename(f"data/lesson-{i+1}", f"data/tutorial-{i+1}")