import numpy as np

def main():
    print("Hello from test-uv-part-ii!")
    # Create a random 10x10 matrix using numpy, using 0 and 1. The ones should draw a heart.
    heart = np.array([[0,0,1,1,0,0,1,1,0,0],
                      [0,1,1,1,1,1,1,1,1,0],
                      [1,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,1],
                      [0,1,1,1,1,1,1,1,1,0],
                      [0,0,1,1,1,1,1,1,0,0],
                      [0,0,0,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]])
    print(heart)
    



if __name__ == "__main__":
    main()
